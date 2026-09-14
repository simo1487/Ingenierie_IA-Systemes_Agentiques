# EPIC-FIL-05 — Livraison reproductible et exploitation réversible

`Référence — Epic candidate`

- **Projet parent :** [`PROJ-FIL-AUTO-IA-001`](../../../SPEC.md)
- **Jour :** `J08`
- **Gate pédagogique associée :** `G7` — aucune approbation inférée
- **Sources alignées :** [`C03`](../../baseline/sources.md#c03) — `J03` / Reproduction, hypothèses concurrentes, rouge/vert comparable, mutation et documentation<br>[`C08`](../../baseline/sources.md#c08) — `J08` / Quatre verdicts, risques gouvernés, preuves bornées et coût complet<br>[`C03-RETOUR`](../../baseline/sources.md#c03-retour) — `J03` / Plan préalable, bornes et comparaisons des tests générés, concurrence, doubles, contrôles dans la chaîne<br>[`C06-G5`](../../baseline/sources.md#c06-g5) — `J06` / Comparaison, journal complet, interruption et mémoire ; revue G5<br>[`C08-G7`](../../baseline/sources.md#c08-g7) — `J08` / Fiche d'une page, trois risques, arrêt/repli testé, ROI et date de révision ; G7<br>[`C06`](../../baseline/sources.md#c06) — `J06` / Comparaison d'organisations, rôles, reprise, idempotence, mémoire et trace<br>[`C07`](../../baseline/sources.md#c07) — `J07` / Politique avant accès, révision pédagogique MCP 2026-07-28, contenu non fiable et cas indépendants
- **Statut documentaire :** `Candidate`
- **Statut de preuve :** `Candidat`
- **Travail :** `À faire`

## Valeur

Identifier ce qui est livré et arrêter un pilote avec un retour arrière démontré.

## Socle et extension

- **Socle formation :** [`US-FIL-503`](user-stories/US-FIL-503.md)
- **Extension production :** [`US-FIL-501`](user-stories/US-FIL-501.md), [`US-FIL-502`](user-stories/US-FIL-502.md), [`US-FIL-504`](user-stories/US-FIL-504.md)

Une source alignée ne prouve ni apprentissage, ni réalisation, ni acceptation. Un artefact existant peut satisfaire un prérequis après revue.

## Enfants

| User Story | Feature | Rôle | Valeur | Niveau / priorité |
|---|---|---|---|---|
| [`US-FIL-501`](user-stories/US-FIL-501.md) | [`FEAT-FIL-501`](features/FEAT-FIL-501/FEATURE.md) | mainteneur | permettre à un tiers de reproduire le périmètre annoncé | Extension production / P1 |
| [`US-FIL-502`](user-stories/US-FIL-502.md) | [`FEAT-FIL-502`](features/FEAT-FIL-502/FEATURE.md) | relecteur intégration | détecter les régressions avant intégration | Extension production / P2 |
| [`US-FIL-503`](user-stories/US-FIL-503.md) | [`FEAT-FIL-503`](features/FEAT-FIL-503/FEATURE.md) | responsable d'exploitation | rendre la décision de pilote réversible | Socle formation / P1 |
| [`US-FIL-504`](user-stories/US-FIL-504.md) | [`FEAT-FIL-504`](features/FEAT-FIL-504/FEATURE.md) | opérateur | détecter un signal d'arrêt sans journaliser les contenus sensibles | Extension production / P2 |

Les Features restent sous leur User Story ; elles ne sont pas parentes des Stories.

## Dépendances

- **Capacités externes à l'Epic :** [`US-FIL-104`](../EPIC-FIL-01/user-stories/US-FIL-104.md), [`US-FIL-201`](../EPIC-FIL-02/user-stories/US-FIL-201.md), [`US-FIL-401`](../EPIC-FIL-04/user-stories/US-FIL-401.md), [`US-FIL-402`](../EPIC-FIL-04/user-stories/US-FIL-402.md), [`US-FIL-202`](../EPIC-FIL-02/user-stories/US-FIL-202.md), [`US-FIL-102`](../EPIC-FIL-01/user-stories/US-FIL-102.md)
- Les dépendances internes sont détaillées dans chaque User Story et ses tâches.

## Périmètres et exclusions

- [`US-FIL-501`](user-stories/US-FIL-501.md) — Packaging et inventaire, pas de publication, déploiement ou push dans ce lot.
- [`US-FIL-502`](user-stories/US-FIL-502.md) — Préparation des contrôles ; aucune modification de protection de branche ni fusion automatique.
- [`US-FIL-503`](user-stories/US-FIL-503.md) — Exercice sans effet sur un service réel ; tout déploiement/retour arrière réel exige une autorisation spécifique.
- [`US-FIL-504`](user-stories/US-FIL-504.md) — Observabilité minimale locale ; plateforme cloud et seuils de service non choisis implicitement.

## Achèvement mesurable

L'Epic ne peut être considérée achevée que lorsque les critères candidats retenus disposent de preuves exécutées, reliées à leurs oracles indépendants et revues humainement. Aucune Gate n'est déclarée franchie ici.
