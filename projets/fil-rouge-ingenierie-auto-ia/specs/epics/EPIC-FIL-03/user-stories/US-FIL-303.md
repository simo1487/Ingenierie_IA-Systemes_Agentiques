# US-FIL-303 — Maintenir les permissions face au contenu non fiable

`Référence — spécification candidate`

- **Projet parent :** [`PROJ-FIL-AUTO-IA-001`](../../../../SPEC.md)
- **Epic parente :** [`EPIC-FIL-03`](../EPIC.md)
- **Feature fille :** [`FEAT-FIL-303`](../features/FEAT-FIL-303/FEATURE.md)
- **Jour :** `J07`
- **Sources de formation :** [`C04`](../../../baseline/sources.md#c04) — `J04` / Corpus autorisé, découpage du sens, lexical/sémantique, Hit@k/MRR et support des citations / `support_actuel`<br>[`C07`](../../../baseline/sources.md#c07) — `J07` / Politique avant accès, révision pédagogique MCP 2026-07-28, contenu non fiable et cas indépendants / `programme_prevu`
- **Relation pédagogique :** Donnée documentaire distincte d'une instruction et politique revérifiée.
- **Niveau :** `Socle formation`
- **Priorité :** `P1`
- **Statut documentaire :** `Candidate`
- **Statut de preuve :** `Candidat`
- **Travail :** `À faire`
- **Responsable :** responsable sécurité — personne à désigner
- **Dépendances :** [`US-FIL-301`](US-FIL-301.md)
- **Ambiguïté :** [`AMB-08`](../../../governance/ambiguities.md#amb-08)

## Besoin

> En tant que responsable sécurité, je veux empêcher un passage lu de devenir une autorisation d'action afin de conserver la frontière quand une donnée contient une instruction.

## Périmètre

Injections factices directes et indirectes ; aucune attaque sur un service externe.

Les décisions restent humaines ; aucune implémentation métier n'est réalisée par cette spécification.

## Entrées et sorties

- **Entrée :** Demandes et passages fictifs marqués non fiables ; politique locale approuvée ; aucun secret ou réseau réel.
- **Sortie :** Observation de tentative et refus technique de l'action non autorisée ; proposition textuelle isolée.

Les baselines sont référencées dans [`sources.md`](../../../baseline/sources.md) ; leur révision est inconnue lorsqu'elle n'y est pas explicitement donnée. La sortie ne constitue pas, à elle seule, une preuve.

## Règle et critères

<a id="rm-fil-303"></a>
`RM-FIL-303` — Une instruction contenue dans une donnée ne modifie ni les droits ni les outils autorisés du run.

<a id="ca-fil-303-01"></a>
- [ ] `CA-FIL-303-01` — Étant donné un passage contient une instruction fictive de consulter B2 hors portée, quand le modèle propose cet appel, alors la politique refuse l'appel avant accès à B2.
<a id="ca-fil-303-02"></a>
- [ ] `CA-FIL-303-02` — Étant donné l'instruction est citée dans un texte légitime, quand le workflow résume le passage, alors la citation peut rester une donnée mais aucun droit supplémentaire n'est accordé.
<a id="ca-fil-303-03"></a>
- [ ] `CA-FIL-303-03` — Étant donné la demande ou le passage prétend être un administrateur, quand une action hors périmètre est proposée, alors le contexte de confiance reste inchangé et l'action est refusée techniquement.

## Example Mapping

| Cas | Étant donné | Quand | Alors |
|---|---|---|---|
| Nominal | un passage contient une instruction fictive de consulter B2 hors portée | le modèle propose cet appel | la politique refuse l'appel avant accès à B2 |
| Frontière | l'instruction est citée dans un texte légitime | le workflow résume le passage | la citation peut rester une donnée mais aucun droit supplémentaire n'est accordé |
| Refus | la demande ou le passage prétend être un administrateur | une action hors périmètre est proposée | le contexte de confiance reste inchangé et l'action est refusée techniquement |

## Scénarios Gherkin

```gherkin
Fonctionnalité: Maintenir les permissions face au contenu non fiable
  Contexte:
    Étant donné le périmètre et les entrées versionnées de US-FIL-303
    Et les attendus ci-dessous définis avant la future réalisation

  Scénario: Nominal — CA-FIL-303-01
    Étant donné un passage contient une instruction fictive de consulter B2 hors portée
    Quand le modèle propose cet appel
    Alors la politique refuse l'appel avant accès à B2

  Scénario: Frontière — CA-FIL-303-02
    Étant donné l'instruction est citée dans un texte légitime
    Quand le workflow résume le passage
    Alors la citation peut rester une donnée mais aucun droit supplémentaire n'est accordé

  Scénario: Refus — CA-FIL-303-03
    Étant donné la demande ou le passage prétend être un administrateur
    Quand une action hors périmètre est proposée
    Alors le contexte de confiance reste inchangé et l'action est refusée techniquement
```

## Oracle indépendant

Invariants d'autorisation et lecteur espion de US-301 ; fixtures défensives sans données réelles ; contrôler les appels effectifs, pas seulement le texte généré.

## Réalisation et preuves

- [`FEAT-FIL-303`](../features/FEAT-FIL-303/FEATURE.md) — Feature candidate
- [`TASK-FIL-303-01`](../features/FEAT-FIL-303/tasks/TASK-FIL-303-01.md) — Figer des fixtures défensives directes/indirectes et les actions attendues refusées sous la politique de US-301.
- [`TASK-FIL-303-02`](../features/FEAT-FIL-303/tasks/TASK-FIL-303-02.md) — Séparer données lues et contexte d'autorisation ; revérifier chaque action proposée avant l'appel d'outil.
- [`TASK-FIL-303-03`](../features/FEAT-FIL-303/tasks/TASK-FIL-303-03.md) — Montrer refus avant accès et invariance des droits, puis transmettre le cas à la non-régression US-402.

Aucune preuve d'acceptation de cette US n'est produite par son rendu. Les artefacts existants peuvent satisfaire un prérequis après revue ; aucune répétition de travaux déjà démontrés n'est imposée.

## Questions ouvertes

Voir [`AMB-08`](../../../governance/ambiguities.md#amb-08).
