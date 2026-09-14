# TASK-FIL-3-03 — Exécuter le même test après le patch et les tests voisins sans affaiblir leurs assertions

`Référence — tâche candidate`

- **Epic parente :** [`EPIC-FIL-00`](../../../EPIC.md)
- **User Story parente :** [`US-FIL-3`](../../../user-stories/US-FIL-3.md)
- **Feature parente :** [`FEAT-FIL-3`](../FEATURE.md)
- **Jour :** `J01–J05`
- **Phase :** Vérifier le vert et les cas voisins
- **Sources héritées :** [`C03`](../../../../../baseline/sources.md#c03) — `J03` / Reproduction, hypothèses concurrentes, rouge/vert comparable, mutation et documentation / `support_actuel`<br>[`C03-RETOUR`](../../../../../baseline/sources.md#c03-retour) — `J03` / Plan préalable, bornes et comparaisons des tests générés, concurrence, doubles, contrôles dans la chaîne / `retour_rapporte`<br>[`N03`](../../../../../baseline/sources.md#n03) — `J03` / Plan préalable, tests générés, scripts, qualité et organisation des spécifications ; propos à confirmer / `synthese_automatique`
- **Niveau :** `Socle formation`
- **Priorité :** `P1`
- **Statut documentaire :** `Candidate`
- **Statut de preuve :** `Candidat`
- **Travail :** `À faire`
- **Responsable :** mainteneur — personne à désigner

## Objectif

Exécuter le même test après le patch et les tests voisins sans affaiblir leurs assertions.

## Prérequis

- **Capacités préalables :** [`TASK-FIL-3-02`](TASK-FIL-3-02.md)
- **Estimation :** non attribuée
- **Date :** non attribuée

Un artefact existant peut satisfaire une capacité préalable après revue ; la tâche ne force pas à refaire un acquis démontré.

## Travail et livrable attendus

**Exécuter le même test après le patch et les tests voisins sans affaiblir leurs assertions**

Réaliser la phase décrite par [`FEAT-FIL-3`](../FEATURE.md) sans revendiquer une disponibilité ou une preuve non observée.

Une fixture ou un replay n’est recevable que si le périmètre de la US l’autorise, avec mode et limites déclarés.

- **Entrée héritée :** Cas autorisé avec version, entrée, conditions, attendu indépendant, observation et procédure de reproduction ; copie isolée pour la mutation.
- **Sortie héritée :** Observations de reproduction, expérience discriminante, rouge/vert, non-régression et mutation ; proposition de correctif avec revue humaine.
- **Périmètre hérité :** Chaîne de preuve générale J03, distincte de la régression hostile J07 ; aucune correction métier appliquée par la rédaction de cette US.
- **Critères de la US parente (références, pas preuve de couverture de cette tâche) :** [`CA-FIL-3-01`](../../../user-stories/US-FIL-3.md#ca-fil-3-01), [`CA-FIL-3-02`](../../../user-stories/US-FIL-3.md#ca-fil-3-02), [`CA-FIL-3-03`](../../../user-stories/US-FIL-3.md#ca-fil-3-03), [`CA-FIL-3-04`](../../../user-stories/US-FIL-3.md#ca-fil-3-04)

Les clauses et oracles de la spécification parente s'appliquent ; toute modification nécessite une nouvelle revue, pas une adaptation implicite au résultat observé.

## Vérification / sortie

- [ ] Artefact complet correspondant à la phase `Vérifier le vert et les cas voisins`
- [ ] Source, version, mode et statut déclarés
- [ ] Preuve ou disposition de revue jointe ; la tâche ne devient pas automatiquement `Terminé`

## Questions

Voir [`AMB-21`](../../../../../governance/ambiguities.md#amb-21).
