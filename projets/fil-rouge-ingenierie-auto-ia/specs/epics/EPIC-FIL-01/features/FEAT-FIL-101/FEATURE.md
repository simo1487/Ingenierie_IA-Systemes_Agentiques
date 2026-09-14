# FEAT-FIL-101 — Autoriser une baseline avant toute étape dépendante

`Référence — feature candidate`

- **Projet parent :** [`PROJ-FIL-AUTO-IA-001`](../../../../../SPEC.md)
- **Epic parente :** [`EPIC-FIL-01`](../../EPIC.md)
- **User Story parente :** [`US-FIL-101`](../../user-stories/US-FIL-101.md)
- **Jour :** `J06`
- **Sources de formation :** [`C02`](../../../../baseline/sources.md#c02) — `J02` / Exigence singulière, inconnues, exemples et oracle indépendant ; Gherkin non universellement obligatoire / `support_actuel`<br>[`C04`](../../../../baseline/sources.md#c04) — `J04` / Corpus autorisé, découpage du sens, lexical/sémantique, Hit@k/MRR et support des citations / `support_actuel`<br>[`C06`](../../../../baseline/sources.md#c06) — `J06` / Comparaison d'organisations, rôles, reprise, idempotence, mémoire et trace / `programme_prevu`
- **Branche :** `feat/fil-rouge-ingenierie-auto-ia`
- **Niveau :** `Socle formation`
- **Priorité :** `P1`
- **Statut documentaire :** `Candidate`
- **Statut de preuve :** `Candidat`
- **Travail :** `À faire`
- **Responsable :** responsable de baseline — personne à désigner

Cette Feature détaille la User Story parente ; elle ne crée pas une exigence indépendante.

## Contrat candidat

- **Entrée :** Manifeste local versionné : run_id, objective, baselines avec id/révision, approbation portant sur cette version. Corpus fictif pour le socle ; corpus réel soumis à AMB-01.
- **Sortie :** Observation de validation ou arrêt Bloqué avec motif, sans appel fournisseur en cas d'échec.
- **Périmètre :** Prévalidation du manifeste et propagation du blocage ; hors périmètre : acquisition de corpus réel.
- **Règle canonique :** [`RM-FIL-101`](../../user-stories/US-FIL-101.md#rm-fil-101)
- **Critères canoniques :** [`CA-FIL-101-01`](../../user-stories/US-FIL-101.md#ca-fil-101-01), [`CA-FIL-101-02`](../../user-stories/US-FIL-101.md#ca-fil-101-02), [`CA-FIL-101-03`](../../user-stories/US-FIL-101.md#ca-fil-101-03)

Surface proposée : `src/auto_ai_flow/orchestrator.py`. Ce rapprochement est candidat et ne constitue pas une trace vérifiée. La baseline actuelle est décrite dans [`current-state.md`](../../../../baseline/current-state.md). Les noms de modules futurs ne sont pas présentés comme existants.

La table de décision candidate associée est [`RM-FIL-101`](../../../../governance/decision-tables.md#prévalidation-rm-fil-101).

## Découpage exécutable

| Tâche | Objectif | Phase | Dépendances |
|---|---|---|---|
| [`TASK-FIL-101-01`](tasks/TASK-FIL-101-01.md) | Figer les variantes M1, corpus vide, révision vide et approbation absente ; écrire la table de décision de prévalidation. | Spécifier et figer l'oracle | [`US-FIL-1`](../../../EPIC-FIL-00/user-stories/US-FIL-1.md), [`US-FIL-4`](../../../EPIC-FIL-00/user-stories/US-FIL-4.md) |
| [`TASK-FIL-101-02`](tasks/TASK-FIL-101-02.md) | Prévoir la validation d'entrée et l'arrêt des étapes dépendantes dans AutomotiveAIFlow.run ; préserver la CLI hors ligne. | Réaliser dans le périmètre autorisé | [`TASK-FIL-101-01`](tasks/TASK-FIL-101-01.md) |
| [`TASK-FIL-101-03`](tasks/TASK-FIL-101-03.md) | Vérifier les refus avec espions, éprouver la suppression du garde de corpus et faire accepter la baseline par un responsable. | Vérifier et soumettre à revue | [`TASK-FIL-101-02`](tasks/TASK-FIL-101-02.md) |

La livraison et les tests sont planifiés ; aucune tâche n'est exécutée par cette spécification.

## Vérification prévue

L'oracle à appliquer est celui de la [`User Story parente`](../../user-stories/US-FIL-101.md#oracle-indépendant) : Manifestes M1 valides et invalides figés par le relecteur ; espion des appels retrieval/fournisseur indépendant des statuts retournés. La sortie seule ne suffit pas à prouver l'absence d'appel.

Les limites d'interruption, de concurrence ou de documentation applicables restent celles des cas de la User Story. Aucun retour de code supplémentaire n'est inventé ici.

## Acceptation

- [ ] [`CA-FIL-101-01`](../../user-stories/US-FIL-101.md#ca-fil-101-01)
- [ ] [`CA-FIL-101-02`](../../user-stories/US-FIL-101.md#ca-fil-101-02)
- [ ] [`CA-FIL-101-03`](../../user-stories/US-FIL-101.md#ca-fil-101-03)

Le responsable nominatif et la décision d'acceptation restent à décider. Les décisions demeurent humaines et [`AMB-01`](../../../../governance/ambiguities.md#amb-01) reste ouverte.
