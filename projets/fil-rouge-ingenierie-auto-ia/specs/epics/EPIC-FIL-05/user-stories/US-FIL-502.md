# US-FIL-502 — Bloquer une intégration dépourvue de preuves

`Référence — spécification candidate`

- **Projet parent :** [`PROJ-FIL-AUTO-IA-001`](../../../../SPEC.md)
- **Epic parente :** [`EPIC-FIL-05`](../EPIC.md)
- **Feature fille :** [`FEAT-FIL-502`](../features/FEAT-FIL-502/FEATURE.md)
- **Jour :** `J08`
- **Sources de formation :** [`C03-RETOUR`](../../../baseline/sources.md#c03-retour) — `J03` / Plan préalable, bornes et comparaisons des tests générés, concurrence, doubles, contrôles dans la chaîne / `retour_rapporte`<br>[`C08`](../../../baseline/sources.md#c08) — `J08` / Quatre verdicts, risques gouvernés, preuves bornées et coût complet / `programme_prevu`
- **Relation pédagogique :** Extension CI : preuves locales et globales distinctes, politiques inchangées.
- **Niveau :** `Extension production`
- **Priorité :** `P2`
- **Statut documentaire :** `Candidate`
- **Statut de preuve :** `Candidat`
- **Travail :** `À faire`
- **Responsable :** relecteur intégration — personne à désigner
- **Dépendances :** [`US-FIL-401`](../../EPIC-FIL-04/user-stories/US-FIL-401.md), [`US-FIL-402`](../../EPIC-FIL-04/user-stories/US-FIL-402.md), [`US-FIL-501`](US-FIL-501.md)
- **Ambiguïté :** [`AMB-14`](../../../governance/ambiguities.md#amb-14)

## Besoin

> En tant que relecteur intégration, je veux disposer de contrôles documentaires et de tests dans la chaîne de revue afin de détecter les régressions avant intégration.

## Périmètre

Préparation des contrôles ; aucune modification de protection de branche ni fusion automatique.

Les décisions restent humaines ; aucune implémentation métier n'est réalisée par cette spécification.

## Entrées et sorties

- **Entrée :** Lot de fichiers, tests hors ligne, liens de specs, résultats de non-régression et politique de revue existante.
- **Sortie :** Observations de contrôles ciblés et globaux séparées, défauts attribués au périmètre ; décision humaine d'intégration.

Les baselines sont référencées dans [`sources.md`](../../../baseline/sources.md) ; leur révision est inconnue lorsqu'elle n'y est pas explicitement donnée. La sortie ne constitue pas, à elle seule, une preuve.

## Règle et critères

<a id="rm-fil-502"></a>
`RM-FIL-502` — Un échec critique ou un contrôle non exécuté ne peut pas être publié comme validation réussie.

<a id="ca-fil-502-01"></a>
- [ ] `CA-FIL-502-01` — Étant donné les contrôles ciblés passent et les preuves sont disponibles, quand le lot est soumis, alors leurs résultats et leur périmètre sont joints à la revue.
<a id="ca-fil-502-02"></a>
- [ ] `CA-FIL-502-02` — Étant donné le global échoue hors périmètre alors que le projet passe, quand le rapport est assemblé, alors les deux résultats restent distincts sans annoncer le monorepo vert.
<a id="ca-fil-502-03"></a>
- [ ] `CA-FIL-502-03` — Étant donné un contrôle de sécurité échoue, quand l'intégration est proposée, alors le défaut reste bloquant et aucune politique n'est contournée.

## Example Mapping

| Cas | Étant donné | Quand | Alors |
|---|---|---|---|
| Nominal | les contrôles ciblés passent et les preuves sont disponibles | le lot est soumis | leurs résultats et leur périmètre sont joints à la revue |
| Frontière | le global échoue hors périmètre alors que le projet passe | le rapport est assemblé | les deux résultats restent distincts sans annoncer le monorepo vert |
| Refus | un contrôle de sécurité échoue | l'intégration est proposée | le défaut reste bloquant et aucune politique n'est contournée |

## Scénarios Gherkin

```gherkin
Fonctionnalité: Bloquer une intégration dépourvue de preuves
  Contexte:
    Étant donné le périmètre et les entrées versionnées de US-FIL-502
    Et les attendus ci-dessous définis avant la future réalisation

  Scénario: Nominal — CA-FIL-502-01
    Étant donné les contrôles ciblés passent et les preuves sont disponibles
    Quand le lot est soumis
    Alors leurs résultats et leur périmètre sont joints à la revue

  Scénario: Frontière — CA-FIL-502-02
    Étant donné le global échoue hors périmètre alors que le projet passe
    Quand le rapport est assemblé
    Alors les deux résultats restent distincts sans annoncer le monorepo vert

  Scénario: Refus — CA-FIL-502-03
    Étant donné un contrôle de sécurité échoue
    Quand l'intégration est proposée
    Alors le défaut reste bloquant et aucune politique n'est contournée
```

## Oracle indépendant

Codes retour réels et journaux de contrôle ; jeu de liens cassés/IDs orphelins pour les specs ; absence de résultat interprétée non exécuté.

## Réalisation et preuves

- [`FEAT-FIL-502`](../features/FEAT-FIL-502/FEATURE.md) — Feature candidate
- [`TASK-FIL-502-01`](../features/FEAT-FIL-502/tasks/TASK-FIL-502-01.md) — Lister les contrôles et leurs périmètres, avec traitement explicite de l'héritage en échec du monorepo.
- [`TASK-FIL-502-02`](../features/FEAT-FIL-502/tasks/TASK-FIL-502-02.md) — Prévoir l'automatisation des tests et de l'intégrité des specs dans la chaîne existante sans modifier les politiques de sécurité.
- [`TASK-FIL-502-03`](../features/FEAT-FIL-502/tasks/TASK-FIL-502-03.md) — Éprouver un lien cassé et un test critique en échec puis faire relire les preuves avant toute intégration autorisée.

Aucune preuve d'acceptation de cette US n'est produite par son rendu. Les artefacts existants peuvent satisfaire un prérequis après revue ; aucune répétition de travaux déjà démontrés n'est imposée.

## Questions ouvertes

Voir [`AMB-14`](../../../governance/ambiguities.md#amb-14).
