"""Audit d'une exigence Zephyr collectée.

Applique les critères de singularité, clarté et vérifiabilité sans inventer
aucune règle non présente dans le schéma.
"""

from __future__ import annotations

import copy


def audit_requirement(requirement: dict) -> dict:
    """Audite une exigence et enrichit ses champs `audit`, `ambiguities` et `status`.

    L'exigence originale n'est pas modifiée : la fonction retourne une copie.
    """
    audited = copy.deepcopy(requirement)

    audit = {
        "singularite": "Candidat",
        "clarte": "Candidat",
        "verifiabilite": "Candidat",
    }
    ambiguities = list(audited.get("ambiguities", []))
    status = audited.get("status", "Observé")

    # Singularité : on ne découpe pas ici, on signale si un texte contient
    # plusieurs énoncés séparés par un point suivi d'un espace.
    text = audited.get("requirement_text") or ""
    if isinstance(text, str) and text.count(". ") > 0:
        audit["singularite"] = "Candidat"
        ambiguities.append(
            "Le texte contient peut-être plusieurs énoncés à vérifier."
        )

    # Clarté : le texte doit être non vide.
    if not text:
        audit["clarte"] = "Bloqué"
        status = "Bloqué"
        ambiguities.append("requirement_text manquant ou vide")

    # Vérifiabilité : identifiant et source doivent être renseignés.
    if audited.get("requirement_id") is None:
        audit["verifiabilite"] = "Bloqué"
        status = "Bloqué"
        ambiguities.append("requirement_id absent")

    if not audited.get("source_url"):
        audit["verifiabilite"] = "Bloqué"
        status = "Bloqué"
        ambiguities.append("source_url manquant")

    audited["audit"] = audit
    audited["ambiguities"] = ambiguities
    audited["status"] = status
    audited["confidence"] = audited.get("confidence", "Candidat")

    return audited
