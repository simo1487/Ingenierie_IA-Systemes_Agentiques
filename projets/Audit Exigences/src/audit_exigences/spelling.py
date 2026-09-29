"""Audit EPIC-01 / US-AUD-102 : orthographe des exigences.

Detection par dictionnaire fige de fautes courantes, avec position exacte
et correction issue du dictionnaire uniquement.
"""

from __future__ import annotations

from audit_exigences.models import Finding, Requirement

# Fautes courantes -> correction (recherche insensible a la casse)
COMMON_TYPOS: dict[str, str] = {
    # Francais
    "systéme": "système",
    "systeme": "système",
    "redemarrer": "redémarrer",
    "aprés": "après",
    "apres": "après",
    "démaré": "démarré",
    "vechicule": "véhicule",
    "securité": "sécurité",
    "étre": "être",
    "etre": "être",
    "a fin de": "afin de",
    "parmis": "parmi",
}


def audit_spelling(requirements: list[Requirement]) -> list[Finding]:
    """Detecte les fautes d'orthographe du dictionnaire dans les exigences."""
    findings: list[Finding] = []
    for req in requirements:
        findings.extend(_check_typos(req))
    return findings


def _check_typos(req: Requirement) -> list[Finding]:
    findings: list[Finding] = []
    lowered = req.text.lower()
    for wrong, correct in COMMON_TYPOS.items():
        if wrong == correct:
            continue
        start = 0
        while True:
            idx = lowered.find(wrong.lower(), start)
            if idx == -1:
                break
            end = idx + len(wrong)
            before_ok = idx == 0 or not lowered[idx - 1].isalnum()
            after_ok = end >= len(lowered) or not lowered[end].isalnum()
            if before_ok and after_ok:
                findings.append(
                    Finding(
                        epic="spelling",
                        requirement_id=req.id,
                        finding_type="spelling",
                        position=idx,
                        detail=f"Faute probable : '{wrong}'",
                        suggestion=correct,
                    )
                )
            start = end
    return findings
