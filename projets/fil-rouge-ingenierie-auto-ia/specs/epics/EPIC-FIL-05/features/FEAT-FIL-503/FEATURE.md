# FEAT-FIL-503 — Arrêter le pilote et revenir à la baseline

`Référence — feature candidate`

- **Projet parent :** [`PROJ-FIL-AUTO-IA-001`](../../../../../SPEC.md)
- **Epic parente :** [`EPIC-FIL-05`](../../EPIC.md)
- **User Story parente :** [`US-FIL-503`](../../user-stories/US-FIL-503.md)
- **Jour :** `J08`
- **Sources de formation :** [`C06-G5`](../../../../baseline/sources.md#c06-g5) — `J06` / Comparaison, journal complet, interruption et mémoire ; revue G5 / `programme_prevu`<br>[`C08-G7`](../../../../baseline/sources.md#c08-g7) — `J08` / Fiche d'une page, trois risques, arrêt/repli testé, ROI et date de révision ; G7 / `programme_prevu`
- **Branche :** `feat/fil-rouge-ingenierie-auto-ia`
- **Niveau :** `Socle formation`
- **Priorité :** `P1`
- **Statut documentaire :** `Candidate`
- **Statut de preuve :** `Candidat`
- **Travail :** `À faire`
- **Responsable :** responsable d'exploitation — personne à désigner

Cette Feature détaille la User Story parente ; elle ne crée pas une exigence indépendante.

## Contrat candidat

- **Entrée :** Baseline de repli identifiée, procédure approuvée, condition d'arrêt observable, responsable ; environnement local fictif.
- **Sortie :** Observation d'exercice d'arrêt et de retour arrière, limites sur runs en cours et décision de reprise humaine.
- **Périmètre :** Exercice sans effet sur un service réel ; tout déploiement/retour arrière réel exige une autorisation spécifique.
- **Règle canonique :** [`RM-FIL-503`](../../user-stories/US-FIL-503.md#rm-fil-503)
- **Critères canoniques :** [`CA-FIL-503-01`](../../user-stories/US-FIL-503.md#ca-fil-503-01), [`CA-FIL-503-02`](../../user-stories/US-FIL-503.md#ca-fil-503-02), [`CA-FIL-503-03`](../../user-stories/US-FIL-503.md#ca-fil-503-03)

Aucune surface future n'est affirmée comme présente ; son emplacement reste à décider avant réalisation. La baseline actuelle est décrite dans [`current-state.md`](../../../../baseline/current-state.md). Les noms de modules futurs ne sont pas présentés comme existants.

## Découpage exécutable

| Tâche | Objectif | Phase | Dépendances |
|---|---|---|---|
| [`TASK-FIL-503-01`](tasks/TASK-FIL-503-01.md) | Nommer baseline de repli, responsable, signal et comportement attendu des runs en cours. | Spécifier et figer l'oracle | [`US-FIL-201`](../../../EPIC-FIL-02/user-stories/US-FIL-201.md), [`US-FIL-202`](../../../EPIC-FIL-02/user-stories/US-FIL-202.md) |
| [`TASK-FIL-503-02`](tasks/TASK-FIL-503-02.md) | Préparer un exercice d'arrêt/repli local ou un replay déclaré en conservant le journal et la décision. | Réaliser dans le périmètre autorisé | [`TASK-FIL-503-01`](tasks/TASK-FIL-503-01.md) |
| [`TASK-FIL-503-03`](tasks/TASK-FIL-503-03.md) | Faire constater l'arrêt des nouveaux runs et le repli par un tiers ; consigner les limites avant décision de pilote. | Vérifier et soumettre à revue | [`TASK-FIL-503-02`](tasks/TASK-FIL-503-02.md) |

La livraison et les tests sont planifiés ; aucune tâche n'est exécutée par cette spécification.

## Vérification prévue

L'oracle à appliquer est celui de la [`User Story parente`](../../user-stories/US-FIL-503.md#oracle-indépendant) : Procédure revue avant essai, compteur de nouveaux runs et identité de baseline de repli ; replay déclaré acceptable au socle mais ne prouve pas un déploiement réel.

Les limites d'interruption, de concurrence ou de documentation applicables restent celles des cas de la User Story. Aucun retour de code supplémentaire n'est inventé ici.

## Acceptation

- [ ] [`CA-FIL-503-01`](../../user-stories/US-FIL-503.md#ca-fil-503-01)
- [ ] [`CA-FIL-503-02`](../../user-stories/US-FIL-503.md#ca-fil-503-02)
- [ ] [`CA-FIL-503-03`](../../user-stories/US-FIL-503.md#ca-fil-503-03)

Le responsable nominatif et la décision d'acceptation restent à décider. Les décisions demeurent humaines et [`AMB-15`](../../../../governance/ambiguities.md#amb-15) reste ouverte.
