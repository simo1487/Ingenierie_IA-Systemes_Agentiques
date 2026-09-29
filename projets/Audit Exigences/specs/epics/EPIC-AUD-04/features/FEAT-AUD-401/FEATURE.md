# FEAT-AUD-401 — Contradictions sémantiques via LLM local

`Référence — Feature candidate`

- **US parente :** [`US-AUD-401`](../../user-stories/US-AUD-401.md)
- **Statut :** `Candidate`
- **Travail :** `À faire`

## Description

Implémenter l'audit sémantique des contradictions : pré-filtre déterministe des paires candidates (sujets partagés, hors détections déjà faites), verdict JSON du LLM local (`contradiction`/`duplicate`/`ok` + rationale), findings `semantic_contradiction` avec provenance du modèle. Backend `fake` pour tests hors-ligne ; abstention propre si le backend est indisponible.

## Critères référencés

Voir `CA-AUD-401-01` à `CA-AUD-401-03` dans [`US-AUD-401`](../../user-stories/US-AUD-401.md).

## Tâches

- [`TASK-AUD-401-01`](tasks/TASK-AUD-401-01.md) — Spécifier et figer l'oracle
- [`TASK-AUD-401-02`](tasks/TASK-AUD-401-02.md) — Réaliser dans le périmètre autorisé
- [`TASK-AUD-401-03`](tasks/TASK-AUD-401-03.md) — Vérifier et soumettre à revue
