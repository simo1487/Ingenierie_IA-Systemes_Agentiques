---
description: "Règles de sécurité, moindre privilège, préservation d'upstream et discipline des branches Git"
trigger: always_on
---

# Règle : Sécurité, Permissions et Discipline des Branches Git

## 1. Principe du moindre privilège
- **`ALLOW` :** Inspection de code, recherche sémantique, lecture de documentation et extraction d'exigences (`read`, `grep`, `glob`).
- **`CONFIRM / ASK` :** Toute écriture de fichier, création de commit, exécution de commande système.
- **`DENY` :**
  - Modification, suppression ou écriture dans `upstream/**` (strictement en lecture seule).
  - Modification directe de la branche `main`.
  - Exécution de commandes manipulant des clés d'API, tokens ou identifiants sensibles.
  - Contournement de paywalls ou de protections légales de normes protégées.

## 2. Discipline des branches de travail
- Chaque contributeur ou équipe travaille exclusivement dans le périmètre de la branche qui lui est attribuée dans [`travail.md`](../../travail.md) :
  - Équipe 1 (Normes) : `feat/GetNormes` et `feat/initSearchSystem`
  - Équipe 2 (Qualité du code) : `feat_Cppcheck`
  - Équipe 3 (Logiciel auto open source) : `feat_list_existing_projects`
  - Équipe 4 (Exigences Zephyr) : `feat_getReq`
  - Intégration : `develop`
- Synchroniser régulièrement sa branche avec `develop` avant toute demande de revue.
- Ne jamais commiter de fichiers personnels, temporaires, caches (`__pycache__`, `.DS_Store`) ou volumineux sans accord explicite.
