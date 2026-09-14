# EPIC-FIL-00 — Capitaliser les acquis avant d'étendre le workflow

`Référence — Epic candidate`

- **Projet parent :** [`PROJ-FIL-AUTO-IA-001`](../../../SPEC.md)
- **Jour :** `J01–J05`
- **Gate pédagogique associée :** `G0–G4 : acquis à examiner, non présumés franchis` — aucune approbation inférée
- **Sources alignées :** [`C01`](../../baseline/sources.md#c01) — `J01` / Mécanisme proportionné, données, hébergement et souveraineté distincts<br>[`C05`](../../baseline/sources.md#c05) — `J05` / Besoin avant framework, règle/recherche/workflow/agent et valeur observable<br>[`N05`](../../baseline/sources.md#n05) — `J05` / Approches simples, types, budgets, contrôle humain et structuration ; propos à confirmer<br>[`C02`](../../baseline/sources.md#c02) — `J02` / Exigence singulière, inconnues, exemples et oracle indépendant ; Gherkin non universellement obligatoire<br>[`N02`](../../baseline/sources.md#n02) — `J02` / Structuration des exigences, moindre privilège et gabarit de feature ; propos à confirmer<br>[`C03`](../../baseline/sources.md#c03) — `J03` / Reproduction, hypothèses concurrentes, rouge/vert comparable, mutation et documentation<br>[`C03-RETOUR`](../../baseline/sources.md#c03-retour) — `J03` / Plan préalable, bornes et comparaisons des tests générés, concurrence, doubles, contrôles dans la chaîne<br>[`N03`](../../baseline/sources.md#n03) — `J03` / Plan préalable, tests générés, scripts, qualité et organisation des spécifications ; propos à confirmer<br>[`C04`](../../baseline/sources.md#c04) — `J04` / Corpus autorisé, découpage du sens, lexical/sémantique, Hit@k/MRR et support des citations<br>[`C04-RETOUR`](../../baseline/sources.md#c04-retour) — `J04` / Requête directe avant modèle, questions attendues, empreintes, doublons et retrait des sources<br>[`N04`](../../baseline/sources.md#n04) — `J04` / Questions avant IA, corpus, empreintes, Qdrant et parsing ; chiffres et décisions à confirmer<br>[`C05-SKILL`](../../baseline/sources.md#c05-skill) — `J05` / Méthode capitalisée, outils/événements versionnés, limites des démonstrations LlamaIndex
- **Statut documentaire :** `Candidate`
- **Statut de preuve :** `Candidat`
- **Travail :** `À faire`

## Valeur

Repartir de besoins, sources et preuves examinés plutôt que multiplier les agents sur une baseline implicite.

Cette Epic capitalise les pièces J01–J05 déjà enseignées ou déjà produites. Elle demande leur examen et seulement la préparation des pièces manquantes ; elle n'impose pas de rejouer l'ensemble des journées.

## Socle et extension

- **Socle formation :** [`US-FIL-1`](user-stories/US-FIL-1.md), [`US-FIL-2`](user-stories/US-FIL-2.md), [`US-FIL-3`](user-stories/US-FIL-3.md), [`US-FIL-4`](user-stories/US-FIL-4.md), [`US-FIL-5`](user-stories/US-FIL-5.md), [`US-FIL-6`](user-stories/US-FIL-6.md)
- **Extension production :** Aucune

Une source alignée ne prouve ni apprentissage, ni réalisation, ni acceptation. Un artefact existant peut satisfaire un prérequis après revue.

## Enfants

| User Story | Feature | Rôle | Valeur | Niveau / priorité |
|---|---|---|---|---|
| [`US-FIL-1`](user-stories/US-FIL-1.md) | [`FEAT-FIL-1`](features/FEAT-FIL-1/FEATURE.md) | responsable produit | éviter une autonomie inutile et un transfert de données non autorisé | Socle formation / P1 |
| [`US-FIL-2`](user-stories/US-FIL-2.md) | [`FEAT-FIL-2`](features/FEAT-FIL-2/FEATURE.md) | ingénieur exigences | définir des attendus réfutables avant génération de code | Socle formation / P1 |
| [`US-FIL-3`](user-stories/US-FIL-3.md) | [`FEAT-FIL-3`](features/FEAT-FIL-3/FEATURE.md) | mainteneur | ne pas accepter un correctif convaincant mais non démontré | Socle formation / P1 |
| [`US-FIL-4`](user-stories/US-FIL-4.md) | [`FEAT-FIL-4`](features/FEAT-FIL-4/FEATURE.md) | responsable de corpus | retrouver la règle avec ses conditions sans confondre identité et pertinence | Socle formation / P1 |
| [`US-FIL-5`](user-stories/US-FIL-5.md) | [`FEAT-FIL-5`](features/FEAT-FIL-5/FEATURE.md) | relecteur exigences | ne pas confondre une citation existante avec une réponse justifiée | Socle formation / P1 |
| [`US-FIL-6`](user-stories/US-FIL-6.md) | [`FEAT-FIL-6`](features/FEAT-FIL-6/FEATURE.md) | intégrateur | préparer J06 sans dépendre d'une conversation implicite | Socle formation / P1 |

Les Features restent sous leur User Story ; elles ne sont pas parentes des Stories.

## Dépendances

- **Capacités externes à l'Epic :** Aucune
- Les dépendances internes sont détaillées dans chaque User Story et ses tâches.

## Périmètres et exclusions

- [`US-FIL-1`](user-stories/US-FIL-1.md) — Cadrage et lecture des acquis J01/J05 ; aucun framework, runtime ou fournisseur nouveau imposé, aucune clé manipulée.
- [`US-FIL-2`](user-stories/US-FIL-2.md) — Audit d'un acquis J02 ; ne pas confondre Draft, proposition et validation d'exigence réelle.
- [`US-FIL-3`](user-stories/US-FIL-3.md) — Chaîne de preuve générale J03, distincte de la régression hostile J07 ; aucune correction métier appliquée par la rédaction de cette US.
- [`US-FIL-4`](user-stories/US-FIL-4.md) — Préparation locale J04, avec parsing/dédoublonnage adaptés aux sources ; Qdrant, Docling et suppression physique sont des choix non imposés.
- [`US-FIL-5`](user-stories/US-FIL-5.md) — Revue de l'ancrage des propositions déjà au cœur du fil rouge ; pas seulement évaluation d'un futur moteur sémantique.
- [`US-FIL-6`](user-stories/US-FIL-6.md) — Capitalisation J05 et interface vers J06 ; ne pas installer un framework ou créer une configuration d'agent dans ce lot documentaire.

## Achèvement mesurable

L'Epic ne peut être considérée achevée que lorsque les critères candidats retenus disposent de preuves exécutées, reliées à leurs oracles indépendants et revues humainement. Aucune Gate n'est déclarée franchie ici.
