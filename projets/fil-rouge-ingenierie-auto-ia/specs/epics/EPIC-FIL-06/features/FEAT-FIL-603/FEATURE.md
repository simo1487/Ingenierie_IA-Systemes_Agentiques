# FEAT-FIL-603 — Attribuer les risques qui conditionnent la suite

`Référence — feature candidate`

- **Projet parent :** [`PROJ-FIL-AUTO-IA-001`](../../../../../SPEC.md)
- **Epic parente :** [`EPIC-FIL-06`](../../EPIC.md)
- **User Story parente :** [`US-FIL-603`](../../user-stories/US-FIL-603.md)
- **Jour :** `J08`
- **Sources de formation :** [`C08`](../../../../baseline/sources.md#c08) — `J08` / Quatre verdicts, risques gouvernés, preuves bornées et coût complet / `programme_prevu`<br>[`C08-G7`](../../../../baseline/sources.md#c08-g7) — `J08` / Fiche d'une page, trois risques, arrêt/repli testé, ROI et date de révision ; G7 / `programme_prevu`
- **Branche :** `feat/fil-rouge-ingenierie-auto-ia`
- **Niveau :** `Socle formation`
- **Priorité :** `P1`
- **Statut documentaire :** `Candidate`
- **Statut de preuve :** `Candidat`
- **Travail :** `À faire`
- **Responsable :** responsable du pilote — personne à désigner

Cette Feature détaille la User Story parente ; elle ne crée pas une exigence indépendante.

## Contrat candidat

- **Entrée :** Échecs observés, risques résiduels et périmètre du pilote ; responsables nominatifs à désigner humainement.
- **Sortie :** Proposition de registre avec trois risques clés pour la fiche J08, chacun doté d'un responsable, signal, action et lien à l'arrêt.
- **Périmètre :** Gouvernance du pilote déclaré ; pas de certification ni de cotation de probabilité inventée.
- **Règle canonique :** [`RM-FIL-603`](../../user-stories/US-FIL-603.md#rm-fil-603)
- **Critères canoniques :** [`CA-FIL-603-01`](../../user-stories/US-FIL-603.md#ca-fil-603-01), [`CA-FIL-603-02`](../../user-stories/US-FIL-603.md#ca-fil-603-02), [`CA-FIL-603-03`](../../user-stories/US-FIL-603.md#ca-fil-603-03)

Aucune surface future n'est affirmée comme présente ; son emplacement reste à décider avant réalisation. La baseline actuelle est décrite dans [`current-state.md`](../../../../baseline/current-state.md). Les noms de modules futurs ne sont pas présentés comme existants.

## Découpage exécutable

| Tâche | Objectif | Phase | Dépendances |
|---|---|---|---|
| [`TASK-FIL-603-01`](tasks/TASK-FIL-603-01.md) | Relier les risques aux observations et proposer les trois risques déterminants sans supprimer les réserves restantes. | Spécifier et figer l'oracle | [`US-FIL-401`](../../../EPIC-FIL-04/user-stories/US-FIL-401.md), [`US-FIL-503`](../../../EPIC-FIL-05/user-stories/US-FIL-503.md) |
| [`TASK-FIL-603-02`](tasks/TASK-FIL-603-02.md) | Faire nommer les responsables et rédiger signaux/actions/arrêts avec leurs modalités de vérification. | Réaliser dans le périmètre autorisé | [`TASK-FIL-603-01`](tasks/TASK-FIL-603-01.md) |
| [`TASK-FIL-603-03`](tasks/TASK-FIL-603-03.md) | Éprouver les signaux sur fixtures et faire accepter les responsabilités avant la fiche finale. | Vérifier et soumettre à revue | [`TASK-FIL-603-02`](tasks/TASK-FIL-603-02.md) |

La livraison et les tests sont planifiés ; aucune tâche n'est exécutée par cette spécification.

## Vérification prévue

L'oracle à appliquer est celui de la [`User Story parente`](../../user-stories/US-FIL-603.md#oracle-indépendant) : Relecture des champs du registre et exercice du signal sur fixture ; présence d'un rôle générique ne vaut pas acceptation d'une personne responsable.

Les limites d'interruption, de concurrence ou de documentation applicables restent celles des cas de la User Story. Aucun retour de code supplémentaire n'est inventé ici.

## Acceptation

- [ ] [`CA-FIL-603-01`](../../user-stories/US-FIL-603.md#ca-fil-603-01)
- [ ] [`CA-FIL-603-02`](../../user-stories/US-FIL-603.md#ca-fil-603-02)
- [ ] [`CA-FIL-603-03`](../../user-stories/US-FIL-603.md#ca-fil-603-03)

Le responsable nominatif et la décision d'acceptation restent à décider. Les décisions demeurent humaines et [`AMB-18`](../../../../governance/ambiguities.md#amb-18) reste ouverte.
