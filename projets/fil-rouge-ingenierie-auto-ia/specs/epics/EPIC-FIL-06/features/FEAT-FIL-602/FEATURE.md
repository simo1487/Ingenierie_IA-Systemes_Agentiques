# FEAT-FIL-602 — Confronter coût complet et bénéfice mesuré

`Référence — feature candidate`

- **Projet parent :** [`PROJ-FIL-AUTO-IA-001`](../../../../../SPEC.md)
- **Epic parente :** [`EPIC-FIL-06`](../../EPIC.md)
- **User Story parente :** [`US-FIL-602`](../../user-stories/US-FIL-602.md)
- **Jour :** `J08`
- **Sources de formation :** [`C05-ROI`](../../../../baseline/sources.md#c05-roi) — `J05` / ROI incrémental avec temps humain complet et absence de double comptage / `support_actuel`<br>[`C08-G7`](../../../../baseline/sources.md#c08-g7) — `J08` / Fiche d'une page, trois risques, arrêt/repli testé, ROI et date de révision ; G7 / `programme_prevu`
- **Branche :** `feat/fil-rouge-ingenierie-auto-ia`
- **Niveau :** `Socle formation`
- **Priorité :** `P1`
- **Statut documentaire :** `Candidate`
- **Statut de preuve :** `Candidat`
- **Travail :** `À faire`
- **Responsable :** responsable produit — personne à désigner

Cette Feature détaille la User Story parente ; elle ne crée pas une exigence indépendante.

## Contrat candidat

- **Entrée :** Observations figées de baseline et essai sur une période comparable : demandes réellement traitées N, temps humains complets t0/t1, tarif h, investissement I et coûts récurrents supplémentaires R ; chaque poste possède sa source et sa nature observée ou hypothétique.
- **Sortie :** Observations et hypothèses séparées, temps humain complet visible, valeur de capacité B, coûts supplémentaires C, valeur nette et ROI incrémental selon MES-05 ; scénarios favorable/pessimiste distincts.
- **Périmètre :** Fiche économique d'un essai ; pas de promesse de gain, projection commerciale ou barème obligatoire.
- **Règle canonique :** [`RM-FIL-602`](../../user-stories/US-FIL-602.md#rm-fil-602)
- **Critères canoniques :** [`CA-FIL-602-01`](../../user-stories/US-FIL-602.md#ca-fil-602-01), [`CA-FIL-602-02`](../../user-stories/US-FIL-602.md#ca-fil-602-02), [`CA-FIL-602-03`](../../user-stories/US-FIL-602.md#ca-fil-602-03), [`CA-FIL-602-04`](../../user-stories/US-FIL-602.md#ca-fil-602-04)

Aucune surface future n'est affirmée comme présente ; son emplacement reste à décider avant réalisation. La baseline actuelle est décrite dans [`current-state.md`](../../../../baseline/current-state.md). Les noms de modules futurs ne sont pas présentés comme existants.

## Découpage exécutable

| Tâche | Objectif | Phase | Dépendances |
|---|---|---|---|
| [`TASK-FIL-602-01`](tasks/TASK-FIL-602-01.md) | Définir période, unité d'œuvre et postes de coûts selon MES-05 ; collecter leurs sources sans inventer les valeurs manquantes. | Spécifier et figer l'oracle | [`US-FIL-103`](../../../EPIC-FIL-01/user-stories/US-FIL-103.md) |
| [`TASK-FIL-602-02`](tasks/TASK-FIL-602-02.md) | Assembler une capture figée des observations et hypothèses avec scénarios favorable/pessimiste explicitement étiquetés. | Réaliser dans le périmètre autorisé | [`TASK-FIL-602-01`](tasks/TASK-FIL-602-01.md) |
| [`TASK-FIL-602-03`](tasks/TASK-FIL-602-03.md) | Effectuer un contre-calcul et présenter les limites, coûts humains et hypothèse fragile au décideur. | Vérifier et soumettre à revue | [`TASK-FIL-602-02`](tasks/TASK-FIL-602-02.md) |

La livraison et les tests sont planifiés ; aucune tâche n'est exécutée par cette spécification.

## Vérification prévue

L'oracle à appliquer est celui de la [`User Story parente`](../../user-stories/US-FIL-602.md#oracle-indépendant) : MES-05 dans governance/measurement-contracts.md ; contre-calcul indépendant sur capture figée des données, jamais sur chiffres inventés par le modèle.

Les limites d'interruption, de concurrence ou de documentation applicables restent celles des cas de la User Story. Aucun retour de code supplémentaire n'est inventé ici.

## Acceptation

- [ ] [`CA-FIL-602-01`](../../user-stories/US-FIL-602.md#ca-fil-602-01)
- [ ] [`CA-FIL-602-02`](../../user-stories/US-FIL-602.md#ca-fil-602-02)
- [ ] [`CA-FIL-602-03`](../../user-stories/US-FIL-602.md#ca-fil-602-03)
- [ ] [`CA-FIL-602-04`](../../user-stories/US-FIL-602.md#ca-fil-602-04)

Le responsable nominatif et la décision d'acceptation restent à décider. Les décisions demeurent humaines et [`AMB-17`](../../../../governance/ambiguities.md#amb-17) reste ouverte.
