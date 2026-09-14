# EPIC-FIL-06 — Gouvernance, coûts et décision humaine

`Référence — Epic candidate`

- **Projet parent :** [`PROJ-FIL-AUTO-IA-001`](../../../SPEC.md)
- **Jour :** `J08`
- **Gate pédagogique associée :** `G7` — aucune approbation inférée
- **Sources alignées :** [`C02`](../../baseline/sources.md#c02) — `J02` / Exigence singulière, inconnues, exemples et oracle indépendant ; Gherkin non universellement obligatoire<br>[`C03`](../../baseline/sources.md#c03) — `J03` / Reproduction, hypothèses concurrentes, rouge/vert comparable, mutation et documentation<br>[`C08`](../../baseline/sources.md#c08) — `J08` / Quatre verdicts, risques gouvernés, preuves bornées et coût complet<br>[`C05-ROI`](../../baseline/sources.md#c05-roi) — `J05` / ROI incrémental avec temps humain complet et absence de double comptage<br>[`C08-G7`](../../baseline/sources.md#c08-g7) — `J08` / Fiche d'une page, trois risques, arrêt/repli testé, ROI et date de révision ; G7
- **Statut documentaire :** `Candidate`
- **Statut de preuve :** `Candidat`
- **Travail :** `À faire`

## Valeur

Choisir une suite justifiée par les preuves, les risques et les coûts complets, y compris arrêter.

## Socle et extension

- **Socle formation :** [`US-FIL-601`](user-stories/US-FIL-601.md), [`US-FIL-602`](user-stories/US-FIL-602.md), [`US-FIL-603`](user-stories/US-FIL-603.md), [`US-FIL-604`](user-stories/US-FIL-604.md)
- **Extension production :** Aucune

Une source alignée ne prouve ni apprentissage, ni réalisation, ni acceptation. Un artefact existant peut satisfaire un prérequis après revue.

## Enfants

| User Story | Feature | Rôle | Valeur | Niveau / priorité |
|---|---|---|---|---|
| [`US-FIL-601`](user-stories/US-FIL-601.md) | [`FEAT-FIL-601`](features/FEAT-FIL-601/FEATURE.md) | relecteur indépendant | ne pas confondre des champs remplis avec une validation | Socle formation / P1 |
| [`US-FIL-602`](user-stories/US-FIL-602.md) | [`FEAT-FIL-602`](features/FEAT-FIL-602/FEATURE.md) | responsable produit | décider sans limiter le coût aux seuls appels IA | Socle formation / P1 |
| [`US-FIL-603`](user-stories/US-FIL-603.md) | [`FEAT-FIL-603`](features/FEAT-FIL-603/FEATURE.md) | responsable du pilote | transformer des réserves vagues en conditions d'arrêt observables | Socle formation / P1 |
| [`US-FIL-604`](user-stories/US-FIL-604.md) | [`FEAT-FIL-604`](features/FEAT-FIL-604/FEATURE.md) | décideur humain | conclure sur un périmètre explicite et révisable | Socle formation / P1 |

Les Features restent sous leur User Story ; elles ne sont pas parentes des Stories.

## Dépendances

- **Capacités externes à l'Epic :** [`US-FIL-2`](../EPIC-FIL-00/user-stories/US-FIL-2.md), [`US-FIL-5`](../EPIC-FIL-00/user-stories/US-FIL-5.md), [`US-FIL-101`](../EPIC-FIL-01/user-stories/US-FIL-101.md), [`US-FIL-401`](../EPIC-FIL-04/user-stories/US-FIL-401.md), [`US-FIL-103`](../EPIC-FIL-01/user-stories/US-FIL-103.md), [`US-FIL-503`](../EPIC-FIL-05/user-stories/US-FIL-503.md)
- Les dépendances internes sont détaillées dans chaque User Story et ses tâches.

## Périmètres et exclusions

- [`US-FIL-601`](user-stories/US-FIL-601.md) — Dossier et revue humaine ; signature cryptographique et référentiel externe non imposés.
- [`US-FIL-602`](user-stories/US-FIL-602.md) — Fiche économique d'un essai ; pas de promesse de gain, projection commerciale ou barème obligatoire.
- [`US-FIL-603`](user-stories/US-FIL-603.md) — Gouvernance du pilote déclaré ; pas de certification ni de cotation de probabilité inventée.
- [`US-FIL-604`](user-stories/US-FIL-604.md) — Fiche et décision pédagogique G7 ; lancement réel, paiement, déploiement et intégration restent des actions séparément autorisées.

## Achèvement mesurable

L'Epic ne peut être considérée achevée que lorsque les critères candidats retenus disposent de preuves exécutées, reliées à leurs oracles indépendants et revues humainement. Aucune Gate n'est déclarée franchie ici.
