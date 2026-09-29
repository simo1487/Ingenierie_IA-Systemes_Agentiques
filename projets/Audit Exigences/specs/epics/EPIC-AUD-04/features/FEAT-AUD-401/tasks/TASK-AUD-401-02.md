# TASK-AUD-401-02 — Réaliser dans le périmètre autorisé

- **Phase :** Réaliser dans le périmètre autorisé
- **Statut :** `À faire`
- **Dépendances :** TASK-AUD-401-01

## Objectif

Implémenter `src/audit_exigences/semantic.py` (pré-filtre de paires, prompt, parsing du verdict JSON) et `src/audit_exigences/llm_backends/` (`base`, `fake`, `lmstudio`) ; brancher le CLI (`--epic 4` / `--semantic`).

## Livrable

Findings `semantic_contradiction` produits sur les paires candidates ; abstention propre si le backend est indisponible.
