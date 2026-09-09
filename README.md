# Portefeuille d’ingénierie assistée par IA

Monorepo de projets et prototypes d’ingénierie assistée par IA. Chaque projet possède une Epic, des User Stories, ses propres baselines, contrôles et preuves, sans imposer une chaîne de build unique au portefeuille.

## Commencer

1. Lire les [règles du dépôt](AGENTS.md).
2. Identifier son équipe et sa branche dans [travail.md](travail.md).
3. Lire la [spécification du projet](projets/README.md).
4. Suivre le [workflow correspondant à la Gate visée](workflows/README.md).
5. Installer le hook Git local avec `make setup-hooks`.
6. Vérifier les fichiers avec `make check` avant une revue.

## Organisation

```text
.devin/                 Configuration, règles et skills Devin
.githooks/              Hooks Git légers et partagés
docs/                   Architecture et conventions transverses
projets/<projet>/       Espace autonome d’un projet ou d’une expérimentation
specs/                  Méthode et modèles documentaires partagés
tools/                  Contrôles génériques du monorepo
workflows/              Workflows G0, G1, G2 et intégration
```

Chaque projet peut employer son propre langage et son propre outillage. Il conserve localement son code, ses tests, sa documentation, ses expériences et ses preuves. Le hook racine ne remplace pas les tests propres au projet.

- [Tutoriel d’utilisation](docs/tutoriel-utilisation.md)
- [Plan concret de migration](docs/plan-migration.md)
- [Architecture du monorepo](docs/architecture-monorepo.md)
- [Guide de contribution](CONTRIBUTING.md)
- [Architecture des spécifications](specs/README.md)
- [Ordre des étapes](specs/ordre-et-etapes.md)
- [Répartition des projets](travail.md)
