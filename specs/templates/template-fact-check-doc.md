# Modèle de Fact-Checking Documentaire & Validation Diátaxis

Ce document sert à auditer toute documentation technique produite (guides, API, tutoriels) afin de s’assurer qu’aucune affirmation technique n’est inventée ou découplée du code réel (livrable de clôture de la Gate G2).

---

## 1. Métadonnées du document audité

- **Identifiant :** `FACT-[DOMAINE]-[NUMÉRO]` (ex: `FACT-DOC-001`)
- **Document source audité :** `[Chemin vers le guide markdown, ex: docs/guides/guide-semaphore.md]`
- **Classification Diátaxis :** `Tutoriel` / `Guide pratique (How-To)` / `Référence` / `Explication`
- **Commit du code source de référence :** `[Hash exact]`
- **Auditeur(s) :** `[Noms]`
- **Date :** `AAAA-MM-JJ`

---

## 2. Contrôle de conformité au cadre Diátaxis

| Quadrant Diátaxis | Rôle attendu | Objectif du document | Respecté ? |
|---|---|---|:---:|
| **Tutoriel** | Orienté apprentissage pas-à-pas pour débutant | Faire réussir une première expérience sans digression | Oui / Non / NA |
| **How-To Guide** | Orienté problème / tâche concrète | Guider la réalisation d'une tâche précise | Oui / Non / NA |
| **Référence** | Orienté information technique neutre | Décrire l'API, les constantes, les codes retour de façon exhaustive | Oui / Non / NA |
| **Explication** | Orienté compréhension / architecture | Clarifier les concepts, choix de conception et compromis | Oui / Non / NA |

*Remarque : Un document ne doit pas mélanger les quatre genres dans une même section.*

---

## 3. Matrice de Fact-Checking : Affirmation ↔ Source ↔ Check

Chaque phrase de la documentation affirmant un comportement technique, une valeur par défaut, une contrainte ou une limite doit être auditée :

| ID | Affirmation dans la documentation | Passage textuel exact | Source canonique (Code / Doc officielle) | Commande de check ou test vérificateur | Statut de vérité |
|---|---|---|---|---|:---:|
| `AFF-01` | [Affirmation à vérifier] | [Citation exacte du document] | `[chemin:ligne ou section]` | `[commande ou test]` | **À vérifier** |
| `AFF-02` | [Affirmation confirmée] | [Citation exacte du document] | `[chemin:ligne ou section]` | `[commande ou test exécuté]` | **Prouvé dans la baseline indiquée** |
| `AFF-03` | [Affirmation sans source retrouvée] | [Citation exacte du document] | Non trouvé | Aucune preuve | **Non prouvé — à retirer ou reformuler** |

### Statuts autorisés :
- **Prouvé :** L'affirmation est formellement confirmée par une ligne de code, un test unitaire passant ou une documentation canonique.
- **Partiellement vrai :** L'affirmation est vraie sous certaines conditions non mentionnées dans le texte (nécessite reformulation).
- **Non prouvé :** Aucune source ne permet d'attester l'affirmation (doit être retirée ou formulée comme inconnue).
- **Contredit :** Le code ou le test prouve le contraire de ce qu'affirme le texte (erreur documentaire critique).

---

## 4. Vérification des diagrammes Mermaid

Pour chaque diagramme inséré dans la documentation :
- [ ] Le code Mermaid est syntaxiquement valide (compilable).
- [ ] Les états, transitions et messages correspondent strictement à l'API et au code source réel.
- [ ] Aucune abstraction imaginaire n'a été ajoutée par l'assistant IA.

---

## 5. Bilan d'audit et décision de publication

- Affirmations totales auditées : `[X]`
- Affirmations prouvées : `[X] ([%])`
- Affirmations corrigées / retirées : `[X]`
- Diagrammes validés : `[X]`

**Verdict d'audit :**
- [ ] **Revue documentaire G2 acceptée dans le périmètre et la baseline indiqués**
- [ ] **Publication bloquée — Révision requise sur les affirmations non prouvées**
