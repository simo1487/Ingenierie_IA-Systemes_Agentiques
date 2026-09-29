# FEAT-AUD-402 — Duplications sémantiques via LLM local

`Référence — Feature candidate`

- **US parente :** [`US-AUD-402`](../../user-stories/US-AUD-402.md)
- **Statut :** `Candidate`
- **Travail :** `À faire`

## Description

Implémenter l'audit sémantique des duplications : même pipeline que FEAT-AUD-401 (pré-filtre, verdict JSON, backend `fake`/`lmstudio`) ; les verdicts `duplicate` produisent des findings `semantic_duplicate`. Les paires déjà signalées par la similarité lexicale (US-AUD-201) sont exclues du pré-filtre.

## Critères référencés

Voir `CA-AUD-402-01` à `CA-AUD-402-03` dans [`US-AUD-402`](../../user-stories/US-AUD-402.md).

## Tâches

- [`TASK-AUD-402-01`](tasks/TASK-AUD-402-01.md) — Spécifier et figer l'oracle
- [`TASK-AUD-402-02`](tasks/TASK-AUD-402-02.md) — Réaliser dans le périmètre autorisé
- [`TASK-AUD-402-03`](tasks/TASK-AUD-402-03.md) — Vérifier et soumettre à revue
