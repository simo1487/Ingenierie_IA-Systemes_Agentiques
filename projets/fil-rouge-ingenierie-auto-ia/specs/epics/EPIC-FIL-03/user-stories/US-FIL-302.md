# US-FIL-302 — Identifier la révision MCP de l'outil préparé

`Référence — spécification candidate`

- **Projet parent :** [`PROJ-FIL-AUTO-IA-001`](../../../../SPEC.md)
- **Epic parente :** [`EPIC-FIL-03`](../EPIC.md)
- **Feature fille :** [`FEAT-FIL-302`](../features/FEAT-FIL-302/FEATURE.md)
- **Jour :** `J07`
- **Sources de formation :** [`C07`](../../../baseline/sources.md#c07) — `J07` / Politique avant accès, révision pédagogique MCP 2026-07-28, contenu non fiable et cas indépendants / `programme_prevu`<br>[`C07-G6`](../../../baseline/sources.md#c07-g6) — `J07` / Outil préparé ou replay, refus avant accès, régression et première divergence ; G6 / `programme_prevu`
- **Relation pédagogique :** Inspection d'un outil préparé et révision pédagogique, compatibilité externe non présumée.
- **Niveau :** `Socle formation`
- **Priorité :** `P1`
- **Statut documentaire :** `Candidate`
- **Statut de preuve :** `Candidat`
- **Travail :** `À faire`
- **Responsable :** intégrateur — personne à désigner
- **Dépendances :** [`US-FIL-301`](US-FIL-301.md)
- **Ambiguïté :** [`AMB-09`](../../../governance/ambiguities.md#amb-09)

## Besoin

> En tant qu’intégrateur, je veux consigner la révision et les capacités réellement annoncées afin de ne pas mélanger des fixtures incompatibles.

## Périmètre

Inspection d'un outil préparé ; aucun développement de serveur ni choix de SDK exigé.

Les décisions restent humaines ; aucune implémentation métier n'est réalisée par cette spécification.

## Entrées et sorties

- **Entrée :** Contrat de l'outil préparé ou trace replay ; révision pédagogique MCP 2026-07-28 ; capacités annoncées et provenance de la fixture.
- **Sortie :** Observation de concordance ou incompatibilité signalée ; mode outil réel, fixture ou replay visible.

Les baselines sont référencées dans [`sources.md`](../../../baseline/sources.md) ; leur révision est inconnue lorsqu'elle n'y est pas explicitement donnée. La sortie ne constitue pas, à elle seule, une preuve.

## Règle et critères

<a id="rm-fil-302"></a>
`RM-FIL-302` — Une révision différente de celle du parcours ne peut pas être présentée comme compatible sans décision documentée.

<a id="ca-fil-302-01"></a>
- [ ] `CA-FIL-302-01` — Étant donné la fixture annonce 2026-07-28 et le mode replay, quand le groupe inspecte le contrat, alors révision et mode sont reportés sans revendiquer une exécution réseau réelle.
<a id="ca-fil-302-02"></a>
- [ ] `CA-FIL-302-02` — Étant donné l'outil annonce une autre révision, quand le groupe prépare les appels, alors la différence est consignée et les jeux ne sont pas mélangés.
<a id="ca-fil-302-03"></a>
- [ ] `CA-FIL-302-03` — Étant donné la révision ou la provenance est absente, quand le groupe évalue la compatibilité, alors la compatibilité reste Non vérifié et la lacune est remontée.

## Example Mapping

| Cas | Étant donné | Quand | Alors |
|---|---|---|---|
| Nominal | la fixture annonce 2026-07-28 et le mode replay | le groupe inspecte le contrat | révision et mode sont reportés sans revendiquer une exécution réseau réelle |
| Frontière | l'outil annonce une autre révision | le groupe prépare les appels | la différence est consignée et les jeux ne sont pas mélangés |
| Refus | la révision ou la provenance est absente | le groupe évalue la compatibilité | la compatibilité reste Non vérifié et la lacune est remontée |

## Scénarios Gherkin

```gherkin
Fonctionnalité: Identifier la révision MCP de l'outil préparé
  Contexte:
    Étant donné le périmètre et les entrées versionnées de US-FIL-302
    Et les attendus ci-dessous définis avant la future réalisation

  Scénario: Nominal — CA-FIL-302-01
    Étant donné la fixture annonce 2026-07-28 et le mode replay
    Quand le groupe inspecte le contrat
    Alors révision et mode sont reportés sans revendiquer une exécution réseau réelle

  Scénario: Frontière — CA-FIL-302-02
    Étant donné l'outil annonce une autre révision
    Quand le groupe prépare les appels
    Alors la différence est consignée et les jeux ne sont pas mélangés

  Scénario: Refus — CA-FIL-302-03
    Étant donné la révision ou la provenance est absente
    Quand le groupe évalue la compatibilité
    Alors la compatibilité reste Non vérifié et la lacune est remontée
```

## Oracle indépendant

Valeur épinglée dans le cours J07, lignes 58–64, comparée à la trace originale de l'outil ; ce contrat ne prétend pas vérifier la validité externe de cette révision MCP.

## Réalisation et preuves

- [`FEAT-FIL-302`](../features/FEAT-FIL-302/FEATURE.md) — Feature candidate
- [`TASK-FIL-302-01`](../features/FEAT-FIL-302/tasks/TASK-FIL-302-01.md) — Préparer la fiche de protocole avec révision pédagogique, capacités, erreurs et provenance des exemples.
- [`TASK-FIL-302-02`](../features/FEAT-FIL-302/tasks/TASK-FIL-302-02.md) — Inspecter l'outil préparé ou rejouer la fixture, en séparant révisions et modes dans les artefacts.
- [`TASK-FIL-302-03`](../features/FEAT-FIL-302/tasks/TASK-FIL-302-03.md) — Consigner toute révision inattendue et faire décider la compatibilité avant d'assembler les preuves G6.

Aucune preuve d'acceptation de cette US n'est produite par son rendu. Les artefacts existants peuvent satisfaire un prérequis après revue ; aucune répétition de travaux déjà démontrés n'est imposée.

## Questions ouvertes

Voir [`AMB-09`](../../../governance/ambiguities.md#amb-09).
