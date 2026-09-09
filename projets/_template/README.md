# Modèle de projet

Copier cette structure logique lors de la création d’un projet. Ne créer que les dossiers contenant un premier artefact utile.

```text
projets/<slug>/
├── README.md
├── SPEC.md
├── experiments/<AAAA-MM-JJ>-<sujet>/README.md
├── src/
├── tests/
├── docs/
├── data/
└── evidence/
```

Le `README.md` du projet contient au minimum :

```markdown
# Nom du projet

## Objectif

## Équipe et branche

## Statut

## Arborescence réelle

## Installation

## Commandes

| Besoin | Commande |
|---|---|
| Vérification rapide | À définir |
| Tests complets | À définir |
| Exécution | À définir |

## Entrées et baselines

## Sorties et preuves

## Limites et questions ouvertes
```

Le `SPEC.md` est créé à partir de [`specs/templates/template-project-spec.md`](../../specs/templates/template-project-spec.md). Il décrit au minimum une Epic, ses User Stories, leurs règles, exemples, critères, oracles, liens de traçabilité et ambiguïtés. Une feature détaillée suit ensuite [`specs/templates/template-feature-spec.md`](../../specs/templates/template-feature-spec.md) et reste reliée à sa User Story parente. Une expérience suit les conventions de [`docs/architecture-monorepo.md`](../../docs/architecture-monorepo.md).
