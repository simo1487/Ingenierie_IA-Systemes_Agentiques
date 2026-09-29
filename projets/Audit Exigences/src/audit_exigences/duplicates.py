"""Audit EPIC-02 : detection des exigences dupliquees.

Similarite de Jaccard sur tokens normalises, avec seuil fige avant execution.
Une exigence negative et une positive ne sont jamais des duplications.
"""

from __future__ import annotations

import re

from audit_exigences.models import Finding, Requirement
from audit_exigences.normalize import normalize_tokens

DEFAULT_THRESHOLD = 0.80

NEGATIVE_PATTERN = re.compile(
    r"\b(ne\s+doit\s+pas|ne\s+devra\s+pas|must\s+not|shall\s+not|never|without)\b",
    re.IGNORECASE,
)


def jaccard_similarity(tokens_a: set[str], tokens_b: set[str]) -> float:
    """Similarite de Jaccard entre deux ensembles de tokens."""
    if not tokens_a or not tokens_b:
        return 0.0
    intersection = tokens_a & tokens_b
    union = tokens_a | tokens_b
    return len(intersection) / len(union) if union else 0.0


def audit_duplicates(
    requirements: list[Requirement],
    threshold: float = DEFAULT_THRESHOLD,
) -> list[Finding]:
    """Detecte les paires d'exigences dont la similarite depasse le seuil."""
    findings: list[Finding] = []
    tokenized = [(req, normalize_tokens(req.text)) for req in requirements]

    for i in range(len(tokenized)):
        req_a, tokens_a = tokenized[i]
        neg_a = bool(NEGATIVE_PATTERN.search(req_a.text))
        for j in range(i + 1, len(tokenized)):
            req_b, tokens_b = tokenized[j]
            neg_b = bool(NEGATIVE_PATTERN.search(req_b.text))
            if neg_a != neg_b:
                # Une exigence negative et une positive ne sont pas des doublons
                continue
            score = jaccard_similarity(tokens_a, tokens_b)
            if score >= threshold:
                findings.append(
                    Finding(
                        epic="duplicates",
                        requirement_id=req_a.id,
                        finding_type="duplicate",
                        position=0,
                        detail=(
                            f"Exigence similaire a '{req_b.id}' "
                            f"(similarite {score:.2f} >= seuil {threshold})"
                        ),
                        related_ids=[req_b.id],
                        score=score,
                    )
                )
    return findings
