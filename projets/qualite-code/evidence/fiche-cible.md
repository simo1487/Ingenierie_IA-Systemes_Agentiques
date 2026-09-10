# Fiche de cible - PROJ-QUAL-001

## 1. Identification de la cible

| Attribut | Valeur |
|---|---|
| **Type de cible** | Fixtures de test |
| **Objectif** | Valider la chaîne de contrôles qualité statiques et dynamiques |
| **Révision** | Fixtures créées pour le prototype (projet qualité-code) |
| **Date de création** | 2026-09-09 |

## 2. Caractéristiques techniques

| Attribut | Valeur |
|---|---|
| **Langages** | C (standard C11) |
| **Extensions analysées** | `.c`, `.cc`, `.cpp`, `.cxx` |
| **Compilateur cible** | GCC / Clang |
| **Commande de build** | `gcc -std=c11 -Wall -Wextra fichier.c -o fichier` |
| **Tests dynamiques** | Aucun dans les fixtures (lacune visible) |

## 3. Description des fixtures

### main.c
- **Type** : Fixture existante (déplacée de src/)
- **Description** : Code C simple avec variables et printf
- **Objectif** : Test nominal pour vérifier que la chaîne fonctionne sur du code C11 standard
- **Statut** : `Validée`

### success.c (à créer)
- **Type** : Fixture de succès
- **Description** : Code C propre sans défauts connus
- **Objectif** : Valider que la chaîne ne produit pas de faux positifs sur du code correct
- **Statut** : `À créer`

### defect.c (à créer)
- **Type** : Fixture avec défaut contrôlé
- **Description** : Code C avec un défaut explicite injecté
- **Objectif** : Valider que la chaîne détecte le défaut et retourne un code non nul (CA-QUAL-05)
- **Statut** : `À créer`

## 4. Commandes de build et de test

### Build
```powershell
# Compiler une fixture
gcc -std=c11 -Wall -Wextra tests/fixtures/main.c -o tests/fixtures/main.exe

# Exécuter le binaire
.\tests\fixtures\main.exe
```

### Tests dynamiques
- **Statut** : Aucun test dynamique implémenté dans les fixtures
- **Note** : Cette lacune est documentée conformément à CA-QUAL-08 (éléments non testés)

## 5. Limites de la cible

| Limite | Description |
|---|---|
| **Portée** | Fixtures de test uniquement, pas de code de production |
| **Complexeité** | Code simple, ne teste pas tous les cas d'usage |
| **Tests dynamiques** | Absence de tests unitaires ou d'intégration |
| **Build système** : Pas de système de build complexe (Make, CMake) |

## 6. Justification du choix

**Pourquoi des fixtures de test ?**
- Permet de valider la chaîne de contrôles sans dépendre d'un projet externe
- Permet de contrôler précisément les défauts injectés pour les tests
- Simplifie la reproductibilité pour les tiers (CA-QUAL-07)
- Évite les dépendances sur l'équipe 3 (logiciel automobile open source)

**Pourquoi C11 ?**
- Standard largement supporté par les outils d'analyse statique
- Compatible avec les cibles automobiles (MISRA C s'appuie sur C)
- Permet de tester les contrôles de style et de portabilité

## 7. Statut des critères d'acceptation liés

- [x] **CA-QUAL-01** : La cible, sa révision, ses langages et ses commandes de build et de test sont définis.
- [ ] **CA-QUAL-08** : Les limites, exclusions, faux positifs et éléments non testés sont listés (en cours).

## 8. Décisions humaines requises

Aucune décision humaine requise pour cette fiche de cible - les fixtures sont acceptées comme cible pour le prototype.