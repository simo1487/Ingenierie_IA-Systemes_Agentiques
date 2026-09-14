# US-FIL-504 — Observer un pilote sans exposer ses données

`Référence — spécification candidate`

- **Projet parent :** [`PROJ-FIL-AUTO-IA-001`](../../../../SPEC.md)
- **Epic parente :** [`EPIC-FIL-05`](../EPIC.md)
- **Feature fille :** [`FEAT-FIL-504`](../features/FEAT-FIL-504/FEATURE.md)
- **Jour :** `J08`
- **Sources de formation :** [`C06`](../../../baseline/sources.md#c06) — `J06` / Comparaison d'organisations, rôles, reprise, idempotence, mémoire et trace / `programme_prevu`<br>[`C07`](../../../baseline/sources.md#c07) — `J07` / Politique avant accès, révision pédagogique MCP 2026-07-28, contenu non fiable et cas indépendants / `programme_prevu`<br>[`C08`](../../../baseline/sources.md#c08) — `J08` / Quatre verdicts, risques gouvernés, preuves bornées et coût complet / `programme_prevu`
- **Relation pédagogique :** Extension exploitation : observations assainies et signaux d'arrêt attribués.
- **Niveau :** `Extension production`
- **Priorité :** `P2`
- **Statut documentaire :** `Candidate`
- **Statut de preuve :** `Candidat`
- **Travail :** `À faire`
- **Responsable :** opérateur — personne à désigner
- **Dépendances :** [`US-FIL-102`](../../EPIC-FIL-01/user-stories/US-FIL-102.md), [`US-FIL-202`](../../EPIC-FIL-02/user-stories/US-FIL-202.md), [`US-FIL-503`](US-FIL-503.md)
- **Ambiguïté :** [`AMB-02`](../../../governance/ambiguities.md#amb-02)

## Besoin

> En tant qu’opérateur, je veux surveiller erreurs, délais et usage via des traces minimales afin de détecter un signal d'arrêt sans journaliser les contenus sensibles.

## Périmètre

Observabilité minimale locale ; plateforme cloud et seuils de service non choisis implicitement.

Les décisions restent humaines ; aucune implémentation métier n'est réalisée par cette spécification.

## Entrées et sorties

- **Entrée :** Événements assainis, politique d'observation versionnée, sources de durée/usage et conditions d'arrêt approuvées.
- **Sortie :** Observations corrélées au run et alertes vers un rôle désigné ; données absentes explicitement non mesurées.

Les baselines sont référencées dans [`sources.md`](../../../baseline/sources.md) ; leur révision est inconnue lorsqu'elle n'y est pas explicitement donnée. La sortie ne constitue pas, à elle seule, une preuve.

## Règle et critères

<a id="rm-fil-504"></a>
`RM-FIL-504` — La surveillance n'ajoute pas de prompts complets, de secrets ou de données personnelles dans les traces par défaut.

<a id="ca-fil-504-01"></a>
- [ ] `CA-FIL-504-01` — Étant donné R1 produit une erreur et une durée mesurée, quand l'opérateur consulte la surveillance, alors il retrouve événement, run et responsable sans contenu du prompt.
<a id="ca-fil-504-02"></a>
- [ ] `CA-FIL-504-02` — Étant donné le fournisseur ne renvoie pas son usage, quand le rapport est produit, alors l'usage est non mesuré et non remplacé par zéro.
<a id="ca-fil-504-03"></a>
- [ ] `CA-FIL-504-03` — Étant donné une exception contient une valeur factice sensible, quand elle traverse la journalisation, alors la valeur brute n'apparaît pas dans l'artefact public de trace.

## Example Mapping

| Cas | Étant donné | Quand | Alors |
|---|---|---|---|
| Nominal | R1 produit une erreur et une durée mesurée | l'opérateur consulte la surveillance | il retrouve événement, run et responsable sans contenu du prompt |
| Frontière | le fournisseur ne renvoie pas son usage | le rapport est produit | l'usage est non mesuré et non remplacé par zéro |
| Refus | une exception contient une valeur factice sensible | elle traverse la journalisation | la valeur brute n'apparaît pas dans l'artefact public de trace |

## Scénarios Gherkin

```gherkin
Fonctionnalité: Observer un pilote sans exposer ses données
  Contexte:
    Étant donné le périmètre et les entrées versionnées de US-FIL-504
    Et les attendus ci-dessous définis avant la future réalisation

  Scénario: Nominal — CA-FIL-504-01
    Étant donné R1 produit une erreur et une durée mesurée
    Quand l'opérateur consulte la surveillance
    Alors il retrouve événement, run et responsable sans contenu du prompt

  Scénario: Frontière — CA-FIL-504-02
    Étant donné le fournisseur ne renvoie pas son usage
    Quand le rapport est produit
    Alors l'usage est non mesuré et non remplacé par zéro

  Scénario: Refus — CA-FIL-504-03
    Étant donné une exception contient une valeur factice sensible
    Quand elle traverse la journalisation
    Alors la valeur brute n'apparaît pas dans l'artefact public de trace
```

## Oracle indépendant

Sentinelles fictives connues, inspection des octets exportés et trace événementielle externe ; aucun secret réel utilisé pour tester l'assainissement.

## Réalisation et preuves

- [`FEAT-FIL-504`](../features/FEAT-FIL-504/FEATURE.md) — Feature candidate
- [`TASK-FIL-504-01`](../features/FEAT-FIL-504/tasks/TASK-FIL-504-01.md) — Définir champs permis, rétention et sources des mesures, sans choisir des seuils de production arbitraires.
- [`TASK-FIL-504-02`](../features/FEAT-FIL-504/tasks/TASK-FIL-504-02.md) — Prévoir une vue d'exploitation corrélée aux runs et un routage explicite des signaux d'arrêt.
- [`TASK-FIL-504-03`](../features/FEAT-FIL-504/tasks/TASK-FIL-504-03.md) — Tester erreur sensible factice et usage absent ; faire revoir ce qui est réellement mesuré et ce qui reste inconnu.

Aucune preuve d'acceptation de cette US n'est produite par son rendu. Les artefacts existants peuvent satisfaire un prérequis après revue ; aucune répétition de travaux déjà démontrés n'est imposée.

## Questions ouvertes

Voir [`AMB-02`](../../../governance/ambiguities.md#amb-02).
