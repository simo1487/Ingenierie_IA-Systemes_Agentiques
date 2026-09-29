# US-AUD-501 — Évaluer les verdicts IA avec DeepEval

`Référence — spécification candidate`

- **Projet parent :** [`PROJ-AUD-EXG-001`](../../../../SPEC.md)
- **Epic parente :** [`EPIC-AUD-05`](../EPIC.md)
- **Feature fille :** [`FEAT-AUD-501`](../features/FEAT-AUD-501/FEATURE.md)
- **Niveau :** `Socle`
- **Priorité :** `P2`
- **Statut documentaire :** `Candidate`
- **Travail :** `À faire`
- **Responsable :** responsable qualité — personne à désigner
- **Dépendances :** US-AUD-401, US-AUD-402

## Besoin

> En tant que responsable qualité, je veux évaluer les verdicts sémantiques de l'outil contre un oracle figé via DeepEval afin d'objectiver la qualité de la partie IA.

## Entrées et sorties

- **Entrée :** Goldens `tests/fixtures/semantic_oracle.json` (paires + verdicts attendus + non-détections) et verdicts produits par l'audit sémantique.
- **Sortie :** Rapport `evidence/deepeval-report.json` avec scores par métrique, verdicts et rationales.

## Règle et critères

`RM-AUD-501` — Chaque paire golden est évaluée en `LLMTestCase` (input, actual_output, expected_output) ; les métriques utilisent un juge LLM local ; un score sous le seuil échoue le test.

- [ ] `CA-AUD-501-01` — Étant donné un golden dont le verdict attendu est `contradiction`, quand l'évaluation DeepEval est exécutée, alors le `LLMTestCase` confronte le verdict produit au verdict attendu et la métrique `JsonCorrectness` vérifie la structure.
- [ ] `CA-AUD-501-02` — Étant donné un golden de non-détection (`ok` attendu), quand l'évaluation est exécutée, alors un verdict `contradiction` ou `duplicate` produit est rapporté comme échec (contrôle anti-faux-positifs).
- [ ] `CA-AUD-501-03` — Étant donné LM Studio est indisponible, quand la suite de tests est exécutée, alors les tests `eval` sont skippés et la suite hors-ligne reste verte.

## Example Mapping

| Cas | Étant donné | Quand | Alors |
|---|---|---|---|
| Nominal | un golden contradiction (REQ-005/006) | l'évaluation DeepEval est exécutée | le verdict produit est confronté au verdict attendu, scores rapportés |
| Frontière | un golden `ok` (REQ-003/004) | l'évaluation est exécutée | tout verdict non-`ok` est rapporté en échec |
| Refus | LM Studio indisponible | la suite est exécutée | tests `eval` skippés, suite verte |

## Scénarios Gherkin

```gherkin
Fonctionnalité: Évaluer les verdicts IA avec DeepEval
  Scénario: Nominal — CA-AUD-501-01
    Étant donné un golden dont le verdict attendu est "contradiction"
    Quand l'évaluation DeepEval est exécutée avec le juge local
    Alors le verdict produit est confronté au verdict attendu et les scores sont rapportés

  Scénario: Refus — CA-AUD-501-03
    Étant donné LM Studio est indisponible
    Quand la suite de tests est exécutée
    Alors les tests "eval" sont skippés et la suite reste verte
```

## Oracle indépendant

Goldens figés dans `tests/fixtures/semantic_oracle.json` avant implémentation ; le juge évalue la rationale (GEval) et la conformité du verdict (JsonCorrectness) ; les scores sont des preuves soumises à revue humaine, pas une décision automatique.

## Réalisation et preuves

- [`FEAT-AUD-501`](../features/FEAT-AUD-501/FEATURE.md) — Feature candidate
- [`TASK-AUD-501-01`](../features/FEAT-AUD-501/tasks/TASK-AUD-501-01.md) — Figer les goldens et le juge
- [`TASK-AUD-501-02`](../features/FEAT-AUD-501/tasks/TASK-AUD-501-02.md) — Implémenter les tests DeepEval
- [`TASK-AUD-501-03`](../features/FEAT-AUD-501/tasks/TASK-AUD-501-03.md) — Produire le rapport et soumettre à revue
