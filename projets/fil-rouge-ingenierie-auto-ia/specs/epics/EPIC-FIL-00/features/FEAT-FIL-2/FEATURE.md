# FEAT-FIL-2 — Auditer une exigence sans inventer sa règle

`Référence — feature candidate`

- **Projet parent :** [`PROJ-FIL-AUTO-IA-001`](../../../../../SPEC.md)
- **Epic parente :** [`EPIC-FIL-00`](../../EPIC.md)
- **User Story parente :** [`US-FIL-2`](../../user-stories/US-FIL-2.md)
- **Jour :** `J01–J05`
- **Sources de formation :** [`C02`](../../../../baseline/sources.md#c02) — `J02` / Exigence singulière, inconnues, exemples et oracle indépendant ; Gherkin non universellement obligatoire / `support_actuel`<br>[`N02`](../../../../baseline/sources.md#n02) — `J02` / Structuration des exigences, moindre privilège et gabarit de feature ; propos à confirmer / `synthese_automatique`
- **Branche :** `feat/fil-rouge-ingenierie-auto-ia`
- **Niveau :** `Socle formation`
- **Priorité :** `P1`
- **Statut documentaire :** `Candidate`
- **Statut de preuve :** `Candidat`
- **Travail :** `À faire`
- **Responsable :** ingénieur exigences — personne à désigner

Cette Feature détaille la User Story parente ; elle ne crée pas une exigence indépendante.

## Contrat candidat

- **Entrée :** Exigence source avec UID, texte original, locator, version, statut et décideur de domaine ; besoins et périmètre issus de US-FIL-1.
- **Sortie :** Proposition d'audit singularité/clarté/vérifiabilité, règles candidates reliées à la source, exemples et questions à décider ; original inchangé.
- **Périmètre :** Audit d'un acquis J02 ; ne pas confondre Draft, proposition et validation d'exigence réelle.
- **Règle canonique :** [`RM-FIL-2`](../../user-stories/US-FIL-2.md#rm-fil-2)
- **Critères canoniques :** [`CA-FIL-2-01`](../../user-stories/US-FIL-2.md#ca-fil-2-01), [`CA-FIL-2-02`](../../user-stories/US-FIL-2.md#ca-fil-2-02), [`CA-FIL-2-03`](../../user-stories/US-FIL-2.md#ca-fil-2-03)

Aucune surface future n'est affirmée comme présente ; son emplacement reste à décider avant réalisation. La baseline actuelle est décrite dans [`current-state.md`](../../../../baseline/current-state.md). Les noms de modules futurs ne sont pas présentés comme existants.

## Découpage exécutable

| Tâche | Objectif | Phase | Dépendances |
|---|---|---|---|
| [`TASK-FIL-2-01`](tasks/TASK-FIL-2-01.md) | Conserver UID, texte, statut, version et locator ; relever chaque ambiguïté et chaque comportement distinct. | Spécifier et figer l'oracle | [`US-FIL-1`](../../user-stories/US-FIL-1.md) |
| [`TASK-FIL-2-02`](tasks/TASK-FIL-2-02.md) | Rédiger les règles candidates, cas nominaux/frontières/refus et oracles sans compléter les inconnues. | Réaliser dans le périmètre autorisé | [`TASK-FIL-2-01`](tasks/TASK-FIL-2-01.md) |
| [`TASK-FIL-2-03`](tasks/TASK-FIL-2-03.md) | Faire relire les propositions contre la source et enregistrer qui doit décider les règles non établies. | Vérifier et soumettre à revue | [`TASK-FIL-2-02`](tasks/TASK-FIL-2-02.md) |

La livraison et les tests sont planifiés ; aucune tâche n'est exécutée par cette spécification.

## Vérification prévue

L'oracle à appliquer est celui de la [`User Story parente`](../../user-stories/US-FIL-2.md#oracle-indépendant) : Texte source et décisions externes au code futur, relus par un ingénieur ; un test ne déduit jamais l'attendu de la sortie à tester. Une table ou des exemples suffisent pour discuter ; le dépôt conserve ses scénarios Gherkin.

Les limites d'interruption, de concurrence ou de documentation applicables restent celles des cas de la User Story. Aucun retour de code supplémentaire n'est inventé ici.

## Acceptation

- [ ] [`CA-FIL-2-01`](../../user-stories/US-FIL-2.md#ca-fil-2-01)
- [ ] [`CA-FIL-2-02`](../../user-stories/US-FIL-2.md#ca-fil-2-02)
- [ ] [`CA-FIL-2-03`](../../user-stories/US-FIL-2.md#ca-fil-2-03)

Le responsable nominatif et la décision d'acceptation restent à décider. Les décisions demeurent humaines et [`AMB-20`](../../../../governance/ambiguities.md#amb-20) reste ouverte.
