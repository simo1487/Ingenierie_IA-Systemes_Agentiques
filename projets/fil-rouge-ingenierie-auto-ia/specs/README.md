# Référence — Spécifications du fil rouge

## Autorité et hiérarchie

[`backlog.json`](backlog.json) est la source canonique du backlog et [`formation-alignment.json`](formation-alignment.json) celle des relations pédagogiques candidates. Les pages Markdown sont des miroirs rendus selon la hiérarchie `PROJ → EPIC → US → FEAT → TASK`. Les règles, critères, cas et oracles appartiennent aux User Stories ; les Features les référencent sans devenir parentes des Stories.

Depuis la racine du projet fil rouge, toute évolution met à jour les JSON et les pages gérées avec `python3 tools/render_specs.py --write`, puis vérifie leur concordance avec `python3 tools/render_specs.py --check`. Les contrats d’évaluation restent dans [`governance/measurement-contracts.md`](governance/measurement-contracts.md) et ne sont pas recomposés par le renderer.

## Lire selon son rôle

- **Produit :** commencer par [`SPEC.md`](../SPEC.md), puis la [`roadmap`](roadmap/README.md) et les Epics actives.
- **Réalisation :** ouvrir une User Story, sa Feature fille et ses tâches ; vérifier auparavant le [`cycle de vie`](governance/lifecycle.md) et l’[`ambiguïté`](governance/ambiguities.md) liée.
- **Revue :** consulter l’[`audit de formation`](baseline/formation-audit.md), confronter les critères et oracles aux preuves futures, puis consulter l’[`état actuel`](baseline/current-state.md) et les [`sources`](baseline/sources.md).

## Arborescence

```text
specs/
├── backlog.json
├── formation-alignment.json
├── baseline/
│   ├── current-state.md
│   ├── formation-audit.md
│   ├── mvp-spec.md
│   └── sources.md
├── epics/EPIC-FIL-00..06/
│   ├── EPIC.md
│   ├── user-stories/US-FIL-*.md
│   └── features/FEAT-FIL-*/
│       ├── FEATURE.md
│       └── tasks/TASK-FIL-*.md
├── governance/
│   ├── README.md
│   ├── ambiguities.md
│   ├── decision-tables.md
│   ├── lifecycle.md
│   └── measurement-contracts.md
└── roadmap/
    ├── README.md
    └── backlog.md
```

Toutes les Stories, Features et tâches restent `Candidate`, `Candidat` et `À faire`. Les critères sont décochés ; aucun responsable nominatif ni verdict de production n’est déclaré.

`tests/test_specs.py` contrôle le schéma, les relations et le miroir documentaire. Ce contrôle structurel ne valide pas le sens des exigences, leur réalisation métier ou leur acceptation humaine.
