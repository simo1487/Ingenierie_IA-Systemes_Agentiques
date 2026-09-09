# Modèle de Matrice de Traçabilité v0

Ce document est le modèle standard pour consigner et vérifier les liens entre exigences, documentation/API, code source et tests automatisés (Livrable clé de la Gate G1 et consolidé en G2).

---

## 1. Métadonnées du référentiel et baselines

- **Identifiant matrice :** `TRAC-[DOMAINE]-[VERSION]` (ex: `TRAC-ZEP-001`)
- **Projet :** [Nom du projet / équipe]
- **Baseline Exigences :** [ex: reqmgmt commit `b9e702780b6dff096bebb151ab724e6c35fe3cd3`, statut `Draft`]
- **Baseline Code / Implémentation :** [ex: Zephyr tag `v4.4.2`, commit `dccb09599635bdff17633fa7e9dab014b91dce90`]
- **Baseline Documentation :** [ex: Documentation Zephyr 4.4.0 / latest]
- **Date de relevé :** `AAAA-MM-JJ`
- **Relecteur :** [Nom de l'ingénieur ayant contrôlé la chaîne]

---

## 2. Tableau de traçabilité v0

| UID Exigence | Titre / Énoncé court | Source & Révision | API publique liée | Fichier code & fonction | Suite de tests liée | Oracle attendu | Statut du lien | Justification / Preuve |
|---|---|---|---|---|---|---|---|---|
| `REQ-001` | Initialisation sémaphore | `docs/sdoc/sem.sdoc:42` | `k_sem_init()` | `kernel/sem.c:k_sem_init` | `tests/.../main.c:test_init` | Valeur du compteur == init | `Vérifié` | Test unitaire exécuté avec succès |
| `REQ-002` | Décrémentation avec timeout | `docs/sdoc/sem.sdoc:58` | `k_sem_take()` | `kernel/sem.c:k_sem_take` | `tests/.../main.c:test_take` | Code retour `0` si ressource disponible | `Candidat` | Scénario écrit, exécution à démontrer |
| `REQ-003` | Appel en contexte ISR | `docs/sdoc/sem.sdoc:89` | `k_sem_give()` | `kernel/sem.c:k_sem_give` | Non trouvé | Retour immédiat sans blocage | `Non trouvé` | Aucun test dédié identifié |

---

## 3. Définition stricte des statuts

1. **`Vérifié` (ou `prouvé`) :** Le lien a été démontré par une preuve concrète (test unitaire exécuté avec succès, code source inspecté à la ligne exacte et validé par un humain).
2. **`Candidat` :** Lien plausible proposé par l'analyse ou l'IA, mais dont l'exécution ou l'exactitude n'a pas encore été formellement validée.
3. **`Observé` :** Entrée présente dans la source brute, mais dont la traçabilité vers les autres couches n'est pas établie.
4. **`Non vérifié` (ou `non trouvé`) :** Exigence sans implémentation ou sans test identifié dans la baseline.
5. **`Bloqué` (ou `non applicable`) :** Exigence hors périmètre ou non testable dans l'environnement actuel.

> **Règle absolue (J02/J03) :** Une proximité lexicale (ex: présence du mot « semaphore » dans un fichier) ne prouve **AUCUNE** relation de couverture ou de traçabilité.

---

## 4. Contrat JSON fermé (Schéma machine-readable)

Pour permettre la validation automatique, chaque matrice doit être convertible selon ce schéma JSON strict :

```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "TraceabilityMatrixV0",
  "type": "object",
  "additionalProperties": false,
  "required": ["matrix_id", "baselines", "items"],
  "properties": {
    "matrix_id": { "type": "string" },
    "baselines": {
      "type": "object",
      "additionalProperties": false,
      "required": ["requirements", "code"],
      "properties": {
        "requirements": { "type": "string" },
        "code": { "type": "string" },
        "documentation": { "type": "string" }
      }
    },
    "items": {
      "type": "array",
      "items": {
        "type": "object",
        "additionalProperties": false,
        "required": ["req_id", "source_path", "api", "code_path", "test_path", "status", "proof"],
        "properties": {
          "req_id": { "type": "string" },
          "source_path": { "type": "string" },
          "api": { "type": "string" },
          "code_path": { "type": "string" },
          "test_path": { "type": "string" },
          "status": {
            "type": "string",
            "enum": ["Observé", "Candidat", "Vérifié", "Non vérifié", "Bloqué"]
          },
          "proof": { "type": "string" }
        }
      }
    }
  }
}
```

---

## 5. Synthèse de couverture et d'inconnues

- Total exigences : `[X]`
- Liens vérifiés : `[X] ([%])`
- Liens candidats : `[X] ([%])`
- Liens non trouvés : `[X] ([%])`
- Points d'ambiguïté restants : `[Liste des questions ouvertes]`
