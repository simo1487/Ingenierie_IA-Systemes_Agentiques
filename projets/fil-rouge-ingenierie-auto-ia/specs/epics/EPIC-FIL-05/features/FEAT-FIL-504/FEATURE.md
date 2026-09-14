# FEAT-FIL-504 — Observer un pilote sans exposer ses données

`Référence — feature candidate`

- **Projet parent :** [`PROJ-FIL-AUTO-IA-001`](../../../../../SPEC.md)
- **Epic parente :** [`EPIC-FIL-05`](../../EPIC.md)
- **User Story parente :** [`US-FIL-504`](../../user-stories/US-FIL-504.md)
- **Jour :** `J08`
- **Sources de formation :** [`C06`](../../../../baseline/sources.md#c06) — `J06` / Comparaison d'organisations, rôles, reprise, idempotence, mémoire et trace / `programme_prevu`<br>[`C07`](../../../../baseline/sources.md#c07) — `J07` / Politique avant accès, révision pédagogique MCP 2026-07-28, contenu non fiable et cas indépendants / `programme_prevu`<br>[`C08`](../../../../baseline/sources.md#c08) — `J08` / Quatre verdicts, risques gouvernés, preuves bornées et coût complet / `programme_prevu`
- **Branche :** `feat/fil-rouge-ingenierie-auto-ia`
- **Niveau :** `Extension production`
- **Priorité :** `P2`
- **Statut documentaire :** `Candidate`
- **Statut de preuve :** `Candidat`
- **Travail :** `À faire`
- **Responsable :** opérateur — personne à désigner

Cette Feature détaille la User Story parente ; elle ne crée pas une exigence indépendante.

## Contrat candidat

- **Entrée :** Événements assainis, politique d'observation versionnée, sources de durée/usage et conditions d'arrêt approuvées.
- **Sortie :** Observations corrélées au run et alertes vers un rôle désigné ; données absentes explicitement non mesurées.
- **Périmètre :** Observabilité minimale locale ; plateforme cloud et seuils de service non choisis implicitement.
- **Règle canonique :** [`RM-FIL-504`](../../user-stories/US-FIL-504.md#rm-fil-504)
- **Critères canoniques :** [`CA-FIL-504-01`](../../user-stories/US-FIL-504.md#ca-fil-504-01), [`CA-FIL-504-02`](../../user-stories/US-FIL-504.md#ca-fil-504-02), [`CA-FIL-504-03`](../../user-stories/US-FIL-504.md#ca-fil-504-03)

Aucune surface future n'est affirmée comme présente ; son emplacement reste à décider avant réalisation. La baseline actuelle est décrite dans [`current-state.md`](../../../../baseline/current-state.md). Les noms de modules futurs ne sont pas présentés comme existants.

## Découpage exécutable

| Tâche | Objectif | Phase | Dépendances |
|---|---|---|---|
| [`TASK-FIL-504-01`](tasks/TASK-FIL-504-01.md) | Définir champs permis, rétention et sources des mesures, sans choisir des seuils de production arbitraires. | Spécifier et figer l'oracle | [`US-FIL-102`](../../../EPIC-FIL-01/user-stories/US-FIL-102.md), [`US-FIL-202`](../../../EPIC-FIL-02/user-stories/US-FIL-202.md), [`US-FIL-503`](../../user-stories/US-FIL-503.md) |
| [`TASK-FIL-504-02`](tasks/TASK-FIL-504-02.md) | Prévoir une vue d'exploitation corrélée aux runs et un routage explicite des signaux d'arrêt. | Réaliser dans le périmètre autorisé | [`TASK-FIL-504-01`](tasks/TASK-FIL-504-01.md) |
| [`TASK-FIL-504-03`](tasks/TASK-FIL-504-03.md) | Tester erreur sensible factice et usage absent ; faire revoir ce qui est réellement mesuré et ce qui reste inconnu. | Vérifier et soumettre à revue | [`TASK-FIL-504-02`](tasks/TASK-FIL-504-02.md) |

La livraison et les tests sont planifiés ; aucune tâche n'est exécutée par cette spécification.

## Vérification prévue

L'oracle à appliquer est celui de la [`User Story parente`](../../user-stories/US-FIL-504.md#oracle-indépendant) : Sentinelles fictives connues, inspection des octets exportés et trace événementielle externe ; aucun secret réel utilisé pour tester l'assainissement.

Les limites d'interruption, de concurrence ou de documentation applicables restent celles des cas de la User Story. Aucun retour de code supplémentaire n'est inventé ici.

## Acceptation

- [ ] [`CA-FIL-504-01`](../../user-stories/US-FIL-504.md#ca-fil-504-01)
- [ ] [`CA-FIL-504-02`](../../user-stories/US-FIL-504.md#ca-fil-504-02)
- [ ] [`CA-FIL-504-03`](../../user-stories/US-FIL-504.md#ca-fil-504-03)

Le responsable nominatif et la décision d'acceptation restent à décider. Les décisions demeurent humaines et [`AMB-02`](../../../../governance/ambiguities.md#amb-02) reste ouverte.
