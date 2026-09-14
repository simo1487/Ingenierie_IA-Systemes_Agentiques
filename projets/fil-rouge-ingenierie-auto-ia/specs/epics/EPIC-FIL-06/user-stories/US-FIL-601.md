# US-FIL-601 — Distinguer un lien déclaré d'une preuve vérifiée

`Référence — spécification candidate`

- **Projet parent :** [`PROJ-FIL-AUTO-IA-001`](../../../../SPEC.md)
- **Epic parente :** [`EPIC-FIL-06`](../EPIC.md)
- **Feature fille :** [`FEAT-FIL-601`](../features/FEAT-FIL-601/FEATURE.md)
- **Jour :** `J08`
- **Sources de formation :** [`C02`](../../../baseline/sources.md#c02) — `J02` / Exigence singulière, inconnues, exemples et oracle indépendant ; Gherkin non universellement obligatoire / `support_actuel`<br>[`C03`](../../../baseline/sources.md#c03) — `J03` / Reproduction, hypothèses concurrentes, rouge/vert comparable, mutation et documentation / `support_actuel`<br>[`C08`](../../../baseline/sources.md#c08) — `J08` / Quatre verdicts, risques gouvernés, preuves bornées et coût complet / `programme_prevu`
- **Relation pédagogique :** Statut de preuve fondé sur examen et portée, pas sur champs non vides.
- **Niveau :** `Socle formation`
- **Priorité :** `P1`
- **Statut documentaire :** `Candidate`
- **Statut de preuve :** `Candidat`
- **Travail :** `À faire`
- **Responsable :** relecteur indépendant — personne à désigner
- **Dépendances :** [`US-FIL-2`](../../EPIC-FIL-00/user-stories/US-FIL-2.md), [`US-FIL-5`](../../EPIC-FIL-00/user-stories/US-FIL-5.md), [`US-FIL-101`](../../EPIC-FIL-01/user-stories/US-FIL-101.md), [`US-FIL-401`](../../EPIC-FIL-04/user-stories/US-FIL-401.md)
- **Ambiguïté :** [`AMB-16`](../../../governance/ambiguities.md#amb-16)

## Besoin

> En tant que relecteur indépendant, je veux examiner la provenance et la portée des preuves avant promotion afin de ne pas confondre des champs remplis avec une validation.

## Périmètre

Dossier et revue humaine ; signature cryptographique et référentiel externe non imposés.

Les décisions restent humaines ; aucune implémentation métier n'est réalisée par cette spécification.

## Entrées et sorties

- **Entrée :** Lien explicite exigence/cible, référence d'oracle, artefact accessible, révision et résultat d'exécution ou examen indépendant ; responsable de revue.
- **Sortie :** Proposition de matrice et décision humaine attribuée avec statut par lien et limites de couverture.

Les baselines sont référencées dans [`sources.md`](../../../baseline/sources.md) ; leur révision est inconnue lorsqu'elle n'y est pas explicitement donnée. La sortie ne constitue pas, à elle seule, une preuve.

## Règle et critères

<a id="rm-fil-601"></a>
`RM-FIL-601` — La seule présence de chaînes oracle et evidence ne justifie jamais le statut Vérifié.

<a id="ca-fil-601-01"></a>
- [ ] `CA-FIL-601-01` — Étant donné un lien explicite possède une preuve contrôlée sur la même révision et une revue attribuée, quand le relecteur consigne son contrôle, alors le lien peut être marqué Vérifié sur ce seul périmètre.
<a id="ca-fil-601-02"></a>
- [ ] `CA-FIL-601-02` — Étant donné oracle et evidence sont non vides mais non consultables, quand le dossier est revu, alors le lien reste Non vérifié ou Bloqué avec raison.
<a id="ca-fil-601-03"></a>
- [ ] `CA-FIL-601-03` — Étant donné seul un mot commun relie exigence et code, quand la matrice est préparée, alors aucun lien de preuve n'est créé par similarité lexicale.

## Example Mapping

| Cas | Étant donné | Quand | Alors |
|---|---|---|---|
| Nominal | un lien explicite possède une preuve contrôlée sur la même révision et une revue attribuée | le relecteur consigne son contrôle | le lien peut être marqué Vérifié sur ce seul périmètre |
| Frontière | oracle et evidence sont non vides mais non consultables | le dossier est revu | le lien reste Non vérifié ou Bloqué avec raison |
| Refus | seul un mot commun relie exigence et code | la matrice est préparée | aucun lien de preuve n'est créé par similarité lexicale |

## Scénarios Gherkin

```gherkin
Fonctionnalité: Distinguer un lien déclaré d'une preuve vérifiée
  Contexte:
    Étant donné le périmètre et les entrées versionnées de US-FIL-601
    Et les attendus ci-dessous définis avant la future réalisation

  Scénario: Nominal — CA-FIL-601-01
    Étant donné un lien explicite possède une preuve contrôlée sur la même révision et une revue attribuée
    Quand le relecteur consigne son contrôle
    Alors le lien peut être marqué Vérifié sur ce seul périmètre

  Scénario: Frontière — CA-FIL-601-02
    Étant donné oracle et evidence sont non vides mais non consultables
    Quand le dossier est revu
    Alors le lien reste Non vérifié ou Bloqué avec raison

  Scénario: Refus — CA-FIL-601-03
    Étant donné seul un mot commun relie exigence et code
    Quand la matrice est préparée
    Alors aucun lien de preuve n'est créé par similarité lexicale
```

## Oracle indépendant

Revue indépendante de l'artefact, de sa révision et du comportement couvert ; preuve fictive inexistante comme contre-exemple. Le test actuel de présence de champs est un constat d'implémentation, pas cet oracle.

## Réalisation et preuves

- [`FEAT-FIL-601`](../features/FEAT-FIL-601/FEATURE.md) — Feature candidate
- [`TASK-FIL-601-01`](../features/FEAT-FIL-601/tasks/TASK-FIL-601-01.md) — Définir les pièces exigées pour vérifier un lien et figer une preuve valide et une référence fictive introuvable.
- [`TASK-FIL-601-02`](../features/FEAT-FIL-601/tasks/TASK-FIL-601-02.md) — Préparer la matrice avec déclaration/proposition séparée de l'acceptation humaine et prévoir la correction du statut prématuré du MVP.
- [`TASK-FIL-601-03`](../features/FEAT-FIL-601/tasks/TASK-FIL-601-03.md) — Contrôler les pièces avec un pair, conserver les inconnues et vérifier qu'une référence non vide mais invalide ne suffit plus.

Aucune preuve d'acceptation de cette US n'est produite par son rendu. Les artefacts existants peuvent satisfaire un prérequis après revue ; aucune répétition de travaux déjà démontrés n'est imposée.

## Questions ouvertes

Voir [`AMB-16`](../../../governance/ambiguities.md#amb-16).
