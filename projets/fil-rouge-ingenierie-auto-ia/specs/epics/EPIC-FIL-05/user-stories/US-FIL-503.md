# US-FIL-503 — Arrêter le pilote et revenir à la baseline

`Référence — spécification candidate`

- **Projet parent :** [`PROJ-FIL-AUTO-IA-001`](../../../../SPEC.md)
- **Epic parente :** [`EPIC-FIL-05`](../EPIC.md)
- **Feature fille :** [`FEAT-FIL-503`](../features/FEAT-FIL-503/FEATURE.md)
- **Jour :** `J08`
- **Sources de formation :** [`C06-G5`](../../../baseline/sources.md#c06-g5) — `J06` / Comparaison, journal complet, interruption et mémoire ; revue G5 / `programme_prevu`<br>[`C08-G7`](../../../baseline/sources.md#c08-g7) — `J08` / Fiche d'une page, trois risques, arrêt/repli testé, ROI et date de révision ; G7 / `programme_prevu`
- **Relation pédagogique :** Préparer et éprouver arrêt/repli avant le verdict de pilote.
- **Niveau :** `Socle formation`
- **Priorité :** `P1`
- **Statut documentaire :** `Candidate`
- **Statut de preuve :** `Candidat`
- **Travail :** `À faire`
- **Responsable :** responsable d'exploitation — personne à désigner
- **Dépendances :** [`US-FIL-201`](../../EPIC-FIL-02/user-stories/US-FIL-201.md), [`US-FIL-202`](../../EPIC-FIL-02/user-stories/US-FIL-202.md)
- **Ambiguïté :** [`AMB-15`](../../../governance/ambiguities.md#amb-15)

## Besoin

> En tant que responsable d'exploitation, je veux déclencher un arrêt prévu et un retour arrière contrôlé afin de rendre la décision de pilote réversible.

## Périmètre

Exercice sans effet sur un service réel ; tout déploiement/retour arrière réel exige une autorisation spécifique.

Les décisions restent humaines ; aucune implémentation métier n'est réalisée par cette spécification.

## Entrées et sorties

- **Entrée :** Baseline de repli identifiée, procédure approuvée, condition d'arrêt observable, responsable ; environnement local fictif.
- **Sortie :** Observation d'exercice d'arrêt et de retour arrière, limites sur runs en cours et décision de reprise humaine.

Les baselines sont référencées dans [`sources.md`](../../../baseline/sources.md) ; leur révision est inconnue lorsqu'elle n'y est pas explicitement donnée. La sortie ne constitue pas, à elle seule, une preuve.

## Règle et critères

<a id="rm-fil-503"></a>
`RM-FIL-503` — Le pilote ne peut être proposé sans condition d'arrêt et retour arrière nommés et testés sur le périmètre déclaré.

<a id="ca-fil-503-01"></a>
- [ ] `CA-FIL-503-01` — Étant donné le signal d'arrêt convenu est présent, quand le responsable applique la procédure sur le pilote fictif, alors les nouveaux runs s'arrêtent et la baseline de repli est identifiable.
<a id="ca-fil-503-02"></a>
- [ ] `CA-FIL-503-02` — Étant donné un run est en cours au déclenchement, quand l'arrêt est appliqué, alors son état et son traitement selon la procédure restent tracés sans double effet.
<a id="ca-fil-503-03"></a>
- [ ] `CA-FIL-503-03` — Étant donné la baseline de repli manque ou n'a jamais été éprouvée, quand un lancement de pilote est demandé, alors la proposition reste à corriger, sans simuler un retour arrière réussi.

## Example Mapping

| Cas | Étant donné | Quand | Alors |
|---|---|---|---|
| Nominal | le signal d'arrêt convenu est présent | le responsable applique la procédure sur le pilote fictif | les nouveaux runs s'arrêtent et la baseline de repli est identifiable |
| Frontière | un run est en cours au déclenchement | l'arrêt est appliqué | son état et son traitement selon la procédure restent tracés sans double effet |
| Refus | la baseline de repli manque ou n'a jamais été éprouvée | un lancement de pilote est demandé | la proposition reste à corriger, sans simuler un retour arrière réussi |

## Scénarios Gherkin

```gherkin
Fonctionnalité: Arrêter le pilote et revenir à la baseline
  Contexte:
    Étant donné le périmètre et les entrées versionnées de US-FIL-503
    Et les attendus ci-dessous définis avant la future réalisation

  Scénario: Nominal — CA-FIL-503-01
    Étant donné le signal d'arrêt convenu est présent
    Quand le responsable applique la procédure sur le pilote fictif
    Alors les nouveaux runs s'arrêtent et la baseline de repli est identifiable

  Scénario: Frontière — CA-FIL-503-02
    Étant donné un run est en cours au déclenchement
    Quand l'arrêt est appliqué
    Alors son état et son traitement selon la procédure restent tracés sans double effet

  Scénario: Refus — CA-FIL-503-03
    Étant donné la baseline de repli manque ou n'a jamais été éprouvée
    Quand un lancement de pilote est demandé
    Alors la proposition reste à corriger, sans simuler un retour arrière réussi
```

## Oracle indépendant

Procédure revue avant essai, compteur de nouveaux runs et identité de baseline de repli ; replay déclaré acceptable au socle mais ne prouve pas un déploiement réel.

## Réalisation et preuves

- [`FEAT-FIL-503`](../features/FEAT-FIL-503/FEATURE.md) — Feature candidate
- [`TASK-FIL-503-01`](../features/FEAT-FIL-503/tasks/TASK-FIL-503-01.md) — Nommer baseline de repli, responsable, signal et comportement attendu des runs en cours.
- [`TASK-FIL-503-02`](../features/FEAT-FIL-503/tasks/TASK-FIL-503-02.md) — Préparer un exercice d'arrêt/repli local ou un replay déclaré en conservant le journal et la décision.
- [`TASK-FIL-503-03`](../features/FEAT-FIL-503/tasks/TASK-FIL-503-03.md) — Faire constater l'arrêt des nouveaux runs et le repli par un tiers ; consigner les limites avant décision de pilote.

Aucune preuve d'acceptation de cette US n'est produite par son rendu. Les artefacts existants peuvent satisfaire un prérequis après revue ; aucune répétition de travaux déjà démontrés n'est imposée.

## Questions ouvertes

Voir [`AMB-15`](../../../governance/ambiguities.md#amb-15).
