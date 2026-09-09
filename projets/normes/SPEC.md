# SPEC — Corpus de normes exploitable et traçable

## 1. Informations générales

- **Identifiant projet :** `PROJ-NORM-001`
- **Équipe :** Normes
- **Responsables :** Alain et Moustapha
- **Branche :** `feat/GetNormes`
- **Statut :** `Candidate`
- **Mission source :** « Récupération et nettoyage des normes » dans `travail.md`
- **Dernière mise à jour :** `2026-09-09`

## 2. Vision et Epic

### `EPIC-NORM-001` — Mettre à disposition un corpus normatif maîtrisé

- **Vision :** transformer les références collectées en données cohérentes, sourcées et réutilisables.
- **Bénéficiaire principal :** analyste d’exigences.
- **Valeur attendue :** rechercher des obligations ou recommandations sans confondre texte source, reformulation et interprétation.
- **Indicateur de succès :** un tiers peut parser le corpus, retrouver la provenance d’un échantillon et reproduire les décisions de nettoyage.

> En tant qu’analyste d’exigences, je veux consulter des règles normalisées avec leur provenance et leur statut afin de préparer une spécification sans confondre réglementation, norme, guide et interprétation.

## 3. Périmètre

### Inclus

- Qualification des sources, éditions, dates et restrictions d’accès.
- Déduplication et normalisation des métadonnées.
- Classement selon une taxonomie documentée.
- Extraction de règles candidates dans un format tabulaire stable.
- Conservation d’un passage autorisé ou d’un pointeur source précis.
- Rapport des décisions, incohérences et informations manquantes.

### Exclus

- Invention ou récupération non autorisée du contenu d’une norme.
- Avis juridique, certification ou décision automatique d’applicabilité.
- Présentation d’une reformulation comme une citation officielle.

## 4. Parties prenantes et décisions humaines réservées

| Partie prenante | Besoin ou responsabilité | Décision réservée |
|---|---|---|
| Analyste d’exigences | Rechercher et comparer les règles | Confirmer l’interprétation et l’applicabilité |
| Responsable du corpus | Garantir stabilité et provenance | Valider fusion, catégorie et changement d’identifiant |
| Expert métier ou juridique | Examiner les contenus protégés | Autoriser l’usage et statuer sur la portée normative |

## 5. Entrées et baselines

| Entrée | Source canonique | Révision / date | Accès | Statut |
|---|---|---|---|---|
| Catalogue initial | `normes-software-embarque-automobile/` | À figer avant traitement | Lecture seule pendant l’analyse | `Observé` |
| Ressources originales | Organismes et éditeurs identifiés dans le catalogue | Édition propre à chaque entrée | Selon droits déclarés | `Non vérifié` jusqu’à revue |
| Prototype de collecte | `projets/normes/initialisation-recherche/SPEC.md` | Version Git du lot | Lecture | `Candidat` |

## 6. Sorties et preuves attendues

| Sortie | Type d’information | Oracle indépendant |
|---|---|---|
| Catalogue normalisé | `Observation` | Validation de schéma et comparaison aux métadonnées sources |
| Règles extraites | `Proposition` puis `Preuve vérifiée` après revue | Passage source retrouvé dans l’édition déclarée |
| Table de correspondance | `Observation` | Contrôle un-à-un entre identifiants historiques et normalisés |
| Journal de nettoyage | `Observation` | Relecture des décisions et de leur auteur |

## 7. User Stories

### `US-NORM-001` — Qualifier chaque source

> En tant que responsable du corpus, je veux enregistrer l’identité, l’édition, la provenance et les droits d’accès de chaque source afin d’empêcher toute attribution ou utilisation non démontrée.

- `RM-NORM-001` — Une édition inconnue reste explicitement inconnue.
- **Nominal :** une publication officielle datée est enregistrée avec son édition et son URL.
- **Frontière :** une source accessible mais sans édition conserve `édition inconnue`.
- **Contre-exemple :** une ressource protégée n’est ni copiée ni contournée.
- **Critères associés :** `CA-NORM-01`, `CA-NORM-04`, `CA-NORM-06`.

### `US-NORM-002` — Normaliser le catalogue

> En tant qu’analyste, je veux un catalogue sans doublons silencieux et conforme à un schéma stable afin de l’exploiter avec des outils standards.

- `RM-NORM-002` — Deux éditions d’une même norme restent deux versions distinctes.
- **Nominal :** deux entrées réellement identiques sont rapprochées avec une décision consignée.
- **Frontière :** deux titres identiques avec éditions différentes restent séparés.
- **Contre-exemple :** un identifiant dupliqué fait échouer le contrôle structurel.
- **Critères associés :** `CA-NORM-02`, `CA-NORM-03`, `CA-NORM-08`.

### `US-NORM-003` — Extraire des règles candidates

> En tant qu’ingénieur exigences, je veux distinguer citation, reformulation et interprétation afin de réutiliser le corpus sans fabriquer de preuve.

- `RM-NORM-003` — Une règle sans passage retrouvable ne peut pas recevoir le statut `Vérifié`.
- **Nominal :** une reformulation est reliée à un passage source et revue humainement.
- **Frontière :** un pointeur précis remplace la citation lorsque la reproduction est interdite.
- **Contre-exemple :** un texte généré sans source reste `Candidat` ou `Non vérifié`.
- **Critères associés :** `CA-NORM-01`, `CA-NORM-05`, `CA-NORM-07`.

### `US-NORM-004` — Publier un corpus reproductible

> En tant que consommateur du corpus, je veux disposer des données, décisions et limites dans des formats documentés afin de reproduire leur contrôle.

- `RM-NORM-004` — Le CSV utilise UTF-8, un en-tête unique et un nombre constant de colonnes.
- **Nominal :** un parseur CSV standard charge toutes les lignes.
- **Frontière :** un corpus vide conserve le schéma et signale l’absence de données.
- **Contre-exemple :** une ligne mal formée bloque la publication.
- **Critères associés :** `CA-NORM-03`, `CA-NORM-08`.

## 8. Critères d’acceptation de l’Epic

- [ ] `CA-NORM-01` — Chaque règle possède une source, une édition connue ou signalée inconnue, et un statut.
- [ ] `CA-NORM-02` — Aucun identifiant de règle n’est dupliqué dans le corpus publié.
- [ ] `CA-NORM-03` — Les fichiers tabulaires passent un parseur CSV standard en UTF-8.
- [ ] `CA-NORM-04` — Les éditions différentes ne sont jamais fusionnées silencieusement.
- [ ] `CA-NORM-05` — Citations, reformulations et interprétations sont distinguées.
- [ ] `CA-NORM-06` — Aucun contenu protégé n’est reproduit ou obtenu sans autorisation.
- [ ] `CA-NORM-07` — Un relecteur retrouve le passage associé à chaque élément d’un échantillon défini avant la revue.
- [ ] `CA-NORM-08` — Le rapport liste les décisions de nettoyage, limites et questions ouvertes.

## 9. Scénarios Gherkin et oracles indépendants

```gherkin
Fonctionnalité: Publier un corpus normatif traçable

  Scénario: Règle traçable
    Étant donné une règle candidate associée à une édition et un passage source
    Quand un relecteur compare le texte produit au passage
    Alors il peut accepter ou refuser le statut Vérifié
    Et la décision et sa date sont conservées

  Scénario: Éditions homonymes
    Étant donné deux sources de même titre mais d’éditions différentes
    Quand le catalogue est normalisé
    Alors deux versions distinctes sont conservées

  Scénario: Source insuffisante
    Étant donné une règle sans édition ni passage retrouvable
    Quand le corpus est contrôlé
    Alors la règle reste Non vérifié ou Bloqué
    Et elle n’est pas présentée comme une obligation démontrée

  Scénario: Fichier tabulaire invalide
    Étant donné une ligne dont le nombre de colonnes diffère de l’en-tête
    Quand le contrôle de publication est exécuté
    Alors le contrôle échoue
```

| Scénario | User Story | Critères | Oracle indépendant |
|---|---|---|---|
| Règle traçable | `US-NORM-003` | `CA-NORM-01`, `CA-NORM-07` | Passage de la source versionnée et décision humaine |
| Éditions homonymes | `US-NORM-002` | `CA-NORM-04` | Métadonnées d’édition des sources |
| Source insuffisante | `US-NORM-001` | `CA-NORM-05` | Registre de provenance |
| Fichier invalide | `US-NORM-004` | `CA-NORM-03` | Parseur CSV indépendant |

## 10. Traçabilité Epic → Stories → preuves

| Epic | User Story | Règle | Critères | Livrable / preuve | Statut |
|---|---|---|---|---|---|
| `EPIC-NORM-001` | `US-NORM-001` | `RM-NORM-001` | `CA-NORM-01/04/06` | Registre des sources | `Candidat` |
| `EPIC-NORM-001` | `US-NORM-002` | `RM-NORM-002` | `CA-NORM-02/03/08` | Catalogue et journal | `Candidat` |
| `EPIC-NORM-001` | `US-NORM-003` | `RM-NORM-003` | `CA-NORM-01/05/07` | Corpus revu | `Candidat` |
| `EPIC-NORM-001` | `US-NORM-004` | `RM-NORM-004` | `CA-NORM-03/08` | Rapport de validation | `Candidat` |

## 11. Risques, ambiguïtés et questions ouvertes

| ID | Description | Décision attendue | Statut |
|---|---|---|---|
| `AMB-NORM-001` | La révision exacte du catalogue initial n’est pas figée dans cette spécification. | Enregistrer le commit de départ avant transformation. | `Ouvert` |
| `AMB-NORM-002` | La taxonomie finale et ses règles de fusion ne sont pas approuvées. | Faire valider le vocabulaire contrôlé. | `Ouvert` |
| `AMB-NORM-003` | La taille de l’échantillon de revue n’est pas définie. | Fixer l’échantillon avant mesure de `CA-NORM-07`. | `Ouvert` |

## 12. Définition de terminé

L’Epic est terminée lorsque les quatre User Stories sont acceptées, que les données passent les contrôles structurels, qu’un tiers reproduit la revue de provenance et que les ambiguïtés bloquantes sont tranchées ou explicitement acceptées.
