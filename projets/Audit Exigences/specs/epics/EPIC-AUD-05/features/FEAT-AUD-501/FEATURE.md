# FEAT-AUD-501 — Évaluation DeepEval des verdicts IA

`Référence — Feature candidate`

- **US parente :** [`US-AUD-501`](../../user-stories/US-AUD-501.md)
- **Statut :** `Candidate`
- **Travail :** `À faire`

## Description

Construire l'écosystème de test DeepEval : goldens-oracle (`tests/fixtures/semantic_oracle.json`), juge local `LMStudioJudge` (`DeepEvalBaseLLM` pointant sur LM Studio), tests `LLMTestCase` avec métriques `JsonCorrectnessMetric` et `GEval`, skip automatique si LM Studio indisponible, rapport `evidence/deepeval-report.json`.

## Critères référencés

Voir `CA-AUD-501-01` à `CA-AUD-501-03` dans [`US-AUD-501`](../../user-stories/US-AUD-501.md).

## Tâches

- [`TASK-AUD-501-01`](tasks/TASK-AUD-501-01.md) — Spécifier et figer l'oracle
- [`TASK-AUD-501-02`](tasks/TASK-AUD-501-02.md) — Réaliser dans le périmètre autorisé
- [`TASK-AUD-501-03`](tasks/TASK-AUD-501-03.md) — Vérifier et soumettre à revue
