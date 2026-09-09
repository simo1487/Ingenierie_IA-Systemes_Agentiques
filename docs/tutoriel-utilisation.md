# Tutoriel — Utiliser FormationIaProject en équipe

## Objectif

Ce tutoriel montre comment trouver son projet, créer une expérimentation, transformer un résultat en code maintenu, lancer les contrôles et préparer une revue. Il s’adresse à tous les groupes, quel que soit le langage utilisé.

## 1. Se placer dans le dépôt

```bash
cd FormationIaProject
git status
git branch --show-current
```

Vérifier que la branche affichée correspond à son équipe dans [`travail.md`](../travail.md) :

| Équipe | Projet | Branche |
|---|---|---|
| Normes | `projets/normes/` | `feat/GetNormes` |
| Initialisation Normes | `projets/normes/experiments/initialisation-recherche/` | `feat/initSearchSystem` |
| Qualité du code | `projets/qualite-code/` | `feat_Cppcheck` |
| Logiciels open source | `projets/logiciel-automobile-open-source/` | `feat_list_existing_projects` |
| Exigences Zephyr | `projets/exigences-zephyr/` | `feat_getReq` |
| Intégration | `projets/socle-commun/` | `develop` |

Ne pas travailler directement sur `main`.

## 2. Trouver les informations utiles

Pour chaque tâche, suivre cet ordre :

1. Le [`README.md` racine](../README.md) explique le dépôt.
2. [`travail.md`](../travail.md) indique l’équipe et la branche.
3. `projets/<projet>/README.md` explique les commandes locales.
4. `projets/<projet>/SPEC.md` définit le périmètre et les critères d’acceptation.
5. [`workflows/README.md`](../workflows/README.md) indique la Gate et les étapes.
6. [`specs/templates/`](../specs/templates/) contient les modèles documentaires.

## 3. Installer les contrôles Git

Une seule fois après le clone :

```bash
make setup-hooks
```

Cette commande configure Git pour utiliser `.githooks/pre-commit`. Elle ne télécharge aucune dépendance.

Contrôle manuel de tout le dépôt :

```bash
make check
```

Contrôle des fichiers déjà ajoutés à l’index Git :

```bash
make check-staged
```

Le hook vérifie l’hygiène commune. Il ne compile pas tous les projets et ne remplace pas leurs tests fonctionnels.

## 4. Commencer une nouvelle expérimentation

Une expérimentation teste une seule hypothèse et ne doit pas être mélangée immédiatement au code maintenu.

Exemple pour l’équipe Qualité :

```bash
mkdir -p projets/qualite-code/experiments/2026-09-09-comparaison-cppcheck-clang-tidy
```

Créer ensuite :

```text
projets/qualite-code/experiments/2026-09-09-comparaison-cppcheck-clang-tidy/
├── README.md
├── sample/
└── results/
```

Le `README.md` de l’expérience contient :

```markdown
# Comparaison Cppcheck / clang-tidy

## Hypothèse
Cppcheck fournit un contrôle rapide utilisable avant commit sur la cible choisie.

## Baseline et entrées
- cible : à préciser ;
- commit : à préciser ;
- versions des outils : à préciser.

## Protocole
1. Exécuter chaque outil sur le même échantillon.
2. Injecter un défaut connu.
3. Comparer le code retour, le diagnostic et la durée.

## Commandes
À renseigner exactement.

## Résultats observés
À renseigner après exécution.

## Limites
À renseigner.

## Décision
Abandon / nouvel essai / promotion vers `src/`.
```

Une sortie d’IA est une proposition. Un rapport fourni est un rapport fourni. Seule une commande réellement exécutée et documentée produit une preuve d’exécution locale.

## 5. Organiser du code selon son langage

Chaque projet garde ses outils localement.

### Exemple Python

```text
projets/exigences-zephyr/
├── README.md
├── SPEC.md
├── pyproject.toml
├── src/
│   └── exigences_zephyr/
└── tests/
    └── test_extraction.py
```

Le README local indique par exemple :

```bash
python3 -m pytest
```

### Exemple C ou C++

```text
projets/qualite-code/
├── README.md
├── SPEC.md
├── CMakeLists.txt
├── src/
├── include/
└── tests/
```

Le README local indique par exemple :

```bash
cmake -S . -B build
cmake --build build
ctest --test-dir build
```

### Exemple JavaScript ou TypeScript

```text
projets/socle-commun/
├── README.md
├── SPEC.md
├── package.json
├── src/
└── tests/
```

Le README local indique les scripts réellement présents, par exemple `npm test`. Ne jamais supposer qu’un outil est installé sans vérifier les fichiers du projet.

## 6. Passer d’une expérience au code maintenu

Une expérience peut être promue vers `src/` uniquement si :

- le comportement attendu est décrit dans la spécification ;
- les inconnues et limites sont visibles ;
- un test discriminant existe ;
- la commande de test est reproductible ;
- les dépendances et versions sont documentées ;
- une revue humaine accepte la décision.

Séquence conseillée :

```text
hypothèse
→ expérience reproductible
→ décision humaine
→ critères d’acceptation
→ test rouge pertinent
→ code minimal
→ test vert
→ mutation ou faux correctif
→ revue
→ promotion dans src/
```

## 7. Préparer un commit

Examiner les modifications :

```bash
git status
git diff
git diff --check
```

Lancer d’abord les tests propres au projet, puis :

```bash
make check
git add <fichiers-concernés>
make check-staged
git diff --cached
```

Créer ensuite le commit lorsque le périmètre est cohérent. Ne pas mélanger dans un même commit :

- déplacement d’arborescence et changement fonctionnel ;
- résultats bruts volumineux et code ;
- plusieurs projets indépendants ;
- refactorisation et correction de bogue sans relation.

## 8. Préparer une revue

La demande de revue indique :

- la branche et le projet concernés ;
- la spécification et les critères couverts ;
- les fichiers modifiés ;
- les commandes exactes exécutées ;
- les résultats observés et codes retour ;
- les limites et questions ouvertes ;
- les fichiers que le relecteur doit examiner en priorité.

Le relecteur doit pouvoir reproduire les contrôles sans dépendre de l’historique d’une conversation IA.

## 9. Comprendre la migration des anciens dossiers

Les chemins historiques ne sont pas la structure définitive. Leur destination exacte est décrite dans [`docs/plan-migration.md`](plan-migration.md).

Résumé :

```text
normes-software-embarque-automobile/
  → projets/normes/{src,data,docs,evidence}/

Zephyr state of art/README.md
  → projets/logiciel-automobile-open-source/docs/etat-de-art-zephyr.md

template-feature-spec.md
  → specs/examples/FEAT-QUAL-001.md

projets/normes/initialisation-recherche/
  → projets/normes/experiments/initialisation-recherche/
```

Ces déplacements seront réalisés projet par projet, après intégration du socle et synchronisation des branches. En attendant, les nouveaux fichiers doivent déjà utiliser l’arborescence cible.

## 10. Les quatre règles à retenir pendant la réunion

1. **Un projet possède son propre espace, ses commandes et son langage.**
2. **Une expérimentation n’est pas encore du code maintenu.**
3. **Une sortie plausible n’est pas une preuve : source, commande et résultat doivent être visibles.**
4. **Le hook protège l’hygiène commune ; les tests métier restent locaux à chaque projet.**
