# Guide d'utilisation - PROJ-QUAL-001

## Vue d'ensemble

Ce projet fournit une chaîne de contrôles qualité reproductibles pour le code C/C++. Deux profils sont disponibles :

- **Profil rapide** : Analyse statique (< 30 secondes)
- **Profil complet** : Analyse statique et dynamique (< 5 minutes)

## Commandes de base

### Profil rapide

```powershell
# Analyse des fixtures par défaut
./projets/qualite-code/src/run-profile-rapide.ps1

# Analyse d'un répertoire spécifique
./projets/qualite-code/src/run-profile-rapide.ps1 -SourceDirectory "chemin/vers/sources"
```

**Outilis inclus :**
- Cppcheck (requis)
- Clang-tidy (optionnel)

**Code retour :**
- `0` : Succès (aucun défaut détecté)
- `1` : Défaut détecté (bloquant)
- `127` : Outil requis absent (Cppcheck)
- `2` : Aucun fichier applicable

### Profil complet

```powershell
# Analyse des fixtures par défaut
./projets/qualite-code/src/run-profile-complet.ps1

# Analyse d'un répertoire spécifique
./projets/qualite-code/src/run-profile-complet.ps1 -SourceDirectory "chemin/vers/sources"
```

**Outils inclus :**
- Cppcheck (requis)
- Clang-tidy (requis)
- AddressSanitizer (requis)
- LeakSanitizer (requis)

**Code retour :**
- `0` : Succès (aucun défaut détecté)
- `1` : Défaut détecté par au moins un outil
- `127` : Outil requis absent
- `2` : Aucun fichier applicable

### Cppcheck seul

```powershell
# Analyse du répertoire src/ par défaut
./projets/qualite-code/src/run-cppcheck.ps1

# Analyse d'un répertoire spécifique
./projets/qualite-code/src/run-cppcheck.ps1 -SourceDirectory "chemin/vers/sources"

# Spécifier un exécutable Cppcheck personnalisé
./projets/qualite-code/src/run-cppcheck.ps1 -CppcheckCommand "chemin/vers/cppcheck.exe"
```

## Scénarios d'utilisation

### Scénario 1 : Développeur local

En tant que développeur, je veux vérifier mon code avant de commiter :

```powershell
# 1. Faire les modifications
# 2. Lancer le profil rapide
./projets/qualite-code/src/run-profile-rapide.ps1 -SourceDirectory "mon/projet/src"

# 3. Si succès, commiter
# 4. Si défaut, corriger et relancer
```

### Scénario 2 : Relecteur qualité

En tant que relecteur, je veux vérifier un pull request :

```powershell
# 1. Cloner le PR
# 2. Lancer le profil complet sur les fichiers modifiés
./projets/qualite-code/src/run-profile-complet.ps1 -SourceDirectory "pr/src"

# 3. Examiner le rapport
# 4. Documenter les décisions dans evidence/rapport-revue.md
```

### Scénario 3 : Intégration continue

En tant qu'intégrateur, je veux automatiser les contrôles :

```yaml
# Exemple de configuration GitHub Actions
- name: Contrôles qualité
  run: |
    ./projets/qualite-code/src/run-profile-rapide.ps1 -SourceDirectory "src"
```

## Interprétation des résultats

### Cppcheck

**Sortie typique :**
```
Cppcheck : C:\Program Files\Cppcheck\cppcheck.exe
Cppcheck 2.13
Analyse de 3 fichier(s) dans : tests/fixtures
✓ Cppcheck : Aucun défaut détecté
```

**En cas de défaut :**
```
Checking tests/fixtures/defect.c ...
[defect.c:15]: (error) Buffer overrun while copying to 'buffer'
✗ Cppcheck : Défaut(s) détecté(s)
```

### Clang-tidy

**Sortie typique :**
```
Clang-tidy : C:\Program Files\LLVM\bin\clang-tidy.exe
LLVM version 19.0.0
Analyse de : defect.c
✓ Clang-tidy : Aucun défaut détecté
```

**En cas de défaut :**
```
defect.c:15:5: warning: strcpy' is deprecated: use strcpy_s instead
    strcpy(buffer, "Ceci est trop long pour le tampon");
    ^
✗ Clang-tidy : Défaut(s) détecté(s)
```

### AddressSanitizer / LeakSanitizer

**Sortie typique :**
```
Compilateur : GCC C:\mingw64\bin\gcc.exe
gcc.exe (GCC) 11.0
Compilation de : defect.c
Exécution avec ASan/LSan : defect.c
✗ ASan/LSan : Défaut détecté pour defect.c
```

**En cas de défaut :**
```
==12345==ERROR: AddressSanitizer: heap-buffer-overflow on address 0x...
WRITE of size 35 at 0x... thread T0
    #0 0x... in strcpy
    #1 0x... in main defect.c:15
0x... is located 0 bytes to the right of 10-byte region
allocated by thread T0 here:
    #0 0x... in malloc
    #1 0x... in main defect.c:12
```

## Tests avec les fixtures

### Fixture de succès (success.c)

```powershell
# Doit passer sans défaut
./projets/qualite-code/src/run-profile-rapide.ps1 -SourceDirectory "tests/fixtures/success.c"
# Résultat attendu : Code retour 0
```

### Fixture avec défaut (defect.c)

```powershell
# Doit détecter le buffer overflow
./projets/qualite-code/src/run-profile-rapide.ps1 -SourceDirectory "tests/fixtures/defect.c"
# Résultat attendu : Code retour 1 avec diagnostic localisable
```

### Répertoire vide

```powershell
# Doit retourner un code spécifique
./projets/qualite-code/src/run-profile-rapide.ps1 -SourceDirectory "tests/fixtures/vide"
# Résultat attendu : Code retour 2
```

### Outil absent

```powershell
# Désinstaller Cppcheck temporairement
# Doit retourner un code spécifique
./projets/qualite-code/src/run-profile-rapide.ps1
# Résultat attendu : Code retour 127
```

## Personnalisation

### Modifier les options Cppcheck

Éditer `src/run-cppcheck.ps1` et modifier la ligne :
```powershell
& $cppcheck.Source `
    --enable=warning,style,performance,portability `
    --std=c11 `
    --error-exitcode=1 `
    $sourceFiles.FullName
```

### Ajouter des exclusions

Créer un fichier `.cppcheck-suppressions.txt` :
```
// Exemple d'exclusion
leaked_storage:src/legacy.c
unusedVariable:src/test.c
```

Puis modifier le script pour l'utiliser :
```powershell
& $cppcheck.Source `
    --suppressions-list=.cppcheck-suppressions.txt `
    $sourceFiles.FullName
```

### Modifier la politique de Gate

Éditer les scripts `run-profile-rapide.ps1` et `run-profile-complet.ps1` pour modifier :
- Les codes retour considérés comme bloquants
- Les catégories d'anomalies bloquantes (erreurs + sécurité)

## Intégration avec Git hooks

### Pre-commit hook

Créer `.git/hooks/pre-commit` :
```bash
#!/bin/bash
./projets/qualite-code/src/run-profile-rapide.ps1 -SourceDirectory "src"
if [ $? -ne 0 ]; then
    echo "Contrôles qualité échoués. Commit annulé."
    exit 1
fi
```

### Pre-push hook

Créer `.git/hooks/pre-push` :
```bash
#!/bin/bash
./projets/qualite-code/src/run-profile-complet.ps1 -SourceDirectory "src"
if [ $? -ne 0 ]; then
    echo "Contrôles qualité échoués. Push annulé."
    exit 1
fi
```

## Dépannage

### Erreur : "Aucun fichier C ou C++ à analyser"
- **Cause** : Répertoire vide ou sans fichiers .c/.cpp
- **Solution** : Vérifier le chemin et les extensions des fichiers

### Erreur : "Cppcheck est introuvable"
- **Cause** : Cppcheck non installé ou non dans le PATH
- **Solution** : Installer Cppcheck (voir docs/installation.md)

### Erreur : "Aucun compilateur (GCC/Clang) disponible"
- **Cause** : GCC ou Clang non installé (pour ASan/LSan)
- **Solution** : Installer GCC ou Clang (voir docs/installation.md)

### Temps d'exécution trop long
- **Cause** : Trop de fichiers ou profil complet sur gros projet
- **Solution** : Utiliser le profil rapide ou limiter la portée

## Rapportage

Pour consigner les résultats d'une revue, utiliser le template dans `evidence/rapport-revue.md` (à créer).