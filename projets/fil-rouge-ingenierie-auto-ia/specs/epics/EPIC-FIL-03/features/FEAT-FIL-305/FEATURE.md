# FEAT-FIL-305 — Importer un diagnostic qualité attribuable

`Référence — feature candidate`

- **Projet parent :** [`PROJ-FIL-AUTO-IA-001`](../../../../../SPEC.md)
- **Epic parente :** [`EPIC-FIL-03`](../../EPIC.md)
- **User Story parente :** [`US-FIL-305`](../../user-stories/US-FIL-305.md)
- **Jour :** `J07`
- **Sources de formation :** [`C03`](../../../../baseline/sources.md#c03) — `J03` / Reproduction, hypothèses concurrentes, rouge/vert comparable, mutation et documentation / `support_actuel`<br>[`N03`](../../../../baseline/sources.md#n03) — `J03` / Plan préalable, tests générés, scripts, qualité et organisation des spécifications ; propos à confirmer / `synthese_automatique`<br>[`C07`](../../../../baseline/sources.md#c07) — `J07` / Politique avant accès, révision pédagogique MCP 2026-07-28, contenu non fiable et cas indépendants / `programme_prevu`
- **Branche :** `feat/fil-rouge-ingenierie-auto-ia`
- **Niveau :** `Extension production`
- **Priorité :** `P2`
- **Statut documentaire :** `Candidate`
- **Statut de preuve :** `Candidat`
- **Travail :** `À faire`
- **Responsable :** responsable qualité — personne à désigner

Cette Feature détaille la User Story parente ; elle ne crée pas une exigence indépendante.

## Contrat candidat

- **Entrée :** Rapport Cppcheck local ou fixture déclarée, version d'outil, options, SHA du code cible et code retour ; droits d'utilisation approuvés.
- **Sortie :** Observation de diagnostic avec provenance et proposition IA séparée ; aucun patch appliqué.
- **Périmètre :** Import read-only et conseil borné ; auto-correction, exécution shell libre et conformité MISRA exclus.
- **Règle canonique :** [`RM-FIL-305`](../../user-stories/US-FIL-305.md#rm-fil-305)
- **Critères canoniques :** [`CA-FIL-305-01`](../../user-stories/US-FIL-305.md#ca-fil-305-01), [`CA-FIL-305-02`](../../user-stories/US-FIL-305.md#ca-fil-305-02), [`CA-FIL-305-03`](../../user-stories/US-FIL-305.md#ca-fil-305-03)

Surface proposée : `src/auto_ai_flow/agents.py`. Ce rapprochement est candidat et ne constitue pas une trace vérifiée. La baseline actuelle est décrite dans [`current-state.md`](../../../../baseline/current-state.md). Les noms de modules futurs ne sont pas présentés comme existants.

## Découpage exécutable

| Tâche | Objectif | Phase | Dépendances |
|---|---|---|---|
| [`TASK-FIL-305-01`](tasks/TASK-FIL-305-01.md) | Figer un rapport et son oracle avec version/options, distinguer absence d'alerte et erreur d'outil. | Spécifier et figer l'oracle | [`US-FIL-3`](../../../EPIC-FIL-00/user-stories/US-FIL-3.md), [`US-FIL-101`](../../../EPIC-FIL-01/user-stories/US-FIL-101.md), [`US-FIL-301`](../../user-stories/US-FIL-301.md) |
| [`TASK-FIL-305-02`](tasks/TASK-FIL-305-02.md) | Prévoir un adaptateur qualité limité au format approuvé et conserver la provenance avec les conseils. | Réaliser dans le périmètre autorisé | [`TASK-FIL-305-01`](tasks/TASK-FIL-305-01.md) |
| [`TASK-FIL-305-03`](tasks/TASK-FIL-305-03.md) | Vérifier nominal, rapport vide et erreur, puis faire qualifier les faux positifs par le responsable qualité. | Vérifier et soumettre à revue | [`TASK-FIL-305-02`](tasks/TASK-FIL-305-02.md) |

La livraison et les tests sont planifiés ; aucune tâche n'est exécutée par cette spécification.

## Vérification prévue

L'oracle à appliquer est celui de la [`User Story parente`](../../user-stories/US-FIL-305.md#oracle-indépendant) : Petit code cible autorisé avec diagnostic attendu relu indépendamment ; rapport de référence externe au parseur. Un code retour d'outil doit être interprété selon sa documentation versionnée.

Les limites d'interruption, de concurrence ou de documentation applicables restent celles des cas de la User Story. Aucun retour de code supplémentaire n'est inventé ici.

## Acceptation

- [ ] [`CA-FIL-305-01`](../../user-stories/US-FIL-305.md#ca-fil-305-01)
- [ ] [`CA-FIL-305-02`](../../user-stories/US-FIL-305.md#ca-fil-305-02)
- [ ] [`CA-FIL-305-03`](../../user-stories/US-FIL-305.md#ca-fil-305-03)

Le responsable nominatif et la décision d'acceptation restent à décider. Les décisions demeurent humaines et [`AMB-10`](../../../../governance/ambiguities.md#amb-10) reste ouverte.
