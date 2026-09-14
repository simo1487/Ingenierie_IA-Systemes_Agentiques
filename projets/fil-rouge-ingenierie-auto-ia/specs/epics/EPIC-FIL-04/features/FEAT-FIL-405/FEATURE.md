# FEAT-FIL-405 — Rendre le classement OSS explicable

`Référence — feature candidate`

- **Projet parent :** [`PROJ-FIL-AUTO-IA-001`](../../../../../SPEC.md)
- **Epic parente :** [`EPIC-FIL-04`](../../EPIC.md)
- **User Story parente :** [`US-FIL-405`](../../user-stories/US-FIL-405.md)
- **Jour :** `J07`
- **Sources de formation :** [`C04`](../../../../baseline/sources.md#c04) — `J04` / Corpus autorisé, découpage du sens, lexical/sémantique, Hit@k/MRR et support des citations / `support_actuel`<br>[`C08`](../../../../baseline/sources.md#c08) — `J08` / Quatre verdicts, risques gouvernés, preuves bornées et coût complet / `programme_prevu`
- **Branche :** `feat/fil-rouge-ingenierie-auto-ia`
- **Niveau :** `Extension production`
- **Priorité :** `P2`
- **Statut documentaire :** `Candidate`
- **Statut de preuve :** `Candidat`
- **Travail :** `À faire`
- **Responsable :** responsable produit — personne à désigner

Cette Feature détaille la User Story parente ; elle ne crée pas une exigence indépendante.

## Contrat candidat

- **Entrée :** Fiches candidates révisées, licences, exigences/tests/qualité référencés ; grille et politique des données manquantes approuvées.
- **Sortie :** Proposition de classement détaillé par critère, inconnues conservées et décision humaine séparée.
- **Périmètre :** Fiches autorisées en lecture seule ; recherche web, clonage/exécution et décision de licence automatiques exclus.
- **Règle canonique :** [`RM-FIL-405`](../../user-stories/US-FIL-405.md#rm-fil-405)
- **Critères canoniques :** [`CA-FIL-405-01`](../../user-stories/US-FIL-405.md#ca-fil-405-01), [`CA-FIL-405-02`](../../user-stories/US-FIL-405.md#ca-fil-405-02), [`CA-FIL-405-03`](../../user-stories/US-FIL-405.md#ca-fil-405-03)

Surface proposée : `src/auto_ai_flow/agents.py`. Ce rapprochement est candidat et ne constitue pas une trace vérifiée. La baseline actuelle est décrite dans [`current-state.md`](../../../../baseline/current-state.md). Les noms de modules futurs ne sont pas présentés comme existants.

## Découpage exécutable

| Tâche | Objectif | Phase | Dépendances |
|---|---|---|---|
| [`TASK-FIL-405-01`](tasks/TASK-FIL-405-01.md) | Faire approuver la grille OSS et la politique des inconnues en distinguant le score fictif 0–10 du MVP. | Spécifier et figer l'oracle | [`US-FIL-101`](../../../EPIC-FIL-01/user-stories/US-FIL-101.md), [`US-FIL-104`](../../../EPIC-FIL-01/user-stories/US-FIL-104.md), [`US-FIL-401`](../../user-stories/US-FIL-401.md) |
| [`TASK-FIL-405-02`](tasks/TASK-FIL-405-02.md) | Prévoir un classement à contributions traçables et conserver égalités, données absentes et sources des fiches. | Réaliser dans le périmètre autorisé | [`TASK-FIL-405-01`](tasks/TASK-FIL-405-01.md) |
| [`TASK-FIL-405-03`](tasks/TASK-FIL-405-03.md) | Recalculer sur données figées selon MES-04, puis faire sélectionner explicitement dépôt et révision par le responsable produit. | Vérifier et soumettre à revue | [`TASK-FIL-405-02`](tasks/TASK-FIL-405-02.md) |

La livraison et les tests sont planifiés ; aucune tâche n'est exécutée par cette spécification.

## Vérification prévue

L'oracle à appliquer est celui de la [`User Story parente`](../../user-stories/US-FIL-405.md#oracle-indépendant) : MES-04 ; grille revue avant calcul et contre-calcul indépendant sur données figées ; aucune pondération réelle fixée ici.

Les limites d'interruption, de concurrence ou de documentation applicables restent celles des cas de la User Story. Aucun retour de code supplémentaire n'est inventé ici.

## Acceptation

- [ ] [`CA-FIL-405-01`](../../user-stories/US-FIL-405.md#ca-fil-405-01)
- [ ] [`CA-FIL-405-02`](../../user-stories/US-FIL-405.md#ca-fil-405-02)
- [ ] [`CA-FIL-405-03`](../../user-stories/US-FIL-405.md#ca-fil-405-03)

Le responsable nominatif et la décision d'acceptation restent à décider. Les décisions demeurent humaines et [`AMB-13`](../../../../governance/ambiguities.md#amb-13) reste ouverte.
