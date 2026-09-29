# US-AUD-401 — Détecter les contradictions sémantiques via LLM local

`Référence — spécification candidate`

- **Projet parent :** [`PROJ-AUD-EXG-001`](../../../../SPEC.md)
- **Epic parente :** [`EPIC-AUD-04`](../EPIC.md)
- **Feature fille :** [`FEAT-AUD-401`](../features/FEAT-AUD-401/FEATURE.md)
- **Niveau :** `Socle`
- **Priorité :** `P2`
- **Statut documentaire :** `Candidate`
- **Travail :** `À faire`
- **Responsable :** ingénieur exigences — personne à désigner
- **Dépendances :** US-AUD-301

## Besoin

> En tant qu'ingénieur exigences, je veux identifier les contradictions sémantiques entre exigences afin de détecter les incohérences sans négation explicite.

## Entrées et sorties

- **Entrée :** Paires d'exigences candidates pré-filtrées (sujets partagés, non déjà détectées par les audits déterministes).
- **Sortie :** Rapport JSON des couples en `semantic_contradiction` avec rationale et modèle utilisé.

## Règle et critères

`RM-AUD-401` — Une contradiction sémantique est signalée uniquement sur verdict `contradiction` du LLM local pour une paire candidate ; le couple reste une proposition à arbitrer.

- [ ] `CA-AUD-401-01` — Étant donné deux exigences imposent des comportements sémantiquement opposés sur le même sujet (ex. disable vs continue), quand l'audit sémantique est exécuté, alors le couple est signalé en `semantic_contradiction` avec la rationale.
- [ ] `CA-AUD-401-02` — Étant donné deux exigences portant sur des sujets proches mais non opposés, quand l'audit sémantique est exécuté, alors aucune contradiction n'est signalée.
- [ ] `CA-AUD-401-03` — Étant donné le backend LLM est indisponible, quand l'audit sémantique est exécuté, alors l'audit est sauté avec un message d'abstention, sans erreur.

## Example Mapping

| Cas | Étant donné | Quand | Alors |
|---|---|---|---|
| Nominal | REQ-005 (disable torque) et REQ-006 (continue torque) | l'audit sémantique est exécuté | le couple est signalé en `semantic_contradiction` |
| Frontière | REQ-003 (overvoltage) et REQ-004 (undervoltage) partagent le sujet DC bus | l'audit sémantique est exécuté | aucune contradiction n'est signalée (grandeurs distinctes) |
| Refus | le backend LLM est indisponible | l'audit sémantique est exécuté | l'audit est sauté avec message d'abstention |

## Scénarios Gherkin

```gherkin
Fonctionnalité: Détecter les contradictions sémantiques
  Scénario: Nominal — CA-AUD-401-01
    Étant donné "The inverter shall disable torque production" et "The inverter shall continue torque production"
    Quand l'audit sémantique est exécuté
    Alors le couple est signalé avec le type "semantic_contradiction"

  Scénario: Refus — CA-AUD-401-03
    Étant donné le backend LLM est indisponible
    Quand l'audit sémantique est exécuté
    Alors l'audit est sauté avec un message d'abstention
```

## Oracle indépendant

Verdicts attendus figés dans `tests/fixtures/semantic_oracle.json` avant exécution ; évaluation de la qualité LLM par l'écosystème DeepEval (EPIC-AUD-05) ; revue humaine des couples signalés.

## Réalisation et preuves

- [`FEAT-AUD-401`](../features/FEAT-AUD-401/FEATURE.md) — Feature candidate
- [`TASK-AUD-401-01`](../features/FEAT-AUD-401/tasks/TASK-AUD-401-01.md) — Figer l'oracle sémantique
- [`TASK-AUD-401-02`](../features/FEAT-AUD-401/tasks/TASK-AUD-401-02.md) — Implémenter l'audit sémantique
- [`TASK-AUD-401-03`](../features/FEAT-AUD-401/tasks/TASK-AUD-401-03.md) — Vérifier et soumettre à revue
