# TASK-AUD-102-02 — Réaliser dans le périmètre autorisé

- **Phase :** Réaliser dans le périmètre autorisé
- **Statut :** `À faire`
- **Dépendances :** `TASK-AUD-102-01`

## Objectif

Implémenter la détection orthographique dans `src/audit_exigences/spelling.py` :
- Recherche des fautes du dictionnaire avec position exacte
- Vérification de mot entier (pas de sous-mot)
- Correction issue du dictionnaire uniquement

## Livrable

Module `spelling.py` avec fonction `audit_spelling(requirements) -> list[Finding]` (type `spelling`).
