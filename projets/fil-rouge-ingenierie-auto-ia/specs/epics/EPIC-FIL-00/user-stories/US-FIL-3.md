# US-FIL-3 — Établir la preuve d'un correctif borné

`Référence — spécification candidate`

- **Projet parent :** [`PROJ-FIL-AUTO-IA-001`](../../../../SPEC.md)
- **Epic parente :** [`EPIC-FIL-00`](../EPIC.md)
- **Feature fille :** [`FEAT-FIL-3`](../features/FEAT-FIL-3/FEATURE.md)
- **Jour :** `J01–J05`
- **Sources de formation :** [`C03`](../../../baseline/sources.md#c03) — `J03` / Reproduction, hypothèses concurrentes, rouge/vert comparable, mutation et documentation / `support_actuel`<br>[`C03-RETOUR`](../../../baseline/sources.md#c03-retour) — `J03` / Plan préalable, bornes et comparaisons des tests générés, concurrence, doubles, contrôles dans la chaîne / `retour_rapporte`<br>[`N03`](../../../baseline/sources.md#n03) — `J03` / Plan préalable, tests générés, scripts, qualité et organisation des spécifications ; propos à confirmer / `synthese_automatique`
- **Relation pédagogique :** Prérequis : preuve d'un correctif et hypothèses discriminées, au-delà des seules injections.
- **Niveau :** `Socle formation`
- **Priorité :** `P1`
- **Statut documentaire :** `Candidate`
- **Statut de preuve :** `Candidat`
- **Travail :** `À faire`
- **Responsable :** mainteneur — personne à désigner
- **Dépendances :** [`US-FIL-2`](US-FIL-2.md)
- **Ambiguïté :** [`AMB-21`](../../../governance/ambiguities.md#amb-21)

## Besoin

> En tant que mainteneur, je veux relier reproduction, hypothèses, correctif et tests discriminants afin de ne pas accepter un correctif convaincant mais non démontré.

## Périmètre

Chaîne de preuve générale J03, distincte de la régression hostile J07 ; aucune correction métier appliquée par la rédaction de cette US.

Les décisions restent humaines ; aucune implémentation métier n'est réalisée par cette spécification.

## Entrées et sorties

- **Entrée :** Cas autorisé avec version, entrée, conditions, attendu indépendant, observation et procédure de reproduction ; copie isolée pour la mutation.
- **Sortie :** Observations de reproduction, expérience discriminante, rouge/vert, non-régression et mutation ; proposition de correctif avec revue humaine.

Les baselines sont référencées dans [`sources.md`](../../../baseline/sources.md) ; leur révision est inconnue lorsqu'elle n'y est pas explicitement donnée. La sortie ne constitue pas, à elle seule, une preuve.

## Règle et critères

<a id="rm-fil-3"></a>
`RM-FIL-3` — Le succès d'un correctif exige le même attendu avant et après le changement et une preuve de sensibilité du test sur le chemin concerné.

<a id="ca-fil-3-01"></a>
- [ ] `CA-FIL-3-01` — Étant donné un défaut est reproduit sous un contrat figé, quand un correctif minimal est essayé, alors le même test échoue pour la cause étudiée avant et passe après, avec les cas voisins conservés.
<a id="ca-fil-3-02"></a>
- [ ] `CA-FIL-3-02` — Étant donné un mutant survit au test, quand le relecteur examine l'essai, alors la pertinence du mutant et le chemin exécuté sont investigués sans déclarer automatiquement un défaut produit.
<a id="ca-fil-3-03"></a>
- [ ] `CA-FIL-3-03` — Étant donné une assertion a été supprimée pour obtenir le vert, quand le dossier est revu, alors la preuve de correction est refusée car l'attendu a changé.
<a id="ca-fil-3-04"></a>
- [ ] `CA-FIL-3-04` — Étant donné deux causes plausibles prédisent des observations différentes, quand une expérience discriminante est exécutée ou fournie avec son mode, alors le résultat soutient ou réfute chaque hypothèse sans transformer une supposition en cause certaine.

## Example Mapping

| Cas | Étant donné | Quand | Alors |
|---|---|---|---|
| Nominal | un défaut est reproduit sous un contrat figé | un correctif minimal est essayé | le même test échoue pour la cause étudiée avant et passe après, avec les cas voisins conservés |
| Frontière | un mutant survit au test | le relecteur examine l'essai | la pertinence du mutant et le chemin exécuté sont investigués sans déclarer automatiquement un défaut produit |
| Refus | une assertion a été supprimée pour obtenir le vert | le dossier est revu | la preuve de correction est refusée car l'attendu a changé |
| Hypothèses | deux causes plausibles prédisent des observations différentes | une expérience discriminante est exécutée ou fournie avec son mode | le résultat soutient ou réfute chaque hypothèse sans transformer une supposition en cause certaine |

## Scénarios Gherkin

```gherkin
Fonctionnalité: Établir la preuve d'un correctif borné
  Contexte:
    Étant donné le périmètre et les entrées versionnées de US-FIL-3
    Et les attendus ci-dessous définis avant la future réalisation

  Scénario: Nominal — CA-FIL-3-01
    Étant donné un défaut est reproduit sous un contrat figé
    Quand un correctif minimal est essayé
    Alors le même test échoue pour la cause étudiée avant et passe après, avec les cas voisins conservés

  Scénario: Frontière — CA-FIL-3-02
    Étant donné un mutant survit au test
    Quand le relecteur examine l'essai
    Alors la pertinence du mutant et le chemin exécuté sont investigués sans déclarer automatiquement un défaut produit

  Scénario: Refus — CA-FIL-3-03
    Étant donné une assertion a été supprimée pour obtenir le vert
    Quand le dossier est revu
    Alors la preuve de correction est refusée car l'attendu a changé

  Scénario: Hypothèses — CA-FIL-3-04
    Étant donné deux causes plausibles prédisent des observations différentes
    Quand une expérience discriminante est exécutée ou fournie avec son mode
    Alors le résultat soutient ou réfute chaque hypothèse sans transformer une supposition en cause certaine
```

## Oracle indépendant

Contrat et observation initiale indépendants du patch ; comparaison des assertions et versions avant/après ; mutation dans une copie autorisée. Une erreur de compilation seule ne reproduit pas un défaut fonctionnel.

## Réalisation et preuves

- [`FEAT-FIL-3`](../features/FEAT-FIL-3/FEATURE.md) — Feature candidate
- [`TASK-FIL-3-01`](../features/FEAT-FIL-3/tasks/TASK-FIL-3-01.md) — Décrire attendu/observé et au moins deux hypothèses plausibles ; choisir l'expérience qui les départage.
- [`TASK-FIL-3-02`](../features/FEAT-FIL-3/tasks/TASK-FIL-3-02.md) — Conserver le rouge pertinent et le plan de correction limité au périmètre autorisé.
- [`TASK-FIL-3-03`](../features/FEAT-FIL-3/tasks/TASK-FIL-3-03.md) — Exécuter le même test après le patch et les tests voisins sans affaiblir leurs assertions.
- [`TASK-FIL-3-04`](../features/FEAT-FIL-3/tasks/TASK-FIL-3-04.md) — Éprouver le test par mutation, restaurer la copie puis confronter code, documentation et décision de revue.

Aucune preuve d'acceptation de cette US n'est produite par son rendu. Les artefacts existants peuvent satisfaire un prérequis après revue ; aucune répétition de travaux déjà démontrés n'est imposée.

## Questions ouvertes

Voir [`AMB-21`](../../../governance/ambiguities.md#amb-21).
