# TASK-AUD-401-03 — Vérifier et soumettre à revue

- **Phase :** Vérifier et soumettre à revue
- **Statut :** `À faire`
- **Dépendances :** TASK-AUD-401-02

## Objectif

Vérifier les findings `semantic_contradiction` contre l'oracle figé (attendus présents, non-détections absentes) avec le backend `fake` ; soumettre les propositions à revue humaine.

## Livrable

Tests de conformité oracle verts dans `tests/test_oracle_compliance.py` (classe `TestSemanticOracle`).
