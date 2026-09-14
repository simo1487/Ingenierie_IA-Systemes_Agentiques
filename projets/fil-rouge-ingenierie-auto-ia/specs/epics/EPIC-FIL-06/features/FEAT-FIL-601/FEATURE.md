# FEAT-FIL-601 — Distinguer un lien déclaré d'une preuve vérifiée

`Référence — feature candidate`

- **Projet parent :** [`PROJ-FIL-AUTO-IA-001`](../../../../../SPEC.md)
- **Epic parente :** [`EPIC-FIL-06`](../../EPIC.md)
- **User Story parente :** [`US-FIL-601`](../../user-stories/US-FIL-601.md)
- **Jour :** `J08`
- **Sources de formation :** [`C02`](../../../../baseline/sources.md#c02) — `J02` / Exigence singulière, inconnues, exemples et oracle indépendant ; Gherkin non universellement obligatoire / `support_actuel`<br>[`C03`](../../../../baseline/sources.md#c03) — `J03` / Reproduction, hypothèses concurrentes, rouge/vert comparable, mutation et documentation / `support_actuel`<br>[`C08`](../../../../baseline/sources.md#c08) — `J08` / Quatre verdicts, risques gouvernés, preuves bornées et coût complet / `programme_prevu`
- **Branche :** `feat/fil-rouge-ingenierie-auto-ia`
- **Niveau :** `Socle formation`
- **Priorité :** `P1`
- **Statut documentaire :** `Candidate`
- **Statut de preuve :** `Candidat`
- **Travail :** `À faire`
- **Responsable :** relecteur indépendant — personne à désigner

Cette Feature détaille la User Story parente ; elle ne crée pas une exigence indépendante.

## Contrat candidat

- **Entrée :** Lien explicite exigence/cible, référence d'oracle, artefact accessible, révision et résultat d'exécution ou examen indépendant ; responsable de revue.
- **Sortie :** Proposition de matrice et décision humaine attribuée avec statut par lien et limites de couverture.
- **Périmètre :** Dossier et revue humaine ; signature cryptographique et référentiel externe non imposés.
- **Règle canonique :** [`RM-FIL-601`](../../user-stories/US-FIL-601.md#rm-fil-601)
- **Critères canoniques :** [`CA-FIL-601-01`](../../user-stories/US-FIL-601.md#ca-fil-601-01), [`CA-FIL-601-02`](../../user-stories/US-FIL-601.md#ca-fil-601-02), [`CA-FIL-601-03`](../../user-stories/US-FIL-601.md#ca-fil-601-03)

Surface proposée : `src/auto_ai_flow/agents.py`. Ce rapprochement est candidat et ne constitue pas une trace vérifiée. La baseline actuelle est décrite dans [`current-state.md`](../../../../baseline/current-state.md). Les noms de modules futurs ne sont pas présentés comme existants.

## Découpage exécutable

| Tâche | Objectif | Phase | Dépendances |
|---|---|---|---|
| [`TASK-FIL-601-01`](tasks/TASK-FIL-601-01.md) | Définir les pièces exigées pour vérifier un lien et figer une preuve valide et une référence fictive introuvable. | Spécifier et figer l'oracle | [`US-FIL-2`](../../../EPIC-FIL-00/user-stories/US-FIL-2.md), [`US-FIL-5`](../../../EPIC-FIL-00/user-stories/US-FIL-5.md), [`US-FIL-101`](../../../EPIC-FIL-01/user-stories/US-FIL-101.md), [`US-FIL-401`](../../../EPIC-FIL-04/user-stories/US-FIL-401.md) |
| [`TASK-FIL-601-02`](tasks/TASK-FIL-601-02.md) | Préparer la matrice avec déclaration/proposition séparée de l'acceptation humaine et prévoir la correction du statut prématuré du MVP. | Réaliser dans le périmètre autorisé | [`TASK-FIL-601-01`](tasks/TASK-FIL-601-01.md) |
| [`TASK-FIL-601-03`](tasks/TASK-FIL-601-03.md) | Contrôler les pièces avec un pair, conserver les inconnues et vérifier qu'une référence non vide mais invalide ne suffit plus. | Vérifier et soumettre à revue | [`TASK-FIL-601-02`](tasks/TASK-FIL-601-02.md) |

La livraison et les tests sont planifiés ; aucune tâche n'est exécutée par cette spécification.

## Vérification prévue

L'oracle à appliquer est celui de la [`User Story parente`](../../user-stories/US-FIL-601.md#oracle-indépendant) : Revue indépendante de l'artefact, de sa révision et du comportement couvert ; preuve fictive inexistante comme contre-exemple. Le test actuel de présence de champs est un constat d'implémentation, pas cet oracle.

Les limites d'interruption, de concurrence ou de documentation applicables restent celles des cas de la User Story. Aucun retour de code supplémentaire n'est inventé ici.

## Acceptation

- [ ] [`CA-FIL-601-01`](../../user-stories/US-FIL-601.md#ca-fil-601-01)
- [ ] [`CA-FIL-601-02`](../../user-stories/US-FIL-601.md#ca-fil-601-02)
- [ ] [`CA-FIL-601-03`](../../user-stories/US-FIL-601.md#ca-fil-601-03)

Le responsable nominatif et la décision d'acceptation restent à décider. Les décisions demeurent humaines et [`AMB-16`](../../../../governance/ambiguities.md#amb-16) reste ouverte.
