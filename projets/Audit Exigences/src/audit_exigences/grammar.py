"""Audit EPIC-01 / US-AUD-101 : grammaire des exigences.

Detection deterministe sans dependance externe :
- accords sujet-verbe apres modal (shall logs -> shall log)
- doubles espaces
- majuscule manquante en debut d'exigence
"""

from __future__ import annotations

from audit_exigences.models import Finding, Requirement

# Erreurs d'accord apres modal -> correction
GRAMMAR_RULES: dict[str, str] = {
    "shall logs": "shall log",
    "shall has": "shall have",
    "shall be transmit": "shall transmit",
    "shall is": "shall be",
    "shall are": "shall be",
}


def audit_grammar(requirements: list[Requirement]) -> list[Finding]:
    """Detecte les anomalies grammaticales dans les exigences."""
    findings: list[Finding] = []
    for req in requirements:
        findings.extend(_check_agreement(req))
        findings.extend(_check_punctuation(req))
        findings.extend(_check_capitalization(req))
    return findings


def _check_agreement(req: Requirement) -> list[Finding]:
    """Detecte les erreurs d'accord apres un modal (shall/must)."""
    findings: list[Finding] = []
    lowered = req.text.lower()
    for wrong, correct in GRAMMAR_RULES.items():
        start = 0
        while True:
            idx = lowered.find(wrong, start)
            if idx == -1:
                break
            end = idx + len(wrong)
            before_ok = idx == 0 or not lowered[idx - 1].isalnum()
            after_ok = end >= len(lowered) or not lowered[end].isalnum()
            if before_ok and after_ok:
                findings.append(
                    Finding(
                        epic="grammar",
                        requirement_id=req.id,
                        finding_type="grammar",
                        position=idx,
                        detail=f"Erreur d'accord probable : '{wrong}'",
                        suggestion=correct,
                    )
                )
            start = end
    return findings


def _check_punctuation(req: Requirement) -> list[Finding]:
    """Detecte les doubles espaces."""
    findings: list[Finding] = []
    idx = req.text.find("  ")
    if idx != -1:
        findings.append(
            Finding(
                epic="grammar",
                requirement_id=req.id,
                finding_type="punctuation",
                position=idx,
                detail="Double espace détecté",
                suggestion="Espace simple",
            )
        )
    return findings


def _check_capitalization(req: Requirement) -> list[Finding]:
    """Detecte l'absence de majuscule en debut de phrase."""
    findings: list[Finding] = []
    stripped = req.text.lstrip()
    if stripped and stripped[0].islower():
        findings.append(
            Finding(
                epic="grammar",
                requirement_id=req.id,
                finding_type="capitalization",
                position=0,
                detail="La phrase ne commence pas par une majuscule",
                suggestion=stripped[0].upper() + stripped[1:],
            )
        )
    return findings
