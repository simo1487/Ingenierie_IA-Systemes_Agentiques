# Guide d'installation - PROJ-QUAL-001

## Prérequis

- PowerShell 5.1 ou supérieur
- Accès internet pour le téléchargement des outils

## Installation des outils

### 1. Cppcheck (requis)

#### Windows
```powershell
# Via Chocolatey
choco install cppcheck

# Via Scoop
scoop install cppcheck

# Manuel : Télécharger depuis https://cppcheck.sourceforge.io/
# Ajouter le chemin d'installation au PATH
```

#### Linux
```bash
# Debian/Ubuntu
sudo apt-get install cppcheck

# Fedora/RHEL
sudo dnf install cppcheck

# Arch Linux
sudo pacman -S cppcheck
```

#### Vérification
```powershell
cppcheck --version
# Résultat attendu : Cppcheck 2.13 (ou supérieur)
```

### 2. Clang-tidy (optionnel pour profil rapide, requis pour profil complet)

#### Windows
```powershell
# Via Chocolatey
choco install llvm

# Via Scoop
scoop install llvm

# Manuel : Télécharger depuis https://releases.llvm.org/
# Ajouter le chemin d'installation au PATH
```

#### Linux
```bash
# Debian/Ubuntu
sudo apt-get install clang-tidy

# Fedora/RHEL
sudo dnf install clang-tools-extra

# Arch Linux
sudo pacman -S clang
```

#### Vérification
```powershell
clang-tidy --version
# Résultat attendu : LLVM version 19.0 (ou supérieur)
```

### 3. GCC ou Clang (requis pour AddressSanitizer/LeakSanitizer)

#### Windows
```powershell
# Via Chocolatey
choco install mingw

# Via Scoop
scoop install gcc

# Manuel : Télécharger depuis https://www.mingw-w64.org/
# Ajouter le chemin d'installation au PATH
```

#### Linux
```bash
# GCC (généralement déjà installé)
sudo apt-get install gcc  # Debian/Ubuntu
sudo dnf install gcc      # Fedora/RHEL

# Clang
sudo apt-get install clang  # Debian/Ubuntu
sudo dnf install clang      # Fedora/RHEL
```

#### Vérification
```powershell
gcc --version
# Résultat attendu : gcc (GCC) 11.0 ou supérieur

# OU
clang --version
# Résultat attendu : clang version 12.0 ou supérieur
```

## Configuration de l'environnement

### Variables d'environnement (Windows)

Ajouter les chemins suivants à la variable PATH :
- `C:\Program Files\Cppcheck` (ou chemin d'installation)
- `C:\Program Files\LLVM\bin` (si installé via LLVM)
- `C:\mingw64\bin` (si installé via MinGW)

### Vérification de l'installation

Exécuter le script de test :
```powershell
./projets/qualite-code/src/run-profile-rapide.ps1
```

Résultat attendu :
- Si Cppcheck est installé : Analyse des fixtures avec succès
- Si Cppcheck est absent : Code retour 127 avec message d'erreur

## Dépannage

### Cppcheck introuvable
- **Erreur** : `Cppcheck est introuvable`
- **Solution** : Vérifier que Cppcheck est installé et ajouté au PATH
- **Commande** : `Get-Command cppcheck`

### Clang-tidy introuvable
- **Erreur** : `Clang-tidy non disponible`
- **Solution** : Installer LLVM ou Clang, c'est optionnel pour le profil rapide
- **Commande** : `Get-Command clang-tidy`

### GCC/Clang introuvable
- **Erreur** : `Aucun compilateur (GCC/Clang) disponible pour ASan/LSan`
- **Solution** : Installer GCC ou Clang
- **Commande** : `Get-Command gcc` ou `Get-Command clang`

### Erreur d'exécution PowerShell
- **Erreur** : `exécution de scripts est désactivée`
- **Solution** : `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser`

## Installation minimale

Pour le **profil rapide** uniquement :
- Cppcheck (requis)
- Clang-tidy (optionnel)

Pour le **profil complet** :
- Cppcheck (requis)
- Clang-tidy (requis)
- GCC ou Clang (requis pour ASan/LSan)

## Notes spécifiques

### Windows Subsystem for Linux (WSL)
Si vous utilisez WSL, installez les outils via le gestionnaire de paquets Linux :
```bash
sudo apt-get update
sudo apt-get install cppcheck clang-tidy gcc
```

### Mac OS X
```bash
# Via Homebrew
brew install cppcheck llvm gcc
```

### Docker
Une image Docker peut être créée pour garantir un environnement reproductible :
```dockerfile
FROM ubuntu:22.04
RUN apt-get update && apt-get install -y \
    cppcheck \
    clang-tidy \
    gcc \
    && rm -rf /var/lib/apt/lists/*
```