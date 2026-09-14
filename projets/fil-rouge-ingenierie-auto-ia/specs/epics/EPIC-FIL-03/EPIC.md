# EPIC-FIL-03 — Outils bornés et frontière MCP

`Référence — Epic candidate`

- **Projet parent :** [`PROJ-FIL-AUTO-IA-001`](../../../SPEC.md)
- **Jour :** `J07`
- **Gate pédagogique associée :** `G6` — aucune approbation inférée
- **Sources alignées :** [`C05-SKILL`](../../baseline/sources.md#c05-skill) — `J05` / Méthode capitalisée, outils/événements versionnés, limites des démonstrations LlamaIndex<br>[`C07-G6`](../../baseline/sources.md#c07-g6) — `J07` / Outil préparé ou replay, refus avant accès, régression et première divergence ; G6<br>[`C07`](../../baseline/sources.md#c07) — `J07` / Politique avant accès, révision pédagogique MCP 2026-07-28, contenu non fiable et cas indépendants<br>[`C04`](../../baseline/sources.md#c04) — `J04` / Corpus autorisé, découpage du sens, lexical/sémantique, Hit@k/MRR et support des citations<br>[`C03`](../../baseline/sources.md#c03) — `J03` / Reproduction, hypothèses concurrentes, rouge/vert comparable, mutation et documentation<br>[`N03`](../../baseline/sources.md#n03) — `J03` / Plan préalable, tests générés, scripts, qualité et organisation des spécifications ; propos à confirmer
- **Statut documentaire :** `Candidate`
- **Statut de preuve :** `Candidat`
- **Travail :** `À faire`

## Valeur

Consulter des ressources autorisées sans confier les permissions à un modèle.

## Socle et extension

- **Socle formation :** [`US-FIL-301`](user-stories/US-FIL-301.md), [`US-FIL-302`](user-stories/US-FIL-302.md), [`US-FIL-303`](user-stories/US-FIL-303.md)
- **Extension production :** [`US-FIL-304`](user-stories/US-FIL-304.md), [`US-FIL-305`](user-stories/US-FIL-305.md)

Une source alignée ne prouve ni apprentissage, ni réalisation, ni acceptation. Un artefact existant peut satisfaire un prérequis après revue.

## Enfants

| User Story | Feature | Rôle | Valeur | Niveau / priorité |
|---|---|---|---|---|
| [`US-FIL-301`](user-stories/US-FIL-301.md) | [`FEAT-FIL-301`](features/FEAT-FIL-301/FEATURE.md) | responsable sécurité | prouver la frontière plutôt qu'un refus verbal du modèle | Socle formation / P1 |
| [`US-FIL-302`](user-stories/US-FIL-302.md) | [`FEAT-FIL-302`](features/FEAT-FIL-302/FEATURE.md) | intégrateur | ne pas mélanger des fixtures incompatibles | Socle formation / P1 |
| [`US-FIL-303`](user-stories/US-FIL-303.md) | [`FEAT-FIL-303`](features/FEAT-FIL-303/FEATURE.md) | responsable sécurité | conserver la frontière quand une donnée contient une instruction | Socle formation / P1 |
| [`US-FIL-304`](user-stories/US-FIL-304.md) | [`FEAT-FIL-304`](features/FEAT-FIL-304/FEATURE.md) | intégrateur | connecter le workflow sans dupliquer les politiques | Extension production / P2 |
| [`US-FIL-305`](user-stories/US-FIL-305.md) | [`FEAT-FIL-305`](features/FEAT-FIL-305/FEATURE.md) | responsable qualité | distinguer une sortie réelle de Cppcheck d'une fixture | Extension production / P2 |

Les Features restent sous leur User Story ; elles ne sont pas parentes des Stories.

## Dépendances

- **Capacités externes à l'Epic :** [`US-FIL-6`](../EPIC-FIL-00/user-stories/US-FIL-6.md), [`US-FIL-101`](../EPIC-FIL-01/user-stories/US-FIL-101.md), [`US-FIL-102`](../EPIC-FIL-01/user-stories/US-FIL-102.md), [`US-FIL-3`](../EPIC-FIL-00/user-stories/US-FIL-3.md)
- Les dépendances internes sont détaillées dans chaque User Story et ses tâches.

## Périmètres et exclusions

- [`US-FIL-301`](user-stories/US-FIL-301.md) — Consultation d'une ressource fictive ; pas de SQL libre, shell, URL libre ni écriture sur sources.
- [`US-FIL-302`](user-stories/US-FIL-302.md) — Inspection d'un outil préparé ; aucun développement de serveur ni choix de SDK exigé.
- [`US-FIL-303`](user-stories/US-FIL-303.md) — Injections factices directes et indirectes ; aucune attaque sur un service externe.
- [`US-FIL-304`](user-stories/US-FIL-304.md) — Adaptateur local minimal ; pas d'exposition publique, d'authentification inventée ou de développement obligatoire pendant J07.
- [`US-FIL-305`](user-stories/US-FIL-305.md) — Import read-only et conseil borné ; auto-correction, exécution shell libre et conformité MISRA exclus.

## Achèvement mesurable

L'Epic ne peut être considérée achevée que lorsque les critères candidats retenus disposent de preuves exécutées, reliées à leurs oracles indépendants et revues humainement. Aucune Gate n'est déclarée franchie ici.
