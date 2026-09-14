# TASK-FIL-404-02 — Prévoir le port d'un retrieval sémantique derrière le contrat de citations, sans versionner les bases générées

`Référence — tâche candidate`

- **Epic parente :** [`EPIC-FIL-04`](../../../EPIC.md)
- **User Story parente :** [`US-FIL-404`](../../../user-stories/US-FIL-404.md)
- **Feature parente :** [`FEAT-FIL-404`](../FEATURE.md)
- **Jour :** `J07`
- **Phase :** Réaliser dans le périmètre autorisé
- **Sources héritées :** [`C04`](../../../../../baseline/sources.md#c04) — `J04` / Corpus autorisé, découpage du sens, lexical/sémantique, Hit@k/MRR et support des citations / `support_actuel`<br>[`C04-RETOUR`](../../../../../baseline/sources.md#c04-retour) — `J04` / Requête directe avant modèle, questions attendues, empreintes, doublons et retrait des sources / `retour_rapporte`<br>[`N04`](../../../../../baseline/sources.md#n04) — `J04` / Questions avant IA, corpus, empreintes, Qdrant et parsing ; chiffres et décisions à confirmer / `synthese_automatique`
- **Niveau :** `Extension production`
- **Priorité :** `P2`
- **Statut documentaire :** `Candidate`
- **Statut de preuve :** `Candidat`
- **Travail :** `À faire`
- **Responsable :** ingénieur exigences — personne à désigner

## Objectif

Prévoir le port d'un retrieval sémantique derrière le contrat de citations, sans versionner les bases générées.

## Prérequis

- **Capacités préalables :** [`TASK-FIL-404-01`](TASK-FIL-404-01.md)
- **Estimation :** non attribuée
- **Date :** non attribuée

Un artefact existant peut satisfaire une capacité préalable après revue ; la tâche ne force pas à refaire un acquis démontré.

## Travail et livrable attendus

**Prévoir le port d'un retrieval sémantique derrière le contrat de citations, sans versionner les bases générées**

Réaliser la phase décrite par [`FEAT-FIL-404`](../FEATURE.md) sans revendiquer une disponibilité ou une preuve non observée.

Un replay ou une fixture prépare la vérification ; il ne suffit pas à prouver l’intégration réelle de l’extension.

- **Entrée héritée :** Corpus autorisé révisé, questions et passages attendus revus, configuration chunking/embedding/index figée, politique d'abstention approuvée.
- **Sortie héritée :** Observations de retrieval avec source/révision/passage, résultats par question et proposition d'adoption ; échecs conservés.
- **Périmètre hérité :** Adaptateur Qdrant ou équivalent à décider, stockage généré hors Git ; pas de promotion de l'ancien index Zephyr défaillant.
- **Critères de la US parente (références, pas preuve de couverture de cette tâche) :** [`CA-FIL-404-01`](../../../user-stories/US-FIL-404.md#ca-fil-404-01), [`CA-FIL-404-02`](../../../user-stories/US-FIL-404.md#ca-fil-404-02), [`CA-FIL-404-03`](../../../user-stories/US-FIL-404.md#ca-fil-404-03)

Les clauses et oracles de la spécification parente s'appliquent ; toute modification nécessite une nouvelle revue, pas une adaptation implicite au résultat observé.

## Vérification / sortie

- [ ] Artefact complet correspondant à la phase `Réaliser dans le périmètre autorisé`
- [ ] Source, version, mode et statut déclarés
- [ ] Preuve ou disposition de revue jointe ; la tâche ne devient pas automatiquement `Terminé`

## Questions

Voir [`AMB-12`](../../../../../governance/ambiguities.md#amb-12).
