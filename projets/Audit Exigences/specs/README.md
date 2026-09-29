# Spécifications — Audit Exigences

## Autorité et hiérarchie

[`backlog.json`](backlog.json) est la source canonique du backlog. Les pages Markdown sont des miroirs selon la hiérarchie `PROJ → EPIC → US → FEAT → TASK`. Les règles, critères, cas et oracles appartiennent aux User Stories.

## Lire selon son rôle

- **Produit :** commencer par [`SPEC.md`](../SPEC.md).
- **Réalisation :** ouvrir une User Story, sa Feature fille et ses tâches.
- **Revue :** confronter les critères et oracles aux preuves.

## Arborescence

```text
specs/
├── backlog.json
├── baseline/
│   ├── current-state.md
│   └── sources.md
├── epics/EPIC-AUD-01..03/
│   ├── EPIC.md
│   ├── user-stories/US-AUD-*.md
│   └── features/FEAT-AUD-*/
│       ├── FEATURE.md
│       └── tasks/TASK-AUD-*.md
├── governance/
│   ├── ambiguities.md
│   └── lifecycle.md
└── roadmap/
    ├── README.md
    └── backlog.md
```

Toutes les Stories, Features et tâches restent `Candidate` et `À faire`. Les critères sont décochés.
