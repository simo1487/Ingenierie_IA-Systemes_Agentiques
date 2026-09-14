# FEAT-FIL-403 — Localiser la première divergence d'une trace

`Référence — feature candidate`

- **Projet parent :** [`PROJ-FIL-AUTO-IA-001`](../../../../../SPEC.md)
- **Epic parente :** [`EPIC-FIL-04`](../../EPIC.md)
- **User Story parente :** [`US-FIL-403`](../../user-stories/US-FIL-403.md)
- **Jour :** `J07`
- **Sources de formation :** [`C03`](../../../../baseline/sources.md#c03) — `J03` / Reproduction, hypothèses concurrentes, rouge/vert comparable, mutation et documentation / `support_actuel`<br>[`C07-G6`](../../../../baseline/sources.md#c07-g6) — `J07` / Outil préparé ou replay, refus avant accès, régression et première divergence ; G6 / `programme_prevu`
- **Branche :** `feat/fil-rouge-ingenierie-auto-ia`
- **Niveau :** `Socle formation`
- **Priorité :** `P1`
- **Statut documentaire :** `Candidate`
- **Statut de preuve :** `Candidat`
- **Travail :** `À faire`
- **Responsable :** mainteneur — personne à désigner

Cette Feature détaille la User Story parente ; elle ne crée pas une exigence indépendante.

## Contrat candidat

- **Entrée :** Trace attendue revue, trace observée assainie, identifiants d'événement et versions d'entrée identiques.
- **Sortie :** Observation du premier événement divergent et proposition de cause ; correction soumise au rejeu.
- **Périmètre :** Comparaison locale et enquête traçable ; pas d'observabilité distribuée obligatoire.
- **Règle canonique :** [`RM-FIL-403`](../../user-stories/US-FIL-403.md#rm-fil-403)
- **Critères canoniques :** [`CA-FIL-403-01`](../../user-stories/US-FIL-403.md#ca-fil-403-01), [`CA-FIL-403-02`](../../user-stories/US-FIL-403.md#ca-fil-403-02), [`CA-FIL-403-03`](../../user-stories/US-FIL-403.md#ca-fil-403-03)

Aucune surface future n'est affirmée comme présente ; son emplacement reste à décider avant réalisation. La baseline actuelle est décrite dans [`current-state.md`](../../../../baseline/current-state.md). Les noms de modules futurs ne sont pas présentés comme existants.

## Découpage exécutable

| Tâche | Objectif | Phase | Dépendances |
|---|---|---|---|
| [`TASK-FIL-403-01`](tasks/TASK-FIL-403-01.md) | Figer les champs d'alignement et trois traces : accès anticipé, horloges différentes, événement absent. | Spécifier et figer l'oracle | [`US-FIL-3`](../../../EPIC-FIL-00/user-stories/US-FIL-3.md), [`US-FIL-102`](../../../EPIC-FIL-01/user-stories/US-FIL-102.md), [`US-FIL-401`](../../user-stories/US-FIL-401.md) |
| [`TASK-FIL-403-02`](tasks/TASK-FIL-403-02.md) | Produire un diagnostic aligné et une hypothèse séparée de l'observation, avec référence au contrôle concerné. | Réaliser dans le périmètre autorisé | [`TASK-FIL-403-01`](tasks/TASK-FIL-403-01.md) |
| [`TASK-FIL-403-03`](tasks/TASK-FIL-403-03.md) | Faire corriger uniquement le contrôle identifié puis rejouer le jeu complet de cas et consigner le résultat. | Vérifier et soumettre à revue | [`TASK-FIL-403-02`](tasks/TASK-FIL-403-02.md) |

La livraison et les tests sont planifiés ; aucune tâche n'est exécutée par cette spécification.

## Vérification prévue

L'oracle à appliquer est celui de la [`User Story parente`](../../user-stories/US-FIL-403.md#oracle-indépendant) : Séquences courtes attendues écrites par le relecteur avec ordre explicite ; champs non sémantiques exclus explicitement ; aucun tri ne doit masquer l'ordre réel des événements.

Les limites d'interruption, de concurrence ou de documentation applicables restent celles des cas de la User Story. Aucun retour de code supplémentaire n'est inventé ici.

## Acceptation

- [ ] [`CA-FIL-403-01`](../../user-stories/US-FIL-403.md#ca-fil-403-01)
- [ ] [`CA-FIL-403-02`](../../user-stories/US-FIL-403.md#ca-fil-403-02)
- [ ] [`CA-FIL-403-03`](../../user-stories/US-FIL-403.md#ca-fil-403-03)

Le responsable nominatif et la décision d'acceptation restent à décider. Les décisions demeurent humaines et [`AMB-02`](../../../../governance/ambiguities.md#amb-02) reste ouverte.
