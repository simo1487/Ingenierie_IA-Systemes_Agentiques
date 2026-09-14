# FEAT-FIL-203 — Refuser une mémoire périmée ou hors périmètre

`Référence — feature candidate`

- **Projet parent :** [`PROJ-FIL-AUTO-IA-001`](../../../../../SPEC.md)
- **Epic parente :** [`EPIC-FIL-02`](../../EPIC.md)
- **User Story parente :** [`US-FIL-203`](../../user-stories/US-FIL-203.md)
- **Jour :** `J06`
- **Sources de formation :** [`C04-RETOUR`](../../../../baseline/sources.md#c04-retour) — `J04` / Requête directe avant modèle, questions attendues, empreintes, doublons et retrait des sources / `retour_rapporte`<br>[`C06-G5`](../../../../baseline/sources.md#c06-g5) — `J06` / Comparaison, journal complet, interruption et mémoire ; revue G5 / `programme_prevu`
- **Branche :** `feat/fil-rouge-ingenierie-auto-ia`
- **Niveau :** `Socle formation`
- **Priorité :** `P1`
- **Statut documentaire :** `Candidate`
- **Statut de preuve :** `Candidat`
- **Travail :** `À faire`
- **Responsable :** responsable de corpus — personne à désigner

Cette Feature détaille la User Story parente ; elle ne crée pas une exigence indépendante.

## Contrat candidat

- **Entrée :** Entrée mémoire avec id, source, révision, portée, created_at, expires_at et responsable ; horloge de référence.
- **Sortie :** Observation de lecture permise ou refus tracé ; correction sous nouvelle version.
- **Périmètre :** Mémoire locale gouvernée et règle datée ; aucune mémoire globale de conversation ni conservation illimitée.
- **Règle canonique :** [`RM-FIL-203`](../../user-stories/US-FIL-203.md#rm-fil-203)
- **Critères canoniques :** [`CA-FIL-203-01`](../../user-stories/US-FIL-203.md#ca-fil-203-01), [`CA-FIL-203-02`](../../user-stories/US-FIL-203.md#ca-fil-203-02), [`CA-FIL-203-03`](../../user-stories/US-FIL-203.md#ca-fil-203-03)

Aucune surface future n'est affirmée comme présente ; son emplacement reste à décider avant réalisation. La baseline actuelle est décrite dans [`current-state.md`](../../../../baseline/current-state.md). Les noms de modules futurs ne sont pas présentés comme existants.

La table de décision candidate associée est [`RM-FIL-203`](../../../../governance/decision-tables.md#mémoire-rm-fil-203).

## Découpage exécutable

| Tâche | Objectif | Phase | Dépendances |
|---|---|---|---|
| [`TASK-FIL-203-01`](tasks/TASK-FIL-203-01.md) | Définir le schéma mémoire, la table portée/expiration et les responsabilités de correction. | Spécifier et figer l'oracle | [`US-FIL-101`](../../../EPIC-FIL-01/user-stories/US-FIL-101.md), [`US-FIL-102`](../../../EPIC-FIL-01/user-stories/US-FIL-102.md) |
| [`TASK-FIL-203-02`](tasks/TASK-FIL-203-02.md) | Mettre en place la lecture filtrée et la correction versionnée, ou un replay explicite de la politique. | Réaliser dans le périmètre autorisé | [`TASK-FIL-203-01`](tasks/TASK-FIL-203-01.md) |
| [`TASK-FIL-203-03`](tasks/TASK-FIL-203-03.md) | Présenter une entrée expirée et hors portée, vérifier le contexte transmis et faire relire la règle de mémoire. | Vérifier et soumettre à revue | [`TASK-FIL-203-02`](tasks/TASK-FIL-203-02.md) |

La livraison et les tests sont planifiés ; aucune tâche n'est exécutée par cette spécification.

## Vérification prévue

L'oracle à appliquer est celui de la [`User Story parente`](../../user-stories/US-FIL-203.md#oracle-indépendant) : Table portée/expiration écrite avant code ; horloge injectée ; inspection du contexte effectivement transmis au fournisseur, pas uniquement du message de refus.

Les limites d'interruption, de concurrence ou de documentation applicables restent celles des cas de la User Story. Aucun retour de code supplémentaire n'est inventé ici.

## Acceptation

- [ ] [`CA-FIL-203-01`](../../user-stories/US-FIL-203.md#ca-fil-203-01)
- [ ] [`CA-FIL-203-02`](../../user-stories/US-FIL-203.md#ca-fil-203-02)
- [ ] [`CA-FIL-203-03`](../../user-stories/US-FIL-203.md#ca-fil-203-03)

Le responsable nominatif et la décision d'acceptation restent à décider. Les décisions demeurent humaines et [`AMB-07`](../../../../governance/ambiguities.md#amb-07) reste ouverte.
