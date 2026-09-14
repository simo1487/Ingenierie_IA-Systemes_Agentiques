# FEAT-FIL-302 — Identifier la révision MCP de l'outil préparé

`Référence — feature candidate`

- **Projet parent :** [`PROJ-FIL-AUTO-IA-001`](../../../../../SPEC.md)
- **Epic parente :** [`EPIC-FIL-03`](../../EPIC.md)
- **User Story parente :** [`US-FIL-302`](../../user-stories/US-FIL-302.md)
- **Jour :** `J07`
- **Sources de formation :** [`C07`](../../../../baseline/sources.md#c07) — `J07` / Politique avant accès, révision pédagogique MCP 2026-07-28, contenu non fiable et cas indépendants / `programme_prevu`<br>[`C07-G6`](../../../../baseline/sources.md#c07-g6) — `J07` / Outil préparé ou replay, refus avant accès, régression et première divergence ; G6 / `programme_prevu`
- **Branche :** `feat/fil-rouge-ingenierie-auto-ia`
- **Niveau :** `Socle formation`
- **Priorité :** `P1`
- **Statut documentaire :** `Candidate`
- **Statut de preuve :** `Candidat`
- **Travail :** `À faire`
- **Responsable :** intégrateur — personne à désigner

Cette Feature détaille la User Story parente ; elle ne crée pas une exigence indépendante.

## Contrat candidat

- **Entrée :** Contrat de l'outil préparé ou trace replay ; révision pédagogique MCP 2026-07-28 ; capacités annoncées et provenance de la fixture.
- **Sortie :** Observation de concordance ou incompatibilité signalée ; mode outil réel, fixture ou replay visible.
- **Périmètre :** Inspection d'un outil préparé ; aucun développement de serveur ni choix de SDK exigé.
- **Règle canonique :** [`RM-FIL-302`](../../user-stories/US-FIL-302.md#rm-fil-302)
- **Critères canoniques :** [`CA-FIL-302-01`](../../user-stories/US-FIL-302.md#ca-fil-302-01), [`CA-FIL-302-02`](../../user-stories/US-FIL-302.md#ca-fil-302-02), [`CA-FIL-302-03`](../../user-stories/US-FIL-302.md#ca-fil-302-03)

Aucune surface future n'est affirmée comme présente ; son emplacement reste à décider avant réalisation. La baseline actuelle est décrite dans [`current-state.md`](../../../../baseline/current-state.md). Les noms de modules futurs ne sont pas présentés comme existants.

## Découpage exécutable

| Tâche | Objectif | Phase | Dépendances |
|---|---|---|---|
| [`TASK-FIL-302-01`](tasks/TASK-FIL-302-01.md) | Préparer la fiche de protocole avec révision pédagogique, capacités, erreurs et provenance des exemples. | Spécifier et figer l'oracle | [`US-FIL-301`](../../user-stories/US-FIL-301.md) |
| [`TASK-FIL-302-02`](tasks/TASK-FIL-302-02.md) | Inspecter l'outil préparé ou rejouer la fixture, en séparant révisions et modes dans les artefacts. | Réaliser dans le périmètre autorisé | [`TASK-FIL-302-01`](tasks/TASK-FIL-302-01.md) |
| [`TASK-FIL-302-03`](tasks/TASK-FIL-302-03.md) | Consigner toute révision inattendue et faire décider la compatibilité avant d'assembler les preuves G6. | Vérifier et soumettre à revue | [`TASK-FIL-302-02`](tasks/TASK-FIL-302-02.md) |

La livraison et les tests sont planifiés ; aucune tâche n'est exécutée par cette spécification.

## Vérification prévue

L'oracle à appliquer est celui de la [`User Story parente`](../../user-stories/US-FIL-302.md#oracle-indépendant) : Valeur épinglée dans le cours J07, lignes 58–64, comparée à la trace originale de l'outil ; ce contrat ne prétend pas vérifier la validité externe de cette révision MCP.

Les limites d'interruption, de concurrence ou de documentation applicables restent celles des cas de la User Story. Aucun retour de code supplémentaire n'est inventé ici.

## Acceptation

- [ ] [`CA-FIL-302-01`](../../user-stories/US-FIL-302.md#ca-fil-302-01)
- [ ] [`CA-FIL-302-02`](../../user-stories/US-FIL-302.md#ca-fil-302-02)
- [ ] [`CA-FIL-302-03`](../../user-stories/US-FIL-302.md#ca-fil-302-03)

Le responsable nominatif et la décision d'acceptation restent à décider. Les décisions demeurent humaines et [`AMB-09`](../../../../governance/ambiguities.md#amb-09) reste ouverte.
