# US-FIL-604 — Consigner une décision réversible sur une page

`Référence — spécification candidate`

- **Projet parent :** [`PROJ-FIL-AUTO-IA-001`](../../../../SPEC.md)
- **Epic parente :** [`EPIC-FIL-06`](../EPIC.md)
- **Feature fille :** [`FEAT-FIL-604`](../features/FEAT-FIL-604/FEATURE.md)
- **Jour :** `J08`
- **Sources de formation :** [`C08-G7`](../../../baseline/sources.md#c08-g7) — `J08` / Fiche d'une page, trois risques, arrêt/repli testé, ROI et date de révision ; G7 / `programme_prevu`
- **Relation pédagogique :** Décision humaine réversible d'une page, arrêter argumenté reste un résultat valide.
- **Niveau :** `Socle formation`
- **Priorité :** `P1`
- **Statut documentaire :** `Candidate`
- **Statut de preuve :** `Candidat`
- **Travail :** `À faire`
- **Responsable :** décideur humain — personne à désigner
- **Dépendances :** [`US-FIL-503`](../../EPIC-FIL-05/user-stories/US-FIL-503.md), [`US-FIL-601`](US-FIL-601.md), [`US-FIL-602`](US-FIL-602.md), [`US-FIL-603`](US-FIL-603.md)
- **Ambiguïté :** [`AMB-18`](../../../governance/ambiguities.md#amb-18)

## Besoin

> En tant que décideur humain, je veux choisir entre arrêter, corriger, pilote limité et préparer un service afin de conclure sur un périmètre explicite et révisable.

## Périmètre

Fiche et décision pédagogique G7 ; lancement réel, paiement, déploiement et intégration restent des actions séparément autorisées.

Les décisions restent humaines ; aucune implémentation métier n'est réalisée par cette spécification.

## Entrées et sorties

- **Entrée :** Dossier G0–G6 avec manques visibles, preuves, risques, coût complet et retour arrière ; décision attribuée et date de révision.
- **Sortie :** Décision humaine d'une page avec verdict, périmètre, preuves citées, limites, trois risques, arrêt/repli, prochaine action, responsable et révision.

Les baselines sont référencées dans [`sources.md`](../../../baseline/sources.md) ; leur révision est inconnue lorsqu'elle n'y est pas explicitement donnée. La sortie ne constitue pas, à elle seule, une preuve.

## Règle et critères

<a id="rm-fil-604"></a>
`RM-FIL-604` — Une synthèse IA n'est jamais enregistrée comme décision humaine de Gate.

<a id="ca-fil-604-01"></a>
- [ ] `CA-FIL-604-01` — Étant donné le décideur dispose des preuves et choisit corriger, quand il consigne son verdict et la prochaine révision, alors la fiche rattache le choix au périmètre et aux preuves avec actions et responsable.
<a id="ca-fil-604-02"></a>
- [ ] `CA-FIL-604-02` — Étant donné les preuves conduisent à arrêter, quand le groupe clôt le parcours, alors arrêter argumenté est accepté comme décision sans forcer un pilote.
<a id="ca-fil-604-03"></a>
- [ ] `CA-FIL-604-03` — Étant donné aucun humain n'a décidé ou le retour arrière n'est pas prouvé, quand une synthèse favorable est produite, alors elle reste Proposition et ne déclenche aucun lancement.

## Example Mapping

| Cas | Étant donné | Quand | Alors |
|---|---|---|---|
| Nominal | le décideur dispose des preuves et choisit corriger | il consigne son verdict et la prochaine révision | la fiche rattache le choix au périmètre et aux preuves avec actions et responsable |
| Frontière | les preuves conduisent à arrêter | le groupe clôt le parcours | arrêter argumenté est accepté comme décision sans forcer un pilote |
| Refus | aucun humain n'a décidé ou le retour arrière n'est pas prouvé | une synthèse favorable est produite | elle reste Proposition et ne déclenche aucun lancement |

## Scénarios Gherkin

```gherkin
Fonctionnalité: Consigner une décision réversible sur une page
  Contexte:
    Étant donné le périmètre et les entrées versionnées de US-FIL-604
    Et les attendus ci-dessous définis avant la future réalisation

  Scénario: Nominal — CA-FIL-604-01
    Étant donné le décideur dispose des preuves et choisit corriger
    Quand il consigne son verdict et la prochaine révision
    Alors la fiche rattache le choix au périmètre et aux preuves avec actions et responsable

  Scénario: Frontière — CA-FIL-604-02
    Étant donné les preuves conduisent à arrêter
    Quand le groupe clôt le parcours
    Alors arrêter argumenté est accepté comme décision sans forcer un pilote

  Scénario: Refus — CA-FIL-604-03
    Étant donné aucun humain n'a décidé ou le retour arrière n'est pas prouvé
    Quand une synthèse favorable est produite
    Alors elle reste Proposition et ne déclenche aucun lancement
```

## Oracle indépendant

Revue contradictoire par un tiers qui retrouve décision, risques et arrêt sans explication orale ; contrôler la trace d'attribution, ne pas transformer un champ rempli par IA en consentement.

## Réalisation et preuves

- [`FEAT-FIL-604`](../features/FEAT-FIL-604/FEATURE.md) — Feature candidate
- [`TASK-FIL-604-01`](../features/FEAT-FIL-604/tasks/TASK-FIL-604-01.md) — Préparer le gabarit d'une page et confronter les quatre verdicts aux preuves, en citant ce qui ferait changer le choix.
- [`TASK-FIL-604-02`](../features/FEAT-FIL-604/tasks/TASK-FIL-604-02.md) — Faire rédiger la décision par le responsable avec coûts, risques, arrêt/repli, limites et date de révision.
- [`TASK-FIL-604-03`](../features/FEAT-FIL-604/tasks/TASK-FIL-604-03.md) — Organiser la revue croisée et conserver la décision attribuée ; vérifier qu'aucun lancement n'est déclenché par une proposition IA.

Aucune preuve d'acceptation de cette US n'est produite par son rendu. Les artefacts existants peuvent satisfaire un prérequis après revue ; aucune répétition de travaux déjà démontrés n'est imposée.

## Questions ouvertes

Voir [`AMB-18`](../../../governance/ambiguities.md#amb-18).
