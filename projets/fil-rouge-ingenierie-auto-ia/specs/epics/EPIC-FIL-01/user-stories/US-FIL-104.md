# US-FIL-104 — Refuser les réponses fournisseur hors contrat

`Référence — spécification candidate`

- **Projet parent :** [`PROJ-FIL-AUTO-IA-001`](../../../../SPEC.md)
- **Epic parente :** [`EPIC-FIL-01`](../EPIC.md)
- **Feature fille :** [`FEAT-FIL-104`](../features/FEAT-FIL-104/FEATURE.md)
- **Jour :** `J06`
- **Sources de formation :** [`C05-SKILL`](../../../baseline/sources.md#c05-skill) — `J05` / Méthode capitalisée, outils/événements versionnés, limites des démonstrations LlamaIndex / `support_actuel`<br>[`N05`](../../../baseline/sources.md#n05) — `J05` / Approches simples, types, budgets, contrôle humain et structuration ; propos à confirmer / `synthese_automatique`
- **Relation pédagogique :** Extension de robustesse des contrats structurés des fournisseurs.
- **Niveau :** `Extension production`
- **Priorité :** `P1`
- **Statut documentaire :** `Candidate`
- **Statut de preuve :** `Candidat`
- **Travail :** `À faire`
- **Responsable :** ingénieur exigences — personne à désigner
- **Dépendances :** [`US-FIL-6`](../../EPIC-FIL-00/user-stories/US-FIL-6.md), [`US-FIL-101`](US-FIL-101.md), [`US-FIL-102`](US-FIL-102.md)
- **Ambiguïté :** [`AMB-04`](../../../governance/ambiguities.md#amb-04)

## Besoin

> En tant qu’ingénieur exigences, je veux recevoir uniquement des propositions structurellement valides afin d’éviter qu'une réponse JSON plausible casse ou trompe le workflow.

## Périmètre

Validation d'adaptateur et erreurs contrôlées ; aucun appel distant requis ni nouveau prompt rédigé dans ce lot.

Les décisions restent humaines ; aucune implémentation métier n'est réalisée par cette spécification.

## Entrées et sorties

- **Entrée :** Réponses des tâches requirement, project-ranking, quality-advice ; identifiants source ; schéma versionné et modèle déclaré.
- **Sortie :** Proposition validée structurellement ou erreur de contrat ; statut Vérifié interdit au fournisseur.

Les baselines sont référencées dans [`sources.md`](../../../baseline/sources.md) ; leur révision est inconnue lorsqu'elle n'y est pas explicitement donnée. La sortie ne constitue pas, à elle seule, une preuve.

## Règle et critères

<a id="rm-fil-104"></a>
`RM-FIL-104` — La présence des clés ne suffit pas : types, champs obligatoires, bornes et références doivent respecter le contrat approuvé de la tâche.

<a id="ca-fil-104-01"></a>
- [ ] `CA-FIL-104-01` — Étant donné une réponse requirement contient id, statement et rationale textuels non vides, quand le validateur la contrôle, alors une proposition est retournée avec références autorisées.
<a id="ca-fil-104-02"></a>
- [ ] `CA-FIL-104-02` — Étant donné un classement contient un score de 10 et max_score de 10 dans le contrat de démonstration, quand le validateur le contrôle, alors la borne est acceptée sans valider le choix produit.
<a id="ca-fil-104-03"></a>
- [ ] `CA-FIL-104-03` — Étant donné le score est une chaîne ou un identifiant de diagnostic n'existe pas dans l'entrée, quand le validateur contrôle la réponse, alors la réponse est refusée sans publier un résultat partiel comme valide.

## Example Mapping

| Cas | Étant donné | Quand | Alors |
|---|---|---|---|
| Nominal | une réponse requirement contient id, statement et rationale textuels non vides | le validateur la contrôle | une proposition est retournée avec références autorisées |
| Frontière | un classement contient un score de 10 et max_score de 10 dans le contrat de démonstration | le validateur le contrôle | la borne est acceptée sans valider le choix produit |
| Refus | le score est une chaîne ou un identifiant de diagnostic n'existe pas dans l'entrée | le validateur contrôle la réponse | la réponse est refusée sans publier un résultat partiel comme valide |

## Scénarios Gherkin

```gherkin
Fonctionnalité: Refuser les réponses fournisseur hors contrat
  Contexte:
    Étant donné le périmètre et les entrées versionnées de US-FIL-104
    Et les attendus ci-dessous définis avant la future réalisation

  Scénario: Nominal — CA-FIL-104-01
    Étant donné une réponse requirement contient id, statement et rationale textuels non vides
    Quand le validateur la contrôle
    Alors une proposition est retournée avec références autorisées

  Scénario: Frontière — CA-FIL-104-02
    Étant donné un classement contient un score de 10 et max_score de 10 dans le contrat de démonstration
    Quand le validateur le contrôle
    Alors la borne est acceptée sans valider le choix produit

  Scénario: Refus — CA-FIL-104-03
    Étant donné le score est une chaîne ou un identifiant de diagnostic n'existe pas dans l'entrée
    Quand le validateur contrôle la réponse
    Alors la réponse est refusée sans publier un résultat partiel comme valide
```

## Oracle indépendant

Réponses HTTP simulées avec attendus de types et références approuvés ; les bornes 0–10 décrivent le contrat de démonstration existant, non une grille OSS réelle. Vérifier séparément contenu valide, champs absents, booléen à la place d'entier et contenu non JSON.

## Réalisation et preuves

- [`FEAT-FIL-104`](../features/FEAT-FIL-104/FEATURE.md) — Feature candidate
- [`TASK-FIL-104-01`](../features/FEAT-FIL-104/tasks/TASK-FIL-104-01.md) — Figer les schémas de sortie, références permises et fixtures HTTP nominales et malformées sans secret réel.
- [`TASK-FIL-104-02`](../features/FEAT-FIL-104/tasks/TASK-FIL-104-02.md) — Renforcer le contrôle de MistralProvider et tester le même contrat autour du fournisseur déterministe.
- [`TASK-FIL-104-03`](../features/FEAT-FIL-104/tasks/TASK-FIL-104-03.md) — Simuler JSON invalide, champs manquants, types invalides et indisponibilité ; confirmer qu'aucun résultat invalide n'est promu.

Aucune preuve d'acceptation de cette US n'est produite par son rendu. Les artefacts existants peuvent satisfaire un prérequis après revue ; aucune répétition de travaux déjà démontrés n'est imposée.

## Questions ouvertes

Voir [`AMB-04`](../../../governance/ambiguities.md#amb-04).
