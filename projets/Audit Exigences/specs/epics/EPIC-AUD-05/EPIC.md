# EPIC-AUD-05 — Écosystème d'évaluation DeepEval

`Référence — Epic candidate`

- **Projet parent :** [`PROJ-AUD-EXG-001`](../../../SPEC.md)
- **Statut documentaire :** `Candidate`
- **Travail :** `À faire`

## Valeur

Éprouver la partie IA de l'outil (EPIC-AUD-04) par un écosystème de test indépendant basé sur DeepEval : goldens-oracle figés, juge LLM local, métriques de conformité du verdict et de la rationale.

## Enfants

| User Story | Feature | Rôle | Valeur |
|---|---|---|---|
| [`US-AUD-501`](user-stories/US-AUD-501.md) | [`FEAT-AUD-501`](features/FEAT-AUD-501/FEATURE.md) | responsable qualité | évaluer les verdicts sémantiques contre l'oracle via DeepEval |

## Périmètre

Évaluation LLM-as-judge via DeepEval avec juge local (LM Studio). Les goldens sont l'oracle indépendant figé avant implémentation : verdicts attendus et non-détections attendues sur paires du dataset. Métriques : conformité JSON du verdict (`JsonCorrectnessMetric`) et qualité sémantique de la rationale (`GEval`). Les tests sont skippés si LM Studio est indisponible ; la suite hors-ligne reste verte via le backend `fake`.

## Achèvement mesurable

Les goldens sont figés, les tests DeepEval s'exécutent avec le juge local et produisent un rapport `evidence/deepeval-report.json` soumis à revue humaine.
