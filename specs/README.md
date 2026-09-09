# Architecture de la documentation des spécifications

Ce dossier centralise l'architecture documentaire du projet, structurée selon les principes d'ingénierie logicielle rigoureuse et les enseignements des trois premiers jours de formation :
- **J01 :** Cadrage, frontières de confiance, baselines figées, distinction formelle entre *Proposition*, *Observation*, *Preuve vérifiée* et *Question ouverte*.
- **J02 :** Analyse d'exigences, Example Mapping, scénarios Gherkin, oracles indépendants et matrice de traçabilité v0 en lecture seule.
- **J03 :** Enquête falsifiable, reproduction avant correction, cycle Red–Green–Refactor, tests de mutation, revue assistée avec tri des faux positifs, et documentation Doc-as-Code (Diátaxis & fact-checking).

---

## 1. Organisation de l'arborescence

```text
FormationIaProject/
├── specs/
│   ├── README.md                      # Guide d'architecture et règles documentaires (ce fichier)
│   ├── ordre-et-etapes.md             # Référentiel des étapes à respecter dans l'ordre strict
│   ├── templates/                     # Modèles normalisés pour chaque type d'artefact
│   │   ├── template-feature-spec.md   # Spécification détaillée d'une exigence / feature
│   │   ├── template-example-mapping.md# Fiche d'atelier Example Mapping & table de décision
│   │   ├── template-matrice-tracabilite.md # Matrice v0 exigences ↔ doc ↔ code ↔ tests
│   │   ├── template-enquete-reproduction.md # Carnet d'enquête et fiche de reproduction de bug
│   │   ├── template-revue-qualite.md  # Rapport de revue assistée par IA et analyse statique
│   │   └── template-fact-check-doc.md # Matrice de vérification documentaire (affirmation → check)
│   ├── matrices/                      # Matrices de traçabilité v0 effectives des équipes
│   └── enquetes/                      # Carnets d'enquêtes et reproductions effectives
├── projets/                           # Spécifications de niveau macro par équipe / mission
│   ├── README.md                      # Index des projets et règles communes
│   ├── socle-commun/SPEC.md           # PROJ-SOCLE-001 (Intégration develop)
│   ├── normes/                        # PROJ-NORM-001 (Alain + Moustapha)
│   ├── qualite-code/                  # PROJ-QUAL-001 (Eric + Céline + Damien)
│   ├── logiciel-automobile-open-source/# PROJ-OSS-AUTO-001 (Sylvain + Nathalie + Romain)
│   └── exigences-zephyr/              # PROJ-ZEPHYR-REQ-001 (Mohammed + Florient)
├── travail.md                         # Répartition opérationnelle des équipes et branches
└── template-feature-spec.md           # Raccourci vers specs/templates/template-feature-spec.md
```

---

## 2. Nomenclature et typologie des identifiants

Chaque document et chaque élément de spécification porte un identifiant unique et pérenne :

| Préfixe | Type de document / artefact | Exemple | Rôle |
|---|---|---|---|
| `PROJ-` | Spécification de projet / équipe | `PROJ-QUAL-001` | Cadrage de haut niveau de la mission d'une équipe |
| `FEAT-` | Spécification de feature / exigence | `FEAT-QUAL-001` | Définition détaillée d'une fonctionnalité avec scénarios et critères |
| `CA-` | Critère d'acceptation | `CA-QUAL-01` | Condition observable et vérifiable validant un comportement |
| `ENQ-` | Carnet d'enquête et reproduction | `ENQ-SEM-001` | Démarche falsifiable, preuve rouge et condition de reproduction |
| `TRAC-` | Matrice de traçabilité v0 | `TRAC-ZEP-001` | Chaîne de liens inspectables entre exigences, doc, code et tests |
| `REV-` | Rapport de revue et qualité | `REV-CPP-001` | Audit de règles, statique/dynamique et tri des faux positifs |
| `FACT-` | Matrice de fact-checking | `FACT-DOC-001` | Vérification des affirmations textuelles contre le code/tests |

---

## 3. Typologie des informations (Règle d'or J01)

Aucune affirmation ne doit être formulée sans que sa nature soit explicitement qualifiée :

1. **Proposition :** Énoncé généré par un modèle d'IA, une hypothèse de travail ou une suggestion. *N'a aucune valeur de preuve tant qu'elle n'est pas vérifiée.*
2. **Observation :** Constat direct et neutre relevé dans une source identifiée (fichier, commit, ligne de code, documentation officielle), sans inférence ni extrapolation.
3. **Preuve vérifiée :** Résultat d'une exécution contrôlée et reproductible (test unitaire passant, compilation réussie, hash vérifié, code retour documenté).
4. **Question ouverte / Inconnue :** Écart identifié, information manquante ou choix non tranché. *Les inconnues doivent rester visibles et ne jamais être comblées artificiellement par l'IA.*

---

## 4. Statuts formels d'une exigence ou d'un lien (J02 / J03)

| Statut | Signification | Transition autorisée vers |
|---|---|---|
| `Observé` | Mentionné textuellement dans une source identifiée mais relation non testée | `Candidat`, `Non vérifié` |
| `Candidat` | Proposition plausible issue d'une extraction ou d'une analyse, en attente de test | `Vérifié`, `Non vérifié`, `Bloqué` |
| `Vérifié` | Preuve formelle apportée (test exécuté avec succès, oracle indépendant validé) | Ne peut être rétrogradé que sur régression |
| `Non vérifié` | Donnée conservée pour traçabilité mais non démontrée | `Candidat`, `Bloqué` |
| `Bloqué` | Travail impossible sans accès, décision d'architecture ou dépendance manquante | `Candidat` après résolution du blocage |

> **Règle absolue :** Une proximité lexicale (mots clés similaires, nom de fonction approchant) ne constitue **JAMAIS** une relation de traçabilité.

---

## 5. Cycle de vie d'une spécification

```mermaid
flowchart TD
    D[1. Draft / Ébauche] -->|Example Mapping & Gherkin| C[2. Candidate]
    C -->|Oracles indépendants & Revue| R[3. In Review]
    R -->|Gate G1 franchie| V[4. Validated]
    V -->|Implémentation Red-Green & Gate G2| I[5. Integrated on develop]
    R -->|Lacunes ou ambiguïtés| D
```

1. **Draft :** Rédaction initiale du besoin, du périmètre et des questions ouvertes.
2. **Candidate :** Modèle complété avec critères d'acceptation observables, Example Mapping et scénarios Gherkin.
3. **In Review :** Relecture croisée par une autre équipe ou un reviewer. Vérification des oracles indépendants (non-tautologiques).
4. **Validated :** Spécification satisfaisant la Gate correspondante (G1 pour conception des tests, G2 pour preuves d'exécution).
5. **Integrated :** Fusionnée dans la branche `develop` après respect de tous les critères.

---

## 6. Références aux guides et templates

- [Points et étapes à respecter dans l'ordre strict](./ordre-et-etapes.md)
- [Template Feature Spec](./templates/template-feature-spec.md)
- [Template Example Mapping](./templates/template-example-mapping.md)
- [Template Matrice de Traçabilité](./templates/template-matrice-tracabilite.md)
- [Template Enquête & Reproduction](./templates/template-enquete-reproduction.md)
- [Template Revue Qualité & Faux Positifs](./templates/template-revue-qualite.md)
- [Template Fact-Check Documentation](./templates/template-fact-check-doc.md)
