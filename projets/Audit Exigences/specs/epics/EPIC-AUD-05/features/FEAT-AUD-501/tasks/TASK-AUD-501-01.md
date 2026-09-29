# TASK-AUD-501-01 — Spécifier et figer l'oracle

- **Phase :** Spécifier et figer l'oracle
- **Statut :** `À faire`
- **Dépendances :** TASK-AUD-401-01

## Objectif

Figer les goldens DeepEval (paires, verdict attendu, non-détections) dans `tests/fixtures/semantic_oracle.json` et le juge local `tests/eval/judge_model.py` (`DeepEvalBaseLLM` sur LM Studio).

## Livrable

Goldens figés + `LMStudioJudge` implémenté (load_model, generate, a_generate, get_model_name).
