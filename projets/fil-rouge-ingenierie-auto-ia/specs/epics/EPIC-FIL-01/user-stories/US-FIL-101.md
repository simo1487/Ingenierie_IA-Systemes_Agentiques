# US-FIL-101 — Autoriser une baseline avant toute étape dépendante

`Référence — spécification candidate`

- **Projet parent :** [`PROJ-FIL-AUTO-IA-001`](../../../../SPEC.md)
- **Epic parente :** [`EPIC-FIL-01`](../EPIC.md)
- **Feature fille :** [`FEAT-FIL-101`](../features/FEAT-FIL-101/FEATURE.md)
- **Jour :** `J06`
- **Sources de formation :** [`C02`](../../../baseline/sources.md#c02) — `J02` / Exigence singulière, inconnues, exemples et oracle indépendant ; Gherkin non universellement obligatoire / `support_actuel`<br>[`C04`](../../../baseline/sources.md#c04) — `J04` / Corpus autorisé, découpage du sens, lexical/sémantique, Hit@k/MRR et support des citations / `support_actuel`<br>[`C06`](../../../baseline/sources.md#c06) — `J06` / Comparaison d'organisations, rôles, reprise, idempotence, mémoire et trace / `programme_prevu`
- **Relation pédagogique :** Transposition en prévalidation du manifeste et arrêt avant les étapes dépendantes.
- **Niveau :** `Socle formation`
- **Priorité :** `P1`
- **Statut documentaire :** `Candidate`
- **Statut de preuve :** `Candidat`
- **Travail :** `À faire`
- **Responsable :** responsable de baseline — personne à désigner
- **Dépendances :** [`US-FIL-1`](../../EPIC-FIL-00/user-stories/US-FIL-1.md), [`US-FIL-4`](../../EPIC-FIL-00/user-stories/US-FIL-4.md)
- **Ambiguïté :** [`AMB-01`](../../../governance/ambiguities.md#amb-01)

## Besoin

> En tant que responsable de baseline, je veux faire contrôler les entrées approuvées avant les appels d'agents afin d’éviter une génération sur un corpus invalide.

## Périmètre

Prévalidation du manifeste et propagation du blocage ; hors périmètre : acquisition de corpus réel.

Les décisions restent humaines ; aucune implémentation métier n'est réalisée par cette spécification.

## Entrées et sorties

- **Entrée :** Manifeste local versionné : run_id, objective, baselines avec id/révision, approbation portant sur cette version. Corpus fictif pour le socle ; corpus réel soumis à AMB-01.
- **Sortie :** Observation de validation ou arrêt Bloqué avec motif, sans appel fournisseur en cas d'échec.

Les baselines sont référencées dans [`sources.md`](../../../baseline/sources.md) ; leur révision est inconnue lorsqu'elle n'y est pas explicitement donnée. La sortie ne constitue pas, à elle seule, une preuve.

## Règle et critères

<a id="rm-fil-101"></a>
`RM-FIL-101` — Une baseline absente, non approuvée ou sans révision interdit toute étape qui en dépend.

<a id="ca-fil-101-01"></a>
- [ ] `CA-FIL-101-01` — Étant donné le manifeste fictif M1 contient B1 révisée et approuvée, quand l'opérateur démarre le lot, alors les étapes dépendantes sont autorisées pour M1.
<a id="ca-fil-101-02"></a>
- [ ] `CA-FIL-101-02` — Étant donné M1 contient une liste de baselines vide, quand l'opérateur démarre le lot, alors le lot est bloqué et le compteur d'appels fournisseur reste à zéro.
<a id="ca-fil-101-03"></a>
- [ ] `CA-FIL-101-03` — Étant donné B1 a une révision vide malgré une approbation à vrai, quand l'opérateur démarre le lot, alors le lot est bloqué avant retrieval et génération.

## Example Mapping

| Cas | Étant donné | Quand | Alors |
|---|---|---|---|
| Nominal | le manifeste fictif M1 contient B1 révisée et approuvée | l'opérateur démarre le lot | les étapes dépendantes sont autorisées pour M1 |
| Frontière | M1 contient une liste de baselines vide | l'opérateur démarre le lot | le lot est bloqué et le compteur d'appels fournisseur reste à zéro |
| Refus | B1 a une révision vide malgré une approbation à vrai | l'opérateur démarre le lot | le lot est bloqué avant retrieval et génération |

Table de décision candidate : [`RM-FIL-101`](../../../governance/decision-tables.md#prévalidation-rm-fil-101).

## Scénarios Gherkin

```gherkin
Fonctionnalité: Autoriser une baseline avant toute étape dépendante
  Contexte:
    Étant donné le périmètre et les entrées versionnées de US-FIL-101
    Et les attendus ci-dessous définis avant la future réalisation

  Scénario: Nominal — CA-FIL-101-01
    Étant donné le manifeste fictif M1 contient B1 révisée et approuvée
    Quand l'opérateur démarre le lot
    Alors les étapes dépendantes sont autorisées pour M1

  Scénario: Frontière — CA-FIL-101-02
    Étant donné M1 contient une liste de baselines vide
    Quand l'opérateur démarre le lot
    Alors le lot est bloqué et le compteur d'appels fournisseur reste à zéro

  Scénario: Refus — CA-FIL-101-03
    Étant donné B1 a une révision vide malgré une approbation à vrai
    Quand l'opérateur démarre le lot
    Alors le lot est bloqué avant retrieval et génération
```

## Oracle indépendant

Manifestes M1 valides et invalides figés par le relecteur ; espion des appels retrieval/fournisseur indépendant des statuts retournés. La sortie seule ne suffit pas à prouver l'absence d'appel.

## Réalisation et preuves

- [`FEAT-FIL-101`](../features/FEAT-FIL-101/FEATURE.md) — Feature candidate
- [`TASK-FIL-101-01`](../features/FEAT-FIL-101/tasks/TASK-FIL-101-01.md) — Figer les variantes M1, corpus vide, révision vide et approbation absente ; écrire la table de décision de prévalidation.
- [`TASK-FIL-101-02`](../features/FEAT-FIL-101/tasks/TASK-FIL-101-02.md) — Prévoir la validation d'entrée et l'arrêt des étapes dépendantes dans AutomotiveAIFlow.run ; préserver la CLI hors ligne.
- [`TASK-FIL-101-03`](../features/FEAT-FIL-101/tasks/TASK-FIL-101-03.md) — Vérifier les refus avec espions, éprouver la suppression du garde de corpus et faire accepter la baseline par un responsable.

Aucune preuve d'acceptation de cette US n'est produite par son rendu. Les artefacts existants peuvent satisfaire un prérequis après revue ; aucune répétition de travaux déjà démontrés n'est imposée.

## Questions ouvertes

Voir [`AMB-01`](../../../governance/ambiguities.md#amb-01).
