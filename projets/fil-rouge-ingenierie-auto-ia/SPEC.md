# SPEC — Fil rouge d’ingénierie automobile assistée par IA

`Référence — spécification projet candidate`

## Informations générales

- **Identifiant :** `PROJ-FIL-AUTO-IA-001`
- **Branche :** `feat/fil-rouge-ingenierie-auto-ia`
- **Statut documentaire :** `Candidate`
- **Statut de preuve :** `Candidat`
- **Travail du backlog :** `À faire`
- **Responsable :** responsable d’intégration — personne à désigner

## Vision

Relier les baselines normatives autorisées, la recherche de projets open source, l’ingénierie des exigences, le RAG, l’analyse qualité et la traçabilité dans un parcours observable. Les agents produisent des observations ou propositions ; la sélection d’une baseline, l’acceptation d’une exigence, l’application d’un correctif, l’adoption d’un composant et le franchissement d’une Gate restent des décisions humaines.

Cette spécification décrit un backlog futur et non une déclaration de disponibilité en production.

## Parties prenantes

| Rôle | Valeur recherchée | Décision réservée |
|---|---|---|
| Responsable de baseline ou corpus | Entrées autorisées et révisées | Approuver les sources et leur version |
| Opérateur et mainteneur | Exécution explicable et reprise bornée | Autoriser un run ou son arrêt |
| Ingénieur exigences et architecte | Propositions sourcées et organisation justifiée | Accepter une exigence ou une complexité |
| Responsable sécurité et qualité | Accès et diagnostics bornés | Autoriser les périmètres et les corrections |
| Responsable produit et pilote | Coûts, risques et options comparables | Sélectionner, corriger, piloter ou arrêter |
| Relecteur indépendant et décideur humain | Preuves contradictoires et limites visibles | Accepter les preuves et consigner une Gate |

Les rôles sont proposés ; les personnes restent à désigner.

## Entrées

- Manifeste versionné, baselines avec identifiants et révisions, approbations humaines et objectifs.
- Corpus, fiches OSS, diagnostics, politiques, cas et oracles dont la provenance est déclarée.
- Fixtures ou replays explicitement étiquetés pour le socle ; ressources réelles uniquement après résolution des ambiguïtés applicables.

Les références et réserves sont détaillées dans [`sources.md`](specs/baseline/sources.md).

## Exclusions globales

- Aucune modification de `upstream/**`, exécution libre de dépôt tiers ou application automatique de correctif.
- Aucune acquisition de norme protégée sans autorisation, conservation de secret dans Git ou base vectorielle générée versionnée.
- Aucune décision réglementaire, certification, Gate ou sélection produit validée par le modèle seul.
- Aucun déploiement, lancement réel, commit, push ou merge n’est autorisé par la rédaction de ce backlog.

## Sorties candidates

- Observations de prévalidation, traces, retrieval, appels autorisés ou refusés, reprise et surveillance.
- Propositions d’exigences, d’organisation, de classement, de risques, de coût et de décision.
- Preuves futures reliées à un oracle indépendant, avec mode, versions, résultats, limites et revue humaine.

Une sortie ou un champ rempli ne constitue pas automatiquement une preuve.

## Epics

1. [`EPIC-FIL-00` — Capitaliser les acquis avant d’étendre le workflow](specs/epics/EPIC-FIL-00/EPIC.md)
2. [`EPIC-FIL-01` — Exécution observable et choix d’organisation](specs/epics/EPIC-FIL-01/EPIC.md)
3. [`EPIC-FIL-02` — Reprise fiable et mémoire gouvernée](specs/epics/EPIC-FIL-02/EPIC.md)
4. [`EPIC-FIL-03` — Outils bornés et frontière MCP](specs/epics/EPIC-FIL-03/EPIC.md)
5. [`EPIC-FIL-04` — Évaluation indépendante et non-régression](specs/epics/EPIC-FIL-04/EPIC.md)
6. [`EPIC-FIL-05` — Livraison reproductible et exploitation réversible](specs/epics/EPIC-FIL-05/EPIC.md)
7. [`EPIC-FIL-06` — Gouvernance, coûts et décision humaine](specs/epics/EPIC-FIL-06/EPIC.md)

`EPIC-FIL-00` capitalise les acquis J01–J05 à examiner ; elle ne présume ni leur maîtrise ni leur réalisation. `EPIC-FIL-AUTO-IA-001` et les identifiants historiques restent consultables dans le [snapshot MVP](specs/baseline/mvp-spec.md). Les Epics actives sont des évolutions de planification, pas une preuve de réalisation.

## Navigation et gouvernance

- [Spécifications et chemins de lecture](specs/README.md)
- [Audit d’alignement avec la formation](specs/baseline/formation-audit.md)
- [Registre canonique d’alignement](specs/formation-alignment.json)
- [Roadmap candidate](specs/roadmap/README.md)
- [Backlog ordonnancé](specs/roadmap/backlog.md)
- [Registre d’ambiguïtés](specs/governance/ambiguities.md)
- [Cycle de vie](specs/governance/lifecycle.md)
- [État actuel observé](specs/baseline/current-state.md)

Aucun critère de la nouvelle hiérarchie n’est accepté dans ce document ; les cases candidates restent dans les User Stories et sont décochées.
