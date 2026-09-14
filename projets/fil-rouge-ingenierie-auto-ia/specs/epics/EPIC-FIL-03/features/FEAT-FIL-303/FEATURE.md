# FEAT-FIL-303 — Maintenir les permissions face au contenu non fiable

`Référence — feature candidate`

- **Projet parent :** [`PROJ-FIL-AUTO-IA-001`](../../../../../SPEC.md)
- **Epic parente :** [`EPIC-FIL-03`](../../EPIC.md)
- **User Story parente :** [`US-FIL-303`](../../user-stories/US-FIL-303.md)
- **Jour :** `J07`
- **Sources de formation :** [`C04`](../../../../baseline/sources.md#c04) — `J04` / Corpus autorisé, découpage du sens, lexical/sémantique, Hit@k/MRR et support des citations / `support_actuel`<br>[`C07`](../../../../baseline/sources.md#c07) — `J07` / Politique avant accès, révision pédagogique MCP 2026-07-28, contenu non fiable et cas indépendants / `programme_prevu`
- **Branche :** `feat/fil-rouge-ingenierie-auto-ia`
- **Niveau :** `Socle formation`
- **Priorité :** `P1`
- **Statut documentaire :** `Candidate`
- **Statut de preuve :** `Candidat`
- **Travail :** `À faire`
- **Responsable :** responsable sécurité — personne à désigner

Cette Feature détaille la User Story parente ; elle ne crée pas une exigence indépendante.

## Contrat candidat

- **Entrée :** Demandes et passages fictifs marqués non fiables ; politique locale approuvée ; aucun secret ou réseau réel.
- **Sortie :** Observation de tentative et refus technique de l'action non autorisée ; proposition textuelle isolée.
- **Périmètre :** Injections factices directes et indirectes ; aucune attaque sur un service externe.
- **Règle canonique :** [`RM-FIL-303`](../../user-stories/US-FIL-303.md#rm-fil-303)
- **Critères canoniques :** [`CA-FIL-303-01`](../../user-stories/US-FIL-303.md#ca-fil-303-01), [`CA-FIL-303-02`](../../user-stories/US-FIL-303.md#ca-fil-303-02), [`CA-FIL-303-03`](../../user-stories/US-FIL-303.md#ca-fil-303-03)

Aucune surface future n'est affirmée comme présente ; son emplacement reste à décider avant réalisation. La baseline actuelle est décrite dans [`current-state.md`](../../../../baseline/current-state.md). Les noms de modules futurs ne sont pas présentés comme existants.

## Découpage exécutable

| Tâche | Objectif | Phase | Dépendances |
|---|---|---|---|
| [`TASK-FIL-303-01`](tasks/TASK-FIL-303-01.md) | Figer des fixtures défensives directes/indirectes et les actions attendues refusées sous la politique de US-301. | Spécifier et figer l'oracle | [`US-FIL-301`](../../user-stories/US-FIL-301.md) |
| [`TASK-FIL-303-02`](tasks/TASK-FIL-303-02.md) | Séparer données lues et contexte d'autorisation ; revérifier chaque action proposée avant l'appel d'outil. | Réaliser dans le périmètre autorisé | [`TASK-FIL-303-01`](tasks/TASK-FIL-303-01.md) |
| [`TASK-FIL-303-03`](tasks/TASK-FIL-303-03.md) | Montrer refus avant accès et invariance des droits, puis transmettre le cas à la non-régression US-402. | Vérifier et soumettre à revue | [`TASK-FIL-303-02`](tasks/TASK-FIL-303-02.md) |

La livraison et les tests sont planifiés ; aucune tâche n'est exécutée par cette spécification.

## Vérification prévue

L'oracle à appliquer est celui de la [`User Story parente`](../../user-stories/US-FIL-303.md#oracle-indépendant) : Invariants d'autorisation et lecteur espion de US-301 ; fixtures défensives sans données réelles ; contrôler les appels effectifs, pas seulement le texte généré.

Les limites d'interruption, de concurrence ou de documentation applicables restent celles des cas de la User Story. Aucun retour de code supplémentaire n'est inventé ici.

## Acceptation

- [ ] [`CA-FIL-303-01`](../../user-stories/US-FIL-303.md#ca-fil-303-01)
- [ ] [`CA-FIL-303-02`](../../user-stories/US-FIL-303.md#ca-fil-303-02)
- [ ] [`CA-FIL-303-03`](../../user-stories/US-FIL-303.md#ca-fil-303-03)

Le responsable nominatif et la décision d'acceptation restent à décider. Les décisions demeurent humaines et [`AMB-08`](../../../../governance/ambiguities.md#amb-08) reste ouverte.
