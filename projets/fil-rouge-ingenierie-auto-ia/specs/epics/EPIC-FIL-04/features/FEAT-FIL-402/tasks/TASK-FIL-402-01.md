# TASK-FIL-402-01 — Choisir le contrôle local à muter et figer le cas qui observe réellement l'accès

`Référence — tâche candidate`

- **Epic parente :** [`EPIC-FIL-04`](../../../EPIC.md)
- **User Story parente :** [`US-FIL-402`](../../../user-stories/US-FIL-402.md)
- **Feature parente :** [`FEAT-FIL-402`](../FEATURE.md)
- **Jour :** `J07`
- **Phase :** Spécifier et figer l'oracle
- **Sources héritées :** [`C03`](../../../../../baseline/sources.md#c03) — `J03` / Reproduction, hypothèses concurrentes, rouge/vert comparable, mutation et documentation / `support_actuel`<br>[`C07-G6`](../../../../../baseline/sources.md#c07-g6) — `J07` / Outil préparé ou replay, refus avant accès, régression et première divergence ; G6 / `programme_prevu`
- **Niveau :** `Socle formation`
- **Priorité :** `P1`
- **Statut documentaire :** `Candidate`
- **Statut de preuve :** `Candidat`
- **Travail :** `À faire`
- **Responsable :** relecteur sécurité — personne à désigner

## Objectif

Choisir le contrôle local à muter et figer le cas qui observe réellement l'accès.

## Prérequis

- **Capacités préalables :** [`US-FIL-3`](../../../../EPIC-FIL-00/user-stories/US-FIL-3.md), [`US-FIL-401`](../../../user-stories/US-FIL-401.md)
- **Estimation :** non attribuée
- **Date :** non attribuée

Un artefact existant peut satisfaire une capacité préalable après revue ; la tâche ne force pas à refaire un acquis démontré.

## Travail et livrable attendus

**Choisir le contrôle local à muter et figer le cas qui observe réellement l'accès**

Produire un artefact relu couvrant les cas et l'oracle de [`US-FIL-402`](../../../user-stories/US-FIL-402.md) dans le mode autorisé.

Une fixture ou un replay n’est recevable que si le périmètre de la US l’autorise, avec mode et limites déclarés.

- **Entrée héritée :** Cas hostile versionné, copie isolée de test et garde d'autorisation identifié ; mutation défensive contrôlée.
- **Sortie héritée :** Observations rouge/vert et mutation avec versions, code retour et décision de revue.
- **Périmètre hérité :** Mutation ciblée défensive en environnement isolé ; aucune désactivation de politique de dépôt.
- **Critères de la US parente (références, pas preuve de couverture de cette tâche) :** [`CA-FIL-402-01`](../../../user-stories/US-FIL-402.md#ca-fil-402-01), [`CA-FIL-402-02`](../../../user-stories/US-FIL-402.md#ca-fil-402-02), [`CA-FIL-402-03`](../../../user-stories/US-FIL-402.md#ca-fil-402-03)

Les clauses et oracles de la spécification parente s'appliquent ; toute modification nécessite une nouvelle revue, pas une adaptation implicite au résultat observé.

## Vérification / sortie

- [ ] Artefact complet correspondant à la phase `Spécifier et figer l'oracle`
- [ ] Source, version, mode et statut déclarés
- [ ] Preuve ou disposition de revue jointe ; la tâche ne devient pas automatiquement `Terminé`

## Questions

Voir [`AMB-11`](../../../../../governance/ambiguities.md#amb-11).
