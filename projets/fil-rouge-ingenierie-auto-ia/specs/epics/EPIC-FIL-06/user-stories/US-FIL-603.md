# US-FIL-603 — Attribuer les risques qui conditionnent la suite

`Référence — spécification candidate`

- **Projet parent :** [`PROJ-FIL-AUTO-IA-001`](../../../../SPEC.md)
- **Epic parente :** [`EPIC-FIL-06`](../EPIC.md)
- **Feature fille :** [`FEAT-FIL-603`](../features/FEAT-FIL-603/FEATURE.md)
- **Jour :** `J08`
- **Sources de formation :** [`C08`](../../../baseline/sources.md#c08) — `J08` / Quatre verdicts, risques gouvernés, preuves bornées et coût complet / `programme_prevu`<br>[`C08-G7`](../../../baseline/sources.md#c08-g7) — `J08` / Fiche d'une page, trois risques, arrêt/repli testé, ROI et date de révision ; G7 / `programme_prevu`
- **Relation pédagogique :** Trois risques déterminants avec responsable, signal et action ; autres risques non effacés.
- **Niveau :** `Socle formation`
- **Priorité :** `P1`
- **Statut documentaire :** `Candidate`
- **Statut de preuve :** `Candidat`
- **Travail :** `À faire`
- **Responsable :** responsable du pilote — personne à désigner
- **Dépendances :** [`US-FIL-401`](../../EPIC-FIL-04/user-stories/US-FIL-401.md), [`US-FIL-503`](../../EPIC-FIL-05/user-stories/US-FIL-503.md)
- **Ambiguïté :** [`AMB-18`](../../../governance/ambiguities.md#amb-18)

## Besoin

> En tant que responsable du pilote, je veux nommer responsable, signal et action pour les risques clés afin de transformer des réserves vagues en conditions d'arrêt observables.

## Périmètre

Gouvernance du pilote déclaré ; pas de certification ni de cotation de probabilité inventée.

Les décisions restent humaines ; aucune implémentation métier n'est réalisée par cette spécification.

## Entrées et sorties

- **Entrée :** Échecs observés, risques résiduels et périmètre du pilote ; responsables nominatifs à désigner humainement.
- **Sortie :** Proposition de registre avec trois risques clés pour la fiche J08, chacun doté d'un responsable, signal, action et lien à l'arrêt.

Les baselines sont référencées dans [`sources.md`](../../../baseline/sources.md) ; leur révision est inconnue lorsqu'elle n'y est pas explicitement donnée. La sortie ne constitue pas, à elle seule, une preuve.

## Règle et critères

<a id="rm-fil-603"></a>
`RM-FIL-603` — Un risque sans responsable nommé, signal observable ou action n'est pas déclaré gouverné.

<a id="ca-fil-603-01"></a>
- [ ] `CA-FIL-603-01` — Étant donné un risque de réponse non sourcée a un responsable et un signal testable, quand le registre est revu, alors l'action et sa relation à la condition d'arrêt sont explicites.
<a id="ca-fil-603-02"></a>
- [ ] `CA-FIL-603-02` — Étant donné plus de trois risques sont recensés, quand la fiche d'une page est préparée, alors trois risques déterminants sont mis en avant et les autres restent accessibles en annexe.
<a id="ca-fil-603-03"></a>
- [ ] `CA-FIL-603-03` — Étant donné le responsable est encore à désigner, quand la gouvernance est évaluée, alors le risque reste à compléter et aucune attribution fictive n'est créée.

## Example Mapping

| Cas | Étant donné | Quand | Alors |
|---|---|---|---|
| Nominal | un risque de réponse non sourcée a un responsable et un signal testable | le registre est revu | l'action et sa relation à la condition d'arrêt sont explicites |
| Frontière | plus de trois risques sont recensés | la fiche d'une page est préparée | trois risques déterminants sont mis en avant et les autres restent accessibles en annexe |
| Refus | le responsable est encore à désigner | la gouvernance est évaluée | le risque reste à compléter et aucune attribution fictive n'est créée |

## Scénarios Gherkin

```gherkin
Fonctionnalité: Attribuer les risques qui conditionnent la suite
  Contexte:
    Étant donné le périmètre et les entrées versionnées de US-FIL-603
    Et les attendus ci-dessous définis avant la future réalisation

  Scénario: Nominal — CA-FIL-603-01
    Étant donné un risque de réponse non sourcée a un responsable et un signal testable
    Quand le registre est revu
    Alors l'action et sa relation à la condition d'arrêt sont explicites

  Scénario: Frontière — CA-FIL-603-02
    Étant donné plus de trois risques sont recensés
    Quand la fiche d'une page est préparée
    Alors trois risques déterminants sont mis en avant et les autres restent accessibles en annexe

  Scénario: Refus — CA-FIL-603-03
    Étant donné le responsable est encore à désigner
    Quand la gouvernance est évaluée
    Alors le risque reste à compléter et aucune attribution fictive n'est créée
```

## Oracle indépendant

Relecture des champs du registre et exercice du signal sur fixture ; présence d'un rôle générique ne vaut pas acceptation d'une personne responsable.

## Réalisation et preuves

- [`FEAT-FIL-603`](../features/FEAT-FIL-603/FEATURE.md) — Feature candidate
- [`TASK-FIL-603-01`](../features/FEAT-FIL-603/tasks/TASK-FIL-603-01.md) — Relier les risques aux observations et proposer les trois risques déterminants sans supprimer les réserves restantes.
- [`TASK-FIL-603-02`](../features/FEAT-FIL-603/tasks/TASK-FIL-603-02.md) — Faire nommer les responsables et rédiger signaux/actions/arrêts avec leurs modalités de vérification.
- [`TASK-FIL-603-03`](../features/FEAT-FIL-603/tasks/TASK-FIL-603-03.md) — Éprouver les signaux sur fixtures et faire accepter les responsabilités avant la fiche finale.

Aucune preuve d'acceptation de cette US n'est produite par son rendu. Les artefacts existants peuvent satisfaire un prérequis après revue ; aucune répétition de travaux déjà démontrés n'est imposée.

## Questions ouvertes

Voir [`AMB-18`](../../../governance/ambiguities.md#amb-18).
