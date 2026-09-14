# FEAT-FIL-6 — Capitaliser un contrat d'outil et de workflow

`Référence — feature candidate`

- **Projet parent :** [`PROJ-FIL-AUTO-IA-001`](../../../../../SPEC.md)
- **Epic parente :** [`EPIC-FIL-00`](../../EPIC.md)
- **User Story parente :** [`US-FIL-6`](../../user-stories/US-FIL-6.md)
- **Jour :** `J01–J05`
- **Sources de formation :** [`C05`](../../../../baseline/sources.md#c05) — `J05` / Besoin avant framework, règle/recherche/workflow/agent et valeur observable / `support_actuel`<br>[`C05-SKILL`](../../../../baseline/sources.md#c05-skill) — `J05` / Méthode capitalisée, outils/événements versionnés, limites des démonstrations LlamaIndex / `support_actuel`<br>[`N05`](../../../../baseline/sources.md#n05) — `J05` / Approches simples, types, budgets, contrôle humain et structuration ; propos à confirmer / `synthese_automatique`
- **Branche :** `feat/fil-rouge-ingenierie-auto-ia`
- **Niveau :** `Socle formation`
- **Priorité :** `P1`
- **Statut documentaire :** `Candidate`
- **Statut de preuve :** `Candidat`
- **Travail :** `À faire`
- **Responsable :** intégrateur — personne à désigner

Cette Feature détaille la User Story parente ; elle ne crée pas une exigence indépendante.

## Contrat candidat

- **Entrée :** Besoin approuvé pour l'exercice, outil de consultation identifié, types d'arguments/résultats, sources admises, permissions, budget et états de succès/échec/revue.
- **Sortie :** Proposition de fiche d'outil et méthode réutilisable versionnées, avec transitions, repli et points de décision humaine ; aucun droit ajouté par la description.
- **Périmètre :** Capitalisation J05 et interface vers J06 ; ne pas installer un framework ou créer une configuration d'agent dans ce lot documentaire.
- **Règle canonique :** [`RM-FIL-6`](../../user-stories/US-FIL-6.md#rm-fil-6)
- **Critères canoniques :** [`CA-FIL-6-01`](../../user-stories/US-FIL-6.md#ca-fil-6-01), [`CA-FIL-6-02`](../../user-stories/US-FIL-6.md#ca-fil-6-02), [`CA-FIL-6-03`](../../user-stories/US-FIL-6.md#ca-fil-6-03)

Aucune surface future n'est affirmée comme présente ; son emplacement reste à décider avant réalisation. La baseline actuelle est décrite dans [`current-state.md`](../../../../baseline/current-state.md). Les noms de modules futurs ne sont pas présentés comme existants.

## Découpage exécutable

| Tâche | Objectif | Phase | Dépendances |
|---|---|---|---|
| [`TASK-FIL-6-01`](tasks/TASK-FIL-6-01.md) | Décrire l'outil étroit, les types et erreurs ainsi que les états/transitions nécessaires au cas retenu. | Spécifier et figer l'oracle | [`US-FIL-1`](../../user-stories/US-FIL-1.md), [`US-FIL-2`](../../user-stories/US-FIL-2.md), [`US-FIL-4`](../../user-stories/US-FIL-4.md) |
| [`TASK-FIL-6-02`](tasks/TASK-FIL-6-02.md) | Capitaliser la méthode avec versions des instructions, outils et corpus, y compris le repli et la validation humaine. | Réaliser dans le périmètre autorisé | [`TASK-FIL-6-01`](tasks/TASK-FIL-6-01.md) |
| [`TASK-FIL-6-03`](tasks/TASK-FIL-6-03.md) | Faire appliquer la méthode par un tiers sur un exemple autorisé et relier les lacunes aux futurs contrôles J06/J07. | Vérifier et soumettre à revue | [`TASK-FIL-6-02`](tasks/TASK-FIL-6-02.md) |

La livraison et les tests sont planifiés ; aucune tâche n'est exécutée par cette spécification.

## Vérification prévue

L'oracle à appliquer est celui de la [`User Story parente`](../../user-stories/US-FIL-6.md#oracle-indépendant) : Fiche approuvée, types et transitions relus par un pair ; la description FunctionTool et les événements Workflow sont des mécanismes pédagogiques, pas une preuve d'autorisation. SKILL.md n'est pas une API universelle de LlamaIndex.

Les limites d'interruption, de concurrence ou de documentation applicables restent celles des cas de la User Story. Aucun retour de code supplémentaire n'est inventé ici.

## Acceptation

- [ ] [`CA-FIL-6-01`](../../user-stories/US-FIL-6.md#ca-fil-6-01)
- [ ] [`CA-FIL-6-02`](../../user-stories/US-FIL-6.md#ca-fil-6-02)
- [ ] [`CA-FIL-6-03`](../../user-stories/US-FIL-6.md#ca-fil-6-03)

Le responsable nominatif et la décision d'acceptation restent à décider. Les décisions demeurent humaines et [`AMB-24`](../../../../governance/ambiguities.md#amb-24) reste ouverte.
