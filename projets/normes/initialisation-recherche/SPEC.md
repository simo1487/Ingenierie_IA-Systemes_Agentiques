# SPEC — Initialisation contrôlée de la recherche de normes

## 1. Informations générales

- **Identifiant projet :** `PROJ-NORM-INIT-001`
- **Projet parent :** `PROJ-NORM-001`
- **Branche :** `feat/initSearchSystem`
- **Statut :** `Candidate`
- **Mission source :** préparer le système de récupération et d’organisation des normes
- **Dernière mise à jour :** `2026-09-09`

## 2. Vision et Epic

### `EPIC-NORM-INIT-001` — Amorcer un corpus de sources reproductible

- **Vision :** fournir au projet Normes une base de collecte relançable, légale et traçable.
- **Bénéficiaire principal :** membre de l’équipe Normes.
- **Valeur attendue :** démarrer l’analyse sans perdre la provenance ni masquer les échecs d’accès.
- **Indicateur de succès :** une autre personne relance la collecte et obtient un manifeste explicite pour chaque source.

> En tant que membre de l’équipe Normes, je veux disposer d’un catalogue sourcé et d’un mécanisme de récupération contrôlé afin de préparer le nettoyage et l’analyse sans perdre la provenance des documents.

## 3. Périmètre

### Inclus

- Catalogue machine-readable des références et métadonnées disponibles.
- Récupération des seules ressources publiquement et légalement accessibles.
- Manifeste des tentatives, redirections, succès et échecs.
- Documentation d’utilisation et des limites du corpus.

### Exclus

- Contournement d’authentification, de paiement ou de protection technique.
- Copie intégrale non autorisée d’un texte protégé.
- Extraction détaillée et validation des exigences, prises en charge par `PROJ-NORM-001`.
- Déclaration de conformité d’un produit.

## 4. Parties prenantes et décisions humaines réservées

| Partie prenante | Responsabilité | Décision réservée |
|---|---|---|
| Mainteneur de la collecte | Maintenir catalogue, script et manifeste | Autoriser une nouvelle source ou un remplacement |
| Équipe Normes | Consommer le corpus initial | Accepter le passage au nettoyage |
| Responsable des droits | Examiner les restrictions | Autoriser la conservation ou redistribution |

## 5. Entrées et baselines

| Entrée | Source canonique | Révision / date | Accès | Statut |
|---|---|---|---|---|
| Liste initiale de références | Actifs historiques du projet Normes | Commit à figer | Lecture | `Observé` |
| Pages et dépôts officiels | URL enregistrée par entrée | Date de consultation par tentative | Réseau en lecture | `Non vérifié` avant collecte |

## 6. Sorties et preuves attendues

| Sortie | Type d’information | Oracle indépendant |
|---|---|---|
| Catalogue de sources | `Observation` | Validation de schéma et ouverture des URL déclarées |
| Ressource récupérée | `Observation` | Code HTTP, empreinte et emplacement du fichier |
| Manifeste d’exécution | `Preuve vérifiée` | Concordance entre tentative contrôlée et statut enregistré |
| Rapport de limites | `Question ouverte` ou `Observation` | Relecture humaine des accès et inconnues |

## 7. User Stories

### `US-NORM-INIT-001` — Enregistrer une référence

> En tant que mainteneur, je veux enregistrer chaque référence avec un identifiant stable, sa source et son édition afin de conserver sa provenance avant toute collecte.

- `RM-NORM-INIT-001` — Une métadonnée inconnue est marquée inconnue, jamais déduite.
- **Nominal :** une source officielle datée complète le catalogue.
- **Frontière :** une édition absente est conservée comme inconnue.
- **Contre-exemple :** une entrée sans identifiant, titre ou source échoue à la validation.
- **Critères associés :** `CA-NORM-INIT-01`, `CA-NORM-INIT-02`.

### `US-NORM-INIT-002` — Récupérer sans contourner les accès

> En tant que mainteneur, je veux tenter la récupération selon une politique explicite afin de conserver les ressources ouvertes et de signaler les restrictions sans les contourner.

- `RM-NORM-INIT-002` — Un refus d’accès est enregistré et met fin à la tentative concernée.
- **Nominal :** une ressource publique est téléchargée et identifiée.
- **Frontière :** une redirection autorisée est distinguée du succès final.
- **Contre-exemple :** une authentification requise ne déclenche aucune tentative de contournement.
- **Critères associés :** `CA-NORM-INIT-03`, `CA-NORM-INIT-04`, `CA-NORM-INIT-06`.

### `US-NORM-INIT-003` — Reproduire une collecte

> En tant que membre de l’équipe Normes, je veux relancer la collecte avec une commande documentée afin de vérifier le manifeste indépendamment de son auteur.

- `RM-NORM-INIT-003` — Une tentative ne remplace pas silencieusement un fichier existant.
- **Nominal :** la commande documentée produit un manifeste complet.
- **Frontière :** aucune ressource disponible produit un manifeste valide sans faux succès.
- **Contre-exemple :** une erreur réseau reste visible et n’est pas requalifiée en succès.
- **Critères associés :** `CA-NORM-INIT-03`, `CA-NORM-INIT-05`, `CA-NORM-INIT-06`.

## 8. Critères d’acceptation de l’Epic

- [ ] `CA-NORM-INIT-01` — Chaque entrée possède un identifiant stable, un titre et une source canonique.
- [ ] `CA-NORM-INIT-02` — L’édition et la date de consultation sont enregistrées ou explicitement inconnues.
- [ ] `CA-NORM-INIT-03` — Le manifeste distingue succès, redirection, accès refusé et erreur réseau.
- [ ] `CA-NORM-INIT-04` — Aucun mécanisme ne contourne une restriction d’accès.
- [ ] `CA-NORM-INIT-05` — Un tiers peut relancer la commande à partir de la documentation.
- [ ] `CA-NORM-INIT-06` — Le catalogue reste exploitable quand aucune copie locale n’est disponible.

## 9. Scénarios Gherkin et oracles indépendants

```gherkin
Fonctionnalité: Initialiser un corpus de normes

  Scénario: Ressource publique disponible
    Étant donné une entrée valide contenant une URL officielle accessible
    Quand la collecte est exécutée
    Alors la ressource est enregistrée à l’emplacement prévu
    Et le manifeste conserve la source et le statut de succès

  Scénario: Édition inconnue
    Étant donné une référence officielle sans édition identifiable
    Quand le catalogue est validé
    Alors l’entrée reste valide avec une édition explicitement inconnue

  Scénario: Ressource protégée
    Étant donné une ressource nécessitant un achat ou une authentification
    Quand le serveur refuse l’accès
    Alors aucun contournement n’est tenté
    Et le manifeste indique que la ressource n’a pas été récupérée

  Scénario: Interruption réseau
    Étant donné une source dont la connexion est interrompue
    Quand la tentative se termine
    Alors aucun succès n’est annoncé
    Et l’erreur est enregistrée dans le manifeste
```

| Scénario | User Story | Critères | Oracle indépendant |
|---|---|---|---|
| Ressource publique | `US-NORM-INIT-002` | `CA-NORM-INIT-03` | Réponse de la source et empreinte du fichier |
| Édition inconnue | `US-NORM-INIT-001` | `CA-NORM-INIT-02` | Schéma du catalogue |
| Ressource protégée | `US-NORM-INIT-002` | `CA-NORM-INIT-04` | Réponse d’accès et absence de fichier |
| Interruption réseau | `US-NORM-INIT-003` | `CA-NORM-INIT-03/06` | État réseau contrôlé et manifeste |

## 10. Traçabilité Epic → Stories → preuves

| Epic | User Story | Règle | Critères | Livrable / preuve | Statut |
|---|---|---|---|---|---|
| `EPIC-NORM-INIT-001` | `US-NORM-INIT-001` | `RM-NORM-INIT-001` | `CA-NORM-INIT-01/02` | Catalogue | `Candidat` |
| `EPIC-NORM-INIT-001` | `US-NORM-INIT-002` | `RM-NORM-INIT-002` | `CA-NORM-INIT-03/04/06` | Ressources et manifeste | `Candidat` |
| `EPIC-NORM-INIT-001` | `US-NORM-INIT-003` | `RM-NORM-INIT-003` | `CA-NORM-INIT-03/05/06` | Procédure de reproduction | `Candidat` |

## 11. Risques, ambiguïtés et questions ouvertes

| ID | Description | Décision attendue | Statut |
|---|---|---|---|
| `AMB-NORM-INIT-001` | Le format canonique du catalogue reste à choisir entre YAML et CSV. | Choisir un format et son schéma avant implémentation maintenue. | `Ouvert` |
| `AMB-NORM-INIT-002` | La politique de remplacement d’un fichier existant n’est pas définie. | Décider refus, versionnement ou remplacement explicite. | `Ouvert` |
| `AMB-NORM-INIT-003` | Les délais et nombres de redirections autorisés ne sont pas fixés. | Définir les bornes avant les tests réseau. | `Ouvert` |

## 12. Définition de terminé

L’Epic est terminée lorsqu’un tiers valide le catalogue, relance la collecte sans secret, retrouve chaque résultat dans le manifeste et peut transmettre les sorties au projet Normes sans rechercher à nouveau leur provenance.
