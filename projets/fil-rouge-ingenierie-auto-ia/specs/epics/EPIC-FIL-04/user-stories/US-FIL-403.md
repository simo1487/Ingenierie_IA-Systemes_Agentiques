# US-FIL-403 — Localiser la première divergence d'une trace

`Référence — spécification candidate`

- **Projet parent :** [`PROJ-FIL-AUTO-IA-001`](../../../../SPEC.md)
- **Epic parente :** [`EPIC-FIL-04`](../EPIC.md)
- **Feature fille :** [`FEAT-FIL-403`](../features/FEAT-FIL-403/FEATURE.md)
- **Jour :** `J07`
- **Sources de formation :** [`C03`](../../../baseline/sources.md#c03) — `J03` / Reproduction, hypothèses concurrentes, rouge/vert comparable, mutation et documentation / `support_actuel`<br>[`C07-G6`](../../../baseline/sources.md#c07-g6) — `J07` / Outil préparé ou replay, refus avant accès, régression et première divergence ; G6 / `programme_prevu`
- **Relation pédagogique :** Enquête sur la première divergence, cause distincte d'une hypothèse.
- **Niveau :** `Socle formation`
- **Priorité :** `P1`
- **Statut documentaire :** `Candidate`
- **Statut de preuve :** `Candidat`
- **Travail :** `À faire`
- **Responsable :** mainteneur — personne à désigner
- **Dépendances :** [`US-FIL-3`](../../EPIC-FIL-00/user-stories/US-FIL-3.md), [`US-FIL-102`](../../EPIC-FIL-01/user-stories/US-FIL-102.md), [`US-FIL-401`](US-FIL-401.md)
- **Ambiguïté :** [`AMB-02`](../../../governance/ambiguities.md#amb-02)

## Besoin

> En tant que mainteneur, je veux aligner une trace sur les événements attendus afin de corriger le premier contrôle fautif plutôt que masquer un symptôme.

## Périmètre

Comparaison locale et enquête traçable ; pas d'observabilité distribuée obligatoire.

Les décisions restent humaines ; aucune implémentation métier n'est réalisée par cette spécification.

## Entrées et sorties

- **Entrée :** Trace attendue revue, trace observée assainie, identifiants d'événement et versions d'entrée identiques.
- **Sortie :** Observation du premier événement divergent et proposition de cause ; correction soumise au rejeu.

Les baselines sont référencées dans [`sources.md`](../../../baseline/sources.md) ; leur révision est inconnue lorsqu'elle n'y est pas explicitement donnée. La sortie ne constitue pas, à elle seule, une preuve.

## Règle et critères

<a id="rm-fil-403"></a>
`RM-FIL-403` — Le diagnostic distingue la première divergence observée d'une hypothèse de cause encore non prouvée.

<a id="ca-fil-403-01"></a>
- [ ] `CA-FIL-403-01` — Étant donné la lecture précède le refus dans une trace, quand les événements sont confrontés à la séquence politique puis accès, alors la lecture anticipée est localisée comme première divergence.
<a id="ca-fil-403-02"></a>
- [ ] `CA-FIL-403-02` — Étant donné seuls les horodatages d'exécution diffèrent, quand les traces sont comparées selon les champs sémantiques déclarés, alors aucune divergence métier n'est inventée.
<a id="ca-fil-403-03"></a>
- [ ] `CA-FIL-403-03` — Étant donné un événement manque ou les versions d'entrée diffèrent, quand le diagnostic est demandé, alors l'incomplétude ou la non-comparabilité est signalée, pas une cause certaine.

## Example Mapping

| Cas | Étant donné | Quand | Alors |
|---|---|---|---|
| Nominal | la lecture précède le refus dans une trace | les événements sont confrontés à la séquence politique puis accès | la lecture anticipée est localisée comme première divergence |
| Frontière | seuls les horodatages d'exécution diffèrent | les traces sont comparées selon les champs sémantiques déclarés | aucune divergence métier n'est inventée |
| Refus | un événement manque ou les versions d'entrée diffèrent | le diagnostic est demandé | l'incomplétude ou la non-comparabilité est signalée, pas une cause certaine |

## Scénarios Gherkin

```gherkin
Fonctionnalité: Localiser la première divergence d'une trace
  Contexte:
    Étant donné le périmètre et les entrées versionnées de US-FIL-403
    Et les attendus ci-dessous définis avant la future réalisation

  Scénario: Nominal — CA-FIL-403-01
    Étant donné la lecture précède le refus dans une trace
    Quand les événements sont confrontés à la séquence politique puis accès
    Alors la lecture anticipée est localisée comme première divergence

  Scénario: Frontière — CA-FIL-403-02
    Étant donné seuls les horodatages d'exécution diffèrent
    Quand les traces sont comparées selon les champs sémantiques déclarés
    Alors aucune divergence métier n'est inventée

  Scénario: Refus — CA-FIL-403-03
    Étant donné un événement manque ou les versions d'entrée diffèrent
    Quand le diagnostic est demandé
    Alors l'incomplétude ou la non-comparabilité est signalée, pas une cause certaine
```

## Oracle indépendant

Séquences courtes attendues écrites par le relecteur avec ordre explicite ; champs non sémantiques exclus explicitement ; aucun tri ne doit masquer l'ordre réel des événements.

## Réalisation et preuves

- [`FEAT-FIL-403`](../features/FEAT-FIL-403/FEATURE.md) — Feature candidate
- [`TASK-FIL-403-01`](../features/FEAT-FIL-403/tasks/TASK-FIL-403-01.md) — Figer les champs d'alignement et trois traces : accès anticipé, horloges différentes, événement absent.
- [`TASK-FIL-403-02`](../features/FEAT-FIL-403/tasks/TASK-FIL-403-02.md) — Produire un diagnostic aligné et une hypothèse séparée de l'observation, avec référence au contrôle concerné.
- [`TASK-FIL-403-03`](../features/FEAT-FIL-403/tasks/TASK-FIL-403-03.md) — Faire corriger uniquement le contrôle identifié puis rejouer le jeu complet de cas et consigner le résultat.

Aucune preuve d'acceptation de cette US n'est produite par son rendu. Les artefacts existants peuvent satisfaire un prérequis après revue ; aucune répétition de travaux déjà démontrés n'est imposée.

## Questions ouvertes

Voir [`AMB-02`](../../../governance/ambiguities.md#amb-02).
