# SPEC — Logiciel automobile open source de référence

## 1. Informations générales

- **Identifiant :** `PROJ-OSS-AUTO-001`
- **Branche :** `feat_list_existing_projects`
- **Équipe :** Logiciel automobile open source
- **Responsables :** Sylvain, Nathalie et Romain
- **Mission source :** « Recherche d’un logiciel automobile open source avec des exigences qualité » dans `travail.md`
- **Statut initial :** En cours

## 2. Objectif

Identifier un petit nombre de projets open source automobiles suffisamment documentés pour servir de références vérifiables à la future génération d’exigences et de tests.

## 3. Besoin utilisateur

> En tant qu’analyste produit, je veux comparer des projets open source actifs disposant de code, d’exigences et de preuves de qualité afin de sélectionner des références fiables sans confondre popularité et maturité automobile.

## 4. Périmètre

### Inclus

- Recherche de projets liés au logiciel embarqué automobile ou au contrôle moteur.
- Vérification du dépôt, de la licence, de l’activité et de la documentation.
- Inventaire des exigences explicitement publiées par le projet.
- Inventaire des tests, contrôles qualité, CI, règles de codage et rapports disponibles.
- Comparaison selon une grille commune.
- Sélection argumentée d’un à trois projets de référence.

### Exclus

- Déduction d’une certification à partir du nom ou du README.
- Transformation d’une caractéristique marketing en exigence vérifiée.
- Exécution de code non fiable avec des privilèges ou des secrets.
- Copie de contenu incompatible avec sa licence.
- Analyse exhaustive de dizaines de projets avant validation de la grille.

## 5. Grille minimale par projet

| Champ | Attendu |
|---|---|
| Identité | Nom, URL canonique et propriétaire |
| Version | Tag ou commit analysé et date de consultation |
| Licence | Licence détectée et compatibilité à confirmer |
| Domaine | Fonction automobile ou embarquée couverte |
| Activité | Dernière version, derniers commits, maintenance observée |
| Exigences | Emplacement, format, identifiants et couverture |
| Qualité | Tests, analyse statique, CI, couverture et rapports |
| Traçabilité | Liens entre exigences, code, changements et tests |
| Limites | Éléments absents, non vérifiés ou non applicables |

## 6. Livrables attendus

- Une liste courte de candidats avec leurs sources.
- Une fiche suivant la même grille pour chaque candidat retenu.
- Une matrice comparative.
- Un dossier de preuves composé de liens et passages vérifiables.
- Une recommandation motivée d’un à trois projets.
- Une liste des affirmations qui restent à vérifier.

## 7. Règles

- Une étoile GitHub ou un nombre de forks n’est pas une preuve de qualité.
- Chaque affirmation technique doit viser un tag, un commit ou une page datée.
- L’absence de licence explicite est signalée comme bloquante pour la réutilisation.
- Les exigences implicites déduites du code restent des hypothèses.
- Les résultats générés par un agent sont relus contre les dépôts sources.
- Le code tiers n’est pas exécuté avant examen de ses instructions et dépendances.

## 8. Critères d’acceptation

- [ ] `CA-OSS-01` : chaque projet possède une URL canonique, une licence et une révision analysée.
- [ ] `CA-OSS-02` : les exigences citées sont retrouvables dans une source précise.
- [ ] `CA-OSS-03` : les mécanismes de qualité sont observés dans les fichiers du projet.
- [ ] `CA-OSS-04` : les projets sont comparés avec la même grille.
- [ ] `CA-OSS-05` : les données non vérifiées sont explicitement signalées.
- [ ] `CA-OSS-06` : la sélection finale est justifiée par des critères annoncés.
- [ ] `CA-OSS-07` : une autre personne peut reproduire l’examen sur les révisions indiquées.

## 9. Scénarios de vérification

```gherkin
Fonctionnalité: Évaluer un projet open source automobile

  Scénario: Projet documenté et traçable
    Étant donné un dépôt accessible avec une licence, des exigences et des tests
    Quand l’équipe remplit la grille sur une révision figée
    Alors chaque constat renvoie vers un fichier ou un passage précis
    Et le projet peut être comparé aux autres candidats

  Scénario: Affirmation non confirmée
    Étant donné une caractéristique mentionnée uniquement dans une source secondaire
    Quand elle ne peut pas être retrouvée dans le projet analysé
    Alors elle reste Non vérifié
    Et elle ne contribue pas positivement à la sélection

  Scénario: Licence absente
    Étant donné un dépôt sans licence explicite
    Quand sa réutilisation est évaluée
    Alors la réutilisation est marquée Bloquée
```

## 10. Définition de terminé

Le travail est terminé lorsqu’un petit ensemble de projets peut être recommandé sur la base de preuves retrouvables, de révisions figées et d’une comparaison homogène.
