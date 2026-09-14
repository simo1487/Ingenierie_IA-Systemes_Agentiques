# US-FIL-305 — Importer un diagnostic qualité attribuable

`Référence — spécification candidate`

- **Projet parent :** [`PROJ-FIL-AUTO-IA-001`](../../../../SPEC.md)
- **Epic parente :** [`EPIC-FIL-03`](../EPIC.md)
- **Feature fille :** [`FEAT-FIL-305`](../features/FEAT-FIL-305/FEATURE.md)
- **Jour :** `J07`
- **Sources de formation :** [`C03`](../../../baseline/sources.md#c03) — `J03` / Reproduction, hypothèses concurrentes, rouge/vert comparable, mutation et documentation / `support_actuel`<br>[`N03`](../../../baseline/sources.md#n03) — `J03` / Plan préalable, tests générés, scripts, qualité et organisation des spécifications ; propos à confirmer / `synthese_automatique`<br>[`C07`](../../../baseline/sources.md#c07) — `J07` / Politique avant accès, révision pédagogique MCP 2026-07-28, contenu non fiable et cas indépendants / `programme_prevu`
- **Relation pédagogique :** Extension outil qualité borné, alertes séparées des verdicts humains.
- **Niveau :** `Extension production`
- **Priorité :** `P2`
- **Statut documentaire :** `Candidate`
- **Statut de preuve :** `Candidat`
- **Travail :** `À faire`
- **Responsable :** responsable qualité — personne à désigner
- **Dépendances :** [`US-FIL-3`](../../EPIC-FIL-00/user-stories/US-FIL-3.md), [`US-FIL-101`](../../EPIC-FIL-01/user-stories/US-FIL-101.md), [`US-FIL-301`](US-FIL-301.md)
- **Ambiguïté :** [`AMB-10`](../../../governance/ambiguities.md#amb-10)

## Besoin

> En tant que responsable qualité, je veux lier un diagnostic à l'outil et à la révision de code analysée afin de distinguer une sortie réelle de Cppcheck d'une fixture.

## Périmètre

Import read-only et conseil borné ; auto-correction, exécution shell libre et conformité MISRA exclus.

Les décisions restent humaines ; aucune implémentation métier n'est réalisée par cette spécification.

## Entrées et sorties

- **Entrée :** Rapport Cppcheck local ou fixture déclarée, version d'outil, options, SHA du code cible et code retour ; droits d'utilisation approuvés.
- **Sortie :** Observation de diagnostic avec provenance et proposition IA séparée ; aucun patch appliqué.

Les baselines sont référencées dans [`sources.md`](../../../baseline/sources.md) ; leur révision est inconnue lorsqu'elle n'y est pas explicitement donnée. La sortie ne constitue pas, à elle seule, une preuve.

## Règle et critères

<a id="rm-fil-305"></a>
`RM-FIL-305` — Un diagnostic sans provenance d'exécution ne peut pas être présenté comme résultat d'une analyse réelle.

<a id="ca-fil-305-01"></a>
- [ ] `CA-FIL-305-01` — Étant donné un rapport complet correspond au code cible figé, quand l'adaptateur importe le diagnostic, alors outil, options, révision et code retour accompagnent l'observation.
<a id="ca-fil-305-02"></a>
- [ ] `CA-FIL-305-02` — Étant donné le rapport réel ne contient aucun diagnostic, quand il est importé, alors le résultat indique l'absence d'alerte observée sans prétendre à la conformité.
<a id="ca-fil-305-03"></a>
- [ ] `CA-FIL-305-03` — Étant donné l'outil est indisponible ou le rapport est malformé, quand l'analyse est demandée, alors l'échec est déclaré sans substitution silencieuse d'une fixture.

## Example Mapping

| Cas | Étant donné | Quand | Alors |
|---|---|---|---|
| Nominal | un rapport complet correspond au code cible figé | l'adaptateur importe le diagnostic | outil, options, révision et code retour accompagnent l'observation |
| Frontière | le rapport réel ne contient aucun diagnostic | il est importé | le résultat indique l'absence d'alerte observée sans prétendre à la conformité |
| Refus | l'outil est indisponible ou le rapport est malformé | l'analyse est demandée | l'échec est déclaré sans substitution silencieuse d'une fixture |

## Scénarios Gherkin

```gherkin
Fonctionnalité: Importer un diagnostic qualité attribuable
  Contexte:
    Étant donné le périmètre et les entrées versionnées de US-FIL-305
    Et les attendus ci-dessous définis avant la future réalisation

  Scénario: Nominal — CA-FIL-305-01
    Étant donné un rapport complet correspond au code cible figé
    Quand l'adaptateur importe le diagnostic
    Alors outil, options, révision et code retour accompagnent l'observation

  Scénario: Frontière — CA-FIL-305-02
    Étant donné le rapport réel ne contient aucun diagnostic
    Quand il est importé
    Alors le résultat indique l'absence d'alerte observée sans prétendre à la conformité

  Scénario: Refus — CA-FIL-305-03
    Étant donné l'outil est indisponible ou le rapport est malformé
    Quand l'analyse est demandée
    Alors l'échec est déclaré sans substitution silencieuse d'une fixture
```

## Oracle indépendant

Petit code cible autorisé avec diagnostic attendu relu indépendamment ; rapport de référence externe au parseur. Un code retour d'outil doit être interprété selon sa documentation versionnée.

## Réalisation et preuves

- [`FEAT-FIL-305`](../features/FEAT-FIL-305/FEATURE.md) — Feature candidate
- [`TASK-FIL-305-01`](../features/FEAT-FIL-305/tasks/TASK-FIL-305-01.md) — Figer un rapport et son oracle avec version/options, distinguer absence d'alerte et erreur d'outil.
- [`TASK-FIL-305-02`](../features/FEAT-FIL-305/tasks/TASK-FIL-305-02.md) — Prévoir un adaptateur qualité limité au format approuvé et conserver la provenance avec les conseils.
- [`TASK-FIL-305-03`](../features/FEAT-FIL-305/tasks/TASK-FIL-305-03.md) — Vérifier nominal, rapport vide et erreur, puis faire qualifier les faux positifs par le responsable qualité.

Aucune preuve d'acceptation de cette US n'est produite par son rendu. Les artefacts existants peuvent satisfaire un prérequis après revue ; aucune répétition de travaux déjà démontrés n'est imposée.

## Questions ouvertes

Voir [`AMB-10`](../../../governance/ambiguities.md#amb-10).
