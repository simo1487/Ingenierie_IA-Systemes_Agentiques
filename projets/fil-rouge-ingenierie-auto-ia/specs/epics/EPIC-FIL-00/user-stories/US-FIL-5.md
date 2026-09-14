# US-FIL-5 — Vérifier le support de chaque affirmation générée

`Référence — spécification candidate`

- **Projet parent :** [`PROJ-FIL-AUTO-IA-001`](../../../../SPEC.md)
- **Epic parente :** [`EPIC-FIL-00`](../EPIC.md)
- **Feature fille :** [`FEAT-FIL-5`](../features/FEAT-FIL-5/FEATURE.md)
- **Jour :** `J01–J05`
- **Sources de formation :** [`C02`](../../../baseline/sources.md#c02) — `J02` / Exigence singulière, inconnues, exemples et oracle indépendant ; Gherkin non universellement obligatoire / `support_actuel`<br>[`C04`](../../../baseline/sources.md#c04) — `J04` / Corpus autorisé, découpage du sens, lexical/sémantique, Hit@k/MRR et support des citations / `support_actuel`
- **Relation pédagogique :** Prérequis : revoir le sens d'une affirmation, pas seulement la validité de sa citation.
- **Niveau :** `Socle formation`
- **Priorité :** `P1`
- **Statut documentaire :** `Candidate`
- **Statut de preuve :** `Candidat`
- **Travail :** `À faire`
- **Responsable :** relecteur exigences — personne à désigner
- **Dépendances :** [`US-FIL-2`](US-FIL-2.md), [`US-FIL-4`](US-FIL-4.md)
- **Ambiguïté :** [`AMB-23`](../../../governance/ambiguities.md#amb-23)

## Besoin

> En tant que relecteur exigences, je veux qualifier la relation entre une affirmation et son passage cité afin de ne pas confondre une citation existante avec une réponse justifiée.

## Périmètre

Revue de l'ancrage des propositions déjà au cœur du fil rouge ; pas seulement évaluation d'un futur moteur sémantique.

Les décisions restent humaines ; aucune implémentation métier n'est réalisée par cette spécification.

## Entrées et sorties

- **Entrée :** Proposition d'exigence ou de réponse découpée en affirmations, citations source/révision/locator et passages autorisés ; critères de support revus avant génération.
- **Sortie :** Proposition avec revue par affirmation : support complet, support partiel, contradiction ou absence de support ; abstention et conflits visibles.

Les baselines sont référencées dans [`sources.md`](../../../baseline/sources.md) ; leur révision est inconnue lorsqu'elle n'y est pas explicitement donnée. La sortie ne constitue pas, à elle seule, une preuve.

## Règle et critères

<a id="rm-fil-5"></a>
`RM-FIL-5` — L'existence d'une citation ne permet pas de déclarer qu'elle soutient toute l'affirmation.

<a id="ca-fil-5-01"></a>
- [ ] `CA-FIL-5-01` — Étant donné le passage cité soutient toutes les conditions de l'affirmation fictive, quand un relecteur confronte texte et source, alors le support complet est consigné sur cette version sans approuver automatiquement l'exigence.
<a id="ca-fil-5-02"></a>
- [ ] `CA-FIL-5-02` — Étant donné la citation soutient une seule partie de l'affirmation, quand la revue est effectuée, alors le support reste partiel et la partie non étayée est identifiée.
<a id="ca-fil-5-03"></a>
- [ ] `CA-FIL-5-03` — Étant donné la citation n'existe pas dans la version annoncée, quand le contrôle mécanique est effectué, alors l'absence de support est déclarée et la réponse n'est pas présentée comme vérifiée.
<a id="ca-fil-5-04"></a>
- [ ] `CA-FIL-5-04` — Étant donné deux passages autorisés se contredisent, quand une synthèse est proposée, alors le conflit est exposé et soumis à arbitrage sans choisir silencieusement une version.
<a id="ca-fil-5-05"></a>
- [ ] `CA-FIL-5-05` — Étant donné aucun passage n'étaye la demande, quand une réponse est demandée, alors le manque est explicite et aucune exigence n'est fabriquée pour le combler.

## Example Mapping

| Cas | Étant donné | Quand | Alors |
|---|---|---|---|
| Nominal | le passage cité soutient toutes les conditions de l'affirmation fictive | un relecteur confronte texte et source | le support complet est consigné sur cette version sans approuver automatiquement l'exigence |
| Frontière | la citation soutient une seule partie de l'affirmation | la revue est effectuée | le support reste partiel et la partie non étayée est identifiée |
| Refus | la citation n'existe pas dans la version annoncée | le contrôle mécanique est effectué | l'absence de support est déclarée et la réponse n'est pas présentée comme vérifiée |
| Contradiction | deux passages autorisés se contredisent | une synthèse est proposée | le conflit est exposé et soumis à arbitrage sans choisir silencieusement une version |
| Abstention | aucun passage n'étaye la demande | une réponse est demandée | le manque est explicite et aucune exigence n'est fabriquée pour le combler |

## Scénarios Gherkin

```gherkin
Fonctionnalité: Vérifier le support de chaque affirmation générée
  Contexte:
    Étant donné le périmètre et les entrées versionnées de US-FIL-5
    Et les attendus ci-dessous définis avant la future réalisation

  Scénario: Nominal — CA-FIL-5-01
    Étant donné le passage cité soutient toutes les conditions de l'affirmation fictive
    Quand un relecteur confronte texte et source
    Alors le support complet est consigné sur cette version sans approuver automatiquement l'exigence

  Scénario: Frontière — CA-FIL-5-02
    Étant donné la citation soutient une seule partie de l'affirmation
    Quand la revue est effectuée
    Alors le support reste partiel et la partie non étayée est identifiée

  Scénario: Refus — CA-FIL-5-03
    Étant donné la citation n'existe pas dans la version annoncée
    Quand le contrôle mécanique est effectué
    Alors l'absence de support est déclarée et la réponse n'est pas présentée comme vérifiée

  Scénario: Contradiction — CA-FIL-5-04
    Étant donné deux passages autorisés se contredisent
    Quand une synthèse est proposée
    Alors le conflit est exposé et soumis à arbitrage sans choisir silencieusement une version

  Scénario: Abstention — CA-FIL-5-05
    Étant donné aucun passage n'étaye la demande
    Quand une réponse est demandée
    Alors le manque est explicite et aucune exigence n'est fabriquée pour le combler
```

## Oracle indépendant

MES-06 : annotations et revue indépendante du sens, séparées de la résolution mécanique des citations et des scores de retrieval. Ni copie de la sortie IA ni juge LLM unique.

## Réalisation et preuves

- [`FEAT-FIL-5`](../features/FEAT-FIL-5/FEATURE.md) — Feature candidate
- [`TASK-FIL-5-01`](../features/FEAT-FIL-5/tasks/TASK-FIL-5-01.md) — Figer les affirmations et les passages fictifs correspondant aux cinq situations, avec attendus revus.
- [`TASK-FIL-5-02`](../features/FEAT-FIL-5/tasks/TASK-FIL-5-02.md) — Préparer le contrôle de provenance et la fiche de revue du support sémantique, séparés de la génération.
- [`TASK-FIL-5-03`](../features/FEAT-FIL-5/tasks/TASK-FIL-5-03.md) — Faire revoir chaque affirmation et conserver les refus, contradictions et abstentions sans les compenser par un score global.

Aucune preuve d'acceptation de cette US n'est produite par son rendu. Les artefacts existants peuvent satisfaire un prérequis après revue ; aucune répétition de travaux déjà démontrés n'est imposée.

## Questions ouvertes

Voir [`AMB-23`](../../../governance/ambiguities.md#amb-23).
