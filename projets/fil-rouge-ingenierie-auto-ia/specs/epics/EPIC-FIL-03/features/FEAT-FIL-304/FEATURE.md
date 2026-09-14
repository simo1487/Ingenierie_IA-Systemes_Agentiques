# FEAT-FIL-304 — Exposer le contrat via un adaptateur MCP réel

`Référence — feature candidate`

- **Projet parent :** [`PROJ-FIL-AUTO-IA-001`](../../../../../SPEC.md)
- **Epic parente :** [`EPIC-FIL-03`](../../EPIC.md)
- **User Story parente :** [`US-FIL-304`](../../user-stories/US-FIL-304.md)
- **Jour :** `J07`
- **Sources de formation :** [`C05-SKILL`](../../../../baseline/sources.md#c05-skill) — `J05` / Méthode capitalisée, outils/événements versionnés, limites des démonstrations LlamaIndex / `support_actuel`<br>[`C07`](../../../../baseline/sources.md#c07) — `J07` / Politique avant accès, révision pédagogique MCP 2026-07-28, contenu non fiable et cas indépendants / `programme_prevu`
- **Branche :** `feat/fil-rouge-ingenierie-auto-ia`
- **Niveau :** `Extension production`
- **Priorité :** `P2`
- **Statut documentaire :** `Candidate`
- **Statut de preuve :** `Candidat`
- **Travail :** `À faire`
- **Responsable :** intégrateur — personne à désigner

Cette Feature détaille la User Story parente ; elle ne crée pas une exigence indépendante.

## Contrat candidat

- **Entrée :** Contrat validé de consultation, choix de transport/SDK et révision compatible approuvés ; stockage local autorisé.
- **Sortie :** Observation d'appel MCP corrélée à la même décision locale que l'appel direct.
- **Périmètre :** Adaptateur local minimal ; pas d'exposition publique, d'authentification inventée ou de développement obligatoire pendant J07.
- **Règle canonique :** [`RM-FIL-304`](../../user-stories/US-FIL-304.md#rm-fil-304)
- **Critères canoniques :** [`CA-FIL-304-01`](../../user-stories/US-FIL-304.md#ca-fil-304-01), [`CA-FIL-304-02`](../../user-stories/US-FIL-304.md#ca-fil-304-02), [`CA-FIL-304-03`](../../user-stories/US-FIL-304.md#ca-fil-304-03)

Aucune surface future n'est affirmée comme présente ; son emplacement reste à décider avant réalisation. La baseline actuelle est décrite dans [`current-state.md`](../../../../baseline/current-state.md). Les noms de modules futurs ne sont pas présentés comme existants.

## Découpage exécutable

| Tâche | Objectif | Phase | Dépendances |
|---|---|---|---|
| [`TASK-FIL-304-01`](tasks/TASK-FIL-304-01.md) | Faire approuver révision, SDK, transport et origine de l'identité ; consigner les incompatibilités connues. | Spécifier et figer l'oracle | [`US-FIL-301`](../../user-stories/US-FIL-301.md), [`US-FIL-302`](../../user-stories/US-FIL-302.md), [`US-FIL-303`](../../user-stories/US-FIL-303.md) |
| [`TASK-FIL-304-02`](tasks/TASK-FIL-304-02.md) | Brancher le transport sur le contrat local sans contourner la politique ni exposer une commande générique. | Réaliser dans le périmètre autorisé | [`TASK-FIL-304-01`](tasks/TASK-FIL-304-01.md) |
| [`TASK-FIL-304-03`](tasks/TASK-FIL-304-03.md) | Tester parité d'autorisation, annulation et capacité interdite, et documenter les différences de protocole réellement observées. | Vérifier et soumettre à revue | [`TASK-FIL-304-02`](tasks/TASK-FIL-304-02.md) |

La livraison et les tests sont planifiés ; aucune tâche n'est exécutée par cette spécification.

## Vérification prévue

L'oracle à appliquer est celui de la [`User Story parente`](../../user-stories/US-FIL-304.md#oracle-indépendant) : Même matrice d'autorisation que US-301 appliquée séparément au transport ; lecteur espion et corpus témoin en lecture seule.

Les limites d'interruption, de concurrence ou de documentation applicables restent celles des cas de la User Story. Aucun retour de code supplémentaire n'est inventé ici.

## Acceptation

- [ ] [`CA-FIL-304-01`](../../user-stories/US-FIL-304.md#ca-fil-304-01)
- [ ] [`CA-FIL-304-02`](../../user-stories/US-FIL-304.md#ca-fil-304-02)
- [ ] [`CA-FIL-304-03`](../../user-stories/US-FIL-304.md#ca-fil-304-03)

Le responsable nominatif et la décision d'acceptation restent à décider. Les décisions demeurent humaines et [`AMB-09`](../../../../governance/ambiguities.md#amb-09) reste ouverte.
