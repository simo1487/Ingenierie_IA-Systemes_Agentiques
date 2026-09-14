# US-FIL-405 — Rendre le classement OSS explicable

`Référence — spécification candidate`

- **Projet parent :** [`PROJ-FIL-AUTO-IA-001`](../../../../SPEC.md)
- **Epic parente :** [`EPIC-FIL-04`](../EPIC.md)
- **Feature fille :** [`FEAT-FIL-405`](../features/FEAT-FIL-405/FEATURE.md)
- **Jour :** `J07`
- **Sources de formation :** [`C04`](../../../baseline/sources.md#c04) — `J04` / Corpus autorisé, découpage du sens, lexical/sémantique, Hit@k/MRR et support des citations / `support_actuel`<br>[`C08`](../../../baseline/sources.md#c08) — `J08` / Quatre verdicts, risques gouvernés, preuves bornées et coût complet / `programme_prevu`
- **Relation pédagogique :** Extension produit : score et données absentes ne remplacent pas la décision.
- **Niveau :** `Extension production`
- **Priorité :** `P2`
- **Statut documentaire :** `Candidate`
- **Statut de preuve :** `Candidat`
- **Travail :** `À faire`
- **Responsable :** responsable produit — personne à désigner
- **Dépendances :** [`US-FIL-101`](../../EPIC-FIL-01/user-stories/US-FIL-101.md), [`US-FIL-104`](../../EPIC-FIL-01/user-stories/US-FIL-104.md), [`US-FIL-401`](US-FIL-401.md)
- **Ambiguïté :** [`AMB-13`](../../../governance/ambiguities.md#amb-13)

## Besoin

> En tant que responsable produit, je veux relier chaque note à une grille approuvée et à des observations afin de sélectionner un candidat sans prendre le score de démonstration pour une preuve.

## Périmètre

Fiches autorisées en lecture seule ; recherche web, clonage/exécution et décision de licence automatiques exclus.

Les décisions restent humaines ; aucune implémentation métier n'est réalisée par cette spécification.

## Entrées et sorties

- **Entrée :** Fiches candidates révisées, licences, exigences/tests/qualité référencés ; grille et politique des données manquantes approuvées.
- **Sortie :** Proposition de classement détaillé par critère, inconnues conservées et décision humaine séparée.

Les baselines sont référencées dans [`sources.md`](../../../baseline/sources.md) ; leur révision est inconnue lorsqu'elle n'y est pas explicitement donnée. La sortie ne constitue pas, à elle seule, une preuve.

## Règle et critères

<a id="rm-fil-405"></a>
`RM-FIL-405` — Une note sans observation source ou hors grille approuvée n'est pas admissible dans un classement réel.

<a id="ca-fil-405-01"></a>
- [ ] `CA-FIL-405-01` — Étant donné deux fiches ont les observations exigées par la même grille, quand le classement est préparé, alors chaque contribution au score est reliée à une source et à la version de grille.
<a id="ca-fil-405-02"></a>
- [ ] `CA-FIL-405-02` — Étant donné les candidats obtiennent le même résultat, quand le classement est affiché, alors l'égalité reste visible sans sélection automatique.
<a id="ca-fil-405-03"></a>
- [ ] `CA-FIL-405-03` — Étant donné une licence ou une observation indispensable manque, quand le classement réel est demandé, alors l'inconnue reste visible et aucune valeur favorable n'est inventée.

## Example Mapping

| Cas | Étant donné | Quand | Alors |
|---|---|---|---|
| Nominal | deux fiches ont les observations exigées par la même grille | le classement est préparé | chaque contribution au score est reliée à une source et à la version de grille |
| Frontière | les candidats obtiennent le même résultat | le classement est affiché | l'égalité reste visible sans sélection automatique |
| Refus | une licence ou une observation indispensable manque | le classement réel est demandé | l'inconnue reste visible et aucune valeur favorable n'est inventée |

## Scénarios Gherkin

```gherkin
Fonctionnalité: Rendre le classement OSS explicable
  Contexte:
    Étant donné le périmètre et les entrées versionnées de US-FIL-405
    Et les attendus ci-dessous définis avant la future réalisation

  Scénario: Nominal — CA-FIL-405-01
    Étant donné deux fiches ont les observations exigées par la même grille
    Quand le classement est préparé
    Alors chaque contribution au score est reliée à une source et à la version de grille

  Scénario: Frontière — CA-FIL-405-02
    Étant donné les candidats obtiennent le même résultat
    Quand le classement est affiché
    Alors l'égalité reste visible sans sélection automatique

  Scénario: Refus — CA-FIL-405-03
    Étant donné une licence ou une observation indispensable manque
    Quand le classement réel est demandé
    Alors l'inconnue reste visible et aucune valeur favorable n'est inventée
```

## Oracle indépendant

MES-04 ; grille revue avant calcul et contre-calcul indépendant sur données figées ; aucune pondération réelle fixée ici.

## Réalisation et preuves

- [`FEAT-FIL-405`](../features/FEAT-FIL-405/FEATURE.md) — Feature candidate
- [`TASK-FIL-405-01`](../features/FEAT-FIL-405/tasks/TASK-FIL-405-01.md) — Faire approuver la grille OSS et la politique des inconnues en distinguant le score fictif 0–10 du MVP.
- [`TASK-FIL-405-02`](../features/FEAT-FIL-405/tasks/TASK-FIL-405-02.md) — Prévoir un classement à contributions traçables et conserver égalités, données absentes et sources des fiches.
- [`TASK-FIL-405-03`](../features/FEAT-FIL-405/tasks/TASK-FIL-405-03.md) — Recalculer sur données figées selon MES-04, puis faire sélectionner explicitement dépôt et révision par le responsable produit.

Aucune preuve d'acceptation de cette US n'est produite par son rendu. Les artefacts existants peuvent satisfaire un prérequis après revue ; aucune répétition de travaux déjà démontrés n'est imposée.

## Questions ouvertes

Voir [`AMB-13`](../../../governance/ambiguities.md#amb-13).
