# US-FIL-301 — Autoriser une consultation avant tout accès

`Référence — spécification candidate`

- **Projet parent :** [`PROJ-FIL-AUTO-IA-001`](../../../../SPEC.md)
- **Epic parente :** [`EPIC-FIL-03`](../EPIC.md)
- **Feature fille :** [`FEAT-FIL-301`](../features/FEAT-FIL-301/FEATURE.md)
- **Jour :** `J07`
- **Sources de formation :** [`C05-SKILL`](../../../baseline/sources.md#c05-skill) — `J05` / Méthode capitalisée, outils/événements versionnés, limites des démonstrations LlamaIndex / `support_actuel`<br>[`C07-G6`](../../../baseline/sources.md#c07-g6) — `J07` / Outil préparé ou replay, refus avant accès, régression et première divergence ; G6 / `programme_prevu`
- **Relation pédagogique :** Contrat d'outil J05 éprouvé par autorisation et refus technique J07.
- **Niveau :** `Socle formation`
- **Priorité :** `P1`
- **Statut documentaire :** `Candidate`
- **Statut de preuve :** `Candidat`
- **Travail :** `À faire`
- **Responsable :** responsable sécurité — personne à désigner
- **Dépendances :** [`US-FIL-6`](../../EPIC-FIL-00/user-stories/US-FIL-6.md), [`US-FIL-101`](../../EPIC-FIL-01/user-stories/US-FIL-101.md), [`US-FIL-102`](../../EPIC-FIL-01/user-stories/US-FIL-102.md)
- **Ambiguïté :** [`AMB-08`](../../../governance/ambiguities.md#amb-08)

## Besoin

> En tant que responsable sécurité, je veux contrôler chaque appel de lecture par une politique locale afin de prouver la frontière plutôt qu'un refus verbal du modèle.

## Périmètre

Consultation d'une ressource fictive ; pas de SQL libre, shell, URL libre ni écriture sur sources.

Les décisions restent humaines ; aucune implémentation métier n'est réalisée par cette spécification.

## Entrées et sorties

- **Entrée :** Identité issue du contexte de confiance, outil read-only nommé, arguments typés par identifiants et périmètre autorisé versionné.
- **Sortie :** Observation autorisé/refusé avec règle, raison et ordre des événements ; résultat uniquement après autorisation.

Les baselines sont référencées dans [`sources.md`](../../../baseline/sources.md) ; leur révision est inconnue lorsqu'elle n'y est pas explicitement donnée. La sortie ne constitue pas, à elle seule, une preuve.

## Règle et critères

<a id="rm-fil-301"></a>
`RM-FIL-301` — Toute lecture non explicitement autorisée est refusée avant l'accès à la ressource.

<a id="ca-fil-301-01"></a>
- [ ] `CA-FIL-301-01` — Étant donné l'identité I1 a le droit de consulter B1, quand I1 demande le passage P1 de B1, alors la décision d'autorisation précède l'accès et P1 est retourné.
<a id="ca-fil-301-02"></a>
- [ ] `CA-FIL-301-02` — Étant donné I1 est connue mais B2 est hors périmètre, quand I1 demande un passage de B2, alors un refus motivé est tracé et le lecteur n'est jamais appelé.
<a id="ca-fil-301-03"></a>
- [ ] `CA-FIL-301-03` — Étant donné l'identité est inconnue ou l'argument est un chemin au lieu d'un identifiant, quand l'appel est reçu, alors le validateur ou la politique refuse avant tout accès.

## Example Mapping

| Cas | Étant donné | Quand | Alors |
|---|---|---|---|
| Nominal | l'identité I1 a le droit de consulter B1 | I1 demande le passage P1 de B1 | la décision d'autorisation précède l'accès et P1 est retourné |
| Frontière | I1 est connue mais B2 est hors périmètre | I1 demande un passage de B2 | un refus motivé est tracé et le lecteur n'est jamais appelé |
| Refus | l'identité est inconnue ou l'argument est un chemin au lieu d'un identifiant | l'appel est reçu | le validateur ou la politique refuse avant tout accès |

Table de décision candidate : [`RM-FIL-301`](../../../governance/decision-tables.md#lecture-doutil-rm-fil-301).

## Scénarios Gherkin

```gherkin
Fonctionnalité: Autoriser une consultation avant tout accès
  Contexte:
    Étant donné le périmètre et les entrées versionnées de US-FIL-301
    Et les attendus ci-dessous définis avant la future réalisation

  Scénario: Nominal — CA-FIL-301-01
    Étant donné l'identité I1 a le droit de consulter B1
    Quand I1 demande le passage P1 de B1
    Alors la décision d'autorisation précède l'accès et P1 est retourné

  Scénario: Frontière — CA-FIL-301-02
    Étant donné I1 est connue mais B2 est hors périmètre
    Quand I1 demande un passage de B2
    Alors un refus motivé est tracé et le lecteur n'est jamais appelé

  Scénario: Refus — CA-FIL-301-03
    Étant donné l'identité est inconnue ou l'argument est un chemin au lieu d'un identifiant
    Quand l'appel est reçu
    Alors le validateur ou la politique refuse avant tout accès
```

## Oracle indépendant

Matrice identité/périmètre/arguments figée par le responsable ; lecteur espion indépendant ; journal établissant décision avant accès. Aucun rôle fourni par le modèle ne vaut identité authentifiée.

## Réalisation et preuves

- [`FEAT-FIL-301`](../features/FEAT-FIL-301/FEATURE.md) — Feature candidate
- [`TASK-FIL-301-01`](../features/FEAT-FIL-301/tasks/TASK-FIL-301-01.md) — Définir la fiche de l'outil consulter_passage, les arguments et la table exhaustive d'autorisation.
- [`TASK-FIL-301-02`](../features/FEAT-FIL-301/tasks/TASK-FIL-301-02.md) — Placer validation et politique avant le lecteur local ; utiliser un outil préparé ou replay pour J07.
- [`TASK-FIL-301-03`](../features/FEAT-FIL-301/tasks/TASK-FIL-301-03.md) — Produire un appel autorisé et un refus hors portée avec compteur d'accès, puis retirer le garde en environnement de test pour éprouver l'oracle.

Aucune preuve d'acceptation de cette US n'est produite par son rendu. Les artefacts existants peuvent satisfaire un prérequis après revue ; aucune répétition de travaux déjà démontrés n'est imposée.

## Questions ouvertes

Voir [`AMB-08`](../../../governance/ambiguities.md#amb-08).
