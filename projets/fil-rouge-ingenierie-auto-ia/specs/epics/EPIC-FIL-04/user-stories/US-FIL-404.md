# US-FIL-404 — Évaluer un retrieval sémantique avant adoption

`Référence — spécification candidate`

- **Projet parent :** [`PROJ-FIL-AUTO-IA-001`](../../../../SPEC.md)
- **Epic parente :** [`EPIC-FIL-04`](../EPIC.md)
- **Feature fille :** [`FEAT-FIL-404`](../features/FEAT-FIL-404/FEATURE.md)
- **Jour :** `J07`
- **Sources de formation :** [`C04`](../../../baseline/sources.md#c04) — `J04` / Corpus autorisé, découpage du sens, lexical/sémantique, Hit@k/MRR et support des citations / `support_actuel`<br>[`C04-RETOUR`](../../../baseline/sources.md#c04-retour) — `J04` / Requête directe avant modèle, questions attendues, empreintes, doublons et retrait des sources / `retour_rapporte`<br>[`N04`](../../../baseline/sources.md#n04) — `J04` / Questions avant IA, corpus, empreintes, Qdrant et parsing ; chiffres et décisions à confirmer / `synthese_automatique`
- **Relation pédagogique :** Extension RAG sémantique après corpus et questions, mesures par étage.
- **Niveau :** `Extension production`
- **Priorité :** `P2`
- **Statut documentaire :** `Candidate`
- **Statut de preuve :** `Candidat`
- **Travail :** `À faire`
- **Responsable :** ingénieur exigences — personne à désigner
- **Dépendances :** [`US-FIL-4`](../../EPIC-FIL-00/user-stories/US-FIL-4.md), [`US-FIL-5`](../../EPIC-FIL-00/user-stories/US-FIL-5.md), [`US-FIL-101`](../../EPIC-FIL-01/user-stories/US-FIL-101.md), [`US-FIL-104`](../../EPIC-FIL-01/user-stories/US-FIL-104.md), [`US-FIL-401`](US-FIL-401.md)
- **Ambiguïté :** [`AMB-12`](../../../governance/ambiguities.md#amb-12)

## Besoin

> En tant qu’ingénieur exigences, je veux comparer un adaptateur RAG réel au retrieval lexical afin d’adopter un index uniquement sur des preuves et conserver l'abstention.

## Périmètre

Adaptateur Qdrant ou équivalent à décider, stockage généré hors Git ; pas de promotion de l'ancien index Zephyr défaillant.

Les décisions restent humaines ; aucune implémentation métier n'est réalisée par cette spécification.

## Entrées et sorties

- **Entrée :** Corpus autorisé révisé, questions et passages attendus revus, configuration chunking/embedding/index figée, politique d'abstention approuvée.
- **Sortie :** Observations de retrieval avec source/révision/passage, résultats par question et proposition d'adoption ; échecs conservés.

Les baselines sont référencées dans [`sources.md`](../../../baseline/sources.md) ; leur révision est inconnue lorsqu'elle n'y est pas explicitement donnée. La sortie ne constitue pas, à elle seule, une preuve.

## Règle et critères

<a id="rm-fil-404"></a>
`RM-FIL-404` — Une amélioration RAG ne peut être revendiquée qu'à corpus, questions et protocole de mesure identiques et approuvés avant essai.

<a id="ca-fil-404-01"></a>
- [ ] `CA-FIL-404-01` — Étant donné la question Q1 possède des passages pertinents annotés, quand les deux retrievers sont exécutés sur la même révision, alors les résultats sont confrontés aux annotations et non à une préférence du modèle.
<a id="ca-fil-404-02"></a>
- [ ] `CA-FIL-404-02` — Étant donné Q2 n'a aucun passage pertinent dans la référence, quand le retriever répond, alors l'abstention est évaluée séparément des questions répondables.
<a id="ca-fil-404-03"></a>
- [ ] `CA-FIL-404-03` — Étant donné l'index ne correspond pas à la révision du corpus, quand le run est préparé, alors la comparaison est refusée et aucun score favorable n'est publié.

## Example Mapping

| Cas | Étant donné | Quand | Alors |
|---|---|---|---|
| Nominal | la question Q1 possède des passages pertinents annotés | les deux retrievers sont exécutés sur la même révision | les résultats sont confrontés aux annotations et non à une préférence du modèle |
| Frontière | Q2 n'a aucun passage pertinent dans la référence | le retriever répond | l'abstention est évaluée séparément des questions répondables |
| Refus | l'index ne correspond pas à la révision du corpus | le run est préparé | la comparaison est refusée et aucun score favorable n'est publié |

## Scénarios Gherkin

```gherkin
Fonctionnalité: Évaluer un retrieval sémantique avant adoption
  Contexte:
    Étant donné le périmètre et les entrées versionnées de US-FIL-404
    Et les attendus ci-dessous définis avant la future réalisation

  Scénario: Nominal — CA-FIL-404-01
    Étant donné la question Q1 possède des passages pertinents annotés
    Quand les deux retrievers sont exécutés sur la même révision
    Alors les résultats sont confrontés aux annotations et non à une préférence du modèle

  Scénario: Frontière — CA-FIL-404-02
    Étant donné Q2 n'a aucun passage pertinent dans la référence
    Quand le retriever répond
    Alors l'abstention est évaluée séparément des questions répondables

  Scénario: Refus — CA-FIL-404-03
    Étant donné l'index ne correspond pas à la révision du corpus
    Quand le run est préparé
    Alors la comparaison est refusée et aucun score favorable n'est publié
```

## Oracle indépendant

MES-03 ; annotation indépendante et cas de non-réponse ; aucun seuil de qualité n'est fixé par cette spécification candidate.

## Réalisation et preuves

- [`FEAT-FIL-404`](../features/FEAT-FIL-404/FEATURE.md) — Feature candidate
- [`TASK-FIL-404-01`](../features/FEAT-FIL-404/tasks/TASK-FIL-404-01.md) — Faire approuver corpus, annotations, politique d'abstention et configuration suivant MES-03 avant sélection de l'adaptateur.
- [`TASK-FIL-404-02`](../features/FEAT-FIL-404/tasks/TASK-FIL-404-02.md) — Prévoir le port d'un retrieval sémantique derrière le contrat de citations, sans versionner les bases générées.
- [`TASK-FIL-404-03`](../features/FEAT-FIL-404/tasks/TASK-FIL-404-03.md) — Comparer sur le jeu figé, conserver tous les échecs et faire décider l'adoption sans substituer un score IA à l'oracle.

Aucune preuve d'acceptation de cette US n'est produite par son rendu. Les artefacts existants peuvent satisfaire un prérequis après revue ; aucune répétition de travaux déjà démontrés n'est imposée.

## Questions ouvertes

Voir [`AMB-12`](../../../governance/ambiguities.md#amb-12).
