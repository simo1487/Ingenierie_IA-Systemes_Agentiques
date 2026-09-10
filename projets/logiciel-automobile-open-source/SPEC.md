# SPEC — Sélection de logiciels automobiles open source de référence

## 1. Informations générales

- **Identifiant projet :** `PROJ-OSS-AUTO-001`
- **Équipe :** Logiciel automobile open source
- **Responsables :** Sylvain, Nathalie et Romain
- **Branche :** `feat_list_existing_projects`
- **Statut :** `Candidate`
- **Mission source :** « Recherche d’un logiciel automobile open source avec des exigences qualité » dans `travail.md`
- **Dernière mise à jour :** `2026-09-09`

## 2. Vision et Epic

### `EPIC-OSS-AUTO-001` — Sélectionner des projets open source avec des exigences vérifiables

- **Vision :** constituer une sélection courte de projets automobiles ou embarqués analysés sur des révisions figées.
- **Bénéficiaire principal :** analyste produit et ingénieur exigences.
- **Valeur attendue :** choisir des références sur leurs preuves disponibles plutôt que sur leur popularité.
- **Indicateur de succès :** un tiers reproduit la comparaison et retrouve chaque constat dans la source indiquée.

> En tant qu’analyste produit, je veux comparer des projets open source actifs disposant de code, d’exigences et de mécanismes qualité afin de sélectionner des références fiables sans confondre popularité et maturité.


## 3. Périmètre

### Inclus

- Recherche de projets liés au logiciel automobile ou embarqué.
- Vérification du dépôt canonique, de la licence, de l’activité et de la documentation.
- Inventaire des exigences, tests, contrôles qualité, CI et relations de traçabilité explicitement publiés.
- Comparaison selon une grille commune et recommandation d’un à trois projets.
- Transmission des références retenues au produit d’ingénierie des exigences agentique.

### Exclus

- Déduction d’une certification à partir d’un nom, d’un badge ou d’un README.
- Transformation d’une promesse marketing en exigence vérifiée.
- Exécution de code tiers avant examen des instructions, dépendances et permissions.
- Copie de contenu incompatible avec sa licence.
- Analyse exhaustive d’un grand nombre de projets avant validation de la grille.

## 4. Parties prenantes et décisions humaines réservées

| Partie prenante | Responsabilité | Décision réservée |
|---|---|---|
| Analyste produit | Construire la liste et la comparaison | Définir les critères et recommander les références |
| Ingénieur exigences | Examiner les exigences publiées | Accepter une source comme exploitable |
| Référent licence ou sécurité | Examiner licence et exécution | Autoriser réutilisation et expérimentation |

## 5. Entrées et baselines

| Entrée | Source canonique | Révision / date | Accès | Statut |
|---|---|---|---|---|
| Dépôts candidats | URL canonique propre à chaque projet | Tag ou commit à figer | Lecture seule avant autorisation | `Candidat` |
| Documentation et exigences | Chemins du dépôt ou documentation officielle | Même baseline ou version explicitement reliée | Lecture | `Non vérifié` |
| Grille de sélection | Artefact de l’équipe | Version Git | Écriture par l’équipe | `Candidat` |

## 6. Sorties et preuves attendues

| Sortie | Type d’information | Oracle indépendant |
|---|---|---|
| Liste courte de candidats | `Proposition` | Existence des dépôts et adéquation aux critères approuvés |
| Fiche par projet | `Observation` | Fichiers et passages de la révision figée |
| Matrice comparative | `Proposition` | Application uniforme de la grille |
| Recommandation finale | `Proposition` puis décision humaine | Revue des preuves et critères annoncés |

## 7. User Stories

### `US-OSS-001` — Identifier des candidats

> En tant qu’analyste produit, je veux recenser des projets dans le domaine visé avec leur dépôt canonique afin de constituer une liste vérifiable.

- `RM-OSS-001` — Chaque candidat possède une identité, une URL canonique et une révision à analyser.
- **Nominal :** un projet automobile maintenu est relié à son dépôt officiel.
- **Frontière :** un projet embarqué non spécifiquement automobile reste candidat avec son domaine explicite.
- **Contre-exemple :** une liste secondaire sans dépôt canonique ne suffit pas à retenir un candidat.
- **Critères associés :** `CA-OSS-01`, `CA-OSS-05`.

### `US-OSS-002` — Qualifier chaque projet

> En tant que relecteur, je veux une fiche homogène sur la licence, l’activité, les exigences et la qualité afin de vérifier chaque affirmation.

- `RM-OSS-002` — Une affirmation technique vise un tag, un commit ou une page versionnée et datée.
- **Nominal :** licence, exigences et tests sont retrouvés dans la baseline.
- **Frontière :** une information uniquement disponible hors dépôt est sourcée et distinguée.
- **Contre-exemple :** une exigence déduite du code reste une hypothèse.
- **Critères associés :** `CA-OSS-01`, `CA-OSS-02`, `CA-OSS-03`, `CA-OSS-05`.

### `US-OSS-003` — Comparer avec une grille commune

> En tant que décideur, je veux comparer tous les candidats selon les mêmes champs et règles afin d’éviter une sélection opportuniste.

- `RM-OSS-003` — Un champ absent reste absent ou `Non vérifié`; il n’est pas estimé.
- **Nominal :** deux projets sont évalués avec la même version de la grille.
- **Frontière :** un projet avec données partielles reste comparable avec des lacunes visibles.
- **Contre-exemple :** changer les pondérations après observation des résultats invalide la comparaison sans nouvelle revue.
- **Critères associés :** `CA-OSS-04`, `CA-OSS-05`, `CA-OSS-07`.

### `US-OSS-004` — Recommander les références

> En tant que responsable produit, je veux une recommandation argumentée d’un à trois projets afin d’alimenter les analyses suivantes avec des baselines approuvées.

- `RM-OSS-004` — Popularité, étoiles et forks ne constituent pas à eux seuls une preuve de qualité.
- **Nominal :** un projet est recommandé avec ses points forts, limites et preuves.
- **Frontière :** aucun candidat satisfaisant produit une recommandation vide et motivée.
- **Contre-exemple :** un dépôt sans licence explicite est bloqué pour la réutilisation.
- **Critères associés :** `CA-OSS-06`, `CA-OSS-07`.

## 8. Critères d’acceptation de l’Epic

- [ ] `CA-OSS-01` — Chaque candidat possède une URL canonique, une licence observée ou signalée absente, et une révision analysée.
- [ ] `CA-OSS-02` — Chaque exigence citée est retrouvable dans une source précise.
- [ ] `CA-OSS-03` — Les mécanismes qualité sont observés dans les fichiers de la baseline.
- [ ] `CA-OSS-04` — Tous les candidats sont comparés avec la même version de la grille.
- [ ] `CA-OSS-05` — Les données absentes, proposées ou non vérifiées sont explicitement signalées.
- [ ] `CA-OSS-06` — La sélection finale applique des critères annoncés avant la décision.
- [ ] `CA-OSS-07` — Une autre personne peut reproduire l’examen sur les révisions indiquées.

## 9. Scénarios Gherkin et oracles indépendants

```gherkin
Fonctionnalité: Évaluer des projets open source automobiles

  Scénario: Projet documenté et traçable
    Étant donné un dépôt accessible avec une licence, des exigences et des tests
    Quand l’équipe remplit la grille sur une révision figée
    Alors chaque constat renvoie vers un fichier ou un passage précis
    Et le projet peut être comparé aux autres candidats

  Scénario: Information partielle
    Étant donné un projet dont les exigences publiées sont incomplètes
    Quand sa fiche est produite
    Alors les champs connus sont conservés
    Et les lacunes restent explicitement Non vérifié

  Scénario: Licence absente
    Étant donné un dépôt sans licence explicite
    Quand sa réutilisation est évaluée
    Alors la réutilisation est marquée Bloquée

  Scénario: Aucun candidat admissible
    Étant donné que tous les candidats échouent sur un critère obligatoire annoncé
    Quand la recommandation est produite
    Alors aucun projet n’est recommandé
    Et les motifs de rejet restent traçables
```

| Scénario | User Story | Critères | Oracle indépendant |
|---|---|---|---|
| Projet traçable | `US-OSS-002` | `CA-OSS-01/02/03` | Fichiers de la révision figée |
| Information partielle | `US-OSS-003` | `CA-OSS-05` | Grille et sources disponibles |
| Licence absente | `US-OSS-004` | `CA-OSS-01` | Racine et métadonnées du dépôt |
| Aucun candidat | `US-OSS-004` | `CA-OSS-06` | Critères approuvés avant comparaison |

## 10. Traçabilité Epic → Stories → preuves

| Epic | User Story | Règle | Critères | Livrable / preuve | Statut |
|---|---|---|---|---|---|
| `EPIC-OSS-AUTO-001` | `US-OSS-001` | `RM-OSS-001` | `CA-OSS-01/05` | Liste des candidats | `Candidat` |
| `EPIC-OSS-AUTO-001` | `US-OSS-002` | `RM-OSS-002` | `CA-OSS-01/02/03/05` | Fiches et passages | `Candidat` |
| `EPIC-OSS-AUTO-001` | `US-OSS-003` | `RM-OSS-003` | `CA-OSS-04/05/07` | Matrice comparative | `Candidat` |
| `EPIC-OSS-AUTO-001` | `US-OSS-004` | `RM-OSS-004` | `CA-OSS-06/07` | Décision de sélection | `Candidat` |

## 11. Risques, ambiguïtés et questions ouvertes

| ID | Description | Décision attendue | Statut |
|---|---|---|---|
| `AMB-OSS-001` | Les critères obligatoires et leur éventuelle pondération ne sont pas approuvés. | Figer la grille avant notation. | `Ouvert` |
| `AMB-OSS-002` | La période définissant un projet « actif » n’est pas précisée. | Définir un seuil observable ou retirer ce critère. | `Ouvert` |
| `AMB-OSS-003` | Les règles d’autorisation avant exécution d’un dépôt tiers ne sont pas détaillées. | Établir une checklist de sécurité et un responsable d’approbation. | `Ouvert` |

## 12. Définition de terminé

L’Epic est terminée lorsqu’un à trois projets, ou aucun si les critères l’imposent, sont recommandés à partir de fiches homogènes, de révisions figées et de preuves retrouvables, puis transmis au projet d’ingénierie des exigences agentique.
