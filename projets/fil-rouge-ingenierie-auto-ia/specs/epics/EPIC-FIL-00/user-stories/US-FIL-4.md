# US-FIL-4 — Préparer des passages autorisés et retrouvables

`Référence — spécification candidate`

- **Projet parent :** [`PROJ-FIL-AUTO-IA-001`](../../../../SPEC.md)
- **Epic parente :** [`EPIC-FIL-00`](../EPIC.md)
- **Feature fille :** [`FEAT-FIL-4`](../features/FEAT-FIL-4/FEATURE.md)
- **Jour :** `J01–J05`
- **Sources de formation :** [`C04`](../../../baseline/sources.md#c04) — `J04` / Corpus autorisé, découpage du sens, lexical/sémantique, Hit@k/MRR et support des citations / `support_actuel`<br>[`C04-RETOUR`](../../../baseline/sources.md#c04-retour) — `J04` / Requête directe avant modèle, questions attendues, empreintes, doublons et retrait des sources / `retour_rapporte`<br>[`N04`](../../../baseline/sources.md#n04) — `J04` / Questions avant IA, corpus, empreintes, Qdrant et parsing ; chiffres et décisions à confirmer / `synthese_automatique`
- **Relation pédagogique :** Prérequis : préparer et interroger les données avant moteur IA.
- **Niveau :** `Socle formation`
- **Priorité :** `P1`
- **Statut documentaire :** `Candidate`
- **Statut de preuve :** `Candidat`
- **Travail :** `À faire`
- **Responsable :** responsable de corpus — personne à désigner
- **Dépendances :** [`US-FIL-1`](US-FIL-1.md)
- **Ambiguïté :** [`AMB-22`](../../../governance/ambiguities.md#amb-22)

## Besoin

> En tant que responsable de corpus, je veux contrôler provenance, intégrité et découpage avant l'indexation afin de retrouver la règle avec ses conditions sans confondre identité et pertinence.

## Périmètre

Préparation locale J04, avec parsing/dédoublonnage adaptés aux sources ; Qdrant, Docling et suppression physique sont des choix non imposés.

Les décisions restent humaines ; aucune implémentation métier n'est réalisée par cette spécification.

## Entrées et sorties

- **Entrée :** Sources locales autorisées et révisées avec kind, statut, droit, empreinte de contenu et locator ; questions prévues et annotations candidates avant moteur.
- **Sortie :** Observation d'inventaire et passages avec id, texte, source, révision, locator, statut et accès ; doublons signalés et rejets de provenance visibles.

Les baselines sont référencées dans [`sources.md`](../../../baseline/sources.md) ; leur révision est inconnue lorsqu'elle n'y est pas explicitement donnée. La sortie ne constitue pas, à elle seule, une preuve.

## Règle et critères

<a id="rm-fil-4"></a>
`RM-FIL-4` — Un passage ne doit pas perdre la provenance, la condition ou l'exception nécessaires pour interpréter la règle extraite.

<a id="ca-fil-4-01"></a>
- [ ] `CA-FIL-4-01` — Étant donné la source fictive contient une règle et son exception, quand le découpage structurel est comparé à une découpe fixe, alors le contrôle vérifie que les passages utilisables conservent le sens et un locator résolvable.
<a id="ca-fil-4-02"></a>
- [ ] `CA-FIL-4-02` — Étant donné deux fichiers ont des octets identiques mais des provenances ou droits différents, quand les empreintes sont comparées, alors le doublon de contenu est signalé sans supprimer les provenances ni élargir les droits.
<a id="ca-fil-4-03"></a>
- [ ] `CA-FIL-4-03` — Étant donné la version ou le droit d'une source est inconnu, quand ses passages sont proposés au contexte, alors ils restent exclus du contexte probant jusqu'à décision.
<a id="ca-fil-4-04"></a>
- [ ] `CA-FIL-4-04` — Étant donné une source est retirée de l'usage autorisé, quand un nouveau contexte est préparé, alors ses passages ne sont plus transmis et les dérivés à invalider sont identifiés sans prétendre les avoir tous effacés.

## Example Mapping

| Cas | Étant donné | Quand | Alors |
|---|---|---|---|
| Nominal | la source fictive contient une règle et son exception | le découpage structurel est comparé à une découpe fixe | le contrôle vérifie que les passages utilisables conservent le sens et un locator résolvable |
| Frontière | deux fichiers ont des octets identiques mais des provenances ou droits différents | les empreintes sont comparées | le doublon de contenu est signalé sans supprimer les provenances ni élargir les droits |
| Refus | la version ou le droit d'une source est inconnu | ses passages sont proposés au contexte | ils restent exclus du contexte probant jusqu'à décision |
| Retrait | une source est retirée de l'usage autorisé | un nouveau contexte est préparé | ses passages ne sont plus transmis et les dérivés à invalider sont identifiés sans prétendre les avoir tous effacés |

## Scénarios Gherkin

```gherkin
Fonctionnalité: Préparer des passages autorisés et retrouvables
  Contexte:
    Étant donné le périmètre et les entrées versionnées de US-FIL-4
    Et les attendus ci-dessous définis avant la future réalisation

  Scénario: Nominal — CA-FIL-4-01
    Étant donné la source fictive contient une règle et son exception
    Quand le découpage structurel est comparé à une découpe fixe
    Alors le contrôle vérifie que les passages utilisables conservent le sens et un locator résolvable

  Scénario: Frontière — CA-FIL-4-02
    Étant donné deux fichiers ont des octets identiques mais des provenances ou droits différents
    Quand les empreintes sont comparées
    Alors le doublon de contenu est signalé sans supprimer les provenances ni élargir les droits

  Scénario: Refus — CA-FIL-4-03
    Étant donné la version ou le droit d'une source est inconnu
    Quand ses passages sont proposés au contexte
    Alors ils restent exclus du contexte probant jusqu'à décision

  Scénario: Retrait — CA-FIL-4-04
    Étant donné une source est retirée de l'usage autorisé
    Quand un nouveau contexte est préparé
    Alors ses passages ne sont plus transmis et les dérivés à invalider sont identifiés sans prétendre les avoir tous effacés
```

## Oracle indépendant

Source originale relue avec conditions et exceptions ; comparaison d'empreintes limitée à l'identité de contenu, jamais à la vérité. Requête directe et inspection du contexte avant tout branchement de modèle ; aucun seuil de similarité universel.

## Réalisation et preuves

- [`FEAT-FIL-4`](../features/FEAT-FIL-4/FEATURE.md) — Feature candidate
- [`TASK-FIL-4-01`](../features/FEAT-FIL-4/tasks/TASK-FIL-4-01.md) — Figer l'inventaire autorisé, les locators et les questions avant moteur ; identifier les règles dont le découpage peut perdre le sens.
- [`TASK-FIL-4-02`](../features/FEAT-FIL-4/tasks/TASK-FIL-4-02.md) — Préparer les passages, empreintes et signalements de doublons, sans fusion automatique de versions ou de droits distincts.
- [`TASK-FIL-4-03`](../features/FEAT-FIL-4/tasks/TASK-FIL-4-03.md) — Contrôler manuellement les locators et une requête directe ; vérifier exclusion d'une source retirée et lister les dérivés concernés.

Aucune preuve d'acceptation de cette US n'est produite par son rendu. Les artefacts existants peuvent satisfaire un prérequis après revue ; aucune répétition de travaux déjà démontrés n'est imposée.

## Questions ouvertes

Voir [`AMB-22`](../../../governance/ambiguities.md#amb-22).
