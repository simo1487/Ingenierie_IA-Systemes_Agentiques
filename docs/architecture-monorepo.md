# Architecture du monorepo

## Objectifs

L’organisation doit permettre de retrouver rapidement une expérimentation, son code, ses tests et ses preuves, même lorsque les projets utilisent des langages différents. Le dépôt partage uniquement les conventions transverses ; chaque projet reste autonome pour son outillage.

## Arborescence cible

```text
FormationIaProject/
├── .devin/                         # Configuration de l’assistant
├── .githooks/                      # Contrôles Git rapides et indépendants des langages
├── docs/                           # Architecture et conventions du dépôt
├── projets/
│   ├── <slug-projet>/
│   │   ├── README.md               # Point d’entrée, commandes et état du projet
│   │   ├── SPEC.md                 # Périmètre et critères d’acceptation
│   │   ├── experiments/            # Essais jetables mais reproductibles
│   │   │   └── <YYYY-MM-DD>-<sujet>/
│   │   │       └── README.md       # Hypothèse, protocole, résultat et décision
│   │   ├── src/                    # Code destiné à être maintenu
│   │   ├── tests/                  # Tests automatisés du projet
│   │   ├── docs/                   # Documentation propre au projet
│   │   ├── data/                   # Petites données redistribuables et documentées
│   │   └── evidence/               # Rapports synthétiques et preuves versionnées
│   └── _template/                  # Convention de création d’un nouveau projet
├── shared/                         # À créer seulement lorsqu’un actif est réellement partagé
├── specs/                          # Méthode et modèles communs de spécification
├── tools/                          # Contrôles génériques sans dépendance du monorepo
└── workflows/                      # Processus G0, G1, G2 et intégration
```

## Responsabilités des emplacements

### `projets/<slug>/experiments/`

Un dossier d’expérience répond à une seule hypothèse. Son `README.md` indique l’objectif, les entrées, la commande exacte, le résultat observé et la décision. Une expérience n’est pas une preuve d’intégration et son code ne devient pas automatiquement du code maintenu.

### `projets/<slug>/src/` et `tests/`

Le code maintenu et les tests restent côte à côte dans leur projet. Chaque projet documente ses commandes dans son `README.md` au lieu d’imposer un gestionnaire de paquets global. Les conventions Python, C/C++, JavaScript ou d’un autre langage restent locales au projet.

### `projets/<slug>/evidence/`

Ce dossier contient des éléments petits, stables et relisibles : synthèse de test, matrice de traçabilité, décision de revue, empreinte d’une source. Les caches, binaires de build et rapports bruts volumineux n’y sont pas versionnés.

### `shared/`

Ne créer un actif partagé qu’après un second usage réel. Les utilitaires propres à une seule expérience restent dans le projet concerné afin d’éviter une abstraction prématurée.

### `tools/` et `.githooks/`

Ils ne contiennent que les contrôles transverses rapides : encodage, marqueurs de conflit, espaces finaux, syntaxe Python/JSON/TOML/shell et protection des sources. Les compilations et tests fonctionnels restent sous la responsabilité de chaque projet.

## Convention d’un projet

Le nom de dossier utilise un slug stable en minuscules avec tirets. Chaque projet possède au minimum :

- un `README.md` avec objectif, équipe, branche, état, commandes et arborescence réelle ;
- un `SPEC.md` avec périmètre, exclusions et critères d’acceptation ;
- des commandes locales explicites pour tester et vérifier ;
- une séparation visible entre expériences, code maintenu et preuves.

Les dossiers ne sont créés que lorsqu’ils contiennent un premier artefact utile ; aucun ensemble de répertoires vides n’est imposé.

## État actuel et migration progressive

Le dossier historique `normes-software-embarque-automobile/` contient déjà une implémentation du projet Normes hors de `projets/normes/`. Il reste en place pour ne pas provoquer de conflits avec les branches actives. Sa migration cible est `projets/normes/`, à réaliser dans une pull request dédiée après synchronisation des branches.

La correspondance précise de chaque fichier, les commandes `git mv` et l’ordre des pull requests sont définis dans le [plan concret de migration](plan-migration.md).

La même règle s’applique aux futurs prototypes : commencer directement sous `projets/<slug>/` et déplacer les actifs historiques séparément, sans mélanger une migration d’arborescence avec un changement fonctionnel.
