# FEAT-FIL-201 — Reprendre un run sans double effet

`Référence — feature candidate`

- **Projet parent :** [`PROJ-FIL-AUTO-IA-001`](../../../../../SPEC.md)
- **Epic parente :** [`EPIC-FIL-02`](../../EPIC.md)
- **User Story parente :** [`US-FIL-201`](../../user-stories/US-FIL-201.md)
- **Jour :** `J06`
- **Sources de formation :** [`C03-RETOUR`](../../../../baseline/sources.md#c03-retour) — `J03` / Plan préalable, bornes et comparaisons des tests générés, concurrence, doubles, contrôles dans la chaîne / `retour_rapporte`<br>[`C06-G5`](../../../../baseline/sources.md#c06-g5) — `J06` / Comparaison, journal complet, interruption et mémoire ; revue G5 / `programme_prevu`
- **Branche :** `feat/fil-rouge-ingenierie-auto-ia`
- **Niveau :** `Socle formation`
- **Priorité :** `P1`
- **Statut documentaire :** `Candidate`
- **Statut de preuve :** `Candidat`
- **Travail :** `À faire`
- **Responsable :** opérateur — personne à désigner

Cette Feature détaille la User Story parente ; elle ne crée pas une exigence indépendante.

## Contrat candidat

- **Entrée :** Checkpoint versionné lié au run, empreinte des entrées, étape vérifiée et identifiant d'opération ; destination locale de test.
- **Sortie :** Observation de reprise ou refus de checkpoint incompatible ; registre des opérations réalisées.
- **Périmètre :** Démonstration locale ou replay documenté pour J06 ; stockage distribué et effets réels exclus.
- **Règle canonique :** [`RM-FIL-201`](../../user-stories/US-FIL-201.md#rm-fil-201)
- **Critères canoniques :** [`CA-FIL-201-01`](../../user-stories/US-FIL-201.md#ca-fil-201-01), [`CA-FIL-201-02`](../../user-stories/US-FIL-201.md#ca-fil-201-02), [`CA-FIL-201-03`](../../user-stories/US-FIL-201.md#ca-fil-201-03), [`CA-FIL-201-04`](../../user-stories/US-FIL-201.md#ca-fil-201-04), [`CA-FIL-201-05`](../../user-stories/US-FIL-201.md#ca-fil-201-05)

Aucune surface future n'est affirmée comme présente ; son emplacement reste à décider avant réalisation. La baseline actuelle est décrite dans [`current-state.md`](../../../../baseline/current-state.md). Les noms de modules futurs ne sont pas présentés comme existants.

## Découpage exécutable

| Tâche | Objectif | Phase | Dépendances |
|---|---|---|---|
| [`TASK-FIL-201-01`](tasks/TASK-FIL-201-01.md) | Figer le protocole checkpoint/opération et les fenêtres de panne, dont effet accompli avant confirmation. | Spécifier et figer l'oracle | [`US-FIL-102`](../../../EPIC-FIL-01/user-stories/US-FIL-102.md) |
| [`TASK-FIL-201-02`](tasks/TASK-FIL-201-02.md) | Réaliser un point de reprise local et une réservation d'opération idempotente, ou préparer un replay déclaré pour le socle. | Réaliser dans le périmètre autorisé | [`TASK-FIL-201-01`](tasks/TASK-FIL-201-01.md) |
| [`TASK-FIL-201-03`](tasks/TASK-FIL-201-03.md) | Interrompre, reprendre deux fois et confronter le registre d'effets ; refuser l'empreinte incompatible et revoir la fenêtre non atomique. | Vérifier et soumettre à revue | [`TASK-FIL-201-02`](tasks/TASK-FIL-201-02.md) |

La livraison et les tests sont planifiés ; aucune tâche n'est exécutée par cette spécification.

## Vérification prévue

L'oracle à appliquer est celui de la [`User Story parente`](../../user-stories/US-FIL-201.md#oracle-indépendant) : Registre d'effets externe au workflow et deux appels concurrents de test ; comparer son cardinal avant/après. Simuler aussi l'interruption entre effet et confirmation : pas de promesse exactly-once sans mécanisme transactionnel explicite.

Les limites d'interruption, de concurrence ou de documentation applicables restent celles des cas de la User Story. Aucun retour de code supplémentaire n'est inventé ici.

## Acceptation

- [ ] [`CA-FIL-201-01`](../../user-stories/US-FIL-201.md#ca-fil-201-01)
- [ ] [`CA-FIL-201-02`](../../user-stories/US-FIL-201.md#ca-fil-201-02)
- [ ] [`CA-FIL-201-03`](../../user-stories/US-FIL-201.md#ca-fil-201-03)
- [ ] [`CA-FIL-201-04`](../../user-stories/US-FIL-201.md#ca-fil-201-04)
- [ ] [`CA-FIL-201-05`](../../user-stories/US-FIL-201.md#ca-fil-201-05)

Le responsable nominatif et la décision d'acceptation restent à décider. Les décisions demeurent humaines et [`AMB-05`](../../../../governance/ambiguities.md#amb-05) reste ouverte.
