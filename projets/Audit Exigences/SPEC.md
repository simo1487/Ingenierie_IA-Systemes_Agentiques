# SPEC — Audit Exigences

`Référence — spécification projet candidate`

## Informations générales

- **Identifiant :** `PROJ-AUD-EXG-001`
- **Nom :** Audit Exigences
- **Branche :** `Mo_filRouge`
- **Statut documentaire :** `Candidate`
- **Statut de preuve :** `Candidat`
- **Travail du backlog :** `À faire`
- **Responsable :** responsable audit — personne à désigner

## Vision

Fournir un outil déterministe d'audit de qualité pour un dataset d'exigences automobiles. L'outil détecte les anomalies linguistiques (grammaire, orthographe), les duplications et les contradictions entre exigences. Toutes les sorties sont des **propositions** ; la correction et la validation restent des décisions humaines.

## Parties prenantes

| Rôle | Valeur recherchée | Décision réservée |
|---|---|---|
| Ingénieur exigences | Anomalies détectées et localisées | Accepter ou rejeter une correction |
| Responsable qualité | Vue consolidée de la qualité du dataset | Qualifier les faux positifs |
| Relecteur indépendant | Preuves et limites visibles | Décider de la Gate finale |

## Entrées

- Dataset d'exigences au format JSON ou Markdown avec `id`, `text`, `source`, `version`.
- Seuils de similarité et patterns de contradiction configurables.

## Exclusions globales

- Aucune modification automatique du dataset source.
- Aucune décision de validation réglementaire par l'outil seul.
- Aucune revendication de conformité ASPICE/MISRA.

## Sorties candidates

- Rapport JSON d'anomalies par EPIC avec localisation, sévérité et proposition.
- Statistiques de qualité du dataset.
- Statut final `ready-for-human-review`.

## Epics

1. [`EPIC-AUD-01`](specs/epics/EPIC-AUD-01/EPIC.md) — Vérifier grammaire et orthographe
2. [`EPIC-AUD-02`](specs/epics/EPIC-AUD-02/EPIC.md) — Vérifier la non-duplication
3. [`EPIC-AUD-03`](specs/epics/EPIC-AUD-03/EPIC.md) — Vérifier la non-contradiction

## Navigation

- [Spécifications](specs/README.md)
- [Backlog ordonnancé](specs/roadmap/backlog.md)
- [Registre d'ambiguïtés](specs/governance/ambiguities.md)
- [Cycle de vie](specs/governance/lifecycle.md)

Aucun critère n'est accepté dans ce document ; les cases candidates restent dans les User Stories et sont décochées.
