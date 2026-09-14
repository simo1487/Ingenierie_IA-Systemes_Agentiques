# US-FIL-201 — Reprendre un run sans double effet

`Référence — spécification candidate`

- **Projet parent :** [`PROJ-FIL-AUTO-IA-001`](../../../../SPEC.md)
- **Epic parente :** [`EPIC-FIL-02`](../EPIC.md)
- **Feature fille :** [`FEAT-FIL-201`](../features/FEAT-FIL-201/FEATURE.md)
- **Jour :** `J06`
- **Sources de formation :** [`C03-RETOUR`](../../../baseline/sources.md#c03-retour) — `J03` / Plan préalable, bornes et comparaisons des tests générés, concurrence, doubles, contrôles dans la chaîne / `retour_rapporte`<br>[`C06-G5`](../../../baseline/sources.md#c06-g5) — `J06` / Comparaison, journal complet, interruption et mémoire ; revue G5 / `programme_prevu`
- **Relation pédagogique :** Reprise et absence de double effet, y compris appels concurrents.
- **Niveau :** `Socle formation`
- **Priorité :** `P1`
- **Statut documentaire :** `Candidate`
- **Statut de preuve :** `Candidat`
- **Travail :** `À faire`
- **Responsable :** opérateur — personne à désigner
- **Dépendances :** [`US-FIL-102`](../../EPIC-FIL-01/user-stories/US-FIL-102.md)
- **Ambiguïté :** [`AMB-05`](../../../governance/ambiguities.md#amb-05)

## Besoin

> En tant qu’opérateur, je veux reprendre au dernier point vérifié afin d’éviter de refaire une opération déjà confirmée.

## Périmètre

Démonstration locale ou replay documenté pour J06 ; stockage distribué et effets réels exclus.

Les décisions restent humaines ; aucune implémentation métier n'est réalisée par cette spécification.

## Entrées et sorties

- **Entrée :** Checkpoint versionné lié au run, empreinte des entrées, étape vérifiée et identifiant d'opération ; destination locale de test.
- **Sortie :** Observation de reprise ou refus de checkpoint incompatible ; registre des opérations réalisées.

Les baselines sont référencées dans [`sources.md`](../../../baseline/sources.md) ; leur révision est inconnue lorsqu'elle n'y est pas explicitement donnée. La sortie ne constitue pas, à elle seule, une preuve.

## Règle et critères

<a id="rm-fil-201"></a>
`RM-FIL-201` — Reprendre une opération confirmée avec la même identité ne doit pas produire un deuxième effet.

<a id="ca-fil-201-01"></a>
- [ ] `CA-FIL-201-01` — Étant donné R1 est interrompu après un export local confirmé, quand l'opérateur reprend depuis son checkpoint, alors les étapes déjà confirmées ne sont pas rejouées et l'export n'est pas dupliqué.
<a id="ca-fil-201-02"></a>
- [ ] `CA-FIL-201-02` — Étant donné deux demandes de reprise ciblent la même opération, quand elles sont traitées, alors une seule obtient le droit d'effectuer l'opération et l'autre constate son état.
<a id="ca-fil-201-03"></a>
- [ ] `CA-FIL-201-03` — Étant donné l'empreinte du manifeste diffère du checkpoint, quand l'opérateur demande une reprise, alors la reprise est refusée et le point existant reste inchangé.
<a id="ca-fil-201-04"></a>
- [ ] `CA-FIL-201-04` — Étant donné le checkpoint ne contient aucune étape vérifiée, quand une reprise est demandée, alors aucune étape n'est déclarée déjà acquise et la reprise probante est refusée.
<a id="ca-fil-201-05"></a>
- [ ] `CA-FIL-201-05` — Étant donné une interruption survient après un effet mais avant sa confirmation durable, quand l'opérateur demande une reprise, alors l'état incertain est signalé et aucune répétition automatique de l'effet n'est autorisée avant résolution.

## Example Mapping

| Cas | Étant donné | Quand | Alors |
|---|---|---|---|
| Nominal | R1 est interrompu après un export local confirmé | l'opérateur reprend depuis son checkpoint | les étapes déjà confirmées ne sont pas rejouées et l'export n'est pas dupliqué |
| Concurrence | deux demandes de reprise ciblent la même opération | elles sont traitées | une seule obtient le droit d'effectuer l'opération et l'autre constate son état |
| Refus | l'empreinte du manifeste diffère du checkpoint | l'opérateur demande une reprise | la reprise est refusée et le point existant reste inchangé |
| Frontière | le checkpoint ne contient aucune étape vérifiée | une reprise est demandée | aucune étape n'est déclarée déjà acquise et la reprise probante est refusée |
| Interruption | une interruption survient après un effet mais avant sa confirmation durable | l'opérateur demande une reprise | l'état incertain est signalé et aucune répétition automatique de l'effet n'est autorisée avant résolution |

## Scénarios Gherkin

```gherkin
Fonctionnalité: Reprendre un run sans double effet
  Contexte:
    Étant donné le périmètre et les entrées versionnées de US-FIL-201
    Et les attendus ci-dessous définis avant la future réalisation

  Scénario: Nominal — CA-FIL-201-01
    Étant donné R1 est interrompu après un export local confirmé
    Quand l'opérateur reprend depuis son checkpoint
    Alors les étapes déjà confirmées ne sont pas rejouées et l'export n'est pas dupliqué

  Scénario: Concurrence — CA-FIL-201-02
    Étant donné deux demandes de reprise ciblent la même opération
    Quand elles sont traitées
    Alors une seule obtient le droit d'effectuer l'opération et l'autre constate son état

  Scénario: Refus — CA-FIL-201-03
    Étant donné l'empreinte du manifeste diffère du checkpoint
    Quand l'opérateur demande une reprise
    Alors la reprise est refusée et le point existant reste inchangé

  Scénario: Frontière — CA-FIL-201-04
    Étant donné le checkpoint ne contient aucune étape vérifiée
    Quand une reprise est demandée
    Alors aucune étape n'est déclarée déjà acquise et la reprise probante est refusée

  Scénario: Interruption — CA-FIL-201-05
    Étant donné une interruption survient après un effet mais avant sa confirmation durable
    Quand l'opérateur demande une reprise
    Alors l'état incertain est signalé et aucune répétition automatique de l'effet n'est autorisée avant résolution
```

## Oracle indépendant

Registre d'effets externe au workflow et deux appels concurrents de test ; comparer son cardinal avant/après. Simuler aussi l'interruption entre effet et confirmation : pas de promesse exactly-once sans mécanisme transactionnel explicite.

## Réalisation et preuves

- [`FEAT-FIL-201`](../features/FEAT-FIL-201/FEATURE.md) — Feature candidate
- [`TASK-FIL-201-01`](../features/FEAT-FIL-201/tasks/TASK-FIL-201-01.md) — Figer le protocole checkpoint/opération et les fenêtres de panne, dont effet accompli avant confirmation.
- [`TASK-FIL-201-02`](../features/FEAT-FIL-201/tasks/TASK-FIL-201-02.md) — Réaliser un point de reprise local et une réservation d'opération idempotente, ou préparer un replay déclaré pour le socle.
- [`TASK-FIL-201-03`](../features/FEAT-FIL-201/tasks/TASK-FIL-201-03.md) — Interrompre, reprendre deux fois et confronter le registre d'effets ; refuser l'empreinte incompatible et revoir la fenêtre non atomique.

Aucune preuve d'acceptation de cette US n'est produite par son rendu. Les artefacts existants peuvent satisfaire un prérequis après revue ; aucune répétition de travaux déjà démontrés n'est imposée.

## Questions ouvertes

Voir [`AMB-05`](../../../governance/ambiguities.md#amb-05).
