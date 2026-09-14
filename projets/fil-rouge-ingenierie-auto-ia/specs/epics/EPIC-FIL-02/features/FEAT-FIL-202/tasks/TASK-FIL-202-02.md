# TASK-FIL-202-02 — Prévoir les gardes de reprise et l'arrêt sur timeout autour des appels, avec événements de budget

`Référence — tâche candidate`

- **Epic parente :** [`EPIC-FIL-02`](../../../EPIC.md)
- **User Story parente :** [`US-FIL-202`](../../../user-stories/US-FIL-202.md)
- **Feature parente :** [`FEAT-FIL-202`](../FEATURE.md)
- **Jour :** `J06`
- **Phase :** Réaliser dans le périmètre autorisé
- **Sources héritées :** [`N05`](../../../../../baseline/sources.md#n05) — `J05` / Approches simples, types, budgets, contrôle humain et structuration ; propos à confirmer / `synthese_automatique`<br>[`C06`](../../../../../baseline/sources.md#c06) — `J06` / Comparaison d'organisations, rôles, reprise, idempotence, mémoire et trace / `programme_prevu`
- **Niveau :** `Socle formation`
- **Priorité :** `P1`
- **Statut documentaire :** `Candidate`
- **Statut de preuve :** `Candidat`
- **Travail :** `À faire`
- **Responsable :** opérateur — personne à désigner

## Objectif

Prévoir les gardes de reprise et l'arrêt sur timeout autour des appels, avec événements de budget.

## Prérequis

- **Capacités préalables :** [`TASK-FIL-202-01`](TASK-FIL-202-01.md)
- **Estimation :** non attribuée
- **Date :** non attribuée

Un artefact existant peut satisfaire une capacité préalable après revue ; la tâche ne force pas à refaire un acquis démontré.

## Travail et livrable attendus

**Prévoir les gardes de reprise et l'arrêt sur timeout autour des appels, avec événements de budget**

Réaliser la phase décrite par [`FEAT-FIL-202`](../FEATURE.md) sans revendiquer une disponibilité ou une preuve non observée.

Une fixture ou un replay n’est recevable que si le périmètre de la US l’autorise, avec mode et limites déclarés.

- **Entrée héritée :** Politique datée avec nombre maximal d'essais, délai et plafond d'usage ; configuration fictive explicitement étiquetée pour les tests.
- **Sortie héritée :** Observation d'arrêt avec raison et budget consommé ; reprise proposée uniquement avec entrée observable modifiée.
- **Périmètre hérité :** Budgets d'essais et de temps ; tarifs et seuils de production restent des décisions humaines.
- **Critères de la US parente (références, pas preuve de couverture de cette tâche) :** [`CA-FIL-202-01`](../../../user-stories/US-FIL-202.md#ca-fil-202-01), [`CA-FIL-202-02`](../../../user-stories/US-FIL-202.md#ca-fil-202-02), [`CA-FIL-202-03`](../../../user-stories/US-FIL-202.md#ca-fil-202-03)

Les clauses et oracles de la spécification parente s'appliquent ; toute modification nécessite une nouvelle revue, pas une adaptation implicite au résultat observé.

## Vérification / sortie

- [ ] Artefact complet correspondant à la phase `Réaliser dans le périmètre autorisé`
- [ ] Source, version, mode et statut déclarés
- [ ] Preuve ou disposition de revue jointe ; la tâche ne devient pas automatiquement `Terminé`

## Questions

Voir [`AMB-06`](../../../../../governance/ambiguities.md#amb-06).
