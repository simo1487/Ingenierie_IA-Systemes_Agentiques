# TASK-FIL-403-01 — Figer les champs d'alignement et trois traces : accès anticipé, horloges différentes, événement absent

`Référence — tâche candidate`

- **Epic parente :** [`EPIC-FIL-04`](../../../EPIC.md)
- **User Story parente :** [`US-FIL-403`](../../../user-stories/US-FIL-403.md)
- **Feature parente :** [`FEAT-FIL-403`](../FEATURE.md)
- **Jour :** `J07`
- **Phase :** Spécifier et figer l'oracle
- **Sources héritées :** [`C03`](../../../../../baseline/sources.md#c03) — `J03` / Reproduction, hypothèses concurrentes, rouge/vert comparable, mutation et documentation / `support_actuel`<br>[`C07-G6`](../../../../../baseline/sources.md#c07-g6) — `J07` / Outil préparé ou replay, refus avant accès, régression et première divergence ; G6 / `programme_prevu`
- **Niveau :** `Socle formation`
- **Priorité :** `P1`
- **Statut documentaire :** `Candidate`
- **Statut de preuve :** `Candidat`
- **Travail :** `À faire`
- **Responsable :** mainteneur — personne à désigner

## Objectif

Figer les champs d'alignement et trois traces : accès anticipé, horloges différentes, événement absent.

## Prérequis

- **Capacités préalables :** [`US-FIL-3`](../../../../EPIC-FIL-00/user-stories/US-FIL-3.md), [`US-FIL-102`](../../../../EPIC-FIL-01/user-stories/US-FIL-102.md), [`US-FIL-401`](../../../user-stories/US-FIL-401.md)
- **Estimation :** non attribuée
- **Date :** non attribuée

Un artefact existant peut satisfaire une capacité préalable après revue ; la tâche ne force pas à refaire un acquis démontré.

## Travail et livrable attendus

**Figer les champs d'alignement et trois traces : accès anticipé, horloges différentes, événement absent**

Produire un artefact relu couvrant les cas et l'oracle de [`US-FIL-403`](../../../user-stories/US-FIL-403.md) dans le mode autorisé.

Une fixture ou un replay n’est recevable que si le périmètre de la US l’autorise, avec mode et limites déclarés.

- **Entrée héritée :** Trace attendue revue, trace observée assainie, identifiants d'événement et versions d'entrée identiques.
- **Sortie héritée :** Observation du premier événement divergent et proposition de cause ; correction soumise au rejeu.
- **Périmètre hérité :** Comparaison locale et enquête traçable ; pas d'observabilité distribuée obligatoire.
- **Critères de la US parente (références, pas preuve de couverture de cette tâche) :** [`CA-FIL-403-01`](../../../user-stories/US-FIL-403.md#ca-fil-403-01), [`CA-FIL-403-02`](../../../user-stories/US-FIL-403.md#ca-fil-403-02), [`CA-FIL-403-03`](../../../user-stories/US-FIL-403.md#ca-fil-403-03)

Les clauses et oracles de la spécification parente s'appliquent ; toute modification nécessite une nouvelle revue, pas une adaptation implicite au résultat observé.

## Vérification / sortie

- [ ] Artefact complet correspondant à la phase `Spécifier et figer l'oracle`
- [ ] Source, version, mode et statut déclarés
- [ ] Preuve ou disposition de revue jointe ; la tâche ne devient pas automatiquement `Terminé`

## Questions

Voir [`AMB-02`](../../../../../governance/ambiguities.md#amb-02).
