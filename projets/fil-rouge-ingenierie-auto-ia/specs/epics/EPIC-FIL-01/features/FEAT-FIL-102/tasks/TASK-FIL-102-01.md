# TASK-FIL-102-01 — Définir les champs du journal et une séquence R1 succès/interruption/erreur avec durées factices

`Référence — tâche candidate`

- **Epic parente :** [`EPIC-FIL-01`](../../../EPIC.md)
- **User Story parente :** [`US-FIL-102`](../../../user-stories/US-FIL-102.md)
- **Feature parente :** [`FEAT-FIL-102`](../FEATURE.md)
- **Jour :** `J06`
- **Phase :** Spécifier et figer l'oracle
- **Sources héritées :** [`C03-RETOUR`](../../../../../baseline/sources.md#c03-retour) — `J03` / Plan préalable, bornes et comparaisons des tests générés, concurrence, doubles, contrôles dans la chaîne / `retour_rapporte`<br>[`C06-G5`](../../../../../baseline/sources.md#c06-g5) — `J06` / Comparaison, journal complet, interruption et mémoire ; revue G5 / `programme_prevu`
- **Niveau :** `Socle formation`
- **Priorité :** `P1`
- **Statut documentaire :** `Candidate`
- **Statut de preuve :** `Candidat`
- **Travail :** `À faire`
- **Responsable :** opérateur — personne à désigner

## Objectif

Définir les champs du journal et une séquence R1 succès/interruption/erreur avec durées factices.

## Prérequis

- **Capacités préalables :** [`US-FIL-101`](../../../user-stories/US-FIL-101.md)
- **Estimation :** non attribuée
- **Date :** non attribuée

Un artefact existant peut satisfaire une capacité préalable après revue ; la tâche ne force pas à refaire un acquis démontré.

## Travail et livrable attendus

**Définir les champs du journal et une séquence R1 succès/interruption/erreur avec durées factices**

Produire un artefact relu couvrant les cas et l'oracle de [`US-FIL-102`](../../../user-stories/US-FIL-102.md) dans le mode autorisé.

Une fixture ou un replay n’est recevable que si le périmètre de la US l’autorise, avec mode et limites déclarés.

- **Entrée héritée :** Run autorisé, versions de code/configuration, mode réel ou fixture ou replay, horloge contrôlée pour les tests.
- **Sortie héritée :** Observation : événements ordonnés avec run_id, event_id, séquence, étape, transition, auteur, décision, références d'entrée/sortie, durée, erreur et versions ; pas de contenu brut sensible.
- **Périmètre hérité :** Journal d'un run séquentiel ; le stockage distribué est exclu.
- **Critères de la US parente (références, pas preuve de couverture de cette tâche) :** [`CA-FIL-102-01`](../../../user-stories/US-FIL-102.md#ca-fil-102-01), [`CA-FIL-102-02`](../../../user-stories/US-FIL-102.md#ca-fil-102-02), [`CA-FIL-102-03`](../../../user-stories/US-FIL-102.md#ca-fil-102-03)

Les clauses et oracles de la spécification parente s'appliquent ; toute modification nécessite une nouvelle revue, pas une adaptation implicite au résultat observé.

## Vérification / sortie

- [ ] Artefact complet correspondant à la phase `Spécifier et figer l'oracle`
- [ ] Source, version, mode et statut déclarés
- [ ] Preuve ou disposition de revue jointe ; la tâche ne devient pas automatiquement `Terminé`

## Questions

Voir [`AMB-02`](../../../../../governance/ambiguities.md#amb-02).
