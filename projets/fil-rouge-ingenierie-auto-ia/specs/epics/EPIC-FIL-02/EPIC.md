# EPIC-FIL-02 — Reprise fiable et mémoire gouvernée

`Référence — Epic candidate`

- **Projet parent :** [`PROJ-FIL-AUTO-IA-001`](../../../SPEC.md)
- **Jour :** `J06`
- **Gate pédagogique associée :** `G5` — aucune approbation inférée
- **Sources alignées :** [`C03-RETOUR`](../../baseline/sources.md#c03-retour) — `J03` / Plan préalable, bornes et comparaisons des tests générés, concurrence, doubles, contrôles dans la chaîne<br>[`C06-G5`](../../baseline/sources.md#c06-g5) — `J06` / Comparaison, journal complet, interruption et mémoire ; revue G5<br>[`N05`](../../baseline/sources.md#n05) — `J05` / Approches simples, types, budgets, contrôle humain et structuration ; propos à confirmer<br>[`C06`](../../baseline/sources.md#c06) — `J06` / Comparaison d'organisations, rôles, reprise, idempotence, mémoire et trace<br>[`C04-RETOUR`](../../baseline/sources.md#c04-retour) — `J04` / Requête directe avant modèle, questions attendues, empreintes, doublons et retrait des sources
- **Statut documentaire :** `Candidate`
- **Statut de preuve :** `Candidat`
- **Travail :** `À faire`

## Valeur

Reprendre un lot sans double effet ni réutilisation d'une information périmée.

## Socle et extension

- **Socle formation :** [`US-FIL-201`](user-stories/US-FIL-201.md), [`US-FIL-202`](user-stories/US-FIL-202.md), [`US-FIL-203`](user-stories/US-FIL-203.md)
- **Extension production :** [`US-FIL-204`](user-stories/US-FIL-204.md)

Une source alignée ne prouve ni apprentissage, ni réalisation, ni acceptation. Un artefact existant peut satisfaire un prérequis après revue.

## Enfants

| User Story | Feature | Rôle | Valeur | Niveau / priorité |
|---|---|---|---|---|
| [`US-FIL-201`](user-stories/US-FIL-201.md) | [`FEAT-FIL-201`](features/FEAT-FIL-201/FEATURE.md) | opérateur | éviter de refaire une opération déjà confirmée | Socle formation / P1 |
| [`US-FIL-202`](user-stories/US-FIL-202.md) | [`FEAT-FIL-202`](features/FEAT-FIL-202/FEATURE.md) | opérateur | éviter une boucle de reprise sans progrès | Socle formation / P1 |
| [`US-FIL-203`](user-stories/US-FIL-203.md) | [`FEAT-FIL-203`](features/FEAT-FIL-203/FEATURE.md) | responsable de corpus | ne pas réinjecter une ancienne règle dans un nouveau lot | Socle formation / P1 |
| [`US-FIL-204`](user-stories/US-FIL-204.md) | [`FEAT-FIL-204`](features/FEAT-FIL-204/FEATURE.md) | responsable des données | appliquer une politique de rétention sans détruire les preuves d'audit | Extension production / P2 |

Les Features restent sous leur User Story ; elles ne sont pas parentes des Stories.

## Dépendances

- **Capacités externes à l'Epic :** [`US-FIL-102`](../EPIC-FIL-01/user-stories/US-FIL-102.md), [`US-FIL-101`](../EPIC-FIL-01/user-stories/US-FIL-101.md)
- Les dépendances internes sont détaillées dans chaque User Story et ses tâches.

## Périmètres et exclusions

- [`US-FIL-201`](user-stories/US-FIL-201.md) — Démonstration locale ou replay documenté pour J06 ; stockage distribué et effets réels exclus.
- [`US-FIL-202`](user-stories/US-FIL-202.md) — Budgets d'essais et de temps ; tarifs et seuils de production restent des décisions humaines.
- [`US-FIL-203`](user-stories/US-FIL-203.md) — Mémoire locale gouvernée et règle datée ; aucune mémoire globale de conversation ni conservation illimitée.
- [`US-FIL-204`](user-stories/US-FIL-204.md) — Révocation locale sur données fictives ; suppression réelle et rétention légale exclues sans confirmation dédiée.

## Achèvement mesurable

L'Epic ne peut être considérée achevée que lorsque les critères candidats retenus disposent de preuves exécutées, reliées à leurs oracles indépendants et revues humainement. Aucune Gate n'est déclarée franchie ici.
