# FEAT-FIL-401 — Versionner des cas à attendu indépendant

`Référence — feature candidate`

- **Projet parent :** [`PROJ-FIL-AUTO-IA-001`](../../../../../SPEC.md)
- **Epic parente :** [`EPIC-FIL-04`](../../EPIC.md)
- **User Story parente :** [`US-FIL-401`](../../user-stories/US-FIL-401.md)
- **Jour :** `J07`
- **Sources de formation :** [`C02`](../../../../baseline/sources.md#c02) — `J02` / Exigence singulière, inconnues, exemples et oracle indépendant ; Gherkin non universellement obligatoire / `support_actuel`<br>[`C07`](../../../../baseline/sources.md#c07) — `J07` / Politique avant accès, révision pédagogique MCP 2026-07-28, contenu non fiable et cas indépendants / `programme_prevu`
- **Branche :** `feat/fil-rouge-ingenierie-auto-ia`
- **Niveau :** `Socle formation`
- **Priorité :** `P1`
- **Statut documentaire :** `Candidate`
- **Statut de preuve :** `Candidat`
- **Travail :** `À faire`
- **Responsable :** responsable évaluation — personne à désigner

Cette Feature détaille la User Story parente ; elle ne crée pas une exigence indépendante.

## Contrat candidat

- **Entrée :** Cas nominaux, erreurs et contenus hostiles fictifs, identité, contexte, attendu, oracle, responsable et version du jeu.
- **Sortie :** Proposition de jeu revue humainement et observations par cas ; cas non exécutés ou non décidables visibles.
- **Périmètre :** Petit jeu pertinent, sans quota historique obligatoire ni seuil de succès inventé.
- **Règle canonique :** [`RM-FIL-401`](../../user-stories/US-FIL-401.md#rm-fil-401)
- **Critères canoniques :** [`CA-FIL-401-01`](../../user-stories/US-FIL-401.md#ca-fil-401-01), [`CA-FIL-401-02`](../../user-stories/US-FIL-401.md#ca-fil-401-02), [`CA-FIL-401-03`](../../user-stories/US-FIL-401.md#ca-fil-401-03)

Aucune surface future n'est affirmée comme présente ; son emplacement reste à décider avant réalisation. La baseline actuelle est décrite dans [`current-state.md`](../../../../baseline/current-state.md). Les noms de modules futurs ne sont pas présentés comme existants.

## Découpage exécutable

| Tâche | Objectif | Phase | Dépendances |
|---|---|---|---|
| [`TASK-FIL-401-01`](tasks/TASK-FIL-401-01.md) | Écrire et faire approuver les cas selon MES-02, y compris identités inconnues et entrées invalides. | Spécifier et figer l'oracle | [`US-FIL-301`](../../../EPIC-FIL-03/user-stories/US-FIL-301.md), [`US-FIL-302`](../../../EPIC-FIL-03/user-stories/US-FIL-302.md), [`US-FIL-303`](../../../EPIC-FIL-03/user-stories/US-FIL-303.md) |
| [`TASK-FIL-401-02`](tasks/TASK-FIL-401-02.md) | Préparer le format de résultats pass/fail/not_run/undecidable avec liens vers observations et version du jeu. | Réaliser dans le périmètre autorisé | [`TASK-FIL-401-01`](tasks/TASK-FIL-401-01.md) |
| [`TASK-FIL-401-03`](tasks/TASK-FIL-401-03.md) | Revoir chaque attendu et vérifier qu'un cas non exécuté ou une violation critique ne disparaît pas dans un agrégat. | Vérifier et soumettre à revue | [`TASK-FIL-401-02`](tasks/TASK-FIL-401-02.md) |

La livraison et les tests sont planifiés ; aucune tâche n'est exécutée par cette spécification.

## Vérification prévue

L'oracle à appliquer est celui de la [`User Story parente`](../../user-stories/US-FIL-401.md#oracle-indépendant) : Contrat MES-02 dans governance/measurement-contracts.md ; les règles critiques restent binaires et non compensables.

Les limites d'interruption, de concurrence ou de documentation applicables restent celles des cas de la User Story. Aucun retour de code supplémentaire n'est inventé ici.

## Acceptation

- [ ] [`CA-FIL-401-01`](../../user-stories/US-FIL-401.md#ca-fil-401-01)
- [ ] [`CA-FIL-401-02`](../../user-stories/US-FIL-401.md#ca-fil-401-02)
- [ ] [`CA-FIL-401-03`](../../user-stories/US-FIL-401.md#ca-fil-401-03)

Le responsable nominatif et la décision d'acceptation restent à décider. Les décisions demeurent humaines et [`AMB-11`](../../../../governance/ambiguities.md#amb-11) reste ouverte.
