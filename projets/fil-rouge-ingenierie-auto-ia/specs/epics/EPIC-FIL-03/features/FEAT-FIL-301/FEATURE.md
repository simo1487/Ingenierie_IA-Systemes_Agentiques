# FEAT-FIL-301 — Autoriser une consultation avant tout accès

`Référence — feature candidate`

- **Projet parent :** [`PROJ-FIL-AUTO-IA-001`](../../../../../SPEC.md)
- **Epic parente :** [`EPIC-FIL-03`](../../EPIC.md)
- **User Story parente :** [`US-FIL-301`](../../user-stories/US-FIL-301.md)
- **Jour :** `J07`
- **Sources de formation :** [`C05-SKILL`](../../../../baseline/sources.md#c05-skill) — `J05` / Méthode capitalisée, outils/événements versionnés, limites des démonstrations LlamaIndex / `support_actuel`<br>[`C07-G6`](../../../../baseline/sources.md#c07-g6) — `J07` / Outil préparé ou replay, refus avant accès, régression et première divergence ; G6 / `programme_prevu`
- **Branche :** `feat/fil-rouge-ingenierie-auto-ia`
- **Niveau :** `Socle formation`
- **Priorité :** `P1`
- **Statut documentaire :** `Candidate`
- **Statut de preuve :** `Candidat`
- **Travail :** `À faire`
- **Responsable :** responsable sécurité — personne à désigner

Cette Feature détaille la User Story parente ; elle ne crée pas une exigence indépendante.

## Contrat candidat

- **Entrée :** Identité issue du contexte de confiance, outil read-only nommé, arguments typés par identifiants et périmètre autorisé versionné.
- **Sortie :** Observation autorisé/refusé avec règle, raison et ordre des événements ; résultat uniquement après autorisation.
- **Périmètre :** Consultation d'une ressource fictive ; pas de SQL libre, shell, URL libre ni écriture sur sources.
- **Règle canonique :** [`RM-FIL-301`](../../user-stories/US-FIL-301.md#rm-fil-301)
- **Critères canoniques :** [`CA-FIL-301-01`](../../user-stories/US-FIL-301.md#ca-fil-301-01), [`CA-FIL-301-02`](../../user-stories/US-FIL-301.md#ca-fil-301-02), [`CA-FIL-301-03`](../../user-stories/US-FIL-301.md#ca-fil-301-03)

Aucune surface future n'est affirmée comme présente ; son emplacement reste à décider avant réalisation. La baseline actuelle est décrite dans [`current-state.md`](../../../../baseline/current-state.md). Les noms de modules futurs ne sont pas présentés comme existants.

La table de décision candidate associée est [`RM-FIL-301`](../../../../governance/decision-tables.md#lecture-doutil-rm-fil-301).

## Découpage exécutable

| Tâche | Objectif | Phase | Dépendances |
|---|---|---|---|
| [`TASK-FIL-301-01`](tasks/TASK-FIL-301-01.md) | Définir la fiche de l'outil consulter_passage, les arguments et la table exhaustive d'autorisation. | Spécifier et figer l'oracle | [`US-FIL-6`](../../../EPIC-FIL-00/user-stories/US-FIL-6.md), [`US-FIL-101`](../../../EPIC-FIL-01/user-stories/US-FIL-101.md), [`US-FIL-102`](../../../EPIC-FIL-01/user-stories/US-FIL-102.md) |
| [`TASK-FIL-301-02`](tasks/TASK-FIL-301-02.md) | Placer validation et politique avant le lecteur local ; utiliser un outil préparé ou replay pour J07. | Réaliser dans le périmètre autorisé | [`TASK-FIL-301-01`](tasks/TASK-FIL-301-01.md) |
| [`TASK-FIL-301-03`](tasks/TASK-FIL-301-03.md) | Produire un appel autorisé et un refus hors portée avec compteur d'accès, puis retirer le garde en environnement de test pour éprouver l'oracle. | Vérifier et soumettre à revue | [`TASK-FIL-301-02`](tasks/TASK-FIL-301-02.md) |

La livraison et les tests sont planifiés ; aucune tâche n'est exécutée par cette spécification.

## Vérification prévue

L'oracle à appliquer est celui de la [`User Story parente`](../../user-stories/US-FIL-301.md#oracle-indépendant) : Matrice identité/périmètre/arguments figée par le responsable ; lecteur espion indépendant ; journal établissant décision avant accès. Aucun rôle fourni par le modèle ne vaut identité authentifiée.

Les limites d'interruption, de concurrence ou de documentation applicables restent celles des cas de la User Story. Aucun retour de code supplémentaire n'est inventé ici.

## Acceptation

- [ ] [`CA-FIL-301-01`](../../user-stories/US-FIL-301.md#ca-fil-301-01)
- [ ] [`CA-FIL-301-02`](../../user-stories/US-FIL-301.md#ca-fil-301-02)
- [ ] [`CA-FIL-301-03`](../../user-stories/US-FIL-301.md#ca-fil-301-03)

Le responsable nominatif et la décision d'acceptation restent à décider. Les décisions demeurent humaines et [`AMB-08`](../../../../governance/ambiguities.md#amb-08) reste ouverte.
