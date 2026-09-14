# EPIC-FIL-04 — Évaluation indépendante et non-régression

`Référence — Epic candidate`

- **Projet parent :** [`PROJ-FIL-AUTO-IA-001`](../../../SPEC.md)
- **Jour :** `J07`
- **Gate pédagogique associée :** `G6` — aucune approbation inférée
- **Sources alignées :** [`C02`](../../baseline/sources.md#c02) — `J02` / Exigence singulière, inconnues, exemples et oracle indépendant ; Gherkin non universellement obligatoire<br>[`C07`](../../baseline/sources.md#c07) — `J07` / Politique avant accès, révision pédagogique MCP 2026-07-28, contenu non fiable et cas indépendants<br>[`C03`](../../baseline/sources.md#c03) — `J03` / Reproduction, hypothèses concurrentes, rouge/vert comparable, mutation et documentation<br>[`C07-G6`](../../baseline/sources.md#c07-g6) — `J07` / Outil préparé ou replay, refus avant accès, régression et première divergence ; G6<br>[`C04`](../../baseline/sources.md#c04) — `J04` / Corpus autorisé, découpage du sens, lexical/sémantique, Hit@k/MRR et support des citations<br>[`C04-RETOUR`](../../baseline/sources.md#c04-retour) — `J04` / Requête directe avant modèle, questions attendues, empreintes, doublons et retrait des sources<br>[`N04`](../../baseline/sources.md#n04) — `J04` / Questions avant IA, corpus, empreintes, Qdrant et parsing ; chiffres et décisions à confirmer<br>[`C08`](../../baseline/sources.md#c08) — `J08` / Quatre verdicts, risques gouvernés, preuves bornées et coût complet
- **Statut documentaire :** `Candidate`
- **Statut de preuve :** `Candidat`
- **Travail :** `À faire`

## Valeur

Mettre à l'épreuve le workflow et ses adaptateurs sans qu'un score masque une violation critique.

## Socle et extension

- **Socle formation :** [`US-FIL-401`](user-stories/US-FIL-401.md), [`US-FIL-402`](user-stories/US-FIL-402.md), [`US-FIL-403`](user-stories/US-FIL-403.md)
- **Extension production :** [`US-FIL-404`](user-stories/US-FIL-404.md), [`US-FIL-405`](user-stories/US-FIL-405.md)

Une source alignée ne prouve ni apprentissage, ni réalisation, ni acceptation. Un artefact existant peut satisfaire un prérequis après revue.

## Enfants

| User Story | Feature | Rôle | Valeur | Niveau / priorité |
|---|---|---|---|---|
| [`US-FIL-401`](user-stories/US-FIL-401.md) | [`FEAT-FIL-401`](features/FEAT-FIL-401/FEATURE.md) | responsable évaluation | éviter une validation par simple plausibilité | Socle formation / P1 |
| [`US-FIL-402`](user-stories/US-FIL-402.md) | [`FEAT-FIL-402`](features/FEAT-FIL-402/FEATURE.md) | relecteur sécurité | écarter les tests de refus purement textuels | Socle formation / P1 |
| [`US-FIL-403`](user-stories/US-FIL-403.md) | [`FEAT-FIL-403`](features/FEAT-FIL-403/FEATURE.md) | mainteneur | corriger le premier contrôle fautif plutôt que masquer un symptôme | Socle formation / P1 |
| [`US-FIL-404`](user-stories/US-FIL-404.md) | [`FEAT-FIL-404`](features/FEAT-FIL-404/FEATURE.md) | ingénieur exigences | adopter un index uniquement sur des preuves et conserver l'abstention | Extension production / P2 |
| [`US-FIL-405`](user-stories/US-FIL-405.md) | [`FEAT-FIL-405`](features/FEAT-FIL-405/FEATURE.md) | responsable produit | sélectionner un candidat sans prendre le score de démonstration pour une preuve | Extension production / P2 |

Les Features restent sous leur User Story ; elles ne sont pas parentes des Stories.

## Dépendances

- **Capacités externes à l'Epic :** [`US-FIL-301`](../EPIC-FIL-03/user-stories/US-FIL-301.md), [`US-FIL-302`](../EPIC-FIL-03/user-stories/US-FIL-302.md), [`US-FIL-303`](../EPIC-FIL-03/user-stories/US-FIL-303.md), [`US-FIL-3`](../EPIC-FIL-00/user-stories/US-FIL-3.md), [`US-FIL-102`](../EPIC-FIL-01/user-stories/US-FIL-102.md), [`US-FIL-4`](../EPIC-FIL-00/user-stories/US-FIL-4.md), [`US-FIL-5`](../EPIC-FIL-00/user-stories/US-FIL-5.md), [`US-FIL-101`](../EPIC-FIL-01/user-stories/US-FIL-101.md), [`US-FIL-104`](../EPIC-FIL-01/user-stories/US-FIL-104.md)
- Les dépendances internes sont détaillées dans chaque User Story et ses tâches.

## Périmètres et exclusions

- [`US-FIL-401`](user-stories/US-FIL-401.md) — Petit jeu pertinent, sans quota historique obligatoire ni seuil de succès inventé.
- [`US-FIL-402`](user-stories/US-FIL-402.md) — Mutation ciblée défensive en environnement isolé ; aucune désactivation de politique de dépôt.
- [`US-FIL-403`](user-stories/US-FIL-403.md) — Comparaison locale et enquête traçable ; pas d'observabilité distribuée obligatoire.
- [`US-FIL-404`](user-stories/US-FIL-404.md) — Adaptateur Qdrant ou équivalent à décider, stockage généré hors Git ; pas de promotion de l'ancien index Zephyr défaillant.
- [`US-FIL-405`](user-stories/US-FIL-405.md) — Fiches autorisées en lecture seule ; recherche web, clonage/exécution et décision de licence automatiques exclus.

## Achèvement mesurable

L'Epic ne peut être considérée achevée que lorsque les critères candidats retenus disposent de preuves exécutées, reliées à leurs oracles indépendants et revues humainement. Aucune Gate n'est déclarée franchie ici.
