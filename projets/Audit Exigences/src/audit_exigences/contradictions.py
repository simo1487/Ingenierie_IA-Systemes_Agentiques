"""Audit EPIC-03 : detection des contradictions entre exigences.

Patterns deterministes :
- negation opposee sur un meme sujet (shall X / shall never X, with / without)
- valeurs numeriques incompatibles sur une meme grandeur
"""

from __future__ import annotations

import re

from audit_exigences.models import Finding, Requirement
from audit_exigences.normalize import normalize_tokens

# Modaux et negations
POSITIVE_PATTERN = re.compile(r"\b(shall|must|devra|doit)\b", re.IGNORECASE)
NEGATIVE_PATTERN = re.compile(
    r"\b(ne\s+doit\s+pas|ne\s+devra\s+pas|must\s+not|shall\s+not|"
    r"never|without|ne\s+peut\s+pas)\b",
    re.IGNORECASE,
)

# Valeurs numeriques avec unite
NUMBER_PATTERN = re.compile(
    r"(?P<value>\d+(?:[.,]\d+)?)\s*"
    r"(?P<unit>%|percent|km/h|km|ms|secondes?|deg\s?C|°C|degr[eé]s?|[Vv]\b|[Aa]\b|bar|kW|Wh|kWh|Mbps|kbps)",
    re.IGNORECASE,
)

# Alias d'unites pour comparer 110 degC / 110 °C / 110 degres
_UNIT_ALIASES = {
    "%": "percent",
    "percent": "percent",
    "km/h": "kmh",
    "km": "km",
    "ms": "ms",
    "s": "s",
    "seconde": "s",
    "secondes": "s",
    "degc": "degc",
    "degc": "degc",
    "°c": "degc",
    "degre": "degc",
    "degres": "degc",
    "degrés": "degc",
    "degré": "degc",
    "v": "v",
    "a": "a",
    "bar": "bar",
    "kw": "kw",
    "wh": "wh",
    "kwh": "kwh",
    "mbps": "mbps",
    "kbps": "kbps",
}

MIN_SHARED_SUBJECTS = 2


def _subject_tokens(text: str) -> set[str]:
    """Tokens de sujet normalises (hors stopwords, unites et modaux)."""
    from audit_exigences.normalize import normalize_tokens

    return normalize_tokens(text)


def audit_contradictions(requirements: list[Requirement]) -> list[Finding]:
    """Detecte les couples d'exigences contradictoires."""
    findings: list[Finding] = []
    findings.extend(_detect_negation_conflicts(requirements))
    findings.extend(_detect_numeric_conflicts(requirements))
    return findings


def _detect_negation_conflicts(requirements: list[Requirement]) -> list[Finding]:
    """Detecte 'shall X' vs 'shall never X' sur un sujet proche."""
    findings: list[Finding] = []
    for i, req_a in enumerate(requirements):
        for req_b in requirements[i + 1:]:
            neg_a = bool(NEGATIVE_PATTERN.search(req_a.text))
            neg_b = bool(NEGATIVE_PATTERN.search(req_b.text))
            pos_a = bool(POSITIVE_PATTERN.search(req_a.text)) and not neg_a
            pos_b = bool(POSITIVE_PATTERN.search(req_b.text)) and not neg_b

            polarity_opposed = (pos_a and neg_b) or (neg_a and pos_b)
            if not polarity_opposed:
                continue

            shared = _subject_tokens(req_a.text) & _subject_tokens(req_b.text)
            if len(shared) >= MIN_SHARED_SUBJECTS:
                findings.append(
                    Finding(
                        epic="contradictions",
                        requirement_id=req_a.id,
                        finding_type="negation_conflict",
                        position=0,
                        detail=(
                            f"Comportements opposés avec '{req_b.id}' "
                            f"sur le sujet commun : {', '.join(sorted(shared))}"
                        ),
                        related_ids=[req_b.id],
                    )
                )
    return findings


def _detect_numeric_conflicts(requirements: list[Requirement]) -> list[Finding]:
    """Detecte des valeurs numeriques incompatibles sur une meme grandeur."""
    findings: list[Finding] = []
    for i, req_a in enumerate(requirements):
        for req_b in requirements[i + 1:]:
            shared = _subject_tokens(req_a.text) & _subject_tokens(req_b.text)
            if len(shared) < MIN_SHARED_SUBJECTS:
                continue
            values_a = _extract_bounds(req_a.text)
            values_b = _extract_bounds(req_b.text)
            for unit_a, value_a in values_a:
                for unit_b, value_b in values_b:
                    if unit_a != unit_b:
                        continue
                    if value_a != value_b:
                        findings.append(
                            Finding(
                                epic="contradictions",
                                requirement_id=req_a.id,
                                finding_type="numeric_conflict",
                                position=0,
                                detail=(
                                    f"Valeurs incompatibles avec '{req_b.id}' : "
                                    f"{value_a} vs {value_b} {unit_a}"
                                ),
                                related_ids=[req_b.id],
                            )
                        )
    return findings


def _extract_bounds(text: str) -> list[tuple[str, float]]:
    """Extrait les couples (unite normalisee, valeur) d'un texte."""
    results = []
    for match in NUMBER_PATTERN.finditer(text):
        value = float(match.group("value").replace(",", "."))
        unit = match.group("unit").lower().replace(" ", "")
        unit = _UNIT_ALIASES.get(unit, unit)
        results.append((unit, value))
    return results
