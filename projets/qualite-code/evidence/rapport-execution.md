# Rapport d'exécution - PROJ-QUAL-001

## 1. Métadonnées

- **Identifiant :** REV-QUAL-001
- **Composant / Branche :** `projets/qualite-code` — `feat_Cppcheck`
- **Commit examiné :** À compléter par le relecteur humain
- **Date d'exécution :** 2026-09-09
- **Outils exécutés :** Cppcheck 2.21.0, Clang-tidy 22.1.8, Clang 22.1.8, Python 3.14.6
- **Relecteur(s) humain(s) :** À compléter
- **Statut global proposé :** **Refusé / Corrections requises** — défaut confirmé sur `defect.c`, anomalie bloquante dans `run-cppcheck.ps1`, fixture `main.c` incorrecte.

## 2. Environnement

| Attribut | Valeur |
|---|---|
| OS | Microsoft Windows NT 10.0.26200.0 |
| PowerShell | 5.1.26100.9168 |
| Cppcheck | 2.21.0 (`C:\Program Files\Cppcheck\cppcheck.exe`) |
| Python | 3.14.6 |
| Clang | 22.1.8 |
| Clang-tidy | 22.1.8 |
| GCC | Non installé |
| Addon MISRA | Présent dans `sources-downloads/cppcheck-misra/` |

## 3. Commandes exécutées et résultats

### 3.1 Vérification de l'environnement (`install-tools.ps1 -CheckOnly`)

```powershell
.\projets\qualite-code\src\install-tools.ps1 -CheckOnly
```

Résultat : `[OK] Environnement prêt...` — `LASTEXITCODE=0`.

### 3.2 Cppcheck direct — fixture `success.c`

```powershell
& "C:\Program Files\Cppcheck\cppcheck.exe" `
    --enable=warning,style,performance,portability `
    --std=c11 --error-exitcode=1 `
    "C:\Users\eric_\Documents\GitHub\FormationIaProject\projets\qualite-code\tests\fixtures\success.c"
```

Sortie :
```text
Checking C:\Users\eric_\Documents\GitHub\FormationIaProject\projets\qualite-code\tests\fixtures\success.c ...
```

`LASTEXITCODE=0` — aucun défaut détecté par Cppcheck.

### 3.3 Cppcheck direct — fixture `defect.c`

Sortie :
```text
Checking C:\Users\eric_\Documents\GitHub\FormationIaProject\projets\qualite-code\tests\fixtures\defect.c ...
C:\Users\eric_\Documents\GitHub\FormationIaProject\projets\qualite-code\tests\fixtures\defect.c:25:12: error: Buffer is accessed out of bounds: buffer [bufferAccessOutOfBounds]
    strcpy(buffer, "Ceci est trop long pour le tampon");
```

`LASTEXITCODE=1` — défaut localisé à la ligne 25, conforme à l'oracle injecté.

### 3.4 Cppcheck direct — fixture `main.c`

Sortie :
```text
Checking C:\Users\eric_\Documents\GitHub\FormationIaProject\projets\qualite-code\tests\fixtures\main.c ...
```

`LASTEXITCODE=0` — Cppcheck ne relève pas d'erreur.

### 3.5 Cppcheck direct — répertoire `tests/fixtures` (3 fichiers)

Sortie :
```text
C:\Users\eric_\Documents\GitHub\FormationIaProject\projets\qualite-code\tests\fixtures\defect.c:25:12: error: Buffer is accessed out of bounds: buffer [bufferAccessOutOfBounds]
```

`LASTEXITCODE=1` — le défaut contrôlé fait bien échouer l'analyse.

### 3.6 Clang-tidy — `success.c`

```powershell
clang-tidy "C:\Users\eric_\Documents\GitHub\FormationIaProject\projets\qualite-code\tests\fixtures\success.c" --checks="*" -- --std=c11
```

Sortie partielle : 454 warnings, majoritairement des règles de style (`llvmlibc-restrict-system-libc-headers`, `cppcoreguidelines-avoid-magic-numbers`, `clang-analyzer-security.insecureAPI.DeprecatedOrUnsafeBufferHandling` sur `fprintf`...).

`LASTEXITCODE=0`.

### 3.7 Clang-tidy — `defect.c`

Sortie partielle :
```text
C:\Users\eric_\Documents\GitHub\FormationIaProject\projets\qualite-code\tests\fixtures\defect.c:25:5: warning: 'strcpy' will always overflow; destination buffer has size 10, but the source string has length 34
C:\Users\eric_\Documents\GitHub\FormationIaProject\projets\qualite-code\tests\fixtures\defect.c:25:5: warning: Call to function 'strcpy' is insecure ... CWE-119
```

`LASTEXITCODE=0`.

### 3.8 Clang-tidy — `main.c`

Sortie partielle :
```text
C:\Users\eric_\Documents\GitHub\FormationIaProject\projets\qualite-code\tests\fixtures\main.c:11:5: error: call to undeclared library function 'printf' with type 'int (const char *, ...)'; ISO C99 and later do not support implicit function declarations
```

`LASTEXITCODE=1` — la fixture ne compile pas car `#include <stdio.h>` est commentée.

### 3.9 Script `run-profile-rapide.ps1` — `tests/fixtures`

```powershell
.\projets\qualite-code\src\run-profile-rapide.ps1 -SourceDirectory "C:\Users\eric_\Documents\GitHub\FormationIaProject\projets\qualite-code\tests\fixtures"
```

Résultat : Cppcheck est lancé, mais la sortie XML est affichée comme erreur native (`RemoteException`) et le script s'arrête avant Clang-tidy.

`LASTEXITCODE=1`.

### 3.10 Script `run-profile-rapide.ps1` — `tests/fixtures/success.c`

Même comportement : `LASTEXITCODE=1` — le script échoue même sur la fixture propre.

### 3.11 Script `run-profile-rapide.ps1` — `tests/fixtures/defect.c`

Même comportement : `LASTEXITCODE=1` — le diagnostic Cppcheck n'est pas restitué.

### 3.12 Script `run-cppcheck.ps1` — outil absent

```powershell
.\projets\qualite-code\src\run-cppcheck.ps1 -CppcheckCommand "C:\Outils\cppcheck_inexistant.exe" -SourceDirectory "C:\Users\eric_\Documents\GitHub\FormationIaProject\projets\qualite-code\tests\fixtures"
```

Sortie : `Cppcheck est introuvable. Ajoutez-le au PATH ou indiquez son exécutable avec -CppcheckCommand.`

`LASTEXITCODE=127` — conforme.

### 3.13 Script `run-cppcheck.ps1` — répertoire vide

```powershell
$empty = Join-Path $env:TEMP "qualite-empty"; New-Item -ItemType Directory -Force -Path $empty | Out-Null
.\projets\qualite-code\src\run-cppcheck.ps1 -SourceDirectory "$empty"
```

Sortie : `Aucun fichier C ou C++ à analyser...`

`LASTEXITCODE=2` — conforme.

### 3.14 Script `run-profile-rapide.ps1` — répertoire vide

`LASTEXITCODE=2` — conforme.

## 4. Registre des alertes (proposition IA — décision humaine requise)

| ID | Outil / Règle | Fichier & Ligne | Description | Qualification proposée | Justification |
|---|---|---|---|---|---|
| ALT-01 | Cppcheck / `bufferAccessOutOfBounds` | `defect.c:25` | Dépassement de tampon sur `buffer` | **Anomalie confirmée** | Défaut injecté, détecté statiquement, code retour non nul |
| ALT-02 | Clang-tidy / `clang-diagnostic-fortify-source` | `defect.c:25` | `strcpy` overflow certain, taille 10 vs 34 | **Anomalie confirmée** | Corrobore le défaut injecté |
| ALT-03 | Clang-tidy / `llvmlibc-restrict-system-libc-headers` | `success.c:1` | Inclusions système interdites | **Faux positif** | Règle spécifique LLVM libc, non applicable au prototype C11 |
| ALT-04 | Clang-tidy / `cppcoreguidelines-avoid-magic-numbers` | `success.c:12,19,20,24` | Constantes 5 et 10 | **Faux positif** | Style, non bloquant |
| ALT-05 | Clang-tidy / `clang-diagnostic-implicit-function-declaration` | `main.c:11` | `printf` non déclaré (`stdio.h` commenté) | **Anomalie confirmée** | La fixture ne compile pas ; correction ou justification requise |
| ALT-06 | `run-cppcheck.ps1` | `src/run-cppcheck.ps1:87` | La sortie XML Cppcheck n'est pas capturée, provoque une `RemoteException` | **Anomalie confirmée** | La redirection `2>` ne convient pas pour la sortie native de `cppcheck --xml` ; le script s'arrête et le rapport XML reste vide |

## 5. Évaluation KISS / YAGNI / SRP

| Principe | Constat | Conforme ? |
|---|---|---:|
| **KISS** | Commandes directes fonctionnent ; les scripts PowerShell sont fragiles à cause de la redirection XML | Non |
| **YAGNI** | Aucune dépendance ou fonctionnalité superflue identifiée | Oui |
| **SRP** | `run-cppcheck.ps1` génère le rapport MISRA, `run-profile-rapide.ps1` orchestre ; rôles séparés | Oui |

## 6. Statut des critères d'acceptation (proposition)

| Critère | Statut proposé | Preuve / Raison |
|---|---|---|
| `CA-QUAL-01` | ✅ Validé | Cible et outils identifiés |
| `CA-QUAL-02` | ✅ Validé | Matrice de comparaison existante (`experiments/matrice-comparaison.md`) |
| `CA-QUAL-03` | ✅ Validé | Versions relevées ci-dessus |
| `CA-QUAL-04` | ⚠️ Partiel | Profil documenté mais `run-profile-rapide` s'arrête sur `run-cppcheck` |
| `CA-QUAL-05` | ✅ Validé | Cppcheck détecte `defect.c:25` (test direct) |
| `CA-QUAL-06` | ✅ Validé | `run-cppcheck.ps1` retourne 127 quand l'outil est absent |
| `CA-QUAL-07` | ⏳ En attente | Nécessite correction de `run-cppcheck.ps1` et reproductibilité par un tiers |
| `CA-QUAL-08` | ✅ Validé | `docs/limites.md` à jour |

## 7. Synthèse

- **Anomalies confirmées :** 3 (`defect.c`, `main.c` fixture, `run-cppcheck.ps1`)
- **Faux positifs proposés :** 2 (règles de style Clang-tidy sur `success.c`)
- **Tests environnementaux OK :** vérification des outils, répertoire vide, outil absent.
- **Bloquants :** `run-cppcheck.ps1` et `run-profile-rapide.ps1` ne sont pas utilisables en l'état ; `main.c` ne compile pas.

## 8. Décision humaine

- [ ] **Accepter pour intégration dans `develop`**
- [x] **Refuser — Corrections requises :**
  - Corriger `src/run-cppcheck.ps1` pour capturer correctement la sortie XML Cppcheck.
  - Corriger ou justifier `tests/fixtures/main.c` (`#include <stdio.h>` commenté).
  - Re-tester `run-profile-rapide.ps1` et `run-profile-complet.ps1` après correction.

*Rapport généré automatiquement par l'agent Devin le 2026-09-09. Décision humaine à consigner.*
