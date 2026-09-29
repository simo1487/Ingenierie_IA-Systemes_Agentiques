# TASK-AUD-101-02 — Réaliser dans le périmètre autorisé

- **Phase :** Réaliser dans le périmètre autorisé
- **Statut :** `À faire`
- **Dépendances :** `TASK-AUD-101-01`

## Objectif

Implémenter la détection grammaticale dans `src/audit_exigences/grammar.py` :
- `audit_grammar()` : accords sujet-verbe après modal, doubles espaces, capitalisation
- Position exacte (index de caractère) pour chaque anomalie

## Livrable

Module `grammar.py` avec fonction `audit_grammar(requirements) -> list[Finding]` (types `grammar`, `punctuation`, `capitalization`).
