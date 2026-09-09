# SPEC — Socle commun et intégration du portefeuille

## 1. Informations générales

- **Identifiant projet :** `PROJ-SOCLE-001`
- **Responsable :** responsable d’intégration du dépôt
- **Contributeurs :** les quatre équipes décrites dans `travail.md`
- **Branche :** `develop`
- **Statut :** `Candidate`
- **Mission source :** intégration des projets dans un monorepo vérifiable
- **Dernière mise à jour :** `2026-09-09`

## 2. Vision et Epic

### `EPIC-SOCLE-001` — Intégrer des projets autonomes sans perdre leur provenance

- **Vision :** maintenir un socle stable où chaque projet possède sa propre spécification, ses contrôles et ses preuves.
- **Bénéficiaire principal :** responsable d’intégration et équipes contributrices.
- **Valeur attendue :** examiner et intégrer les livrables sans mélanger les responsabilités ni promouvoir une proposition en preuve.
- **Indicateur de succès :** chaque branche candidate est attribuable, vérifiable et intégrable selon une décision consignée.

> En tant que responsable d’intégration, je veux appliquer des conventions et Gates communes à des projets autonomes afin d’intégrer uniquement des livrables attribuables, reproductibles et explicitement revus.

## 3. Périmètre

### Inclus

- Architecture commune et index des projets.
- Modèles Epic, User Stories, features, critères, scénarios et preuves.
- Contrôles génériques du dépôt et règles de revue.
- Vérification de la synchronisation, de la provenance et des statuts avant intégration.
- Journal des décisions d’acceptation, refus ou ajournement.

### Exclus

- Réalisation des recherches ou implémentations spécialisées à la place des équipes.
- Validation réglementaire ou certification des résultats.
- Fusion d’un contenu dont la provenance, le propriétaire ou le statut n’est pas explicite.
- Substitution des contrôles racine aux tests propres à chaque projet.

## 4. Parties prenantes et décisions humaines réservées

| Partie prenante | Responsabilité | Décision réservée |
|---|---|---|
| Responsable d’intégration | Maintenir le socle et conduire les revues | Accepter, ajourner ou refuser une intégration |
| Responsable de projet | Fournir spec, livrables et preuves | Déclarer le lot candidat à la revue |
| Relecteur croisé | Reproduire les contrôles | Confirmer ou contredire les preuves |

## 5. Entrées et baselines

| Entrée | Source canonique | Révision / date | Accès | Statut |
|---|---|---|---|---|
| Missions et branches | `travail.md` | Version Git de la revue | Lecture | `Observé` |
| Spécifications | `projets/*/SPEC.md` | Commit de la branche candidate | Lecture | Selon chaque projet |
| Différences de branche | Git | Commit candidat et base `develop` | Lecture | `Observation` |
| Résultats de vérification | Dossier de preuves du projet | Run et environnement identifiés | Lecture | `Non vérifié` avant reproduction |

## 6. Sorties et preuves attendues

| Sortie | Type d’information | Oracle indépendant |
|---|---|---|
| Index et conventions | `Observation` | Contrôle des liens et de l’arborescence réelle |
| Rapport des contrôles communs | `Preuve vérifiée` | Code retour de `make check` |
| Revue d’un projet | `Observation` et `Question ouverte` | Critères de la SPEC et commandes du README |
| Décision d’intégration | `Preuve vérifiée` | Identité du décideur, commit et réserves consignés |

## 7. User Stories

### `US-SOCLE-001` — Enregistrer un projet autonome

> En tant que responsable de projet, je veux un emplacement, une branche, une Epic et des User Stories identifiés afin que mon périmètre soit explicite.

- `RM-SOCLE-001` — Chaque projet possède un identifiant, un propriétaire, une branche et une spécification liée depuis l’index.
- **Nominal :** un nouveau projet suit le modèle et apparaît dans l’index.
- **Frontière :** un prototype rattaché possède son Epic propre et un lien vers son projet parent.
- **Contre-exemple :** un dossier sans propriétaire ni SPEC ne devient pas un projet intégrable.
- **Critères associés :** `CA-SOCLE-01`, `CA-SOCLE-02`.

### `US-SOCLE-002` — Vérifier un lot candidat

> En tant que relecteur croisé, je veux exécuter les contrôles communs et ceux du projet afin d’obtenir des résultats reproductibles avant décision.

- `RM-SOCLE-002` — Un contrôle non exécuté n’est jamais déclaré réussi.
- **Nominal :** les commandes documentées passent sur le commit candidat.
- **Frontière :** un projet documentaire sans build exécute les validations applicables et signale les contrôles non pertinents.
- **Contre-exemple :** une commande absente ou un résultat non reproductible ajourne la preuve concernée.
- **Critères associés :** `CA-SOCLE-03`, `CA-SOCLE-04`, `CA-SOCLE-05`.

### `US-SOCLE-003` — Décider l’intégration

> En tant que responsable d’intégration, je veux examiner critères, provenance, risques et questions ouvertes afin de rendre une décision explicite sans surévaluer les résultats.

- `RM-SOCLE-003` — Une fusion ne transforme jamais une proposition en information vérifiée.
- **Nominal :** un lot synchronisé et vérifié reçoit une décision attribuée.
- **Frontière :** une question ouverte non bloquante est acceptée avec réserve explicite.
- **Contre-exemple :** une affirmation de conformité non démontrée empêche son intégration comme preuve.
- **Critères associés :** `CA-SOCLE-06`, `CA-SOCLE-07`.

### `US-SOCLE-004` — Préserver l’historique et les frontières

> En tant que contributeur, je veux que les actifs historiques, sources tierces et changements fonctionnels restent séparés afin de relire l’évolution sans ambiguïté.

- `RM-SOCLE-004` — Aucun chemin `upstream/**` n’est modifié et une migration n’est pas mélangée à une évolution fonctionnelle.
- **Nominal :** une migration dédiée conserve l’historique Git.
- **Frontière :** un fichier tiers nécessaire reste référencé en lecture seule.
- **Contre-exemple :** cache, secret ou actif personnel n’est pas intégré.
- **Critères associés :** `CA-SOCLE-04`, `CA-SOCLE-05`, `CA-SOCLE-07`.

## 8. Critères d’acceptation de l’Epic

- [ ] `CA-SOCLE-01` — Chaque mission est reliée à une branche, un propriétaire et une SPEC contenant une Epic et des User Stories.
- [ ] `CA-SOCLE-02` — Chaque Story définit valeur, règle, exemples, critères et traçabilité.
- [ ] `CA-SOCLE-03` — Chaque branche candidate est synchronisée avec `develop` au moment de la revue.
- [ ] `CA-SOCLE-04` — Les contrôles communs et les tests applicables du projet sont exécutés et leurs résultats consignés.
- [ ] `CA-SOCLE-05` — Les sources, révisions et statuts de vérification sont conservés.
- [ ] `CA-SOCLE-06` — Aucune revendication de conformité non démontrée n’est intégrée comme preuve.
- [ ] `CA-SOCLE-07` — La décision, le commit examiné, les réserves et questions ouvertes sont consignés.

## 9. Scénarios Gherkin et oracles indépendants

```gherkin
Fonctionnalité: Intégrer un livrable de projet

  Scénario: Projet prêt pour la revue
    Étant donné une branche synchronisée avec develop
    Et une Epic dont les User Stories candidates possèdent des preuves
    Quand le relecteur exécute les contrôles documentés
    Alors il peut reproduire les résultats
    Et le responsable consigne une décision sur le commit examiné

  Scénario: Prototype rattaché
    Étant donné un prototype avec un projet parent explicite
    Quand l’index et sa spécification sont contrôlés
    Alors son périmètre et son passage vers le parent sont retrouvables

  Scénario: Provenance insuffisante
    Étant donné une affirmation sans source identifiable
    Quand la branche est examinée
    Alors l’affirmation reste Non vérifié
    Et elle n’est pas utilisée comme preuve d’intégration

  Scénario: Contrôle interrompu
    Étant donné un contrôle applicable démarré sur le commit candidat
    Quand son exécution est interrompue ou dépasse sa limite
    Alors aucun succès n’est enregistré pour ce contrôle
    Et la décision mentionne l’état inconclusif
```

| Scénario | User Story | Critères | Oracle indépendant |
|---|---|---|---|
| Projet prêt | `US-SOCLE-002/03` | `CA-SOCLE-03/04/07` | Git, commandes documentées et décision humaine |
| Prototype rattaché | `US-SOCLE-001` | `CA-SOCLE-01/02` | Index et SPEC parent |
| Provenance insuffisante | `US-SOCLE-003` | `CA-SOCLE-05/06` | Source absente du dossier de preuves |
| Contrôle interrompu | `US-SOCLE-002` | `CA-SOCLE-04` | Code retour ou timeout du processus |

## 10. Traçabilité Epic → Stories → preuves

| Epic | User Story | Règle | Critères | Livrable / preuve | Statut |
|---|---|---|---|---|---|
| `EPIC-SOCLE-001` | `US-SOCLE-001` | `RM-SOCLE-001` | `CA-SOCLE-01/02` | Index et SPEC | `Candidat` |
| `EPIC-SOCLE-001` | `US-SOCLE-002` | `RM-SOCLE-002` | `CA-SOCLE-03/04/05` | Résultats de contrôles | `Candidat` |
| `EPIC-SOCLE-001` | `US-SOCLE-003` | `RM-SOCLE-003` | `CA-SOCLE-06/07` | Décision de revue | `Candidat` |
| `EPIC-SOCLE-001` | `US-SOCLE-004` | `RM-SOCLE-004` | `CA-SOCLE-04/05/07` | Historique et inspection | `Candidat` |

## 11. Risques, ambiguïtés et questions ouvertes

| ID | Description | Décision attendue | Statut |
|---|---|---|---|
| `AMB-SOCLE-001` | Le format persistant des décisions d’intégration n’est pas défini. | Choisir l’artefact et son emplacement. | `Ouvert` |
| `AMB-SOCLE-002` | Les conditions autorisant une question ouverte non bloquante ne sont pas formalisées. | Définir la politique de réserve. | `Ouvert` |
| `AMB-SOCLE-003` | Les branches historiques ne suivent pas toutes une convention homogène. | Conserver les noms attribués ou planifier une migration distincte. | `Ouvert` |

## 12. Définition de terminé

L’Epic est terminée lorsque les six spécifications du portefeuille suivent la hiérarchie Epic → User Stories, que leurs contrôles applicables sont reproductibles et que chaque décision d’intégration est attribuée, sourcée et assortie de ses réserves.
