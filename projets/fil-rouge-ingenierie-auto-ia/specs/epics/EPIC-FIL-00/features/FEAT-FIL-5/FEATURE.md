# FEAT-FIL-5 — Vérifier le support de chaque affirmation générée

`Référence — feature candidate`

- **Projet parent :** [`PROJ-FIL-AUTO-IA-001`](../../../../../SPEC.md)
- **Epic parente :** [`EPIC-FIL-00`](../../EPIC.md)
- **User Story parente :** [`US-FIL-5`](../../user-stories/US-FIL-5.md)
- **Jour :** `J01–J05`
- **Sources de formation :** [`C02`](../../../../baseline/sources.md#c02) — `J02` / Exigence singulière, inconnues, exemples et oracle indépendant ; Gherkin non universellement obligatoire / `support_actuel`<br>[`C04`](../../../../baseline/sources.md#c04) — `J04` / Corpus autorisé, découpage du sens, lexical/sémantique, Hit@k/MRR et support des citations / `support_actuel`
- **Branche :** `feat/fil-rouge-ingenierie-auto-ia`
- **Niveau :** `Socle formation`
- **Priorité :** `P1`
- **Statut documentaire :** `Candidate`
- **Statut de preuve :** `Candidat`
- **Travail :** `À faire`
- **Responsable :** relecteur exigences — personne à désigner

Cette Feature détaille la User Story parente ; elle ne crée pas une exigence indépendante.

## Contrat candidat

- **Entrée :** Proposition d'exigence ou de réponse découpée en affirmations, citations source/révision/locator et passages autorisés ; critères de support revus avant génération.
- **Sortie :** Proposition avec revue par affirmation : support complet, support partiel, contradiction ou absence de support ; abstention et conflits visibles.
- **Périmètre :** Revue de l'ancrage des propositions déjà au cœur du fil rouge ; pas seulement évaluation d'un futur moteur sémantique.
- **Règle canonique :** [`RM-FIL-5`](../../user-stories/US-FIL-5.md#rm-fil-5)
- **Critères canoniques :** [`CA-FIL-5-01`](../../user-stories/US-FIL-5.md#ca-fil-5-01), [`CA-FIL-5-02`](../../user-stories/US-FIL-5.md#ca-fil-5-02), [`CA-FIL-5-03`](../../user-stories/US-FIL-5.md#ca-fil-5-03), [`CA-FIL-5-04`](../../user-stories/US-FIL-5.md#ca-fil-5-04), [`CA-FIL-5-05`](../../user-stories/US-FIL-5.md#ca-fil-5-05)

Aucune surface future n'est affirmée comme présente ; son emplacement reste à décider avant réalisation. La baseline actuelle est décrite dans [`current-state.md`](../../../../baseline/current-state.md). Les noms de modules futurs ne sont pas présentés comme existants.

## Découpage exécutable

| Tâche | Objectif | Phase | Dépendances |
|---|---|---|---|
| [`TASK-FIL-5-01`](tasks/TASK-FIL-5-01.md) | Figer les affirmations et les passages fictifs correspondant aux cinq situations, avec attendus revus. | Spécifier et figer l'oracle | [`US-FIL-2`](../../user-stories/US-FIL-2.md), [`US-FIL-4`](../../user-stories/US-FIL-4.md) |
| [`TASK-FIL-5-02`](tasks/TASK-FIL-5-02.md) | Préparer le contrôle de provenance et la fiche de revue du support sémantique, séparés de la génération. | Réaliser dans le périmètre autorisé | [`TASK-FIL-5-01`](tasks/TASK-FIL-5-01.md) |
| [`TASK-FIL-5-03`](tasks/TASK-FIL-5-03.md) | Faire revoir chaque affirmation et conserver les refus, contradictions et abstentions sans les compenser par un score global. | Vérifier et soumettre à revue | [`TASK-FIL-5-02`](tasks/TASK-FIL-5-02.md) |

La livraison et les tests sont planifiés ; aucune tâche n'est exécutée par cette spécification.

## Vérification prévue

L'oracle à appliquer est celui de la [`User Story parente`](../../user-stories/US-FIL-5.md#oracle-indépendant) : MES-06 : annotations et revue indépendante du sens, séparées de la résolution mécanique des citations et des scores de retrieval. Ni copie de la sortie IA ni juge LLM unique.

Les limites d'interruption, de concurrence ou de documentation applicables restent celles des cas de la User Story. Aucun retour de code supplémentaire n'est inventé ici.

## Acceptation

- [ ] [`CA-FIL-5-01`](../../user-stories/US-FIL-5.md#ca-fil-5-01)
- [ ] [`CA-FIL-5-02`](../../user-stories/US-FIL-5.md#ca-fil-5-02)
- [ ] [`CA-FIL-5-03`](../../user-stories/US-FIL-5.md#ca-fil-5-03)
- [ ] [`CA-FIL-5-04`](../../user-stories/US-FIL-5.md#ca-fil-5-04)
- [ ] [`CA-FIL-5-05`](../../user-stories/US-FIL-5.md#ca-fil-5-05)

Le responsable nominatif et la décision d'acceptation restent à décider. Les décisions demeurent humaines et [`AMB-23`](../../../../governance/ambiguities.md#amb-23) reste ouverte.
