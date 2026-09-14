# FEAT-FIL-104 — Refuser les réponses fournisseur hors contrat

`Référence — feature candidate`

- **Projet parent :** [`PROJ-FIL-AUTO-IA-001`](../../../../../SPEC.md)
- **Epic parente :** [`EPIC-FIL-01`](../../EPIC.md)
- **User Story parente :** [`US-FIL-104`](../../user-stories/US-FIL-104.md)
- **Jour :** `J06`
- **Sources de formation :** [`C05-SKILL`](../../../../baseline/sources.md#c05-skill) — `J05` / Méthode capitalisée, outils/événements versionnés, limites des démonstrations LlamaIndex / `support_actuel`<br>[`N05`](../../../../baseline/sources.md#n05) — `J05` / Approches simples, types, budgets, contrôle humain et structuration ; propos à confirmer / `synthese_automatique`
- **Branche :** `feat/fil-rouge-ingenierie-auto-ia`
- **Niveau :** `Extension production`
- **Priorité :** `P1`
- **Statut documentaire :** `Candidate`
- **Statut de preuve :** `Candidat`
- **Travail :** `À faire`
- **Responsable :** ingénieur exigences — personne à désigner

Cette Feature détaille la User Story parente ; elle ne crée pas une exigence indépendante.

## Contrat candidat

- **Entrée :** Réponses des tâches requirement, project-ranking, quality-advice ; identifiants source ; schéma versionné et modèle déclaré.
- **Sortie :** Proposition validée structurellement ou erreur de contrat ; statut Vérifié interdit au fournisseur.
- **Périmètre :** Validation d'adaptateur et erreurs contrôlées ; aucun appel distant requis ni nouveau prompt rédigé dans ce lot.
- **Règle canonique :** [`RM-FIL-104`](../../user-stories/US-FIL-104.md#rm-fil-104)
- **Critères canoniques :** [`CA-FIL-104-01`](../../user-stories/US-FIL-104.md#ca-fil-104-01), [`CA-FIL-104-02`](../../user-stories/US-FIL-104.md#ca-fil-104-02), [`CA-FIL-104-03`](../../user-stories/US-FIL-104.md#ca-fil-104-03)

Surface proposée : `src/auto_ai_flow/providers.py`. Ce rapprochement est candidat et ne constitue pas une trace vérifiée. La baseline actuelle est décrite dans [`current-state.md`](../../../../baseline/current-state.md). Les noms de modules futurs ne sont pas présentés comme existants.

## Découpage exécutable

| Tâche | Objectif | Phase | Dépendances |
|---|---|---|---|
| [`TASK-FIL-104-01`](tasks/TASK-FIL-104-01.md) | Figer les schémas de sortie, références permises et fixtures HTTP nominales et malformées sans secret réel. | Spécifier et figer l'oracle | [`US-FIL-6`](../../../EPIC-FIL-00/user-stories/US-FIL-6.md), [`US-FIL-101`](../../user-stories/US-FIL-101.md), [`US-FIL-102`](../../user-stories/US-FIL-102.md) |
| [`TASK-FIL-104-02`](tasks/TASK-FIL-104-02.md) | Renforcer le contrôle de MistralProvider et tester le même contrat autour du fournisseur déterministe. | Réaliser dans le périmètre autorisé | [`TASK-FIL-104-01`](tasks/TASK-FIL-104-01.md) |
| [`TASK-FIL-104-03`](tasks/TASK-FIL-104-03.md) | Simuler JSON invalide, champs manquants, types invalides et indisponibilité ; confirmer qu'aucun résultat invalide n'est promu. | Vérifier et soumettre à revue | [`TASK-FIL-104-02`](tasks/TASK-FIL-104-02.md) |

La livraison et les tests sont planifiés ; aucune tâche n'est exécutée par cette spécification.

## Vérification prévue

L'oracle à appliquer est celui de la [`User Story parente`](../../user-stories/US-FIL-104.md#oracle-indépendant) : Réponses HTTP simulées avec attendus de types et références approuvés ; les bornes 0–10 décrivent le contrat de démonstration existant, non une grille OSS réelle. Vérifier séparément contenu valide, champs absents, booléen à la place d'entier et contenu non JSON.

Les limites d'interruption, de concurrence ou de documentation applicables restent celles des cas de la User Story. Aucun retour de code supplémentaire n'est inventé ici.

## Acceptation

- [ ] [`CA-FIL-104-01`](../../user-stories/US-FIL-104.md#ca-fil-104-01)
- [ ] [`CA-FIL-104-02`](../../user-stories/US-FIL-104.md#ca-fil-104-02)
- [ ] [`CA-FIL-104-03`](../../user-stories/US-FIL-104.md#ca-fil-104-03)

Le responsable nominatif et la décision d'acceptation restent à décider. Les décisions demeurent humaines et [`AMB-04`](../../../../governance/ambiguities.md#amb-04) reste ouverte.
