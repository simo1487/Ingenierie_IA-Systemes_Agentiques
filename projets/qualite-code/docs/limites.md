# Limites et exclusions - PROJ-QUAL-001

## 1. Limites de la chaîne de contrôles

### 1.1 Limites de la cible (fixtures)

| Limite | Description | Impact |
|---|---|---|
| **Portée réduite** | Les fixtures sont des fichiers de test simples, pas du code de production | La chaîne n'est pas validée sur du code complexe |
| **Absence de tests dynamiques** | Les fixtures n'incluent pas de tests unitaires ou d'intégration | La lacune est documentée mais non testée |
| **Complexité limitée** | Pas de multi-threading, de templates C++ ou de méta-programmation | Certains types de défauts ne sont pas testés |
| **Build simple** | Pas de système de build complexe (Make, CMake, autotools) | L'intégration avec des systèmes de build réels n'est pas testée |

### 1.2 Limites des outils

#### Cppcheck
| Limite | Description | Impact |
|---|---|---|
| **Faux positifs** | Peut signaler des problèmes inexistants sur code simple | Nécessite une revue humaine pour trier les faux positifs |
| **Analyse inter-procédures limitée** | Ne suit pas tous les chemins d'exécution complexes | Certains défauts peuvent être manqués |
| **Pas d'analyse de data flow** | Analyse principalement statique sans exécution | Dépendances d'exécution non détectées |
| **Support C++ incomplet** | Support partiel des fonctionnalités C++ modernes | Limité pour les projets C++ récents |

#### Clang-tidy
| Limite | Description | Impact |
|---|---|---|
| **Dépendance LLVM** | Nécessite une installation de LLVM complète | Installation plus lourde que Cppcheck |
| **Configuration complexe** | Beaucoup d'options et de checks disponibles | Courbe d'apprentissage élevée |
| **Focus sur C++** | Optimisé pour C++, support C limité | Moins efficace pour les projets C purs |
| **Faux positifs sur code ancien** | Peut signaler des problèmes sur code legacy | Nécessite des exclusions spécifiques |

#### AddressSanitizer (ASan)
| Limite | Description | Impact |
|---|---|---|
| **Surcoût mémoire** | Utilise jusqu'à 2x plus de mémoire | Problématique pour les gros projets |
| **Nécessite recompilation** | Doit être activé à la compilation | Ne fonctionne pas sur binaires existants |
| **Non disponible sur vieux compilateurs** | Nécessite GCC 11+ ou Clang 12+ | Problème pour les projets avec vieux toolchains |
| **Interaction avec d'autres sanitizers** | Certains mélanges sont instables | Tests séparés nécessaires |

#### LeakSanitizer (LSan)
| Limite | Description | Impact |
|---|---|---|
| **Fuites indirectes** | Peut manquer certaines fuites indirectes | Couverture incomplète |
| **Faux positifs avec malloc hooks** | Peut confondre certaines allocations légitimes | Nécessite configuration spécifique |
| **Limité à l'exécution** | Ne détecte que les fuites effectivement exécutées | Code mort non testé |

### 1.3 Limites de l'environnement

| Limite | Description | Impact |
|---|---|---|
| **Windows focus** | Scripts PowerShell optimisés pour Windows | Linux/macOS nécessitent des adaptations |
| **Pas de conteneurisation** | Pas d'image Docker fournie | Reproductibilité dépendante de l'environnement local |
| **Pas d'intégration CI** | Pas de configuration GitHub Actions/GitLab CI fournie | Intégration manuelle nécessaire |
| **Dépendances système** | Nécessite installation des outils sur chaque machine | Setup complexe pour les nouveaux contributeurs |

## 2. Exclusions documentées

### 2.1 Exclusions Cppcheck

Actuellement, aucune exclusion n'est configurée. Les exclusions suivantes pourront être ajoutées si nécessaire :

```cpp
// Exemple : Exclure les warnings sur du code legacy
// cppcheck-suppress: unusedVariable
// cppcheck-suppress: missingIncludeSystem
```

### 2.2 Exclusions Clang-tidy

Actuellement, aucune exclusion n'est configurée. Les exclusions suivantes pourront être ajoutées si nécessaire :

```yaml
# Exemple : .clang-tidy
Checks: '-*,clang-analyzer-*'
WarningsAsErrors: ''
HeaderFilterRegex: ''
```

### 2.3 Exclusions ASan/LSan

Actuellement, aucune exclusion n'est configurée. Les exclusions suivantes pourront être ajoutées si nécessaire :

```bash
# Exemple : ASAN_OPTIONS
ASAN_OPTIONS=detect_leaks=1:halt_on_error=0:suppressions=my_suppressions.txt
```

## 3. Faux positifs connus

### 3.1 Cppcheck

| Faux positif | Contexte | Action |
|---|---|---|
| **Variable inutilisée** | Variables déclarées pour debug ou futures utilisations | Ignorer ou supprimer si confirmé |
| **Include manquant** | Headers inclus via autres headers | Documenter dans exclusion |
| **Style warnings** | Préférences de style personnelles | Configurer selon les standards du projet |

### 3.2 Clang-tidy

| Faux positif | Contexte | Action |
|---|---|---|
| **Modernize-* checks** | Code legacy C/C++ | Désactiver si non applicable |
| **Performance warnings** | Optimisations prématurées | Ignorer si non critique |
| **C++11 features** | Code C pur | Désactiver les checks C++ |

### 3.3 ASan/LSan

| Faux positif | Contexte | Action |
|---|---|---|
| **Fuites de bibliothèques tierces** | Bibliothèques avec fuites connues | Exclure via suppressions |
| **Initialisation tardive** | Globales initialisées après main | Configurer ASAN_OPTIONS |
| **Allocations système** | Allocations spécifiques à l'OS | Exclure si nécessaire |

## 4. Éléments non testés

### 4.1 Types de défauts non testés

| Type de défaut | Pourquoi non testé | Comment tester |
|---|---|---|
| **Data races** | Fixtures sans multi-threading | Ajouter fixture avec threads |
| **Deadlocks** | Fixtures sans multi-threading | Ajouter fixture avec mutex |
| **Integer overflow** | Fixtures sans calculs complexes | Ajouter fixture arithmétique |
| **Format string vulnerabilities** | Fixtures avec printf simple | Ajouter fixture avec user input |
| **Use-after-return** | Complexité des fixtures | Ajouter fixture spécifique |
| **Memory leaks indirectes** | Fixtures simples | Ajouter fixture avec allocations complexes |

### 4.2 Environnements non testés

| Environnement | Pourquoi non testé | Comment tester |
|---|---|---|
| **Linux** | Focus initial sur Windows | Tester sur WSL ou machine Linux |
| **macOS** | Pas d'accès à macOS | Tester via contributeur macOS |
| **Docker** | Non prioritaire pour prototype | Créer Dockerfile |
| **CI/CD** | Non prioritaire pour prototype | Configurer GitHub Actions |

### 4.3 Scénarios non testés

| Scénario | Pourquoi non testé | Comment tester |
|---|---|---|
| **Gros projet** | Fixtures simples | Tester sur projet réel équipe 3 |
| **Code C++ moderne** | Fixtures C11 | Ajouter fixtures C++17/20 |
| **Système de build complexe** | Compilation directe | Intégrer avec CMake |
| **Dépendances externes** | Fixtures autonomes | Tester avec bibliothèques |

## 5. Déviations acceptées

### 5.1 Déviations par rapport à la SPEC

| Déviation | Justification | Impact |
|---|---|---|
| **Cible = fixtures au lieu de projet réel** | Permet de valider la chaîne sans dépendance externe | Limité pour l'application immédiate sur projet réel |
| **Clang-tidy optionnel dans profil rapide** | Réduit la dépendance pour le profil rapide | Moins de couverture dans le profil rapide |
| **Pas de tests unitaires dans fixtures** | Focus sur analyse statique/dynamique | Lacune documentée (CA-QUAL-08) |

### 5.2 Déviations par rapport aux meilleures pratiques

| Déviation | Justification | Impact |
|---|---|---|
| **Pas de conteneurisation** | Priorité au prototype fonctionnel | Reproductibilité dépendante de l'environnement |
| **Scripts PowerShell uniquement** | Environnement Windows principal | Non portable Linux/macOS sans adaptation |
| **Pas de configuration CI/CD** | Prototype local | Intégration manuelle nécessaire |

## 6. Recommandations pour améliorations futures

### 6.1 Améliorations à court terme

1. **Ajouter des fixtures C++** pour tester les fonctionnalités C++ modernes
2. **Créer des scripts Bash** pour Linux/macOS
3. **Ajouter une image Docker** pour garantir la reproductibilité
4. **Implémenter des tests unitaires** dans les fixtures

### 6.2 Améliorations à moyen terme

1. **Intégrer avec un projet réel** de l'équipe 3
2. **Configurer GitHub Actions** pour l'intégration continue
3. **Ajouter Valgrind** comme alternative à ASan/LSan
4. **Implémenter un système de suppressions** partagé

### 6.3 Améliorations à long terme

1. **Étendre à d'autres langages** (Python, Java, etc.)
2. **Intégrer SonarQube** pour les gros projets
3. **Automatiser la revue des faux positifs** avec ML
4. **Créer un dashboard** de suivi de la qualité

## 7. Décisions humaines requises

### 7.1 Validation des limites

- [ ] Les limites documentées sont acceptables pour le prototype
- [ ] Les exclusions proposées sont pertinentes
- [ ] Les éléments non testés sont justifiés

### 7.2 Autorisation de passage

- [ ] L'équipe qualité (Eric, Céline, Damien) valide les limites
- [ ] Les déviations par rapport à la SPEC sont acceptées
- [ ] Le profil peut être utilisé malgré les limites connues

## 8. Statut

- **Limites de la cible** : ✅ Documentées
- **Limites des outils** : ✅ Documentées
- **Exclusions** : ✅ Documentées (aucune active)
- **Faux positifs** : ✅ Documentés
- **Éléments non testés** : ✅ Documentés
- **Déviations** : ✅ Documentées
- **Validation humaine** : ⏳ En attente