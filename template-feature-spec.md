# Template de spécification de feature

> Template neutre à copier pour décrire une feature. Remplacer les éléments entre crochets et supprimer les sections inutiles.

## 1. Informations générales

- **Identifiant :** `[FEAT-XXX]`
- **Nom de la feature :** `[Nom court et explicite]`
- **Responsable(s) :** `[Nom ou équipe]`
- **Priorité :** `[P0 / P1 / P2]`
- **Statut :** `[Proposée / En cours / À revoir / Terminée]`
- **Date :** `[AAAA-MM-JJ]`

## 2. Objectif

Décrire en une ou deux phrases le résultat attendu et la valeur apportée.

> Cette feature permet de `[résultat attendu]` afin de `[valeur ou problème résolu]`.

## 3. Besoin utilisateur

> En tant que `[type d'utilisateur]`, je veux `[action ou capacité]`, afin de `[bénéfice attendu]`.

## 4. Contexte et problème

- **Situation actuelle :** `[Décrire le fonctionnement ou la difficulté actuelle]`
- **Problème rencontré :** `[Décrire le problème observable]`
- **Décision qui reste humaine :** `[Décision qui ne doit pas être déléguée au système]`
- **Question ouverte :** `[Information manquante ou décision à prendre]`

## 5. Périmètre

### Inclus

- `[Élément inclus 1]`
- `[Élément inclus 2]`
- `[Élément inclus 3]`

### Exclus

- `[Élément explicitement hors périmètre 1]`
- `[Élément explicitement hors périmètre 2]`

## 6. Entrées

| Entrée | Source | Version / date | Statut | Accès autorisé |
|---|---|---|---|---|
| `[Donnée, fichier ou ressource]` | `[Source]` | `[Version / date]` | `[Draft / validé / à vérifier]` | `[Lecture / écriture]` |

## 7. Sorties attendues

- `[Livrable ou résultat 1]`
- `[Livrable ou résultat 2]`
- `[Livrable ou résultat 3]`

Pour chaque sortie, préciser si elle constitue :

- une **proposition** ;
- une **observation** ;
- une **preuve vérifiée** ;
- une **question ouverte**.

## 8. Règles métier et contraintes

- `[Règle métier 1]`
- `[Règle métier 2]`
- `[Contrainte technique, réglementaire ou organisationnelle]`
- `[Permission ou limite de sécurité]`

## 9. Critères d'acceptation

- [ ] `[Critère observable et vérifiable 1]`
- [ ] `[Critère observable et vérifiable 2]`
- [ ] `[Critère observable et vérifiable 3]`
- [ ] `[Les sources, versions et statuts sont conservés]`
- [ ] `[Les informations inconnues restent explicitement ouvertes]`
- [ ] `[Aucune preuve ou conformité n'est revendiquée sans vérification]`

## 10. Scénarios Gherkin

```gherkin
Fonctionnalité: [Nom de la fonctionnalité]

  Contexte:
    Étant donné [contexte initial commun]
    Et [précondition commune]

  Scénario: [Cas nominal]
    Étant donné [état initial]
    Quand [action réalisée]
    Alors [résultat observable attendu]
    Et [règle ou contrainte vérifiée]

  Scénario: [Cas frontière ou limite]
    Étant donné [état à la limite]
    Quand [action réalisée]
    Alors [résultat observable attendu]

  Scénario: [Cas d'erreur, de refus ou d'information manquante]
    Étant donné [situation invalide, interdite ou incomplète]
    Quand [action réalisée]
    Alors [refus, erreur ou question ouverte observable]
```

### Couverture des scénarios

| Scénario | Critère couvert | Source de l'attendu | Oracle / observation | Statut |
|---|---|---|---|---|
| `[Nom du scénario]` | `[CA-XX]` | `[Source et passage]` | `[Ce qui permet de contredire le résultat]` | `[Candidat / vérifié / ouvert]` |

## 11. Traçabilité

| Élément | Source ou identifiant | Relation | Preuve / passage | Statut |
|---|---|---|---|---|
| `[Exigence]` | `[Référence]` | `[Vers règle, documentation, code ou test]` | `[Lien ou extrait court]` | `[Vérifié / candidat / non trouvé / non applicable]` |

> Une proximité de vocabulaire, un nom de fichier ou la présence d'un test ne suffit pas à prouver une relation.

## 12. Vérification

Décrire comment une autre personne peut vérifier la feature sans dépendre d'une interprétation implicite.

1. `[Étape de vérification 1]`
2. `[Étape de vérification 2]`
3. `[Étape de vérification 3]`

- **Environnement :** `[Version, outil ou configuration]`
- **Données utilisées :** `[Données autorisées]`
- **Résultat attendu :** `[Résultat observable]`
- **Limites de la vérification :** `[Ce qui n'est pas démontré]`

## 13. Dépendances et risques

### Dépendances

- `[Feature, équipe, donnée ou décision nécessaire]`

### Risques

| Risque | Impact | Probabilité | Mesure de maîtrise | Responsable |
|---|---|---|---|---|
| `[Risque identifié]` | `[Faible / moyen / fort]` | `[Faible / moyen / fort]` | `[Action]` | `[Nom]` |

## 14. Décision de revue

- **Relecteur(s) :** `[Nom ou équipe]`
- **Date de revue :** `[AAAA-MM-JJ]`
- **Décision :** `[Acceptée / À corriger / Bloquée]`
- **Corrections demandées :** `[Liste des corrections]`
- **Points restant ouverts :** `[Liste des questions]`

## Checklist finale

- [ ] Le besoin utilisateur est compréhensible.
- [ ] Le périmètre et les exclusions sont explicites.
- [ ] Les entrées et leurs versions sont identifiées.
- [ ] Les sorties sont distinguées des preuves.
- [ ] Les critères d'acceptation sont observables.
- [ ] Il existe au moins un scénario nominal.
- [ ] Il existe au moins un scénario frontière, erreur ou refus.
- [ ] Chaque scénario possède un attendu et un oracle.
- [ ] Les relations de traçabilité sont sourcées.
- [ ] Les inconnues ne sont pas inventées.
- [ ] La vérification est reproductible par une autre personne.
- [ ] Les limites et risques sont documentés.
