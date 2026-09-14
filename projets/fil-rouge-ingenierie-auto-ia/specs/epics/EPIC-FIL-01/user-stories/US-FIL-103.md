# US-FIL-103 — Comparer deux organisations à cas figés

`Référence — spécification candidate`

- **Projet parent :** [`PROJ-FIL-AUTO-IA-001`](../../../../SPEC.md)
- **Epic parente :** [`EPIC-FIL-01`](../EPIC.md)
- **Feature fille :** [`FEAT-FIL-103`](../features/FEAT-FIL-103/FEATURE.md)
- **Jour :** `J06`
- **Sources de formation :** [`C05`](../../../baseline/sources.md#c05) — `J05` / Besoin avant framework, règle/recherche/workflow/agent et valeur observable / `support_actuel`<br>[`C06-G5`](../../../baseline/sources.md#c06-g5) — `J06` / Comparaison, journal complet, interruption et mémoire ; revue G5 / `programme_prevu`
- **Relation pédagogique :** Comparer deux organisations seulement après choix d'un mécanisme utile.
- **Niveau :** `Socle formation`
- **Priorité :** `P1`
- **Statut documentaire :** `Candidate`
- **Statut de preuve :** `Candidat`
- **Travail :** `À faire`
- **Responsable :** architecte — personne à désigner
- **Dépendances :** [`US-FIL-6`](../../EPIC-FIL-00/user-stories/US-FIL-6.md), [`US-FIL-102`](US-FIL-102.md)
- **Ambiguïté :** [`AMB-03`](../../../governance/ambiguities.md#amb-03)

## Besoin

> En tant qu’architecte, je veux comparer la séquence actuelle à une séparation producteur-vérificateur afin de retenir une complexité justifiée par des erreurs observées.

## Périmètre

Comparaison séquence/producteur-vérificateur avec replay possible ; ni parallélisme imposé ni benchmark de fournisseurs.

Les décisions restent humaines ; aucune implémentation métier n'est réalisée par cette spécification.

## Entrées et sorties

- **Entrée :** Cas, références et attendus figés avant essai ; deux organisations A/B ; vérificateur avec sources indépendantes ; mode d'exécution déclaré.
- **Sortie :** Observations par cas et proposition de choix avec erreurs, durées, limites et décision humaine ; aucun gain présumé.

Les baselines sont référencées dans [`sources.md`](../../../baseline/sources.md) ; leur révision est inconnue lorsqu'elle n'y est pas explicitement donnée. La sortie ne constitue pas, à elle seule, une preuve.

## Règle et critères

<a id="rm-fil-103"></a>
`RM-FIL-103` — Une comparaison n'est recevable que si les deux organisations utilisent les mêmes cas et le même oracle indépendant.

<a id="ca-fil-103-01"></a>
- [ ] `CA-FIL-103-01` — Étant donné A et B traitent le même cas figé, quand le relecteur compare leurs journaux, alors les erreurs et durées de chaque organisation sont reliées au cas et à la même vérification.
<a id="ca-fil-103-02"></a>
- [ ] `CA-FIL-103-02` — Étant donné les erreurs observées sont identiques pour A et B, quand le relecteur conclut, alors le rapport conserve écart nul sans déclarer B plus fiable.
<a id="ca-fil-103-03"></a>
- [ ] `CA-FIL-103-03` — Étant donné le cas ou l'oracle change entre A et B, quand le relecteur contrôle la comparaison, alors la comparaison est déclarée non comparable et aucune amélioration n'est revendiquée.

## Example Mapping

| Cas | Étant donné | Quand | Alors |
|---|---|---|---|
| Nominal | A et B traitent le même cas figé | le relecteur compare leurs journaux | les erreurs et durées de chaque organisation sont reliées au cas et à la même vérification |
| Frontière | les erreurs observées sont identiques pour A et B | le relecteur conclut | le rapport conserve écart nul sans déclarer B plus fiable |
| Refus | le cas ou l'oracle change entre A et B | le relecteur contrôle la comparaison | la comparaison est déclarée non comparable et aucune amélioration n'est revendiquée |

## Scénarios Gherkin

```gherkin
Fonctionnalité: Comparer deux organisations à cas figés
  Contexte:
    Étant donné le périmètre et les entrées versionnées de US-FIL-103
    Et les attendus ci-dessous définis avant la future réalisation

  Scénario: Nominal — CA-FIL-103-01
    Étant donné A et B traitent le même cas figé
    Quand le relecteur compare leurs journaux
    Alors les erreurs et durées de chaque organisation sont reliées au cas et à la même vérification

  Scénario: Frontière — CA-FIL-103-02
    Étant donné les erreurs observées sont identiques pour A et B
    Quand le relecteur conclut
    Alors le rapport conserve écart nul sans déclarer B plus fiable

  Scénario: Refus — CA-FIL-103-03
    Étant donné le cas ou l'oracle change entre A et B
    Quand le relecteur contrôle la comparaison
    Alors la comparaison est déclarée non comparable et aucune amélioration n'est revendiquée
```

## Oracle indépendant

Contrat MES-01 dans governance/measurement-contracts.md ; attendus indépendants du texte produit par A/B. Un second juge LLM n'est pas l'arbitre final.

## Réalisation et preuves

- [`FEAT-FIL-103`](../features/FEAT-FIL-103/FEATURE.md) — Feature candidate
- [`TASK-FIL-103-01`](../features/FEAT-FIL-103/tasks/TASK-FIL-103-01.md) — Figer les cas, les références et les entrées distinctes des rôles conformément à MES-01.
- [`TASK-FIL-103-02`](../features/FEAT-FIL-103/tasks/TASK-FIL-103-02.md) — Préparer deux exécutions ou deux replays déclarés, en conservant leurs journaux et décisions sans mélanger les modes.
- [`TASK-FIL-103-03`](../features/FEAT-FIL-103/tasks/TASK-FIL-103-03.md) — Confronter chaque résultat à l'attendu figé puis faire consigner le choix humain et les limites de comparaison.

Aucune preuve d'acceptation de cette US n'est produite par son rendu. Les artefacts existants peuvent satisfaire un prérequis après revue ; aucune répétition de travaux déjà démontrés n'est imposée.

## Questions ouvertes

Voir [`AMB-03`](../../../governance/ambiguities.md#amb-03).
