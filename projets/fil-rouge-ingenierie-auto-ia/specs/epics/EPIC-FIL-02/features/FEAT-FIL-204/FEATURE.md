# FEAT-FIL-204 — Prouver l'effacement logique d'une mémoire

`Référence — feature candidate`

- **Projet parent :** [`PROJ-FIL-AUTO-IA-001`](../../../../../SPEC.md)
- **Epic parente :** [`EPIC-FIL-02`](../../EPIC.md)
- **User Story parente :** [`US-FIL-204`](../../user-stories/US-FIL-204.md)
- **Jour :** `J06`
- **Sources de formation :** [`C04-RETOUR`](../../../../baseline/sources.md#c04-retour) — `J04` / Requête directe avant modèle, questions attendues, empreintes, doublons et retrait des sources / `retour_rapporte`<br>[`C06`](../../../../baseline/sources.md#c06) — `J06` / Comparaison d'organisations, rôles, reprise, idempotence, mémoire et trace / `programme_prevu`
- **Branche :** `feat/fil-rouge-ingenierie-auto-ia`
- **Niveau :** `Extension production`
- **Priorité :** `P2`
- **Statut documentaire :** `Candidate`
- **Statut de preuve :** `Candidat`
- **Travail :** `À faire`
- **Responsable :** responsable des données — personne à désigner

Cette Feature détaille la User Story parente ; elle ne crée pas une exigence indépendante.

## Contrat candidat

- **Entrée :** Demande autorisée visant une entrée et une politique de rétention approuvée ; copies de test uniquement.
- **Sortie :** Observation de révocation et reçu minimal sans contenu effacé ; limites sur sauvegardes explicitement déclarées.
- **Périmètre :** Révocation locale sur données fictives ; suppression réelle et rétention légale exclues sans confirmation dédiée.
- **Règle canonique :** [`RM-FIL-204`](../../user-stories/US-FIL-204.md#rm-fil-204)
- **Critères canoniques :** [`CA-FIL-204-01`](../../user-stories/US-FIL-204.md#ca-fil-204-01), [`CA-FIL-204-02`](../../user-stories/US-FIL-204.md#ca-fil-204-02), [`CA-FIL-204-03`](../../user-stories/US-FIL-204.md#ca-fil-204-03)

Aucune surface future n'est affirmée comme présente ; son emplacement reste à décider avant réalisation. La baseline actuelle est décrite dans [`current-state.md`](../../../../baseline/current-state.md). Les noms de modules futurs ne sont pas présentés comme existants.

## Découpage exécutable

| Tâche | Objectif | Phase | Dépendances |
|---|---|---|---|
| [`TASK-FIL-204-01`](tasks/TASK-FIL-204-01.md) | Recenser les copies/cache et définir la portée du reçu ainsi que l'autorité de révocation. | Spécifier et figer l'oracle | [`US-FIL-203`](../../user-stories/US-FIL-203.md) |
| [`TASK-FIL-204-02`](tasks/TASK-FIL-204-02.md) | Concevoir l'invalidation de lecture et de cache avec reçu minimal, sans purger les preuves de run. | Réaliser dans le périmètre autorisé | [`TASK-FIL-204-01`](tasks/TASK-FIL-204-01.md) |
| [`TASK-FIL-204-03`](tasks/TASK-FIL-204-03.md) | Vérifier la non-réutilisation et l'idempotence sur fixtures puis documenter les limites de sauvegarde. | Vérifier et soumettre à revue | [`TASK-FIL-204-02`](tasks/TASK-FIL-204-02.md) |

La livraison et les tests sont planifiés ; aucune tâche n'est exécutée par cette spécification.

## Vérification prévue

L'oracle à appliquer est celui de la [`User Story parente`](../../user-stories/US-FIL-204.md#oracle-indépendant) : Lecture via tous les chemins de cache déclarés sur fixtures ; reçu comparé à l'identité de la demande. L'effacement physique des sauvegardes n'est pas affirmé sans preuve spécifique.

Les limites d'interruption, de concurrence ou de documentation applicables restent celles des cas de la User Story. Aucun retour de code supplémentaire n'est inventé ici.

## Acceptation

- [ ] [`CA-FIL-204-01`](../../user-stories/US-FIL-204.md#ca-fil-204-01)
- [ ] [`CA-FIL-204-02`](../../user-stories/US-FIL-204.md#ca-fil-204-02)
- [ ] [`CA-FIL-204-03`](../../user-stories/US-FIL-204.md#ca-fil-204-03)

Le responsable nominatif et la décision d'acceptation restent à décider. Les décisions demeurent humaines et [`AMB-07`](../../../../governance/ambiguities.md#amb-07) reste ouverte.
