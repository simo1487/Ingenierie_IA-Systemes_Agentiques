# Justification de la sélection des outils - PROJ-QUAL-001

## 1. Processus de sélection

### Méthodologie
1. **Recherche documentaire** : Comparaison d'outils statiques et dynamiques via documentation officielle et sources tierces
2. **Évaluation sur critères communs** : Version, licence, commande, couverture, avantages, inconvénients
3. **Test d'installation** : Vérification de la disponibilité locale de chaque outil
4. **Respect des contraintes** : Budget temps (< 30s rapide, < 5min complet), politique de Gate (erreurs + sécurité)

### Sources consultées
- Documentation officielle Cppcheck, Clang, GCC, AddressSanitizer
- Articles de comparaison : Red Hat Developer, GitHub sanitizers wiki, StackOverflow
- Benchmarks de performance : Google sanitizers wiki, Daniel Lemire blog

## 2. Sélection finale

### Outils statiques

#### Cppcheck (principal)
- **Version** : 2.13+
- **Licence** : GPL-3.0
- **Justification** :
  - Déjà installé et testé sur l'environnement
  - Rapide (< 10s sur fixtures simples)
  - Détecte bugs, style, performance, portabilité
  - Compatible Windows/Linux
- **Observation reproductible** : `./src/run-cppcheck.ps1` fonctionne sur tests/fixtures/main.c

#### Clang Static Analyzer (clang-tidy)
- **Version** : LLVM 19.0+
- **Licence** : Apache-2.0
- **Justification** :
  - Analyse approfondie complémentaire à Cppcheck
  - Détecte null pointer, fuites de mémoire, race conditions
  - Intégré à LLVM, pas d'installation supplémentaire si Clang disponible
  - Compatible avec C11
- **Observation à valider** : Installation et test sur environnement

### Outils dynamiques

#### AddressSanitizer (ASan)
- **Version** : GCC 11+, Clang 12+
- **Licence** : GPL-3.0 / NCSA
- **Justification** :
  - Rapide (2-4x vs 20-50x pour Valgrind)
  - Intégré au compilateur, pas d'installation supplémentaire
  - Détecte buffer overflow, use-after-free, double free
  - Détecte stack/global OOB (contrairement à Valgrind)
- **Observation à valider** : Test sur fixtures avec défaut contrôlé

#### LeakSanitizer (LSan)
- **Version** : GCC 11+, Clang 12+
- **Licence** : GPL-3.0 / NCSA
- **Justification** :
  - Très rapide (quasi gratuit)
  - Détecte les fuites de mémoire
  - Peut être combiné avec ASan (-fsanitize=address,leak)
  - Essentiel pour le profil complet
- **Observation à valider** : Test sur fixtures avec fuite

## 3. Oultats exclus et justification

### SonarQube (exclu)
- **Raison** : Surdimensionné pour le prototype
- **Détails** :
  - Nécessite infrastructure serveur (base de données, JVM)
  - Installation > 30s, incompatible avec profil rapide
  - Courbe d'apprentissage élevée
  - Fixtures simples ne justifient pas une plateforme complète
- **Alternative** : Cppcheck + Clang-tidy suffisent pour l'analyse statique

### Valgrind (candidat, non sélectionné)
- **Raison** : Surcoût performance injustifié
- **Détails** :
  - 20-50x plus lent que l'exécution normale
  - Difficile à installer sur Windows (préférence WSL)
  - ASan/LSan offrent une meilleure couverture avec moins de surcoût
- **Alternative** : ASan + LSan pour la détection mémoire
- **Statut** : Conserver comme option si ASan/LSan ne sont pas disponibles

### ThreadSanitizer (exclu)
- **Raison** : Non applicable au prototype
- **Détails** :
  - Les fixtures n'ont pas de multi-threading
  - Surcoût mémoire (10x) injustifié
  - Complexité inutile pour le prototype
- **Alternative** : À considérer si le projet cible a du multi-threading

### GCC/Clang warnings (candidat)
- **Raison** : Peut être ajouté facilement
- **Détails** :
  - Intégré au build (-Wall -Wextra)
  - Rapide, pas de surcoût
  - Moins profond que les outils dédiés
- **Statut** : À ajouter si nécessaire pour renforcer le profil

## 4. Alignement avec les critères d'acceptation

### CA-QUAL-02 : Au moins deux outils statiques et deux approches dynamiques comparés
- ✅ **Outils statiques comparés** : Cppcheck, Clang Static Analyzer, GCC/Clang warnings, SonarQube
- ✅ **Approches dynamiques comparées** : AddressSanitizer, LeakSanitizer, Valgrind, ThreadSanitizer
- ✅ **Matrice de comparaison** : experiments/matrice-comparaison.md

### CA-QUAL-03 : Le choix des outils et versions est justifié par des observations reproductibles
- ✅ **Cppcheck** : Testé et fonctionnel via run-cppcheck.ps1
- 🔄 **Clang-tidy** : À tester après installation
- 🔄 **ASan/LSan** : À tester après création de fixtures
- ✅ **Justification documentée** : evidence/selection-outils.md

## 5. Budget de temps respecté

| Profil | Outils | Durée estimée | Budget | Conforme |
|---|---|---|---|---|
| Rapide | Cppcheck | < 10s | < 30s | ✅ |
| Rapide | Cppcheck + Clang-tidy | < 20s | < 30s | ✅ |
| Complet | Cppcheck + Clang-tidy + ASan + LSan | < 2min | < 5min | ✅ |

## 6. Politique de Gate appliquée

### Catégories bloquantes : Erreurs + Sécurité
- **Cppcheck** : Configuré avec --error-exitcode=1 (déjà implémenté)
- **Clang-tidy** : À configurer pour bloquer sur warnings de sécurité
- **ASan/LSan** : Retournent un code non nul en cas d'erreur mémoire
- **Profil rapide** : Bloque sur erreurs critiques et avertissements de sécurité
- **Profil complet** : Bloque sur tous les diagnostics

## 7. Risques et mitigations

| Risque | Probabilité | Impact | Mitigation |
|---|---|---|---|
| Clang non disponible | Moyenne | Moyen | Utiliser GCC warnings comme alternative |
| ASan non supporté par compilateur | Faible | Moyen | Utiliser Valgrind comme alternative |
| Faux positifs Cppcheck | Élevée | Faible | Documenter les exclusions dans docs/limites.md |
| Surcoût temps ASan sur gros projet | Moyenne | Faible | Fixtures simples, surcoût acceptable |

## 8. Décisions humaines requises

### Validation de la sélection
- [ ] Cppcheck + Clang-tidy + ASan + LSan est-il acceptable pour le prototype ?
- [ ] Faut-il ajouter GCC/Clang warnings (-Wall -Wextra) ?
- [ ] Faut-il inclure Valgrind malgré le surcoût ?

### Autorisation de passage à l'implémentation
- [ ] L'équipe qualité (Eric, Céline, Damien) valide la sélection
- [ ] Les observations reproductibles sont confirmées
- [ ] Les budgets de temps sont acceptés

## 9. Statut

- **Matrice de comparaison** : ✅ Complétée
- **Justification de sélection** : ✅ Complétée
- **Tests d'installation** : 🔄 En cours (Cppcheck validé, autres à tester)
- **Validation humaine** : ⏳ En attente