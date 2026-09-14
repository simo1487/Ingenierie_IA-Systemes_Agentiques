# TASK-FIL-201-01 — Figer le protocole checkpoint/opération et les fenêtres de panne, dont effet accompli avant confirmation

`Référence — tâche candidate`

- **Epic parente :** [`EPIC-FIL-02`](../../../EPIC.md)
- **User Story parente :** [`US-FIL-201`](../../../user-stories/US-FIL-201.md)
- **Feature parente :** [`FEAT-FIL-201`](../FEATURE.md)
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

Figer le protocole checkpoint/opération et les fenêtres de panne, dont effet accompli avant confirmation.

## Prérequis

- **Capacités préalables :** [`US-FIL-102`](../../../../EPIC-FIL-01/user-stories/US-FIL-102.md)
- **Estimation :** non attribuée
- **Date :** non attribuée

Un artefact existant peut satisfaire une capacité préalable après revue ; la tâche ne force pas à refaire un acquis démontré.

## Travail et livrable attendus

**Figer le protocole checkpoint/opération et les fenêtres de panne, dont effet accompli avant confirmation**

Produire un artefact relu couvrant les cas et l'oracle de [`US-FIL-201`](../../../user-stories/US-FIL-201.md) dans le mode autorisé.

Une fixture ou un replay n’est recevable que si le périmètre de la US l’autorise, avec mode et limites déclarés.

- **Entrée héritée :** Checkpoint versionné lié au run, empreinte des entrées, étape vérifiée et identifiant d'opération ; destination locale de test.
- **Sortie héritée :** Observation de reprise ou refus de checkpoint incompatible ; registre des opérations réalisées.
- **Périmètre hérité :** Démonstration locale ou replay documenté pour J06 ; stockage distribué et effets réels exclus.
- **Critères de la US parente (références, pas preuve de couverture de cette tâche) :** [`CA-FIL-201-01`](../../../user-stories/US-FIL-201.md#ca-fil-201-01), [`CA-FIL-201-02`](../../../user-stories/US-FIL-201.md#ca-fil-201-02), [`CA-FIL-201-03`](../../../user-stories/US-FIL-201.md#ca-fil-201-03), [`CA-FIL-201-04`](../../../user-stories/US-FIL-201.md#ca-fil-201-04), [`CA-FIL-201-05`](../../../user-stories/US-FIL-201.md#ca-fil-201-05)

Les clauses et oracles de la spécification parente s'appliquent ; toute modification nécessite une nouvelle revue, pas une adaptation implicite au résultat observé.

## Vérification / sortie

- [ ] Artefact complet correspondant à la phase `Spécifier et figer l'oracle`
- [ ] Source, version, mode et statut déclarés
- [ ] Preuve ou disposition de revue jointe ; la tâche ne devient pas automatiquement `Terminé`

## Questions

Voir [`AMB-05`](../../../../../governance/ambiguities.md#amb-05).
