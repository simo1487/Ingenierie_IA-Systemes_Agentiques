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

Le `SPEC.md` est créé à partir de la méthode décrite dans [`specs/README.md`](../../specs/README.md). Une expérience suit les conventions de [`docs/architecture-monorepo.md`](../../docs/architecture-monorepo.md).
