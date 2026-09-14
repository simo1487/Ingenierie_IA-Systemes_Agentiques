# US-FIL-401 — Versionner des cas à attendu indépendant

`Référence — spécification candidate`

- **Projet parent :** [`PROJ-FIL-AUTO-IA-001`](../../../../SPEC.md)
- **Epic parente :** [`EPIC-FIL-04`](../EPIC.md)
- **Feature fille :** [`FEAT-FIL-401`](../features/FEAT-FIL-401/FEATURE.md)
- **Jour :** `J07`
- **Sources de formation :** [`C02`](../../../baseline/sources.md#c02) — `J02` / Exigence singulière, inconnues, exemples et oracle indépendant ; Gherkin non universellement obligatoire / `support_actuel`<br>[`C07`](../../../baseline/sources.md#c07) — `J07` / Politique avant accès, révision pédagogique MCP 2026-07-28, contenu non fiable et cas indépendants / `programme_prevu`
- **Relation pédagogique :** Attendus indépendants avant essai, classes hostiles et refus non compensable.
- **Niveau :** `Socle formation`
- **Priorité :** `P1`
- **Statut documentaire :** `Candidate`
- **Statut de preuve :** `Candidat`
- **Travail :** `À faire`
- **Responsable :** responsable évaluation — personne à désigner
- **Dépendances :** [`US-FIL-301`](../../EPIC-FIL-03/user-stories/US-FIL-301.md), [`US-FIL-302`](../../EPIC-FIL-03/user-stories/US-FIL-302.md), [`US-FIL-303`](../../EPIC-FIL-03/user-stories/US-FIL-303.md)
- **Ambiguïté :** [`AMB-11`](../../../governance/ambiguities.md#amb-11)

## Besoin

> En tant que responsable évaluation, je veux maintenir un jeu de cas pouvant contredire le workflow afin d’éviter une validation par simple plausibilité.

## Périmètre

Petit jeu pertinent, sans quota historique obligatoire ni seuil de succès inventé.

Les décisions restent humaines ; aucune implémentation métier n'est réalisée par cette spécification.

## Entrées et sorties

- **Entrée :** Cas nominaux, erreurs et contenus hostiles fictifs, identité, contexte, attendu, oracle, responsable et version du jeu.
- **Sortie :** Proposition de jeu revue humainement et observations par cas ; cas non exécutés ou non décidables visibles.

Les baselines sont référencées dans [`sources.md`](../../../baseline/sources.md) ; leur révision est inconnue lorsqu'elle n'y est pas explicitement donnée. La sortie ne constitue pas, à elle seule, une preuve.

## Règle et critères

<a id="rm-fil-401"></a>
`RM-FIL-401` — Aucun cas ne peut être compté comme réussi sans attendu décidable figé avant l'exécution et observation correspondante.

<a id="ca-fil-401-01"></a>
- [ ] `CA-FIL-401-01` — Étant donné C1 possède entrée, identité et attendu revus, quand son exécution satisfait l'oracle indépendant, alors C1 porte un résultat pass avec référence de preuve.
<a id="ca-fil-401-02"></a>
- [ ] `CA-FIL-401-02` — Étant donné aucun cas n'a été exécuté, quand le rapport est produit, alors le rapport indique non mesuré, pas un taux de réussite.
<a id="ca-fil-401-03"></a>
- [ ] `CA-FIL-401-03` — Étant donné l'attendu de C1 manque ou provient de la réponse du système, quand le jeu est préparé, alors C1 est bloqué pour revue et n'est pas compté comme réussi.

## Example Mapping

| Cas | Étant donné | Quand | Alors |
|---|---|---|---|
| Nominal | C1 possède entrée, identité et attendu revus | son exécution satisfait l'oracle indépendant | C1 porte un résultat pass avec référence de preuve |
| Frontière | aucun cas n'a été exécuté | le rapport est produit | le rapport indique non mesuré, pas un taux de réussite |
| Refus | l'attendu de C1 manque ou provient de la réponse du système | le jeu est préparé | C1 est bloqué pour revue et n'est pas compté comme réussi |

## Scénarios Gherkin

```gherkin
Fonctionnalité: Versionner des cas à attendu indépendant
  Contexte:
    Étant donné le périmètre et les entrées versionnées de US-FIL-401
    Et les attendus ci-dessous définis avant la future réalisation

  Scénario: Nominal — CA-FIL-401-01
    Étant donné C1 possède entrée, identité et attendu revus
    Quand son exécution satisfait l'oracle indépendant
    Alors C1 porte un résultat pass avec référence de preuve

  Scénario: Frontière — CA-FIL-401-02
    Étant donné aucun cas n'a été exécuté
    Quand le rapport est produit
    Alors le rapport indique non mesuré, pas un taux de réussite

  Scénario: Refus — CA-FIL-401-03
    Étant donné l'attendu de C1 manque ou provient de la réponse du système
    Quand le jeu est préparé
    Alors C1 est bloqué pour revue et n'est pas compté comme réussi
```

## Oracle indépendant

Contrat MES-02 dans governance/measurement-contracts.md ; les règles critiques restent binaires et non compensables.

## Réalisation et preuves

- [`FEAT-FIL-401`](../features/FEAT-FIL-401/FEATURE.md) — Feature candidate
- [`TASK-FIL-401-01`](../features/FEAT-FIL-401/tasks/TASK-FIL-401-01.md) — Écrire et faire approuver les cas selon MES-02, y compris identités inconnues et entrées invalides.
- [`TASK-FIL-401-02`](../features/FEAT-FIL-401/tasks/TASK-FIL-401-02.md) — Préparer le format de résultats pass/fail/not_run/undecidable avec liens vers observations et version du jeu.
- [`TASK-FIL-401-03`](../features/FEAT-FIL-401/tasks/TASK-FIL-401-03.md) — Revoir chaque attendu et vérifier qu'un cas non exécuté ou une violation critique ne disparaît pas dans un agrégat.

Aucune preuve d'acceptation de cette US n'est produite par son rendu. Les artefacts existants peuvent satisfaire un prérequis après revue ; aucune répétition de travaux déjà démontrés n'est imposée.

## Questions ouvertes

Voir [`AMB-11`](../../../governance/ambiguities.md#amb-11).
