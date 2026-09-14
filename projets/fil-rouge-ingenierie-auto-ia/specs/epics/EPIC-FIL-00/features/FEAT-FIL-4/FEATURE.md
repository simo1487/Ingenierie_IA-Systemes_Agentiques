# FEAT-FIL-4 — Préparer des passages autorisés et retrouvables

`Référence — feature candidate`

- **Projet parent :** [`PROJ-FIL-AUTO-IA-001`](../../../../../SPEC.md)
- **Epic parente :** [`EPIC-FIL-00`](../../EPIC.md)
- **User Story parente :** [`US-FIL-4`](../../user-stories/US-FIL-4.md)
- **Jour :** `J01–J05`
- **Sources de formation :** [`C04`](../../../../baseline/sources.md#c04) — `J04` / Corpus autorisé, découpage du sens, lexical/sémantique, Hit@k/MRR et support des citations / `support_actuel`<br>[`C04-RETOUR`](../../../../baseline/sources.md#c04-retour) — `J04` / Requête directe avant modèle, questions attendues, empreintes, doublons et retrait des sources / `retour_rapporte`<br>[`N04`](../../../../baseline/sources.md#n04) — `J04` / Questions avant IA, corpus, empreintes, Qdrant et parsing ; chiffres et décisions à confirmer / `synthese_automatique`
- **Branche :** `feat/fil-rouge-ingenierie-auto-ia`
- **Niveau :** `Socle formation`
- **Priorité :** `P1`
- **Statut documentaire :** `Candidate`
- **Statut de preuve :** `Candidat`
- **Travail :** `À faire`
- **Responsable :** responsable de corpus — personne à désigner

Cette Feature détaille la User Story parente ; elle ne crée pas une exigence indépendante.

## Contrat candidat

- **Entrée :** Sources locales autorisées et révisées avec kind, statut, droit, empreinte de contenu et locator ; questions prévues et annotations candidates avant moteur.
- **Sortie :** Observation d'inventaire et passages avec id, texte, source, révision, locator, statut et accès ; doublons signalés et rejets de provenance visibles.
- **Périmètre :** Préparation locale J04, avec parsing/dédoublonnage adaptés aux sources ; Qdrant, Docling et suppression physique sont des choix non imposés.
- **Règle canonique :** [`RM-FIL-4`](../../user-stories/US-FIL-4.md#rm-fil-4)
- **Critères canoniques :** [`CA-FIL-4-01`](../../user-stories/US-FIL-4.md#ca-fil-4-01), [`CA-FIL-4-02`](../../user-stories/US-FIL-4.md#ca-fil-4-02), [`CA-FIL-4-03`](../../user-stories/US-FIL-4.md#ca-fil-4-03), [`CA-FIL-4-04`](../../user-stories/US-FIL-4.md#ca-fil-4-04)

Aucune surface future n'est affirmée comme présente ; son emplacement reste à décider avant réalisation. La baseline actuelle est décrite dans [`current-state.md`](../../../../baseline/current-state.md). Les noms de modules futurs ne sont pas présentés comme existants.

## Découpage exécutable

| Tâche | Objectif | Phase | Dépendances |
|---|---|---|---|
| [`TASK-FIL-4-01`](tasks/TASK-FIL-4-01.md) | Figer l'inventaire autorisé, les locators et les questions avant moteur ; identifier les règles dont le découpage peut perdre le sens. | Spécifier et figer l'oracle | [`US-FIL-1`](../../user-stories/US-FIL-1.md) |
| [`TASK-FIL-4-02`](tasks/TASK-FIL-4-02.md) | Préparer les passages, empreintes et signalements de doublons, sans fusion automatique de versions ou de droits distincts. | Réaliser dans le périmètre autorisé | [`TASK-FIL-4-01`](tasks/TASK-FIL-4-01.md) |
| [`TASK-FIL-4-03`](tasks/TASK-FIL-4-03.md) | Contrôler manuellement les locators et une requête directe ; vérifier exclusion d'une source retirée et lister les dérivés concernés. | Vérifier et soumettre à revue | [`TASK-FIL-4-02`](tasks/TASK-FIL-4-02.md) |

La livraison et les tests sont planifiés ; aucune tâche n'est exécutée par cette spécification.

## Vérification prévue

L'oracle à appliquer est celui de la [`User Story parente`](../../user-stories/US-FIL-4.md#oracle-indépendant) : Source originale relue avec conditions et exceptions ; comparaison d'empreintes limitée à l'identité de contenu, jamais à la vérité. Requête directe et inspection du contexte avant tout branchement de modèle ; aucun seuil de similarité universel.

Les limites d'interruption, de concurrence ou de documentation applicables restent celles des cas de la User Story. Aucun retour de code supplémentaire n'est inventé ici.

## Acceptation

- [ ] [`CA-FIL-4-01`](../../user-stories/US-FIL-4.md#ca-fil-4-01)
- [ ] [`CA-FIL-4-02`](../../user-stories/US-FIL-4.md#ca-fil-4-02)
- [ ] [`CA-FIL-4-03`](../../user-stories/US-FIL-4.md#ca-fil-4-03)
- [ ] [`CA-FIL-4-04`](../../user-stories/US-FIL-4.md#ca-fil-4-04)

Le responsable nominatif et la décision d'acceptation restent à décider. Les décisions demeurent humaines et [`AMB-22`](../../../../governance/ambiguities.md#amb-22) reste ouverte.
