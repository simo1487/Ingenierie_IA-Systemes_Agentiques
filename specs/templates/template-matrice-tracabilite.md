# Modèle de Matrice de Traçabilité v0

Ce document est le modèle standard pour consigner et vérifier les liens entre exigences, documentation/API, code source et tests automatisés (Livrable clé de la Gate G1 et consolidé en G2).

---

## 1. Métadonnées du référentiel et baselines

- **Identifiant matrice :** `TRAC-[DOMAINE]-[VERSION]` (ex: `TRAC-QUAL-001`)
- **Projet :** [Nom du projet / équipe]
- **Epic :** `EPIC-[DOMAINE]-[NUMÉRO]`
- **Baseline Exigences :** [chemin ou URL, tag ou commit exact, statut]
- **Baseline Code / Implémentation :** [dépôt canonique, tag ou commit exact]
- **Baseline Documentation :** [source et version exactes]
- **Date de relevé :** `AAAA-MM-JJ`
- **Relecteur :** [Nom de l'ingénieur ayant contrôlé la chaîne]

---

## 2. Tableau de traçabilité v0

| Epic | User Story | UID Exigence | Titre / Énoncé court | Source & Révision | API publique liée | Fichier code & fonction | Suite de tests liée | Oracle attendu | Statut du lien | Justification / Preuve |
|---|---|---|---|---|---|---|---|---|---|---|
| `EPIC-QUAL-001` | `US-QUAL-003` | `REQ-QUAL-001` | Exécuter le profil rapide | `projets/qualite-code/SPEC.md` à une révision figée | `[commande publique]` | `[fichier et symbole]` | `[test nominal]` | Tous les contrôles configurés sont observés | `Candidat` | Exécution à démontrer |
| `EPIC-QUAL-001` | `US-QUAL-003` | `REQ-QUAL-002` | Refuser un défaut bloquant | `projets/qualite-code/SPEC.md` à une révision figée | `[commande publique]` | `[fichier et symbole]` | `[test sur fixture fautive]` | Code non nul et diagnostic localisable | `Non vérifié` | Test non encore identifié |

---

## 3. Définition stricte des statuts

1. **`Vérifié` (ou `prouvé`) :** Le lien a été démontré par une preuve concrète (test unitaire exécuté avec succès, code source inspecté à la ligne exacte et validé par un humain).
2. **`Candidat` :** Lien plausible proposé par l'analyse ou l'IA, mais dont l'exécution ou l'exactitude n'a pas encore été formellement validée.
3. **`Observé` :** Entrée présente dans la source brute, mais dont la traçabilité vers les autres couches n'est pas établie.
4. **`Non vérifié` (ou `non trouvé`) :** Exigence sans implémentation ou sans test identifié dans la baseline.
5. **`Bloqué` (ou `non applicable`) :** Exigence hors périmètre ou non testable dans l'environnement actuel.

> **Règle absolue :** Une proximité lexicale ne prouve **AUCUNE** relation de couverture ou de traçabilité.

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
        "required": ["epic_id", "user_story_id", "req_id", "source_path", "api", "code_path", "test_path", "status", "proof"],
        "properties": {
          "epic_id": { "type": "string", "pattern": "^EPIC-" },
          "user_story_id": { "type": "string", "pattern": "^US-" },
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
