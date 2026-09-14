# US-FIL-304 — Exposer le contrat via un adaptateur MCP réel

`Référence — spécification candidate`

- **Projet parent :** [`PROJ-FIL-AUTO-IA-001`](../../../../SPEC.md)
- **Epic parente :** [`EPIC-FIL-03`](../EPIC.md)
- **Feature fille :** [`FEAT-FIL-304`](../features/FEAT-FIL-304/FEATURE.md)
- **Jour :** `J07`
- **Sources de formation :** [`C05-SKILL`](../../../baseline/sources.md#c05-skill) — `J05` / Méthode capitalisée, outils/événements versionnés, limites des démonstrations LlamaIndex / `support_actuel`<br>[`C07`](../../../baseline/sources.md#c07) — `J07` / Politique avant accès, révision pédagogique MCP 2026-07-28, contenu non fiable et cas indépendants / `programme_prevu`
- **Relation pédagogique :** Extension de transport MCP réelle ; non exigée pour le socle J07.
- **Niveau :** `Extension production`
- **Priorité :** `P2`
- **Statut documentaire :** `Candidate`
- **Statut de preuve :** `Candidat`
- **Travail :** `À faire`
- **Responsable :** intégrateur — personne à désigner
- **Dépendances :** [`US-FIL-301`](US-FIL-301.md), [`US-FIL-302`](US-FIL-302.md), [`US-FIL-303`](US-FIL-303.md)
- **Ambiguïté :** [`AMB-09`](../../../governance/ambiguities.md#amb-09)

## Besoin

> En tant qu’intégrateur, je veux réutiliser le contrat read-only depuis un client MCP afin de connecter le workflow sans dupliquer les politiques.

## Périmètre

Adaptateur local minimal ; pas d'exposition publique, d'authentification inventée ou de développement obligatoire pendant J07.

Les décisions restent humaines ; aucune implémentation métier n'est réalisée par cette spécification.

## Entrées et sorties

- **Entrée :** Contrat validé de consultation, choix de transport/SDK et révision compatible approuvés ; stockage local autorisé.
- **Sortie :** Observation d'appel MCP corrélée à la même décision locale que l'appel direct.

Les baselines sont référencées dans [`sources.md`](../../../baseline/sources.md) ; leur révision est inconnue lorsqu'elle n'y est pas explicitement donnée. La sortie ne constitue pas, à elle seule, une preuve.

## Règle et critères

<a id="rm-fil-304"></a>
`RM-FIL-304` — L'adaptateur MCP applique la même politique avant accès que l'outil local et n'ajoute aucun droit.

<a id="ca-fil-304-01"></a>
- [ ] `CA-FIL-304-01` — Étant donné le client autorisé demande P1, quand l'adaptateur reçoit l'appel, alors le résultat et la décision de politique correspondent au contrat local.
<a id="ca-fil-304-02"></a>
- [ ] `CA-FIL-304-02` — Étant donné le client annule l'appel avant lecture, quand l'adaptateur traite l'annulation, alors aucune réussite ultérieure n'est publiée pour cet appel.
<a id="ca-fil-304-03"></a>
- [ ] `CA-FIL-304-03` — Étant donné le client demande une capacité d'écriture absente, quand l'adaptateur traite la requête, alors la demande est refusée sans modifier le corpus.

## Example Mapping

| Cas | Étant donné | Quand | Alors |
|---|---|---|---|
| Nominal | le client autorisé demande P1 | l'adaptateur reçoit l'appel | le résultat et la décision de politique correspondent au contrat local |
| Frontière | le client annule l'appel avant lecture | l'adaptateur traite l'annulation | aucune réussite ultérieure n'est publiée pour cet appel |
| Refus | le client demande une capacité d'écriture absente | l'adaptateur traite la requête | la demande est refusée sans modifier le corpus |

## Scénarios Gherkin

```gherkin
Fonctionnalité: Exposer le contrat via un adaptateur MCP réel
  Contexte:
    Étant donné le périmètre et les entrées versionnées de US-FIL-304
    Et les attendus ci-dessous définis avant la future réalisation

  Scénario: Nominal — CA-FIL-304-01
    Étant donné le client autorisé demande P1
    Quand l'adaptateur reçoit l'appel
    Alors le résultat et la décision de politique correspondent au contrat local

  Scénario: Frontière — CA-FIL-304-02
    Étant donné le client annule l'appel avant lecture
    Quand l'adaptateur traite l'annulation
    Alors aucune réussite ultérieure n'est publiée pour cet appel

  Scénario: Refus — CA-FIL-304-03
    Étant donné le client demande une capacité d'écriture absente
    Quand l'adaptateur traite la requête
    Alors la demande est refusée sans modifier le corpus
```

## Oracle indépendant

Même matrice d'autorisation que US-301 appliquée séparément au transport ; lecteur espion et corpus témoin en lecture seule.

## Réalisation et preuves

- [`FEAT-FIL-304`](../features/FEAT-FIL-304/FEATURE.md) — Feature candidate
- [`TASK-FIL-304-01`](../features/FEAT-FIL-304/tasks/TASK-FIL-304-01.md) — Faire approuver révision, SDK, transport et origine de l'identité ; consigner les incompatibilités connues.
- [`TASK-FIL-304-02`](../features/FEAT-FIL-304/tasks/TASK-FIL-304-02.md) — Brancher le transport sur le contrat local sans contourner la politique ni exposer une commande générique.
- [`TASK-FIL-304-03`](../features/FEAT-FIL-304/tasks/TASK-FIL-304-03.md) — Tester parité d'autorisation, annulation et capacité interdite, et documenter les différences de protocole réellement observées.

Aucune preuve d'acceptation de cette US n'est produite par son rendu. Les artefacts existants peuvent satisfaire un prérequis après revue ; aucune répétition de travaux déjà démontrés n'est imposée.

## Questions ouvertes

Voir [`AMB-09`](../../../governance/ambiguities.md#amb-09).
