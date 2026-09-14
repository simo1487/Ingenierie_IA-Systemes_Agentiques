# FEAT-FIL-404 — Évaluer un retrieval sémantique avant adoption

`Référence — feature candidate`

- **Projet parent :** [`PROJ-FIL-AUTO-IA-001`](../../../../../SPEC.md)
- **Epic parente :** [`EPIC-FIL-04`](../../EPIC.md)
- **User Story parente :** [`US-FIL-404`](../../user-stories/US-FIL-404.md)
- **Jour :** `J07`
- **Sources de formation :** [`C04`](../../../../baseline/sources.md#c04) — `J04` / Corpus autorisé, découpage du sens, lexical/sémantique, Hit@k/MRR et support des citations / `support_actuel`<br>[`C04-RETOUR`](../../../../baseline/sources.md#c04-retour) — `J04` / Requête directe avant modèle, questions attendues, empreintes, doublons et retrait des sources / `retour_rapporte`<br>[`N04`](../../../../baseline/sources.md#n04) — `J04` / Questions avant IA, corpus, empreintes, Qdrant et parsing ; chiffres et décisions à confirmer / `synthese_automatique`
- **Branche :** `feat/fil-rouge-ingenierie-auto-ia`
- **Niveau :** `Extension production`
- **Priorité :** `P2`
- **Statut documentaire :** `Candidate`
- **Statut de preuve :** `Candidat`
- **Travail :** `À faire`
- **Responsable :** ingénieur exigences — personne à désigner

Cette Feature détaille la User Story parente ; elle ne crée pas une exigence indépendante.

## Contrat candidat

- **Entrée :** Corpus autorisé révisé, questions et passages attendus revus, configuration chunking/embedding/index figée, politique d'abstention approuvée.
- **Sortie :** Observations de retrieval avec source/révision/passage, résultats par question et proposition d'adoption ; échecs conservés.
- **Périmètre :** Adaptateur Qdrant ou équivalent à décider, stockage généré hors Git ; pas de promotion de l'ancien index Zephyr défaillant.
- **Règle canonique :** [`RM-FIL-404`](../../user-stories/US-FIL-404.md#rm-fil-404)
- **Critères canoniques :** [`CA-FIL-404-01`](../../user-stories/US-FIL-404.md#ca-fil-404-01), [`CA-FIL-404-02`](../../user-stories/US-FIL-404.md#ca-fil-404-02), [`CA-FIL-404-03`](../../user-stories/US-FIL-404.md#ca-fil-404-03)

Surface proposée : `src/auto_ai_flow/agents.py`. Ce rapprochement est candidat et ne constitue pas une trace vérifiée. La baseline actuelle est décrite dans [`current-state.md`](../../../../baseline/current-state.md). Les noms de modules futurs ne sont pas présentés comme existants.

## Découpage exécutable

| Tâche | Objectif | Phase | Dépendances |
|---|---|---|---|
| [`TASK-FIL-404-01`](tasks/TASK-FIL-404-01.md) | Faire approuver corpus, annotations, politique d'abstention et configuration suivant MES-03 avant sélection de l'adaptateur. | Spécifier et figer l'oracle | [`US-FIL-4`](../../../EPIC-FIL-00/user-stories/US-FIL-4.md), [`US-FIL-5`](../../../EPIC-FIL-00/user-stories/US-FIL-5.md), [`US-FIL-101`](../../../EPIC-FIL-01/user-stories/US-FIL-101.md), [`US-FIL-104`](../../../EPIC-FIL-01/user-stories/US-FIL-104.md), [`US-FIL-401`](../../user-stories/US-FIL-401.md) |
| [`TASK-FIL-404-02`](tasks/TASK-FIL-404-02.md) | Prévoir le port d'un retrieval sémantique derrière le contrat de citations, sans versionner les bases générées. | Réaliser dans le périmètre autorisé | [`TASK-FIL-404-01`](tasks/TASK-FIL-404-01.md) |
| [`TASK-FIL-404-03`](tasks/TASK-FIL-404-03.md) | Comparer sur le jeu figé, conserver tous les échecs et faire décider l'adoption sans substituer un score IA à l'oracle. | Vérifier et soumettre à revue | [`TASK-FIL-404-02`](tasks/TASK-FIL-404-02.md) |

La livraison et les tests sont planifiés ; aucune tâche n'est exécutée par cette spécification.

## Vérification prévue

L'oracle à appliquer est celui de la [`User Story parente`](../../user-stories/US-FIL-404.md#oracle-indépendant) : MES-03 ; annotation indépendante et cas de non-réponse ; aucun seuil de qualité n'est fixé par cette spécification candidate.

Les limites d'interruption, de concurrence ou de documentation applicables restent celles des cas de la User Story. Aucun retour de code supplémentaire n'est inventé ici.

## Acceptation

- [ ] [`CA-FIL-404-01`](../../user-stories/US-FIL-404.md#ca-fil-404-01)
- [ ] [`CA-FIL-404-02`](../../user-stories/US-FIL-404.md#ca-fil-404-02)
- [ ] [`CA-FIL-404-03`](../../user-stories/US-FIL-404.md#ca-fil-404-03)

Le responsable nominatif et la décision d'acceptation restent à décider. Les décisions demeurent humaines et [`AMB-12`](../../../../governance/ambiguities.md#amb-12) reste ouverte.
