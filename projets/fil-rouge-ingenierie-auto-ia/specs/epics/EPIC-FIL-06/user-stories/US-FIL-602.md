# US-FIL-602 — Confronter coût complet et bénéfice mesuré

`Référence — spécification candidate`

- **Projet parent :** [`PROJ-FIL-AUTO-IA-001`](../../../../SPEC.md)
- **Epic parente :** [`EPIC-FIL-06`](../EPIC.md)
- **Feature fille :** [`FEAT-FIL-602`](../features/FEAT-FIL-602/FEATURE.md)
- **Jour :** `J08`
- **Sources de formation :** [`C05-ROI`](../../../baseline/sources.md#c05-roi) — `J05` / ROI incrémental avec temps humain complet et absence de double comptage / `support_actuel`<br>[`C08-G7`](../../../baseline/sources.md#c08-g7) — `J08` / Fiche d'une page, trois risques, arrêt/repli testé, ROI et date de révision ; G7 / `programme_prevu`
- **Relation pédagogique :** Même convention de ROI incrémental, temps humain complet visible et aucun double compte.
- **Niveau :** `Socle formation`
- **Priorité :** `P1`
- **Statut documentaire :** `Candidate`
- **Statut de preuve :** `Candidat`
- **Travail :** `À faire`
- **Responsable :** responsable produit — personne à désigner
- **Dépendances :** [`US-FIL-103`](../../EPIC-FIL-01/user-stories/US-FIL-103.md)
- **Ambiguïté :** [`AMB-17`](../../../governance/ambiguities.md#amb-17)

## Besoin

> En tant que responsable produit, je veux comparer le coût du workflow à une baseline documentée afin de décider sans limiter le coût aux seuls appels IA.

## Périmètre

Fiche économique d'un essai ; pas de promesse de gain, projection commerciale ou barème obligatoire.

Les décisions restent humaines ; aucune implémentation métier n'est réalisée par cette spécification.

## Entrées et sorties

- **Entrée :** Observations figées de baseline et essai sur une période comparable : demandes réellement traitées N, temps humains complets t0/t1, tarif h, investissement I et coûts récurrents supplémentaires R ; chaque poste possède sa source et sa nature observée ou hypothétique.
- **Sortie :** Observations et hypothèses séparées, temps humain complet visible, valeur de capacité B, coûts supplémentaires C, valeur nette et ROI incrémental selon MES-05 ; scénarios favorable/pessimiste distincts.

Les baselines sont référencées dans [`sources.md`](../../../baseline/sources.md) ; leur révision est inconnue lorsqu'elle n'y est pas explicitement donnée. La sortie ne constitue pas, à elle seule, une preuve.

## Règle et critères

<a id="rm-fil-602"></a>
`RM-FIL-602` — Une donnée de coût absente n'est jamais imputée à zéro pour produire un ROI favorable.

<a id="ca-fil-602-01"></a>
- [ ] `CA-FIL-602-01` — Étant donné toutes les composantes comparables sont renseignées avec sources, quand le dossier économique est établi, alors coût complet, bénéfice et hypothèses sont présentés selon MES-05.
<a id="ca-fil-602-02"></a>
- [ ] `CA-FIL-602-02` — Étant donné le dénominateur du ROI est nul, quand le calcul est demandé, alors le ROI est non calculable et les montants restent visibles.
<a id="ca-fil-602-03"></a>
- [ ] `CA-FIL-602-03` — Étant donné le temps de revue ou le coût de correction manque, quand le dossier est examiné, alors le coût complet est incomplet et aucun ROI mesuré n'est revendiqué.
<a id="ca-fil-602-04"></a>
- [ ] `CA-FIL-602-04` — Étant donné le temps humain avec IA t1 dépasse t0 à qualité comparable, quand le dossier économique est établi, alors le bénéfice négatif est conservé et les coûts de revue déjà inclus dans t1 ne sont pas déduits une seconde fois dans R.

## Example Mapping

| Cas | Étant donné | Quand | Alors |
|---|---|---|---|
| Nominal | toutes les composantes comparables sont renseignées avec sources | le dossier économique est établi | coût complet, bénéfice et hypothèses sont présentés selon MES-05 |
| Frontière | le dénominateur du ROI est nul | le calcul est demandé | le ROI est non calculable et les montants restent visibles |
| Refus | le temps de revue ou le coût de correction manque | le dossier est examiné | le coût complet est incomplet et aucun ROI mesuré n'est revendiqué |
| Régression de valeur | le temps humain avec IA t1 dépasse t0 à qualité comparable | le dossier économique est établi | le bénéfice négatif est conservé et les coûts de revue déjà inclus dans t1 ne sont pas déduits une seconde fois dans R |

## Scénarios Gherkin

```gherkin
Fonctionnalité: Confronter coût complet et bénéfice mesuré
  Contexte:
    Étant donné le périmètre et les entrées versionnées de US-FIL-602
    Et les attendus ci-dessous définis avant la future réalisation

  Scénario: Nominal — CA-FIL-602-01
    Étant donné toutes les composantes comparables sont renseignées avec sources
    Quand le dossier économique est établi
    Alors coût complet, bénéfice et hypothèses sont présentés selon MES-05

  Scénario: Frontière — CA-FIL-602-02
    Étant donné le dénominateur du ROI est nul
    Quand le calcul est demandé
    Alors le ROI est non calculable et les montants restent visibles

  Scénario: Refus — CA-FIL-602-03
    Étant donné le temps de revue ou le coût de correction manque
    Quand le dossier est examiné
    Alors le coût complet est incomplet et aucun ROI mesuré n'est revendiqué

  Scénario: Régression de valeur — CA-FIL-602-04
    Étant donné le temps humain avec IA t1 dépasse t0 à qualité comparable
    Quand le dossier économique est établi
    Alors le bénéfice négatif est conservé et les coûts de revue déjà inclus dans t1 ne sont pas déduits une seconde fois dans R
```

## Oracle indépendant

MES-05 dans governance/measurement-contracts.md ; contre-calcul indépendant sur capture figée des données, jamais sur chiffres inventés par le modèle.

## Réalisation et preuves

- [`FEAT-FIL-602`](../features/FEAT-FIL-602/FEATURE.md) — Feature candidate
- [`TASK-FIL-602-01`](../features/FEAT-FIL-602/tasks/TASK-FIL-602-01.md) — Définir période, unité d'œuvre et postes de coûts selon MES-05 ; collecter leurs sources sans inventer les valeurs manquantes.
- [`TASK-FIL-602-02`](../features/FEAT-FIL-602/tasks/TASK-FIL-602-02.md) — Assembler une capture figée des observations et hypothèses avec scénarios favorable/pessimiste explicitement étiquetés.
- [`TASK-FIL-602-03`](../features/FEAT-FIL-602/tasks/TASK-FIL-602-03.md) — Effectuer un contre-calcul et présenter les limites, coûts humains et hypothèse fragile au décideur.

Aucune preuve d'acceptation de cette US n'est produite par son rendu. Les artefacts existants peuvent satisfaire un prérequis après revue ; aucune répétition de travaux déjà démontrés n'est imposée.

## Questions ouvertes

Voir [`AMB-17`](../../../governance/ambiguities.md#amb-17).
