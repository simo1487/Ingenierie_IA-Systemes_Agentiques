# US-FIL-2 — Auditer une exigence sans inventer sa règle

`Référence — spécification candidate`

- **Projet parent :** [`PROJ-FIL-AUTO-IA-001`](../../../../SPEC.md)
- **Epic parente :** [`EPIC-FIL-00`](../EPIC.md)
- **Feature fille :** [`FEAT-FIL-2`](../features/FEAT-FIL-2/FEATURE.md)
- **Jour :** `J01–J05`
- **Sources de formation :** [`C02`](../../../baseline/sources.md#c02) — `J02` / Exigence singulière, inconnues, exemples et oracle indépendant ; Gherkin non universellement obligatoire / `support_actuel`<br>[`N02`](../../../baseline/sources.md#n02) — `J02` / Structuration des exigences, moindre privilège et gabarit de feature ; propos à confirmer / `synthese_automatique`
- **Relation pédagogique :** Prérequis : auditer l'exigence et conserver les inconnues avant génération.
- **Niveau :** `Socle formation`
- **Priorité :** `P1`
- **Statut documentaire :** `Candidate`
- **Statut de preuve :** `Candidat`
- **Travail :** `À faire`
- **Responsable :** ingénieur exigences — personne à désigner
- **Dépendances :** [`US-FIL-1`](US-FIL-1.md)
- **Ambiguïté :** [`AMB-20`](../../../governance/ambiguities.md#amb-20)

## Besoin

> En tant qu’ingénieur exigences, je veux isoler les comportements singuliers et les inconnues d'une exigence source afin de définir des attendus réfutables avant génération de code.

## Périmètre

Audit d'un acquis J02 ; ne pas confondre Draft, proposition et validation d'exigence réelle.

Les décisions restent humaines ; aucune implémentation métier n'est réalisée par cette spécification.

## Entrées et sorties

- **Entrée :** Exigence source avec UID, texte original, locator, version, statut et décideur de domaine ; besoins et périmètre issus de US-FIL-1.
- **Sortie :** Proposition d'audit singularité/clarté/vérifiabilité, règles candidates reliées à la source, exemples et questions à décider ; original inchangé.

Les baselines sont référencées dans [`sources.md`](../../../baseline/sources.md) ; leur révision est inconnue lorsqu'elle n'y est pas explicitement donnée. La sortie ne constitue pas, à elle seule, une preuve.

## Règle et critères

<a id="rm-fil-2"></a>
`RM-FIL-2` — Une reformulation d'exigence ne peut ajouter un délai, un seuil ou un effet absent de la source sans décision explicite.

<a id="ca-fil-2-01"></a>
- [ ] `CA-FIL-2-01` — Étant donné l'exigence fictive décrit un comportement observable sous une condition précise, quand l'audit est réalisé, alors le comportement, la condition et l'oracle proposé restent reliés au texte révisé.
<a id="ca-fil-2-02"></a>
- [ ] `CA-FIL-2-02` — Étant donné la source regroupe deux comportements indépendants, quand l'audit la décompose, alors deux propositions singulières conservent le même locator sans perdre une condition.
<a id="ca-fil-2-03"></a>
- [ ] `CA-FIL-2-03` — Étant donné la source demande une réponse rapide sans borne définie, quand l'IA suggère un délai numérique, alors le délai reste une proposition non adoptée et l'ambiguïté est adressée au décideur.

## Example Mapping

| Cas | Étant donné | Quand | Alors |
|---|---|---|---|
| Nominal | l'exigence fictive décrit un comportement observable sous une condition précise | l'audit est réalisé | le comportement, la condition et l'oracle proposé restent reliés au texte révisé |
| Frontière | la source regroupe deux comportements indépendants | l'audit la décompose | deux propositions singulières conservent le même locator sans perdre une condition |
| Refus | la source demande une réponse rapide sans borne définie | l'IA suggère un délai numérique | le délai reste une proposition non adoptée et l'ambiguïté est adressée au décideur |

## Scénarios Gherkin

```gherkin
Fonctionnalité: Auditer une exigence sans inventer sa règle
  Contexte:
    Étant donné le périmètre et les entrées versionnées de US-FIL-2
    Et les attendus ci-dessous définis avant la future réalisation

  Scénario: Nominal — CA-FIL-2-01
    Étant donné l'exigence fictive décrit un comportement observable sous une condition précise
    Quand l'audit est réalisé
    Alors le comportement, la condition et l'oracle proposé restent reliés au texte révisé

  Scénario: Frontière — CA-FIL-2-02
    Étant donné la source regroupe deux comportements indépendants
    Quand l'audit la décompose
    Alors deux propositions singulières conservent le même locator sans perdre une condition

  Scénario: Refus — CA-FIL-2-03
    Étant donné la source demande une réponse rapide sans borne définie
    Quand l'IA suggère un délai numérique
    Alors le délai reste une proposition non adoptée et l'ambiguïté est adressée au décideur
```

## Oracle indépendant

Texte source et décisions externes au code futur, relus par un ingénieur ; un test ne déduit jamais l'attendu de la sortie à tester. Une table ou des exemples suffisent pour discuter ; le dépôt conserve ses scénarios Gherkin.

## Réalisation et preuves

- [`FEAT-FIL-2`](../features/FEAT-FIL-2/FEATURE.md) — Feature candidate
- [`TASK-FIL-2-01`](../features/FEAT-FIL-2/tasks/TASK-FIL-2-01.md) — Conserver UID, texte, statut, version et locator ; relever chaque ambiguïté et chaque comportement distinct.
- [`TASK-FIL-2-02`](../features/FEAT-FIL-2/tasks/TASK-FIL-2-02.md) — Rédiger les règles candidates, cas nominaux/frontières/refus et oracles sans compléter les inconnues.
- [`TASK-FIL-2-03`](../features/FEAT-FIL-2/tasks/TASK-FIL-2-03.md) — Faire relire les propositions contre la source et enregistrer qui doit décider les règles non établies.

Aucune preuve d'acceptation de cette US n'est produite par son rendu. Les artefacts existants peuvent satisfaire un prérequis après revue ; aucune répétition de travaux déjà démontrés n'est imposée.

## Questions ouvertes

Voir [`AMB-20`](../../../governance/ambiguities.md#amb-20).
