[CmdletBinding(SupportsShouldProcess)]
param(
    [switch]$CheckOnly
)

$ErrorActionPreference = "Stop"
$projectDirectory = Split-Path -Parent $PSScriptRoot

function Find-Cppcheck {
    $command = Get-Command -Name "cppcheck" -ErrorAction SilentlyContinue
    if ($null -ne $command) {
        return $command.Source
    }

    $defaultLocations = @($env:ProgramFiles, $env:ProgramW6432) |
        Where-Object { -not [string]::IsNullOrWhiteSpace($_) } |
        ForEach-Object { Join-Path $_ "Cppcheck\cppcheck.exe" } |
        Select-Object -Unique

    return $defaultLocations |
        Where-Object { Test-Path -LiteralPath $_ -PathType Leaf } |
        Select-Object -First 1
}

function Find-CommandPath([string]$Name) {
    $command = Get-Command -Name $Name -ErrorAction SilentlyContinue
    if ($null -ne $command) {
        return $command.Source
    }

    if ($Name -in @("clang", "clang-tidy")) {
        $defaultLocations = @($env:ProgramFiles, $env:ProgramW6432) |
            Where-Object { -not [string]::IsNullOrWhiteSpace($_) } |
            ForEach-Object { Join-Path $_ "LLVM\bin\$Name.exe" } |
            Select-Object -Unique

        return $defaultLocations |
            Where-Object { Test-Path -LiteralPath $_ -PathType Leaf } |
            Select-Object -First 1
    }

    return $null
}

function Install-WingetPackage([string]$Id, [string]$Name) {
    if ($CheckOnly) {
        return
    }

    if ($PSCmdlet.ShouldProcess($Name, "Installer le paquet winget $Id")) {
        & winget install --exact --id $Id --accept-package-agreements --accept-source-agreements --disable-interactivity
        if ($LASTEXITCODE -ne 0) {
            throw "L'installation de $Name a échoué (code $LASTEXITCODE)."
        }
    }
}

if ($env:OS -ne "Windows_NT") {
    [Console]::Error.WriteLine("Cet installateur est prévu pour Windows. Utilisez le gestionnaire de paquets de votre système.")
    exit 64
}

if ($PSVersionTable.PSVersion.Major -lt 5) {
    [Console]::Error.WriteLine("PowerShell 5.1 ou une version plus récente est requis.")
    exit 64
}

$misraFiles = @("misra.py", "misra_9.py", "cppcheckdata.py") |
    ForEach-Object { Join-Path $projectDirectory "sources-downloads\cppcheck-misra\$_" }
$missingMisraFiles = $misraFiles | Where-Object { -not (Test-Path -LiteralPath $_ -PathType Leaf) }
if ($missingMisraFiles.Count -gt 0) {
    [Console]::Error.WriteLine("Fichiers de l'addon MISRA absents : $($missingMisraFiles -join ', ')")
    exit 3
}

$cppcheckPath = Find-Cppcheck
$pythonPath = Find-CommandPath "python"
$clangPath = Find-CommandPath "clang"
$clangTidyPath = Find-CommandPath "clang-tidy"

$missingPackages = @()
if ($null -eq $cppcheckPath) {
    $missingPackages += @{ Id = "Cppcheck.Cppcheck"; Name = "Cppcheck" }
}
if ($null -eq $pythonPath) {
    $missingPackages += @{ Id = "Python.Python.3.12"; Name = "Python 3.12" }
}
if ($null -eq $clangPath -or $null -eq $clangTidyPath) {
    $missingPackages += @{ Id = "LLVM.LLVM"; Name = "LLVM (Clang et Clang-tidy)" }
}

Write-Host "=== Vérification de l'environnement qualité ===" -ForegroundColor Cyan
Write-Host "Windows : $([Environment]::OSVersion.VersionString)"
Write-Host "PowerShell : $($PSVersionTable.PSVersion)"
Write-Host "Cppcheck : $(if ($cppcheckPath) { $cppcheckPath } else { 'absent' })"
Write-Host "Python : $(if ($pythonPath) { $pythonPath } else { 'absent' })"
Write-Host "Clang : $(if ($clangPath) { $clangPath } else { 'absent' })"
Write-Host "Clang-tidy : $(if ($clangTidyPath) { $clangTidyPath } else { 'absent' })"
Write-Host "Addon MISRA : présent"

if ($missingPackages.Count -gt 0 -and -not $CheckOnly) {
    if ($null -eq (Find-CommandPath "winget")) {
        [Console]::Error.WriteLine("winget est requis pour installer : $($missingPackages.Name -join ', '). Installez App Installer puis relancez ce script.")
        exit 125
    }

    foreach ($package in $missingPackages) {
        Install-WingetPackage -Id $package.Id -Name $package.Name
    }

    $cppcheckPath = Find-Cppcheck
    $pythonPath = Find-CommandPath "python"
    $clangPath = Find-CommandPath "clang"
    $clangTidyPath = Find-CommandPath "clang-tidy"
}

$missingTools = @()
if ($null -eq $cppcheckPath) { $missingTools += "Cppcheck" }
if ($null -eq $pythonPath) { $missingTools += "Python" }
if ($null -eq $clangPath) { $missingTools += "Clang" }
if ($null -eq $clangTidyPath) { $missingTools += "Clang-tidy" }

if ($missingTools.Count -gt 0) {
    [Console]::Error.WriteLine("Outils manquants : $($missingTools -join ', ')")
    [Console]::Error.WriteLine("Si l'installation vient de se terminer, ouvrez une nouvelle fenêtre PowerShell puis relancez avec -CheckOnly.")
    exit 1
}

Write-Host ""
Write-Host "Versions détectées :" -ForegroundColor Cyan
& $cppcheckPath --version
& $pythonPath --version
& $clangPath --version | Select-Object -First 1
& $clangTidyPath --version | Select-Object -First 1

Write-Host ""
Write-Host "[OK] Environnement prêt pour Cppcheck, le rapport MISRA et les profils de qualité." -ForegroundColor Green
