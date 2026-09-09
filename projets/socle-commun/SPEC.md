# SPEC — Socle commun et intégration

## 1. Informations générales

- **Identifiant :** `PROJ-SOCLE-001`
- **Branche :** `develop`
- **Responsable :** responsable d’intégration du dépôt
- **Contributeurs :** les quatre équipes décrites dans `travail.md`
- **Statut initial :** À organiser

## 2. Objectif

Maintenir une base commune stable dans laquelle les livrables des équipes peuvent être examinés, vérifiés et intégrés sans mélanger les responsabilités ni perdre la provenance des informations.

## 3. Périmètre

### Inclus

- Définition de l’arborescence commune des projets.
- Mise à disposition des spécifications de chaque équipe.
- Revue de la structure, des sources et des statuts de vérification.
- Intégration des branches après satisfaction de leurs critères d’acceptation.
- Conservation d’un historique Git lisible.

### Exclus

- Réalisation à la place des équipes de leurs recherches spécialisées.
- Validation réglementaire ou certification des résultats.
- Fusion d’un contenu dont la provenance ou le statut n’est pas explicite.

## 4. Entrées

- Les missions de `travail.md`.
- Les spécifications présentes sous `projets/`.
- Les pull requests ou différences de chaque branche de travail.
- Les résultats de vérification fournis par les équipes.

## 5. Sorties attendues

- Une arborescence cohérente et documentée.
- Une spécification dédiée pour chaque branche hors `main`.
- Des branches resynchronisées avant intégration.
- Une revue indiquant ce qui est accepté, refusé ou encore ouvert.
- Un `develop` ne contenant pas de conflit ni de livrable non attribué.

## 6. Règles

- `main` ne reçoit pas directement les travaux d’atelier.
- Chaque branche doit avoir un objectif unique et un propriétaire identifié.
- Une fusion ne transforme pas une proposition en information vérifiée.
- Les conflits sont résolus en conservant la provenance et les décisions de revue.
- Les artefacts générés, caches et fichiers personnels restent hors du dépôt.

## 7. Critères d’acceptation

- [ ] `CA-SOCLE-01` : chaque mission de `travail.md` est reliée à une branche et à une spécification.
- [ ] `CA-SOCLE-02` : chaque spécification définit des livrables observables et des limites.
- [ ] `CA-SOCLE-03` : chaque branche candidate est à jour avec `develop` au moment de la revue.
- [ ] `CA-SOCLE-04` : les fichiers intégrés passent les contrôles de format ou de syntaxe applicables.
- [ ] `CA-SOCLE-05` : les sources et statuts de vérification sont conservés.
- [ ] `CA-SOCLE-06` : aucune revendication de conformité non démontrée n’est intégrée.
- [ ] `CA-SOCLE-07` : la décision d’intégration et les questions ouvertes sont consignées.

## 8. Scénarios de vérification

```gherkin
Fonctionnalité: Intégrer un livrable d’équipe

  Scénario: Livrable prêt pour la revue
    Étant donné une branche synchronisée avec develop
    Et des livrables conformes à sa spécification
    Quand le responsable examine les sources, les statuts et les contrôles
    Alors il peut reproduire la vérification
    Et consigner une décision d’intégration

  Scénario: Provenance insuffisante
    Étant donné un document contenant une affirmation sans source identifiable
    Quand la branche est examinée
    Alors l’affirmation reste non vérifiée
    Et la branche n’est pas présentée comme validée
```

## 9. Définition de terminé

Le socle est prêt lorsque les quatre projets ont une spécification, que leurs livrables sont attribuables et vérifiables, et que leur intégration peut être décidée sans information implicite.
