[CmdletBinding()]
param(
    [string]$SourceDirectory = ""
)

$ErrorActionPreference = "Stop"
$scriptPath = $PSScriptRoot

# Déterminer le répertoire source
if ([string]::IsNullOrEmpty($SourceDirectory)) {
    $sourceDirectory = Join-Path $scriptPath "..\tests\fixtures"
} else {
    $sourceDirectory = $SourceDirectory
}

Write-Host "=== Profil Rapide - Controles Qualite ===" -ForegroundColor Cyan
Write-Host "Repertoire source : $sourceDirectory"
Write-Host ""

# Verifier que le repertoire existe
if (-not (Test-Path $sourceDirectory)) {
    [Console]::Error.WriteLine("Erreur : Repertoire source introuvable : $sourceDirectory")
    exit 1
}

# Recuperer les fichiers C/C++
$sourceFiles = Get-ChildItem -Path $sourceDirectory -Recurse -File |
    Where-Object { $_.Extension -in ".c", ".cc", ".cpp", ".cxx" }

if ($sourceFiles.Count -eq 0) {
    [Console]::Error.WriteLine("Aucun fichier C ou C++ a analyser dans : $sourceDirectory")
    exit 2
}

Write-Host "Fichiers trouves : $($sourceFiles.Count)" -ForegroundColor Green
foreach ($file in $sourceFiles) {
    Write-Host "  - $($file.Name)"
}
Write-Host ""

# Controle 1 : Cppcheck
Write-Host "--- Controle 1 : Cppcheck ---" -ForegroundColor Yellow
$cppcheckScript = Join-Path $scriptPath "run-cppcheck.ps1"
$cppcheckPath = "C:\Program Files\Cppcheck\cppcheck.exe"
if (Test-Path $cppcheckScript) {
    & $cppcheckScript -SourceDirectory $sourceDirectory -CppcheckCommand $cppcheckPath
    $cppcheckExitCode = $LASTEXITCODE
    
    if ($cppcheckExitCode -eq 127) {
        Write-Host "[WARNING] Cppcheck non disponible" -ForegroundColor Red
        exit 127
    } elseif ($cppcheckExitCode -eq 0) {
        Write-Host "[OK] Cppcheck : Aucun defaut detecte" -ForegroundColor Green
    } elseif ($cppcheckExitCode -eq 1) {
        Write-Host "[FAIL] Cppcheck : Defaut(s) detecte(s)" -ForegroundColor Red
    } else {
        Write-Host "[UNKNOWN] Cppcheck : Code retour inattendu : $cppcheckExitCode" -ForegroundColor Yellow
    }
} else {
    Write-Host "[WARNING] Script Cppcheck introuvable : $cppcheckScript" -ForegroundColor Red
    exit 127
}
Write-Host ""

# Controle 2 : Clang-tidy (optionnel)
Write-Host "--- Controle 2 : Clang-tidy (optionnel) ---" -ForegroundColor Yellow
$clangTidy = Get-Command -Name "clang-tidy" -ErrorAction SilentlyContinue
if ($null -eq $clangTidy) {
    Write-Host "[WARNING] Clang-tidy non disponible (optionnel, pas bloquant)" -ForegroundColor Yellow
    $clangTidyExitCode = 0
} else {
    Write-Host "Clang-tidy : $($clangTidy.Source)"
    & $clangTidy.Source --version
    $clangTidyExitCode = 0
    
    foreach ($file in $sourceFiles) {
        Write-Host "Analyse de : $($file.Name)"
        & $clangTidy.Source $file.FullName --checks="*" -- --std=c11
        if ($LASTEXITCODE -ne 0) {
            $clangTidyExitCode = $LASTEXITCODE
        }
    }
    
    if ($clangTidyExitCode -eq 0) {
        Write-Host "[OK] Clang-tidy : Aucun defaut detecte" -ForegroundColor Green
    } else {
        Write-Host "[FAIL] Clang-tidy : Defaut(s) detecte(s)" -ForegroundColor Red
    }
}
Write-Host ""

# Resume
Write-Host "=== Resume du Profil Rapide ===" -ForegroundColor Cyan
Write-Host "Fichiers analyses : $($sourceFiles.Count)"
Write-Host "Cppcheck : $(if ($cppcheckExitCode -eq 0) { 'OK' } else { 'ECHEC' })"
Write-Host "Clang-tidy : $(if ($clangTidyExitCode -eq 0) { 'OK (optionnel)' } else { 'ECHEC' })"
Write-Host ""

# Code retour global
if ($cppcheckExitCode -eq 127) {
    # Outil requis absent
    exit 127
} elseif ($cppcheckExitCode -ne 0) {
    # Défaut détecté par Cppcheck (bloquant)
    exit 1
} else {
    # Succes
    Write-Host "[OK] Profil rapide termine avec succes" -ForegroundColor Green
    exit 0
}