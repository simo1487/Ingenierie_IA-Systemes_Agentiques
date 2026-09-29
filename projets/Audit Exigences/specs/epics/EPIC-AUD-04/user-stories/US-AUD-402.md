# US-AUD-402 — Détecter les duplications sémantiques via LLM local

`Référence — spécification candidate`

- **Projet parent :** [`PROJ-AUD-EXG-001`](../../../../SPEC.md)
- **Epic parente :** [`EPIC-AUD-04`](../EPIC.md)
- **Feature fille :** [`FEAT-AUD-402`](../features/FEAT-AUD-402/FEATURE.md)
- **Niveau :** `Socle`
- **Priorité :** `P2`
- **Statut documentaire :** `Candidate`
- **Travail :** `À faire`
- **Responsable :** ingénieur exigences — personne à désigner
- **Dépendances :** US-AUD-201

## Besoin

> En tant qu'ingénieur exigences, je veux identifier les exigences sémantiquement équivalentes afin de détecter les reformulations que la similarité lexicale ne voit pas.

## Entrées et sorties

- **Entrée :** Paires d'exigences candidates pré-filtrées (sujets partagés, sous le seuil lexical de US-AUD-201).
- **Sortie :** Rapport JSON des couples en `semantic_duplicate` avec rationale et modèle utilisé.

## Règle et critères

`RM-AUD-402` — Une duplication sémantique est signalée uniquement sur verdict `duplicate` du LLM local pour une paire candidate ; le couple reste une proposition à arbitrer.

- [ ] `CA-AUD-402-01` — Étant donné deux exigences expriment la même obligation avec un vocabulaire disjoint, quand l'audit sémantique est exécuté, alors le couple est signalé en `semantic_duplicate` avec la rationale.
- [ ] `CA-AUD-402-02` — Étant donné deux exigences partagent des sujets mais imposent des obligations distinctes, quand l'audit sémantique est exécuté, alors aucune duplication n'est signalée.
- [ ] `CA-AUD-402-03` — Étant donné le backend LLM est indisponible, quand l'audit sémantique est exécuté, alors l'audit est sauté avec un message d'abstention, sans erreur.

## Example Mapping

| Cas | Étant donné | Quand | Alors |
|---|---|---|---|
| Nominal | deux exigences paraphrasées imposant la même obligation | l'audit sémantique est exécuté | le couple est signalé en `semantic_duplicate` |
| Frontière | REQ-011 et REQ-012 (services UDS 0x10 et 0x11 distincts) | l'audit sémantique est exécuté | aucune duplication n'est signalée |
| Refus | le backend LLM est indisponible | l'audit sémantique est exécuté | l'audit est sauté avec message d'abstention |

## Scénarios Gherkin

```gherkin
Fonctionnalité: Détecter les duplications sémantiques
  Scénario: Frontière — CA-AUD-402-02
    Étant donné "shall support UDS service 0x10" et "shall support UDS service 0x11"
    Quand l'audit sémantique est exécuté
    Alors aucune duplication n'est signalée

  Scénario: Refus — CA-AUD-402-03
    Étant donné le backend LLM est indisponible
    Quand l'audit sémantique est exécuté
    Alors l'audit est sauté avec un message d'abstention
```

## Oracle indépendant

Verdicts attendus figés dans `tests/fixtures/semantic_oracle.json` avant exécution ; évaluation de la qualité LLM par l'écosystème DeepEval (EPIC-AUD-05) ; revue humaine des couples signalés.

## Réalisation et preuves

- [`FEAT-AUD-402`](../features/FEAT-AUD-402/FEATURE.md) — Feature candidate
- [`TASK-AUD-402-01`](../features/FEAT-AUD-402/tasks/TASK-AUD-402-01.md) — Figer l'oracle sémantique
- [`TASK-AUD-402-02`](../features/FEAT-AUD-402/tasks/TASK-AUD-402-02.md) — Implémenter l'audit sémantique
- [`TASK-AUD-402-03`](../features/FEAT-AUD-402/tasks/TASK-AUD-402-03.md) — Vérifier et soumettre à revue
