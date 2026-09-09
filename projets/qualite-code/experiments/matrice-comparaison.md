# Matrice de comparaison des outils de contrôle qualité

## 1. Outils statiques (Static Analysis)

| Outil | Version | Licence | Commande | Couverture | Avantages | Inconvénients | Statut |
|---|---|---|---|---|---|---|---|
| **Cppcheck** | 2.13+ | GPL-3.0 | `cppcheck fichiers.c` | C/C++, détecte bugs, style, performance, portabilité | Léger, rapide, facile à installer, détecte de nombreux types de défauts | Faux positifs possibles, moins profond que les outils de compilateur | ✅ Sélectionné |
| **Clang Static Analyzer** (scan-build/clang-tidy) | LLVM 19.0+ | Apache-2.0 | `scan-build gcc fichier.c` ou `clang-tidy fichier.c` | C/C++, Objective-C, détecte bugs sérieux, fuites de mémoire | Profond, intégré à LLVM, détecte null pointer, leaks, race conditions | Nécessite LLVM/Clang, pas de couverture style/complexité | 🔄 Candidat |
| **GCC/Clang warnings** | GCC 11+, Clang 12+ | GPL-3.0 / NCSA | `gcc -Wall -Wextra -Werror fichier.c` | C/C++, avertissements compilateur | Intégré au build, rapide, détecte erreurs classiques | Moins profond que les outils dédiés, limité aux avertissements standards | 🔄 Candidat |
| **SonarQube** | 9.9+ | LGPL-3.0 | `sonar-scanner` | 30+ langages, bugs, vulnérabilités, code smells, duplications | Plateforme complète, CI/CD, multi-langages, interface web | Lourd, nécessite serveur, courbe d'apprentissage, surdimensionné pour prototype | ❌ Exclu (trop lourd) |

## 2. Outils dynamiques (Dynamic Analysis)

| Outil | Version | Licence | Commande | Couverture | Avantages | Inconvénients | Statut |
|---|---|---|---|---|---|---|---|
| **AddressSanitizer (ASan)** | GCC 11+, Clang 12+ | GPL-3.0 / NCSA | `gcc -fsanitize=address fichier.c` | C/C++, buffer overflow, use-after-free, double free | Rapide (2-4x), intégré au compilateur, détecte stack/global OOB | Nécessite recompilation, pas disponible sur tous les compilateurs anciens | ✅ Sélectionné |
| **LeakSanitizer (LSan)** | GCC 11+, Clang 12+ | GPL-3.0 / NCSA | `gcc -fsanitize=leak fichier.c` | C/C++, fuites de mémoire | Très rapide (quasi gratuit), intégré au compilateur | Peut être combiné avec ASan, limité aux fuites | ✅ Sélectionné |
| **Valgrind (Memcheck)** | 3.19+ | GPL-2.0 | `valgrind ./programme` | C/C++, memory errors, leaks, uninitialized reads | Fonctionne sur binaire non modifié, très complet | Très lent (20-50x), usage intensif CPU, limité multi-threading | 🔄 Candidat |
| **ThreadSanitizer (TSan)** | GCC 11+, Clang 12+ | GPL-3.0 / NCSA | `gcc -fsanitize=thread fichier.c` | C/C++, data races, deadlocks | Détecte data races (5-15x), support multi-threading | Nécessite recompilation, surcoût mémoire (10x) | ❌ Exclu (prototype sans multi-threading) |

## 3. Résumé de la sélection

### Outils statiques sélectionnés
1. **Cppcheck** - Outil principal, rapide et léger
2. **Clang Static Analyzer (clang-tidy)** - Analyse approfondie complémentaire

### Outils dynamiques sélectionnés
1. **AddressSanitizer (ASan)** - Détection rapide des erreurs mémoire
2. **LeakSanitizer (LSan)** - Détection des fuites de mémoire

### Outils candidats (alternatives)
- **GCC/Clang warnings** - Peut être ajouté facilement si nécessaire
- **Valgrind** - Alternative si ASan/LSan ne sont pas disponibles

### Outils exclus
- **SonarQube** - Trop lourd pour le prototype, nécessite infrastructure serveur
- **ThreadSanitizer** - Prototype sans multi-threading, surcoût injustifié

## 4. Justification de la sélection

### Pourquoi Cppcheck + Clang Static Analyzer ?
- **Complémentarité** : Cppcheck est rapide et détecte de nombreux défauts de style/performance, Clang détecte des bugs plus sérieux (null pointer, leaks)
- **Légèreté** : Les deux sont des outils ligne de commande, pas d'infrastructure serveur
- **Compatibilité** : Les deux supportent C11 et sont disponibles sur Windows/Linux

### Pourquoi ASan + LSan ?
- **Performance** : 2-4x plus rapide que Valgrind, respecte le budget < 30s pour le profil rapide
- **Intégration** : Directement intégré à GCC/Clang, pas d'installation supplémentaire
- **Couverture** : ASan détecte les erreurs mémoire courantes, LSan détecte les fuites
- **Alternative à Valgrind** : Moins de surcoût, meilleur pour CI/CD

### Pourquoi exclure SonarQube ?
- **Surdimensionnement** : Plateforme serveur complète, inutile pour prototype de fixtures
- **Complexité** : Nécessite infrastructure, base de données, configuration
- **Budget temps** : Installation et configuration > 30s, incompatible avec profil rapide

### Pourquoi exclure ThreadSanitizer ?
- **Non applicable** : Les fixtures n'ont pas de multi-threading
- **Surcoût** : 10x mémoire, 5-15x CPU, injustifié pour le prototype

## 5. Observations reproductibles

### Test réalisé : Installation et exécution de Cppcheck
- **Commande** : `cppcheck --version`
- **Résultat** : Cppcheck 2.13 installé et fonctionnel
- **Code retour** : 0 (succès)
- **Preuve** : Script run-cppcheck.ps1 fonctionnel

### Test à réaliser : Clang Static Analyzer
- **Commande** : `clang-tidy --version` ou `scan-build --help`
- **Attendu** : Détection de clang-tidy ou scan-build
- **Résultat** : À documenter après installation

### Test à réaliser : AddressSanitizer
- **Commande** : `gcc -fsanitize=address tests/fixtures/main.c -o main.exe && ./main.exe`
- **Attendu** : Compilation réussie, exécution sans erreur (code propre)
- **Résultat** : À documenter après test

## 6. Budget de temps estimé

| Profil | Outils | Durée estimée | Budget |
|---|---|---|---|
| **Rapide** | Cppcheck seul | < 10s | ✅ < 30s |
| **Rapide** | Cppcheck + Clang-tidy | < 20s | ✅ < 30s |
| **Complet** | Cppcheck + Clang-tidy + ASan + LSan | < 2min | ✅ < 5min |
| **Complet** | + Valgrind (optionnel) | < 5min | ✅ < 5min |

## 7. Limites connues

| Limite | Outil | Description |
|---|---|---|
| **Faux positifs** | Cppcheck | Peut signaler des problèmes inexistants sur code simple |
| **Dépendance compilateur** | ASan/LSan | Nécessite GCC 11+ ou Clang 12+ |
| **Windows** | Valgrind | Difficile à installer sur Windows (préférence WSL) |
| **Répertoire vide** | Tous outils | Doit retourner un état explicite, pas un succès silencieux |

## 8. Décision humaine requise

**Validation de la sélection :**
- Cppcheck + Clang-tidy + ASan + LSan est-il acceptable pour le prototype ?
- Faut-il ajouter GCC/Clang warnings (-Wall -Wextra) ?
- Faut-il inclure Valgrind malgré le surcoût ?

**Réponse attendue :** À confirmer par l'équipe qualité (Eric, Céline, Damien)