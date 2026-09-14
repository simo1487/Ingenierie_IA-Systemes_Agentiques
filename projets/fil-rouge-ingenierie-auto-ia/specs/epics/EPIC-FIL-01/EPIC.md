# EPIC-FIL-01 — Exécution observable et choix d'organisation

`Référence — Epic candidate`

- **Projet parent :** [`PROJ-FIL-AUTO-IA-001`](../../../SPEC.md)
- **Jour :** `J06`
- **Gate pédagogique associée :** `G5` — aucune approbation inférée
- **Sources alignées :** [`C02`](../../baseline/sources.md#c02) — `J02` / Exigence singulière, inconnues, exemples et oracle indépendant ; Gherkin non universellement obligatoire<br>[`C04`](../../baseline/sources.md#c04) — `J04` / Corpus autorisé, découpage du sens, lexical/sémantique, Hit@k/MRR et support des citations<br>[`C06`](../../baseline/sources.md#c06) — `J06` / Comparaison d'organisations, rôles, reprise, idempotence, mémoire et trace<br>[`C03-RETOUR`](../../baseline/sources.md#c03-retour) — `J03` / Plan préalable, bornes et comparaisons des tests générés, concurrence, doubles, contrôles dans la chaîne<br>[`C06-G5`](../../baseline/sources.md#c06-g5) — `J06` / Comparaison, journal complet, interruption et mémoire ; revue G5<br>[`C05`](../../baseline/sources.md#c05) — `J05` / Besoin avant framework, règle/recherche/workflow/agent et valeur observable<br>[`C05-SKILL`](../../baseline/sources.md#c05-skill) — `J05` / Méthode capitalisée, outils/événements versionnés, limites des démonstrations LlamaIndex<br>[`N05`](../../baseline/sources.md#n05) — `J05` / Approches simples, types, budgets, contrôle humain et structuration ; propos à confirmer
- **Statut documentaire :** `Candidate`
- **Statut de preuve :** `Candidat`
- **Travail :** `À faire`

## Valeur

Expliquer un run automobile et choisir une organisation sur des observations comparables, sans multiplier les agents par défaut.

## Socle et extension

- **Socle formation :** [`US-FIL-101`](user-stories/US-FIL-101.md), [`US-FIL-102`](user-stories/US-FIL-102.md), [`US-FIL-103`](user-stories/US-FIL-103.md)
- **Extension production :** [`US-FIL-104`](user-stories/US-FIL-104.md)

Une source alignée ne prouve ni apprentissage, ni réalisation, ni acceptation. Un artefact existant peut satisfaire un prérequis après revue.

## Enfants

| User Story | Feature | Rôle | Valeur | Niveau / priorité |
|---|---|---|---|---|
| [`US-FIL-101`](user-stories/US-FIL-101.md) | [`FEAT-FIL-101`](features/FEAT-FIL-101/FEATURE.md) | responsable de baseline | éviter une génération sur un corpus invalide | Socle formation / P1 |
| [`US-FIL-102`](user-stories/US-FIL-102.md) | [`FEAT-FIL-102`](features/FEAT-FIL-102/FEATURE.md) | opérateur | expliquer un arrêt sans information orale | Socle formation / P1 |
| [`US-FIL-103`](user-stories/US-FIL-103.md) | [`FEAT-FIL-103`](features/FEAT-FIL-103/FEATURE.md) | architecte | retenir une complexité justifiée par des erreurs observées | Socle formation / P1 |
| [`US-FIL-104`](user-stories/US-FIL-104.md) | [`FEAT-FIL-104`](features/FEAT-FIL-104/FEATURE.md) | ingénieur exigences | éviter qu'une réponse JSON plausible casse ou trompe le workflow | Extension production / P1 |

Les Features restent sous leur User Story ; elles ne sont pas parentes des Stories.

## Dépendances

- **Capacités externes à l'Epic :** [`US-FIL-1`](../EPIC-FIL-00/user-stories/US-FIL-1.md), [`US-FIL-4`](../EPIC-FIL-00/user-stories/US-FIL-4.md), [`US-FIL-6`](../EPIC-FIL-00/user-stories/US-FIL-6.md)
- Les dépendances internes sont détaillées dans chaque User Story et ses tâches.

## Périmètres et exclusions

- [`US-FIL-101`](user-stories/US-FIL-101.md) — Prévalidation du manifeste et propagation du blocage ; hors périmètre : acquisition de corpus réel.
- [`US-FIL-102`](user-stories/US-FIL-102.md) — Journal d'un run séquentiel ; le stockage distribué est exclu.
- [`US-FIL-103`](user-stories/US-FIL-103.md) — Comparaison séquence/producteur-vérificateur avec replay possible ; ni parallélisme imposé ni benchmark de fournisseurs.
- [`US-FIL-104`](user-stories/US-FIL-104.md) — Validation d'adaptateur et erreurs contrôlées ; aucun appel distant requis ni nouveau prompt rédigé dans ce lot.

## Achèvement mesurable

L'Epic ne peut être considérée achevée que lorsque les critères candidats retenus disposent de preuves exécutées, reliées à leurs oracles indépendants et revues humainement. Aucune Gate n'est déclarée franchie ici.
