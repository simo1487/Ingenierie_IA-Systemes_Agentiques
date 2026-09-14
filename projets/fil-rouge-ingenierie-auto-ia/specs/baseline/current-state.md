# Explication — État actuel et écarts candidats

**Nature :** Observation issue de la revue directe déjà réalisée par le responsable du lot. Ce document ne prétend pas qu’une modification future est déjà appliquée.

## Comportements observés

- `src/auto_ai_flow/orchestrator.py:14-26` contrôle quatre clés requises et le booléen d’approbation des baselines.
- `src/auto_ai_flow/orchestrator.py:27-34` exécute les agents suivants même lorsque `CorpusAgent` retourne `Bloqué`. `src/auto_ai_flow/agents.py:20-29` signale ce blocage pour une liste de baselines vide ou une révision manquante. L’entrée invalide peut donc échouer plus tard ; aucune protection de court-circuit n’est prouvée. La continuation planifiée est [`US-FIL-101`](../epics/EPIC-FIL-01/user-stories/US-FIL-101.md).
- `src/auto_ai_flow/agents.py:40-61` effectue un retrieval lexical top 3. Si le premier score est positif, toute la sélection est émise, y compris d’éventuels passages de score nul. Aucune exactitude sémantique n’est prouvée ; les politiques futures de [`US-FIL-404`](../epics/EPIC-FIL-04/user-stories/US-FIL-404.md) exigent une approbation.
- `src/auto_ai_flow/providers.py:43-88` contrôle la tâche et la présence de clés requises pour Mistral, mais pas l’intégralité des types, bornes et références. Voir [`US-FIL-104`](../epics/EPIC-FIL-01/user-stories/US-FIL-104.md).
- `src/auto_ai_flow/agents.py:118-126` attribue `Vérifié` lorsque les champs `oracle` et `evidence` sont tous deux non vides. Le code n’ouvre pas l’artefact, ne contrôle pas sa vérité et n’enregistre pas une approbation humaine. Voir [`US-FIL-601`](../epics/EPIC-FIL-06/user-stories/US-FIL-601.md).
- `src/auto_ai_flow/orchestrator.py:39` produit `generated_at` avec l’heure courante. `tests/test_cli.py:16-25` vérifie le code retour et l’état du rapport, mais pas l’égalité de deux rapports répétés. Voir [`US-FIL-501`](../epics/EPIC-FIL-05/user-stories/US-FIL-501.md).

## Surfaces présentes et absentes

Le fournisseur déterministe est une fixture, pas une mesure d’IA en ligne. Six tests métier existent dans la baseline et des preuves antérieures sont conservées ; ce document n’enregistre aucune nouvelle exécution historique. Aucun checkpoint durable, mémoire gouvernée, serveur MCP, registre d’audit de traces ou revue signée n’est actuellement implémenté. Les adaptateurs futurs, retours de code et comportements de concurrence restent candidats tant que leurs US ne sont pas réalisés et vérifiés.

## Continuité de planification historique

Les liens suivants expriment une continuité de planification, jamais une trace de preuve :

| Identifiant historique | Continuation candidate |
|---|---|
| `US-FIL-AUTO-IA-001` | [`US-FIL-101`](../epics/EPIC-FIL-01/user-stories/US-FIL-101.md) |
| `US-FIL-AUTO-IA-002` | [`US-FIL-404`](../epics/EPIC-FIL-04/user-stories/US-FIL-404.md) |
| `US-FIL-AUTO-IA-003` | [`US-FIL-104`](../epics/EPIC-FIL-01/user-stories/US-FIL-104.md) et [`US-FIL-601`](../epics/EPIC-FIL-06/user-stories/US-FIL-601.md) |
| `US-FIL-AUTO-IA-004` | [`US-FIL-305`](../epics/EPIC-FIL-03/user-stories/US-FIL-305.md) et [`US-FIL-405`](../epics/EPIC-FIL-04/user-stories/US-FIL-405.md) |
| `US-FIL-AUTO-IA-005` | [`US-FIL-601`](../epics/EPIC-FIL-06/user-stories/US-FIL-601.md) |
| `US-FIL-AUTO-IA-006` | [`US-FIL-604`](../epics/EPIC-FIL-06/user-stories/US-FIL-604.md) |

`EPIC-FIL-AUTO-IA-001` demeure le MVP original dans [`mvp-spec.md`](mvp-spec.md). Les Epics `EPIC-FIL-01` à `EPIC-FIL-06` sont des évolutions candidates.
