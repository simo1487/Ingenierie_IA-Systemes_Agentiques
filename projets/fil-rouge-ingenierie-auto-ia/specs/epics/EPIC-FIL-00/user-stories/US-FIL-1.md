# US-FIL-1 — Choisir une assistance proportionnée au besoin

`Référence — spécification candidate`

- **Projet parent :** [`PROJ-FIL-AUTO-IA-001`](../../../../SPEC.md)
- **Epic parente :** [`EPIC-FIL-00`](../EPIC.md)
- **Feature fille :** [`FEAT-FIL-1`](../features/FEAT-FIL-1/FEATURE.md)
- **Jour :** `J01–J05`
- **Sources de formation :** [`C01`](../../../baseline/sources.md#c01) — `J01` / Mécanisme proportionné, données, hébergement et souveraineté distincts / `support_actuel`<br>[`C05`](../../../baseline/sources.md#c05) — `J05` / Besoin avant framework, règle/recherche/workflow/agent et valeur observable / `support_actuel`<br>[`N05`](../../../baseline/sources.md#n05) — `J05` / Approches simples, types, budgets, contrôle humain et structuration ; propos à confirmer / `synthese_automatique`
- **Relation pédagogique :** Prérequis : besoin et droits avant modèle ; aucune obligation de multi-agent.
- **Niveau :** `Socle formation`
- **Priorité :** `P1`
- **Statut documentaire :** `Candidate`
- **Statut de preuve :** `Candidat`
- **Travail :** `À faire`
- **Responsable :** responsable produit — personne à désigner
- **Dépendances :** Aucune
- **Ambiguïté :** [`AMB-19`](../../../governance/ambiguities.md#amb-19)

## Besoin

> En tant que responsable produit, je veux justifier la place d'une règle, d'une recherche, d'un workflow ou d'un agent afin d’éviter une autonomie inutile et un transfert de données non autorisé.

## Périmètre

Cadrage et lecture des acquis J01/J05 ; aucun framework, runtime ou fournisseur nouveau imposé, aucune clé manipulée.

Les décisions restent humaines ; aucune implémentation métier n'est réalisée par cette spécification.

## Entrées et sorties

- **Entrée :** Fiche de besoin révisée : résultat utile, utilisateurs, données admises, destinations de traitement, actions permises et décideur ; modèle et hébergement envisagés séparément.
- **Sortie :** Proposition de mécanisme minimal avec justification, alternative et questions ouvertes ; aucune autorisation d'accès déduite du modèle choisi.

Les baselines sont référencées dans [`sources.md`](../../../baseline/sources.md) ; leur révision est inconnue lorsqu'elle n'y est pas explicitement donnée. La sortie ne constitue pas, à elle seule, une preuve.

## Règle et critères

<a id="rm-fil-1"></a>
`RM-FIL-1` — Le mécanisme est choisi à partir du comportement nécessaire, pas du nombre d'agents ou du framework disponible.

<a id="ca-fil-1-01"></a>
- [ ] `CA-FIL-1-01` — Étant donné une règle de classement déterministe suffit au besoin fictif, quand l'architecte propose un mécanisme, alors la règle est conservée comme option sans imposer de modèle.
<a id="ca-fil-1-02"></a>
- [ ] `CA-FIL-1-02` — Étant donné la prochaine consultation dépend d'observations variables, quand une marge d'autonomie est proposée, alors son utilité, ses outils permis, ses limites et le contrôle humain sont décrits avant adoption.
<a id="ca-fil-1-03"></a>
- [ ] `CA-FIL-1-03` — Étant donné le droit de transmettre le corpus à un fournisseur est inconnu, quand une exécution distante est envisagée, alors le transfert n'est pas autorisé et la décision manquante reste explicite.

## Example Mapping

| Cas | Étant donné | Quand | Alors |
|---|---|---|---|
| Nominal | une règle de classement déterministe suffit au besoin fictif | l'architecte propose un mécanisme | la règle est conservée comme option sans imposer de modèle |
| Frontière | la prochaine consultation dépend d'observations variables | une marge d'autonomie est proposée | son utilité, ses outils permis, ses limites et le contrôle humain sont décrits avant adoption |
| Refus | le droit de transmettre le corpus à un fournisseur est inconnu | une exécution distante est envisagée | le transfert n'est pas autorisé et la décision manquante reste explicite |

## Scénarios Gherkin

```gherkin
Fonctionnalité: Choisir une assistance proportionnée au besoin
  Contexte:
    Étant donné le périmètre et les entrées versionnées de US-FIL-1
    Et les attendus ci-dessous définis avant la future réalisation

  Scénario: Nominal — CA-FIL-1-01
    Étant donné une règle de classement déterministe suffit au besoin fictif
    Quand l'architecte propose un mécanisme
    Alors la règle est conservée comme option sans imposer de modèle

  Scénario: Frontière — CA-FIL-1-02
    Étant donné la prochaine consultation dépend d'observations variables
    Quand une marge d'autonomie est proposée
    Alors son utilité, ses outils permis, ses limites et le contrôle humain sont décrits avant adoption

  Scénario: Refus — CA-FIL-1-03
    Étant donné le droit de transmettre le corpus à un fournisseur est inconnu
    Quand une exécution distante est envisagée
    Alors le transfert n'est pas autorisé et la décision manquante reste explicite
```

## Oracle indépendant

Revue de la fiche de besoin par le responsable et confrontation au tableau des mécanismes de J05 ; la présence d'un framework ou l'exécution locale ne prouvent ni nécessité ni sûreté.

## Réalisation et preuves

- [`FEAT-FIL-1`](../features/FEAT-FIL-1/FEATURE.md) — Feature candidate
- [`TASK-FIL-1-01`](../features/FEAT-FIL-1/tasks/TASK-FIL-1-01.md) — Rassembler le besoin, les actions permises et la classification des données, en séparant faits et hypothèses.
- [`TASK-FIL-1-02`](../features/FEAT-FIL-1/tasks/TASK-FIL-1-02.md) — Comparer les mécanismes nécessaires à ce besoin et décrire les flux de données, y compris repli et télémétrie envisagés.
- [`TASK-FIL-1-03`](../features/FEAT-FIL-1/tasks/TASK-FIL-1-03.md) — Faire examiner la justification et les droits de traitement ; conserver les décisions non prises sans revendiquer une architecture approuvée.

Aucune preuve d'acceptation de cette US n'est produite par son rendu. Les artefacts existants peuvent satisfaire un prérequis après revue ; aucune répétition de travaux déjà démontrés n'est imposée.

## Questions ouvertes

Voir [`AMB-19`](../../../governance/ambiguities.md#amb-19).
