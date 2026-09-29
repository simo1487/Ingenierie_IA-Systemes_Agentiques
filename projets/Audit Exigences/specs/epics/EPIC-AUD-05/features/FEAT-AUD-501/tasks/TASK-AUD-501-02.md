# TASK-AUD-501-02 — Réaliser dans le périmètre autorisé

- **Phase :** Réaliser dans le périmètre autorisé
- **Statut :** `À faire`
- **Dépendances :** TASK-AUD-501-01

## Objectif

Implémenter `tests/eval/test_deepeval_semantic.py` : `LLMTestCase` par golden, métriques `JsonCorrectnessMetric` et `GEval`, marqueur `eval` et skip si LM Studio indisponible.

## Livrable

Tests DeepEval exécutables via `pytest -m eval` ; skippés proprement hors-ligne.
