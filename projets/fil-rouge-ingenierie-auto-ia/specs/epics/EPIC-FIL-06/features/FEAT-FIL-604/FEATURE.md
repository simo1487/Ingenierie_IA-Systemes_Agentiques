# FEAT-FIL-604 — Consigner une décision réversible sur une page

`Référence — feature candidate`

- **Projet parent :** [`PROJ-FIL-AUTO-IA-001`](../../../../../SPEC.md)
- **Epic parente :** [`EPIC-FIL-06`](../../EPIC.md)
- **User Story parente :** [`US-FIL-604`](../../user-stories/US-FIL-604.md)
- **Jour :** `J08`
- **Sources de formation :** [`C08-G7`](../../../../baseline/sources.md#c08-g7) — `J08` / Fiche d'une page, trois risques, arrêt/repli testé, ROI et date de révision ; G7 / `programme_prevu`
- **Branche :** `feat/fil-rouge-ingenierie-auto-ia`
- **Niveau :** `Socle formation`
- **Priorité :** `P1`
- **Statut documentaire :** `Candidate`
- **Statut de preuve :** `Candidat`
- **Travail :** `À faire`
- **Responsable :** décideur humain — personne à désigner

Cette Feature détaille la User Story parente ; elle ne crée pas une exigence indépendante.

## Contrat candidat

- **Entrée :** Dossier G0–G6 avec manques visibles, preuves, risques, coût complet et retour arrière ; décision attribuée et date de révision.
- **Sortie :** Décision humaine d'une page avec verdict, périmètre, preuves citées, limites, trois risques, arrêt/repli, prochaine action, responsable et révision.
- **Périmètre :** Fiche et décision pédagogique G7 ; lancement réel, paiement, déploiement et intégration restent des actions séparément autorisées.
- **Règle canonique :** [`RM-FIL-604`](../../user-stories/US-FIL-604.md#rm-fil-604)
- **Critères canoniques :** [`CA-FIL-604-01`](../../user-stories/US-FIL-604.md#ca-fil-604-01), [`CA-FIL-604-02`](../../user-stories/US-FIL-604.md#ca-fil-604-02), [`CA-FIL-604-03`](../../user-stories/US-FIL-604.md#ca-fil-604-03)

Aucune surface future n'est affirmée comme présente ; son emplacement reste à décider avant réalisation. La baseline actuelle est décrite dans [`current-state.md`](../../../../baseline/current-state.md). Les noms de modules futurs ne sont pas présentés comme existants.

## Découpage exécutable

| Tâche | Objectif | Phase | Dépendances |
|---|---|---|---|
| [`TASK-FIL-604-01`](tasks/TASK-FIL-604-01.md) | Préparer le gabarit d'une page et confronter les quatre verdicts aux preuves, en citant ce qui ferait changer le choix. | Spécifier et figer l'oracle | [`US-FIL-503`](../../../EPIC-FIL-05/user-stories/US-FIL-503.md), [`US-FIL-601`](../../user-stories/US-FIL-601.md), [`US-FIL-602`](../../user-stories/US-FIL-602.md), [`US-FIL-603`](../../user-stories/US-FIL-603.md) |
| [`TASK-FIL-604-02`](tasks/TASK-FIL-604-02.md) | Faire rédiger la décision par le responsable avec coûts, risques, arrêt/repli, limites et date de révision. | Réaliser dans le périmètre autorisé | [`TASK-FIL-604-01`](tasks/TASK-FIL-604-01.md) |
| [`TASK-FIL-604-03`](tasks/TASK-FIL-604-03.md) | Organiser la revue croisée et conserver la décision attribuée ; vérifier qu'aucun lancement n'est déclenché par une proposition IA. | Vérifier et soumettre à revue | [`TASK-FIL-604-02`](tasks/TASK-FIL-604-02.md) |

La livraison et les tests sont planifiés ; aucune tâche n'est exécutée par cette spécification.

## Vérification prévue

L'oracle à appliquer est celui de la [`User Story parente`](../../user-stories/US-FIL-604.md#oracle-indépendant) : Revue contradictoire par un tiers qui retrouve décision, risques et arrêt sans explication orale ; contrôler la trace d'attribution, ne pas transformer un champ rempli par IA en consentement.

Les limites d'interruption, de concurrence ou de documentation applicables restent celles des cas de la User Story. Aucun retour de code supplémentaire n'est inventé ici.

## Acceptation

- [ ] [`CA-FIL-604-01`](../../user-stories/US-FIL-604.md#ca-fil-604-01)
- [ ] [`CA-FIL-604-02`](../../user-stories/US-FIL-604.md#ca-fil-604-02)
- [ ] [`CA-FIL-604-03`](../../user-stories/US-FIL-604.md#ca-fil-604-03)

Le responsable nominatif et la décision d'acceptation restent à décider. Les décisions demeurent humaines et [`AMB-18`](../../../../governance/ambiguities.md#amb-18) reste ouverte.
