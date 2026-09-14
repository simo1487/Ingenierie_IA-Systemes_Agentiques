# US-FIL-204 — Prouver l'effacement logique d'une mémoire

`Référence — spécification candidate`

- **Projet parent :** [`PROJ-FIL-AUTO-IA-001`](../../../../SPEC.md)
- **Epic parente :** [`EPIC-FIL-02`](../EPIC.md)
- **Feature fille :** [`FEAT-FIL-204`](../features/FEAT-FIL-204/FEATURE.md)
- **Jour :** `J06`
- **Sources de formation :** [`C04-RETOUR`](../../../baseline/sources.md#c04-retour) — `J04` / Requête directe avant modèle, questions attendues, empreintes, doublons et retrait des sources / `retour_rapporte`<br>[`C06`](../../../baseline/sources.md#c06) — `J06` / Comparaison d'organisations, rôles, reprise, idempotence, mémoire et trace / `programme_prevu`
- **Relation pédagogique :** Extension de révocation et invalidation, sans revendiquer l'effacement des sauvegardes.
- **Niveau :** `Extension production`
- **Priorité :** `P2`
- **Statut documentaire :** `Candidate`
- **Statut de preuve :** `Candidat`
- **Travail :** `À faire`
- **Responsable :** responsable des données — personne à désigner
- **Dépendances :** [`US-FIL-203`](US-FIL-203.md)
- **Ambiguïté :** [`AMB-07`](../../../governance/ambiguities.md#amb-07)

## Besoin

> En tant que responsable des données, je veux révoquer la réutilisation d'une entrée afin d’appliquer une politique de rétention sans détruire les preuves d'audit.

## Périmètre

Révocation locale sur données fictives ; suppression réelle et rétention légale exclues sans confirmation dédiée.

Les décisions restent humaines ; aucune implémentation métier n'est réalisée par cette spécification.

## Entrées et sorties

- **Entrée :** Demande autorisée visant une entrée et une politique de rétention approuvée ; copies de test uniquement.
- **Sortie :** Observation de révocation et reçu minimal sans contenu effacé ; limites sur sauvegardes explicitement déclarées.

Les baselines sont référencées dans [`sources.md`](../../../baseline/sources.md) ; leur révision est inconnue lorsqu'elle n'y est pas explicitement donnée. La sortie ne constitue pas, à elle seule, une preuve.

## Règle et critères

<a id="rm-fil-204"></a>
`RM-FIL-204` — Une entrée révoquée ne peut plus alimenter de nouveau contexte, même si elle était présente dans un cache.

<a id="ca-fil-204-01"></a>
- [ ] `CA-FIL-204-01` — Étant donné M1 est active et sa révocation est autorisée, quand la révocation est enregistrée, alors une nouvelle recherche n'injecte plus M1.
<a id="ca-fil-204-02"></a>
- [ ] `CA-FIL-204-02` — Étant donné la même révocation est rejouée, quand le système la traite, alors M1 reste révoquée sans nouvel effet métier.
<a id="ca-fil-204-03"></a>
- [ ] `CA-FIL-204-03` — Étant donné la demande provient d'un rôle non autorisé, quand la révocation est sollicitée, alors l'accès est refusé et aucune entrée n'est modifiée.

## Example Mapping

| Cas | Étant donné | Quand | Alors |
|---|---|---|---|
| Nominal | M1 est active et sa révocation est autorisée | la révocation est enregistrée | une nouvelle recherche n'injecte plus M1 |
| Frontière | la même révocation est rejouée | le système la traite | M1 reste révoquée sans nouvel effet métier |
| Refus | la demande provient d'un rôle non autorisé | la révocation est sollicitée | l'accès est refusé et aucune entrée n'est modifiée |

## Scénarios Gherkin

```gherkin
Fonctionnalité: Prouver l'effacement logique d'une mémoire
  Contexte:
    Étant donné le périmètre et les entrées versionnées de US-FIL-204
    Et les attendus ci-dessous définis avant la future réalisation

  Scénario: Nominal — CA-FIL-204-01
    Étant donné M1 est active et sa révocation est autorisée
    Quand la révocation est enregistrée
    Alors une nouvelle recherche n'injecte plus M1

  Scénario: Frontière — CA-FIL-204-02
    Étant donné la même révocation est rejouée
    Quand le système la traite
    Alors M1 reste révoquée sans nouvel effet métier

  Scénario: Refus — CA-FIL-204-03
    Étant donné la demande provient d'un rôle non autorisé
    Quand la révocation est sollicitée
    Alors l'accès est refusé et aucune entrée n'est modifiée
```

## Oracle indépendant

Lecture via tous les chemins de cache déclarés sur fixtures ; reçu comparé à l'identité de la demande. L'effacement physique des sauvegardes n'est pas affirmé sans preuve spécifique.

## Réalisation et preuves

- [`FEAT-FIL-204`](../features/FEAT-FIL-204/FEATURE.md) — Feature candidate
- [`TASK-FIL-204-01`](../features/FEAT-FIL-204/tasks/TASK-FIL-204-01.md) — Recenser les copies/cache et définir la portée du reçu ainsi que l'autorité de révocation.
- [`TASK-FIL-204-02`](../features/FEAT-FIL-204/tasks/TASK-FIL-204-02.md) — Concevoir l'invalidation de lecture et de cache avec reçu minimal, sans purger les preuves de run.
- [`TASK-FIL-204-03`](../features/FEAT-FIL-204/tasks/TASK-FIL-204-03.md) — Vérifier la non-réutilisation et l'idempotence sur fixtures puis documenter les limites de sauvegarde.

Aucune preuve d'acceptation de cette US n'est produite par son rendu. Les artefacts existants peuvent satisfaire un prérequis après revue ; aucune répétition de travaux déjà démontrés n'est imposée.

## Questions ouvertes

Voir [`AMB-07`](../../../governance/ambiguities.md#amb-07).
