# US-FIL-501 — Identifier une livraison reproductible

`Référence — spécification candidate`

- **Projet parent :** [`PROJ-FIL-AUTO-IA-001`](../../../../SPEC.md)
- **Epic parente :** [`EPIC-FIL-05`](../EPIC.md)
- **Feature fille :** [`FEAT-FIL-501`](../features/FEAT-FIL-501/FEATURE.md)
- **Jour :** `J08`
- **Sources de formation :** [`C03`](../../../baseline/sources.md#c03) — `J03` / Reproduction, hypothèses concurrentes, rouge/vert comparable, mutation et documentation / `support_actuel`<br>[`C08`](../../../baseline/sources.md#c08) — `J08` / Quatre verdicts, risques gouvernés, preuves bornées et coût complet / `programme_prevu`
- **Relation pédagogique :** Extension livraison : provenance et reproductibilité des artefacts, pas déterminisme garanti d'un modèle.
- **Niveau :** `Extension production`
- **Priorité :** `P1`
- **Statut documentaire :** `Candidate`
- **Statut de preuve :** `Candidat`
- **Travail :** `À faire`
- **Responsable :** mainteneur — personne à désigner
- **Dépendances :** [`US-FIL-104`](../../EPIC-FIL-01/user-stories/US-FIL-104.md), [`US-FIL-201`](../../EPIC-FIL-02/user-stories/US-FIL-201.md), [`US-FIL-401`](../../EPIC-FIL-04/user-stories/US-FIL-401.md)
- **Ambiguïté :** [`AMB-14`](../../../governance/ambiguities.md#amb-14)

## Besoin

> En tant que mainteneur, je veux rassembler les versions et commandes nécessaires au rejeu afin de permettre à un tiers de reproduire le périmètre annoncé.

## Périmètre

Packaging et inventaire, pas de publication, déploiement ou push dans ce lot.

Les décisions restent humaines ; aucune implémentation métier n'est réalisée par cette spécification.

## Entrées et sorties

- **Entrée :** Révision de code, versions/configurations sans secret, corpus et jeu d'essai figés ; mode d'exécution déclaré.
- **Sortie :** Observation : manifeste de livraison avec empreintes et procédure de reproduction ; limites des modèles distants visibles.

Les baselines sont référencées dans [`sources.md`](../../../baseline/sources.md) ; leur révision est inconnue lorsqu'elle n'y est pas explicitement donnée. La sortie ne constitue pas, à elle seule, une preuve.

## Règle et critères

<a id="rm-fil-501"></a>
`RM-FIL-501` — Une livraison ne peut être dite reproductible sans identification des entrées, outils, configuration et mode effectivement utilisés.

<a id="ca-fil-501-01"></a>
- [ ] `CA-FIL-501-01` — Étant donné un tiers dispose du manifeste complet et du mode hors ligne, quand il rejoue le cas, alors les sorties sémantiques attendues concordent et les horodatages restent distincts.
<a id="ca-fil-501-02"></a>
- [ ] `CA-FIL-501-02` — Étant donné le fournisseur est un modèle distant non figé, quand le dossier décrit la reproduction, alors le rejeu des preuves est distingué d'une nouvelle génération non garantie identique.
<a id="ca-fil-501-03"></a>
- [ ] `CA-FIL-501-03` — Étant donné une empreinte d'entrée ne correspond pas au manifeste, quand le rejeu est préparé, alors la non-correspondance bloque la déclaration de reproduction.

## Example Mapping

| Cas | Étant donné | Quand | Alors |
|---|---|---|---|
| Nominal | un tiers dispose du manifeste complet et du mode hors ligne | il rejoue le cas | les sorties sémantiques attendues concordent et les horodatages restent distincts |
| Frontière | le fournisseur est un modèle distant non figé | le dossier décrit la reproduction | le rejeu des preuves est distingué d'une nouvelle génération non garantie identique |
| Refus | une empreinte d'entrée ne correspond pas au manifeste | le rejeu est préparé | la non-correspondance bloque la déclaration de reproduction |

## Scénarios Gherkin

```gherkin
Fonctionnalité: Identifier une livraison reproductible
  Contexte:
    Étant donné le périmètre et les entrées versionnées de US-FIL-501
    Et les attendus ci-dessous définis avant la future réalisation

  Scénario: Nominal — CA-FIL-501-01
    Étant donné un tiers dispose du manifeste complet et du mode hors ligne
    Quand il rejoue le cas
    Alors les sorties sémantiques attendues concordent et les horodatages restent distincts

  Scénario: Frontière — CA-FIL-501-02
    Étant donné le fournisseur est un modèle distant non figé
    Quand le dossier décrit la reproduction
    Alors le rejeu des preuves est distingué d'une nouvelle génération non garantie identique

  Scénario: Refus — CA-FIL-501-03
    Étant donné une empreinte d'entrée ne correspond pas au manifeste
    Quand le rejeu est préparé
    Alors la non-correspondance bloque la déclaration de reproduction
```

## Oracle indépendant

Artefacts attendus du cas approuvé, contrôlés hors du sérialiseur ; comparer explicitement champs métier et non generated_at. Le test CLI actuel ne prouve pas l'identité de deux runs.

## Réalisation et preuves

- [`FEAT-FIL-501`](../features/FEAT-FIL-501/FEATURE.md) — Feature candidate
- [`TASK-FIL-501-01`](../features/FEAT-FIL-501/tasks/TASK-FIL-501-01.md) — Définir le manifeste de livraison et les champs sémantiques comparables, avec modes et dépendances exactes.
- [`TASK-FIL-501-02`](../features/FEAT-FIL-501/tasks/TASK-FIL-501-02.md) — Préparer un paquet local et une procédure de rejeu sans secret, en excluant caches et bases vectorielles.
- [`TASK-FIL-501-03`](../features/FEAT-FIL-501/tasks/TASK-FIL-501-03.md) — Faire rejouer par un tiers et conserver les écarts, surtout modèle distant et versions manquantes.

Aucune preuve d'acceptation de cette US n'est produite par son rendu. Les artefacts existants peuvent satisfaire un prérequis après revue ; aucune répétition de travaux déjà démontrés n'est imposée.

## Questions ouvertes

Voir [`AMB-14`](../../../governance/ambiguities.md#amb-14).
