# FEAT-FIL-501 — Identifier une livraison reproductible

`Référence — feature candidate`

- **Projet parent :** [`PROJ-FIL-AUTO-IA-001`](../../../../../SPEC.md)
- **Epic parente :** [`EPIC-FIL-05`](../../EPIC.md)
- **User Story parente :** [`US-FIL-501`](../../user-stories/US-FIL-501.md)
- **Jour :** `J08`
- **Sources de formation :** [`C03`](../../../../baseline/sources.md#c03) — `J03` / Reproduction, hypothèses concurrentes, rouge/vert comparable, mutation et documentation / `support_actuel`<br>[`C08`](../../../../baseline/sources.md#c08) — `J08` / Quatre verdicts, risques gouvernés, preuves bornées et coût complet / `programme_prevu`
- **Branche :** `feat/fil-rouge-ingenierie-auto-ia`
- **Niveau :** `Extension production`
- **Priorité :** `P1`
- **Statut documentaire :** `Candidate`
- **Statut de preuve :** `Candidat`
- **Travail :** `À faire`
- **Responsable :** mainteneur — personne à désigner

Cette Feature détaille la User Story parente ; elle ne crée pas une exigence indépendante.

## Contrat candidat

- **Entrée :** Révision de code, versions/configurations sans secret, corpus et jeu d'essai figés ; mode d'exécution déclaré.
- **Sortie :** Observation : manifeste de livraison avec empreintes et procédure de reproduction ; limites des modèles distants visibles.
- **Périmètre :** Packaging et inventaire, pas de publication, déploiement ou push dans ce lot.
- **Règle canonique :** [`RM-FIL-501`](../../user-stories/US-FIL-501.md#rm-fil-501)
- **Critères canoniques :** [`CA-FIL-501-01`](../../user-stories/US-FIL-501.md#ca-fil-501-01), [`CA-FIL-501-02`](../../user-stories/US-FIL-501.md#ca-fil-501-02), [`CA-FIL-501-03`](../../user-stories/US-FIL-501.md#ca-fil-501-03)

Surface proposée : `src/auto_ai_flow/orchestrator.py` et `tests/test_cli.py`. Ce rapprochement est candidat et ne constitue pas une trace vérifiée. La baseline actuelle est décrite dans [`current-state.md`](../../../../baseline/current-state.md). Les noms de modules futurs ne sont pas présentés comme existants.

## Découpage exécutable

| Tâche | Objectif | Phase | Dépendances |
|---|---|---|---|
| [`TASK-FIL-501-01`](tasks/TASK-FIL-501-01.md) | Définir le manifeste de livraison et les champs sémantiques comparables, avec modes et dépendances exactes. | Spécifier et figer l'oracle | [`US-FIL-104`](../../../EPIC-FIL-01/user-stories/US-FIL-104.md), [`US-FIL-201`](../../../EPIC-FIL-02/user-stories/US-FIL-201.md), [`US-FIL-401`](../../../EPIC-FIL-04/user-stories/US-FIL-401.md) |
| [`TASK-FIL-501-02`](tasks/TASK-FIL-501-02.md) | Préparer un paquet local et une procédure de rejeu sans secret, en excluant caches et bases vectorielles. | Réaliser dans le périmètre autorisé | [`TASK-FIL-501-01`](tasks/TASK-FIL-501-01.md) |
| [`TASK-FIL-501-03`](tasks/TASK-FIL-501-03.md) | Faire rejouer par un tiers et conserver les écarts, surtout modèle distant et versions manquantes. | Vérifier et soumettre à revue | [`TASK-FIL-501-02`](tasks/TASK-FIL-501-02.md) |

La livraison et les tests sont planifiés ; aucune tâche n'est exécutée par cette spécification.

## Vérification prévue

L'oracle à appliquer est celui de la [`User Story parente`](../../user-stories/US-FIL-501.md#oracle-indépendant) : Artefacts attendus du cas approuvé, contrôlés hors du sérialiseur ; comparer explicitement champs métier et non generated_at. Le test CLI actuel ne prouve pas l'identité de deux runs.

Les limites d'interruption, de concurrence ou de documentation applicables restent celles des cas de la User Story. Aucun retour de code supplémentaire n'est inventé ici.

## Acceptation

- [ ] [`CA-FIL-501-01`](../../user-stories/US-FIL-501.md#ca-fil-501-01)
- [ ] [`CA-FIL-501-02`](../../user-stories/US-FIL-501.md#ca-fil-501-02)
- [ ] [`CA-FIL-501-03`](../../user-stories/US-FIL-501.md#ca-fil-501-03)

Le responsable nominatif et la décision d'acceptation restent à décider. Les décisions demeurent humaines et [`AMB-14`](../../../../governance/ambiguities.md#amb-14) reste ouverte.
