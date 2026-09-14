# US-FIL-6 — Capitaliser un contrat d'outil et de workflow

`Référence — spécification candidate`

- **Projet parent :** [`PROJ-FIL-AUTO-IA-001`](../../../../SPEC.md)
- **Epic parente :** [`EPIC-FIL-00`](../EPIC.md)
- **Feature fille :** [`FEAT-FIL-6`](../features/FEAT-FIL-6/FEATURE.md)
- **Jour :** `J01–J05`
- **Sources de formation :** [`C05`](../../../baseline/sources.md#c05) — `J05` / Besoin avant framework, règle/recherche/workflow/agent et valeur observable / `support_actuel`<br>[`C05-SKILL`](../../../baseline/sources.md#c05-skill) — `J05` / Méthode capitalisée, outils/événements versionnés, limites des démonstrations LlamaIndex / `support_actuel`<br>[`N05`](../../../baseline/sources.md#n05) — `J05` / Approches simples, types, budgets, contrôle humain et structuration ; propos à confirmer / `synthese_automatique`
- **Relation pédagogique :** Prérequis : méthode, types, états et outil étroit réutilisables avant orchestration avancée.
- **Niveau :** `Socle formation`
- **Priorité :** `P1`
- **Statut documentaire :** `Candidate`
- **Statut de preuve :** `Candidat`
- **Travail :** `À faire`
- **Responsable :** intégrateur — personne à désigner
- **Dépendances :** [`US-FIL-1`](US-FIL-1.md), [`US-FIL-2`](US-FIL-2.md), [`US-FIL-4`](US-FIL-4.md)
- **Ambiguïté :** [`AMB-24`](../../../governance/ambiguities.md#amb-24)

## Besoin

> En tant qu’intégrateur, je veux réutiliser une capacité étroite avec des échanges et arrêts documentés afin de préparer J06 sans dépendre d'une conversation implicite.

## Périmètre

Capitalisation J05 et interface vers J06 ; ne pas installer un framework ou créer une configuration d'agent dans ce lot documentaire.

Les décisions restent humaines ; aucune implémentation métier n'est réalisée par cette spécification.

## Entrées et sorties

- **Entrée :** Besoin approuvé pour l'exercice, outil de consultation identifié, types d'arguments/résultats, sources admises, permissions, budget et états de succès/échec/revue.
- **Sortie :** Proposition de fiche d'outil et méthode réutilisable versionnées, avec transitions, repli et points de décision humaine ; aucun droit ajouté par la description.

Les baselines sont référencées dans [`sources.md`](../../../baseline/sources.md) ; leur révision est inconnue lorsqu'elle n'y est pas explicitement donnée. La sortie ne constitue pas, à elle seule, une preuve.

## Règle et critères

<a id="rm-fil-6"></a>
`RM-FIL-6` — La description de l'outil ou la méthode réutilisable ne peut autoriser une action que l'application interdit.

<a id="ca-fil-6-01"></a>
- [ ] `CA-FIL-6-01` — Étant donné un outil étroit reçoit un identifiant valide autorisé, quand un tiers applique la méthode versionnée, alors il retrouve entrée, résultat attendu, états et conditions d'arrêt sans conversation supplémentaire.
<a id="ca-fil-6-02"></a>
- [ ] `CA-FIL-6-02` — Étant donné la consultation ne trouve pas de résultat, quand le workflow suit son contrat, alors il produit un manque ou une revue requise sans boucle ouverte.
<a id="ca-fil-6-03"></a>
- [ ] `CA-FIL-6-03` — Étant donné la description de l'outil demande un accès plus large que sa politique, quand le contrat est examiné, alors le désaccord est bloquant et aucune autorité supplémentaire n'est accordée.

## Example Mapping

| Cas | Étant donné | Quand | Alors |
|---|---|---|---|
| Nominal | un outil étroit reçoit un identifiant valide autorisé | un tiers applique la méthode versionnée | il retrouve entrée, résultat attendu, états et conditions d'arrêt sans conversation supplémentaire |
| Frontière | la consultation ne trouve pas de résultat | le workflow suit son contrat | il produit un manque ou une revue requise sans boucle ouverte |
| Refus | la description de l'outil demande un accès plus large que sa politique | le contrat est examiné | le désaccord est bloquant et aucune autorité supplémentaire n'est accordée |

## Scénarios Gherkin

```gherkin
Fonctionnalité: Capitaliser un contrat d'outil et de workflow
  Contexte:
    Étant donné le périmètre et les entrées versionnées de US-FIL-6
    Et les attendus ci-dessous définis avant la future réalisation

  Scénario: Nominal — CA-FIL-6-01
    Étant donné un outil étroit reçoit un identifiant valide autorisé
    Quand un tiers applique la méthode versionnée
    Alors il retrouve entrée, résultat attendu, états et conditions d'arrêt sans conversation supplémentaire

  Scénario: Frontière — CA-FIL-6-02
    Étant donné la consultation ne trouve pas de résultat
    Quand le workflow suit son contrat
    Alors il produit un manque ou une revue requise sans boucle ouverte

  Scénario: Refus — CA-FIL-6-03
    Étant donné la description de l'outil demande un accès plus large que sa politique
    Quand le contrat est examiné
    Alors le désaccord est bloquant et aucune autorité supplémentaire n'est accordée
```

## Oracle indépendant

Fiche approuvée, types et transitions relus par un pair ; la description FunctionTool et les événements Workflow sont des mécanismes pédagogiques, pas une preuve d'autorisation. SKILL.md n'est pas une API universelle de LlamaIndex.

## Réalisation et preuves

- [`FEAT-FIL-6`](../features/FEAT-FIL-6/FEATURE.md) — Feature candidate
- [`TASK-FIL-6-01`](../features/FEAT-FIL-6/tasks/TASK-FIL-6-01.md) — Décrire l'outil étroit, les types et erreurs ainsi que les états/transitions nécessaires au cas retenu.
- [`TASK-FIL-6-02`](../features/FEAT-FIL-6/tasks/TASK-FIL-6-02.md) — Capitaliser la méthode avec versions des instructions, outils et corpus, y compris le repli et la validation humaine.
- [`TASK-FIL-6-03`](../features/FEAT-FIL-6/tasks/TASK-FIL-6-03.md) — Faire appliquer la méthode par un tiers sur un exemple autorisé et relier les lacunes aux futurs contrôles J06/J07.

Aucune preuve d'acceptation de cette US n'est produite par son rendu. Les artefacts existants peuvent satisfaire un prérequis après revue ; aucune répétition de travaux déjà démontrés n'est imposée.

## Questions ouvertes

Voir [`AMB-24`](../../../governance/ambiguities.md#amb-24).
