# TASK-FIL-4-01 — Figer l'inventaire autorisé, les locators et les questions avant moteur ; identifier les règles dont le découpage peut perdre le sens

`Référence — tâche candidate`

- **Epic parente :** [`EPIC-FIL-00`](../../../EPIC.md)
- **User Story parente :** [`US-FIL-4`](../../../user-stories/US-FIL-4.md)
- **Feature parente :** [`FEAT-FIL-4`](../FEATURE.md)
- **Jour :** `J01–J05`
- **Phase :** Spécifier et figer l'oracle
- **Sources héritées :** [`C04`](../../../../../baseline/sources.md#c04) — `J04` / Corpus autorisé, découpage du sens, lexical/sémantique, Hit@k/MRR et support des citations / `support_actuel`<br>[`C04-RETOUR`](../../../../../baseline/sources.md#c04-retour) — `J04` / Requête directe avant modèle, questions attendues, empreintes, doublons et retrait des sources / `retour_rapporte`<br>[`N04`](../../../../../baseline/sources.md#n04) — `J04` / Questions avant IA, corpus, empreintes, Qdrant et parsing ; chiffres et décisions à confirmer / `synthese_automatique`
- **Niveau :** `Socle formation`
- **Priorité :** `P1`
- **Statut documentaire :** `Candidate`
- **Statut de preuve :** `Candidat`
- **Travail :** `À faire`
- **Responsable :** responsable de corpus — personne à désigner

## Objectif

Figer l'inventaire autorisé, les locators et les questions avant moteur ; identifier les règles dont le découpage peut perdre le sens.

## Prérequis

- **Capacités préalables :** [`US-FIL-1`](../../../user-stories/US-FIL-1.md)
- **Estimation :** non attribuée
- **Date :** non attribuée

Un artefact existant peut satisfaire une capacité préalable après revue ; la tâche ne force pas à refaire un acquis démontré.

## Travail et livrable attendus

**Figer l'inventaire autorisé, les locators et les questions avant moteur ; identifier les règles dont le découpage peut perdre le sens**

Produire un artefact relu couvrant les cas et l'oracle de [`US-FIL-4`](../../../user-stories/US-FIL-4.md) dans le mode autorisé.

Une fixture ou un replay n’est recevable que si le périmètre de la US l’autorise, avec mode et limites déclarés.

- **Entrée héritée :** Sources locales autorisées et révisées avec kind, statut, droit, empreinte de contenu et locator ; questions prévues et annotations candidates avant moteur.
- **Sortie héritée :** Observation d'inventaire et passages avec id, texte, source, révision, locator, statut et accès ; doublons signalés et rejets de provenance visibles.
- **Périmètre hérité :** Préparation locale J04, avec parsing/dédoublonnage adaptés aux sources ; Qdrant, Docling et suppression physique sont des choix non imposés.
- **Critères de la US parente (références, pas preuve de couverture de cette tâche) :** [`CA-FIL-4-01`](../../../user-stories/US-FIL-4.md#ca-fil-4-01), [`CA-FIL-4-02`](../../../user-stories/US-FIL-4.md#ca-fil-4-02), [`CA-FIL-4-03`](../../../user-stories/US-FIL-4.md#ca-fil-4-03), [`CA-FIL-4-04`](../../../user-stories/US-FIL-4.md#ca-fil-4-04)

Les clauses et oracles de la spécification parente s'appliquent ; toute modification nécessite une nouvelle revue, pas une adaptation implicite au résultat observé.

## Vérification / sortie

- [ ] Artefact complet correspondant à la phase `Spécifier et figer l'oracle`
- [ ] Source, version, mode et statut déclarés
- [ ] Preuve ou disposition de revue jointe ; la tâche ne devient pas automatiquement `Terminé`

## Questions

Voir [`AMB-22`](../../../../../governance/ambiguities.md#amb-22).
