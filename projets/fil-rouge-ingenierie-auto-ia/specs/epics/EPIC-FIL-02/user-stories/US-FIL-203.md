# US-FIL-203 — Refuser une mémoire périmée ou hors périmètre

`Référence — spécification candidate`

- **Projet parent :** [`PROJ-FIL-AUTO-IA-001`](../../../../SPEC.md)
- **Epic parente :** [`EPIC-FIL-02`](../EPIC.md)
- **Feature fille :** [`FEAT-FIL-203`](../features/FEAT-FIL-203/FEATURE.md)
- **Jour :** `J06`
- **Sources de formation :** [`C04-RETOUR`](../../../baseline/sources.md#c04-retour) — `J04` / Requête directe avant modèle, questions attendues, empreintes, doublons et retrait des sources / `retour_rapporte`<br>[`C06-G5`](../../../baseline/sources.md#c06-g5) — `J06` / Comparaison, journal complet, interruption et mémoire ; revue G5 / `programme_prevu`
- **Relation pédagogique :** Mémoire portée/expiration distincte du seul contexte de génération.
- **Niveau :** `Socle formation`
- **Priorité :** `P1`
- **Statut documentaire :** `Candidate`
- **Statut de preuve :** `Candidat`
- **Travail :** `À faire`
- **Responsable :** responsable de corpus — personne à désigner
- **Dépendances :** [`US-FIL-101`](../../EPIC-FIL-01/user-stories/US-FIL-101.md), [`US-FIL-102`](../../EPIC-FIL-01/user-stories/US-FIL-102.md)
- **Ambiguïté :** [`AMB-07`](../../../governance/ambiguities.md#amb-07)

## Besoin

> En tant que responsable de corpus, je veux définir la portée et l'expiration des informations réutilisables afin de ne pas réinjecter une ancienne règle dans un nouveau lot.

## Périmètre

Mémoire locale gouvernée et règle datée ; aucune mémoire globale de conversation ni conservation illimitée.

Les décisions restent humaines ; aucune implémentation métier n'est réalisée par cette spécification.

## Entrées et sorties

- **Entrée :** Entrée mémoire avec id, source, révision, portée, created_at, expires_at et responsable ; horloge de référence.
- **Sortie :** Observation de lecture permise ou refus tracé ; correction sous nouvelle version.

Les baselines sont référencées dans [`sources.md`](../../../baseline/sources.md) ; leur révision est inconnue lorsqu'elle n'y est pas explicitement donnée. La sortie ne constitue pas, à elle seule, une preuve.

## Règle et critères

<a id="rm-fil-203"></a>
`RM-FIL-203` — Une entrée n'est utilisable que dans sa portée autorisée et strictement avant son expiration.

<a id="ca-fil-203-01"></a>
- [ ] `CA-FIL-203-01` — Étant donné M1 appartient à B1 et expire après l'instant de lecture, quand R1 autorisé sur B1 la consulte, alors M1 est utilisée avec sa source et sa révision.
<a id="ca-fil-203-02"></a>
- [ ] `CA-FIL-203-02` — Étant donné l'instant de lecture égale expires_at, quand R1 consulte M1, alors M1 est refusée comme périmée.
<a id="ca-fil-203-03"></a>
- [ ] `CA-FIL-203-03` — Étant donné M1 appartient à une autre baseline, quand R1 la demande, alors aucun contenu M1 n'est injecté dans le contexte.

## Example Mapping

| Cas | Étant donné | Quand | Alors |
|---|---|---|---|
| Nominal | M1 appartient à B1 et expire après l'instant de lecture | R1 autorisé sur B1 la consulte | M1 est utilisée avec sa source et sa révision |
| Frontière | l'instant de lecture égale expires_at | R1 consulte M1 | M1 est refusée comme périmée |
| Refus | M1 appartient à une autre baseline | R1 la demande | aucun contenu M1 n'est injecté dans le contexte |

Table de décision candidate : [`RM-FIL-203`](../../../governance/decision-tables.md#mémoire-rm-fil-203).

## Scénarios Gherkin

```gherkin
Fonctionnalité: Refuser une mémoire périmée ou hors périmètre
  Contexte:
    Étant donné le périmètre et les entrées versionnées de US-FIL-203
    Et les attendus ci-dessous définis avant la future réalisation

  Scénario: Nominal — CA-FIL-203-01
    Étant donné M1 appartient à B1 et expire après l'instant de lecture
    Quand R1 autorisé sur B1 la consulte
    Alors M1 est utilisée avec sa source et sa révision

  Scénario: Frontière — CA-FIL-203-02
    Étant donné l'instant de lecture égale expires_at
    Quand R1 consulte M1
    Alors M1 est refusée comme périmée

  Scénario: Refus — CA-FIL-203-03
    Étant donné M1 appartient à une autre baseline
    Quand R1 la demande
    Alors aucun contenu M1 n'est injecté dans le contexte
```

## Oracle indépendant

Table portée/expiration écrite avant code ; horloge injectée ; inspection du contexte effectivement transmis au fournisseur, pas uniquement du message de refus.

## Réalisation et preuves

- [`FEAT-FIL-203`](../features/FEAT-FIL-203/FEATURE.md) — Feature candidate
- [`TASK-FIL-203-01`](../features/FEAT-FIL-203/tasks/TASK-FIL-203-01.md) — Définir le schéma mémoire, la table portée/expiration et les responsabilités de correction.
- [`TASK-FIL-203-02`](../features/FEAT-FIL-203/tasks/TASK-FIL-203-02.md) — Mettre en place la lecture filtrée et la correction versionnée, ou un replay explicite de la politique.
- [`TASK-FIL-203-03`](../features/FEAT-FIL-203/tasks/TASK-FIL-203-03.md) — Présenter une entrée expirée et hors portée, vérifier le contexte transmis et faire relire la règle de mémoire.

Aucune preuve d'acceptation de cette US n'est produite par son rendu. Les artefacts existants peuvent satisfaire un prérequis après revue ; aucune répétition de travaux déjà démontrés n'est imposée.

## Questions ouvertes

Voir [`AMB-07`](../../../governance/ambiguities.md#amb-07).
