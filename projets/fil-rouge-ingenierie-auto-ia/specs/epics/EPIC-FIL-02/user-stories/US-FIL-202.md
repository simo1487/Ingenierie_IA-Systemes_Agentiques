# US-FIL-202 — Borner les reprises et les appels IA

`Référence — spécification candidate`

- **Projet parent :** [`PROJ-FIL-AUTO-IA-001`](../../../../SPEC.md)
- **Epic parente :** [`EPIC-FIL-02`](../EPIC.md)
- **Feature fille :** [`FEAT-FIL-202`](../features/FEAT-FIL-202/FEATURE.md)
- **Jour :** `J06`
- **Sources de formation :** [`N05`](../../../baseline/sources.md#n05) — `J05` / Approches simples, types, budgets, contrôle humain et structuration ; propos à confirmer / `synthese_automatique`<br>[`C06`](../../../baseline/sources.md#c06) — `J06` / Comparaison d'organisations, rôles, reprise, idempotence, mémoire et trace / `programme_prevu`
- **Relation pédagogique :** Budgets et reprise bornée ; valeurs réelles à décider, pas de quota recopié.
- **Niveau :** `Socle formation`
- **Priorité :** `P1`
- **Statut documentaire :** `Candidate`
- **Statut de preuve :** `Candidat`
- **Travail :** `À faire`
- **Responsable :** opérateur — personne à désigner
- **Dépendances :** [`US-FIL-102`](../../EPIC-FIL-01/user-stories/US-FIL-102.md)
- **Ambiguïté :** [`AMB-06`](../../../governance/ambiguities.md#amb-06)

## Besoin

> En tant qu’opérateur, je veux arrêter les essais lorsqu'un budget approuvé est atteint afin d’éviter une boucle de reprise sans progrès.

## Périmètre

Budgets d'essais et de temps ; tarifs et seuils de production restent des décisions humaines.

Les décisions restent humaines ; aucune implémentation métier n'est réalisée par cette spécification.

## Entrées et sorties

- **Entrée :** Politique datée avec nombre maximal d'essais, délai et plafond d'usage ; configuration fictive explicitement étiquetée pour les tests.
- **Sortie :** Observation d'arrêt avec raison et budget consommé ; reprise proposée uniquement avec entrée observable modifiée.

Les baselines sont référencées dans [`sources.md`](../../../baseline/sources.md) ; leur révision est inconnue lorsqu'elle n'y est pas explicitement donnée. La sortie ne constitue pas, à elle seule, une preuve.

## Règle et critères

<a id="rm-fil-202"></a>
`RM-FIL-202` — Aucun nouvel essai n'est lancé après épuisement du budget applicable ou sans modification de l'entrée justifiant la reprise.

<a id="ca-fil-202-01"></a>
- [ ] `CA-FIL-202-01` — Étant donné un premier essai échoue et une entrée corrigée arrive avant la limite, quand l'opérateur autorise la reprise, alors un essai supplémentaire est tracé dans le budget.
<a id="ca-fil-202-02"></a>
- [ ] `CA-FIL-202-02` — Étant donné le compteur atteint exactement la limite de la fixture, quand une reprise est demandée, alors aucun nouvel appel n'est lancé.
<a id="ca-fil-202-03"></a>
- [ ] `CA-FIL-202-03` — Étant donné l'entrée est inchangée ou la politique manque, quand une reprise automatique est proposée, alors la reprise est refusée avec motif visible.

## Example Mapping

| Cas | Étant donné | Quand | Alors |
|---|---|---|---|
| Nominal | un premier essai échoue et une entrée corrigée arrive avant la limite | l'opérateur autorise la reprise | un essai supplémentaire est tracé dans le budget |
| Frontière | le compteur atteint exactement la limite de la fixture | une reprise est demandée | aucun nouvel appel n'est lancé |
| Refus | l'entrée est inchangée ou la politique manque | une reprise automatique est proposée | la reprise est refusée avec motif visible |

## Scénarios Gherkin

```gherkin
Fonctionnalité: Borner les reprises et les appels IA
  Contexte:
    Étant donné le périmètre et les entrées versionnées de US-FIL-202
    Et les attendus ci-dessous définis avant la future réalisation

  Scénario: Nominal — CA-FIL-202-01
    Étant donné un premier essai échoue et une entrée corrigée arrive avant la limite
    Quand l'opérateur autorise la reprise
    Alors un essai supplémentaire est tracé dans le budget

  Scénario: Frontière — CA-FIL-202-02
    Étant donné le compteur atteint exactement la limite de la fixture
    Quand une reprise est demandée
    Alors aucun nouvel appel n'est lancé

  Scénario: Refus — CA-FIL-202-03
    Étant donné l'entrée est inchangée ou la politique manque
    Quand une reprise automatique est proposée
    Alors la reprise est refusée avec motif visible
```

## Oracle indépendant

Horloge factice et compteur externe d'appels, limites choisies comme données de test et non valeurs de production ; cas d'expiration en cours d'appel et d'annulation à spécifier avant implémentation.

## Réalisation et preuves

- [`FEAT-FIL-202`](../features/FEAT-FIL-202/FEATURE.md) — Feature candidate
- [`TASK-FIL-202-01`](../features/FEAT-FIL-202/tasks/TASK-FIL-202-01.md) — Définir la politique de budget et les attendus aux limites, en séparant essai initial et reprises.
- [`TASK-FIL-202-02`](../features/FEAT-FIL-202/tasks/TASK-FIL-202-02.md) — Prévoir les gardes de reprise et l'arrêt sur timeout autour des appels, avec événements de budget.
- [`TASK-FIL-202-03`](../features/FEAT-FIL-202/tasks/TASK-FIL-202-03.md) — Tester limites exactes, entrée inchangée et fournisseur lent avec horloge factice ; faire approuver les paramètres réels séparément.

Aucune preuve d'acceptation de cette US n'est produite par son rendu. Les artefacts existants peuvent satisfaire un prérequis après revue ; aucune répétition de travaux déjà démontrés n'est imposée.

## Questions ouvertes

Voir [`AMB-06`](../../../governance/ambiguities.md#amb-06).
