# TASK-FIL-101-02 — Prévoir la validation d'entrée et l'arrêt des étapes dépendantes dans AutomotiveAIFlow.run ; préserver la CLI hors ligne

`Référence — tâche candidate`

- **Epic parente :** [`EPIC-FIL-01`](../../../EPIC.md)
- **User Story parente :** [`US-FIL-101`](../../../user-stories/US-FIL-101.md)
- **Feature parente :** [`FEAT-FIL-101`](../FEATURE.md)
- **Jour :** `J06`
- **Phase :** Réaliser dans le périmètre autorisé
- **Sources héritées :** [`C02`](../../../../../baseline/sources.md#c02) — `J02` / Exigence singulière, inconnues, exemples et oracle indépendant ; Gherkin non universellement obligatoire / `support_actuel`<br>[`C04`](../../../../../baseline/sources.md#c04) — `J04` / Corpus autorisé, découpage du sens, lexical/sémantique, Hit@k/MRR et support des citations / `support_actuel`<br>[`C06`](../../../../../baseline/sources.md#c06) — `J06` / Comparaison d'organisations, rôles, reprise, idempotence, mémoire et trace / `programme_prevu`
- **Niveau :** `Socle formation`
- **Priorité :** `P1`
- **Statut documentaire :** `Candidate`
- **Statut de preuve :** `Candidat`
- **Travail :** `À faire`
- **Responsable :** responsable de baseline — personne à désigner

## Objectif

Prévoir la validation d'entrée et l'arrêt des étapes dépendantes dans AutomotiveAIFlow.run ; préserver la CLI hors ligne.

## Prérequis

- **Capacités préalables :** [`TASK-FIL-101-01`](TASK-FIL-101-01.md)
- **Estimation :** non attribuée
- **Date :** non attribuée

Un artefact existant peut satisfaire une capacité préalable après revue ; la tâche ne force pas à refaire un acquis démontré.

## Travail et livrable attendus

**Prévoir la validation d'entrée et l'arrêt des étapes dépendantes dans AutomotiveAIFlow.run ; préserver la CLI hors ligne**

Réaliser la phase décrite par [`FEAT-FIL-101`](../FEATURE.md) sans revendiquer une disponibilité ou une preuve non observée.

Une fixture ou un replay n’est recevable que si le périmètre de la US l’autorise, avec mode et limites déclarés.

- **Entrée héritée :** Manifeste local versionné : run_id, objective, baselines avec id/révision, approbation portant sur cette version. Corpus fictif pour le socle ; corpus réel soumis à AMB-01.
- **Sortie héritée :** Observation de validation ou arrêt Bloqué avec motif, sans appel fournisseur en cas d'échec.
- **Périmètre hérité :** Prévalidation du manifeste et propagation du blocage ; hors périmètre : acquisition de corpus réel.
- **Critères de la US parente (références, pas preuve de couverture de cette tâche) :** [`CA-FIL-101-01`](../../../user-stories/US-FIL-101.md#ca-fil-101-01), [`CA-FIL-101-02`](../../../user-stories/US-FIL-101.md#ca-fil-101-02), [`CA-FIL-101-03`](../../../user-stories/US-FIL-101.md#ca-fil-101-03)

Les clauses et oracles de la spécification parente s'appliquent ; toute modification nécessite une nouvelle revue, pas une adaptation implicite au résultat observé.

## Vérification / sortie

- [ ] Artefact complet correspondant à la phase `Réaliser dans le périmètre autorisé`
- [ ] Source, version, mode et statut déclarés
- [ ] Preuve ou disposition de revue jointe ; la tâche ne devient pas automatiquement `Terminé`

## Questions

Voir [`AMB-01`](../../../../../governance/ambiguities.md#amb-01).
