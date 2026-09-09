[CmdletBinding()]
param(
    [string]$CppcheckCommand = "cppcheck",
    [string]$PythonCommand = "python",
    [string]$ReportPath,
    [string]$SourceDirectory
)

$ErrorActionPreference = "Stop"
if ([string]::IsNullOrWhiteSpace($SourceDirectory)) {
    $sourceDirectory = $PSScriptRoot
}
else {
    if (-not (Test-Path -LiteralPath $SourceDirectory)) {
        [Console]::Error.WriteLine("Répertoire source introuvable : $SourceDirectory")
        exit 2
    }
    $sourceDirectory = (Resolve-Path -LiteralPath $SourceDirectory).Path
}
$projectDirectory = Split-Path -Parent $PSScriptRoot
$sourceFiles = Get-ChildItem -Path $sourceDirectory -Recurse -File |
    Where-Object { $_.Extension -in ".c", ".cc", ".cpp", ".cxx" }

if ($sourceFiles.Count -eq 0) {
    [Console]::Error.WriteLine("Aucun fichier C ou C++ a analyser dans : $sourceDirectory")
    exit 2
}

$cppcheckPath = $null
if (Test-Path -LiteralPath $CppcheckCommand -PathType Leaf) {
    $cppcheckPath = (Resolve-Path -LiteralPath $CppcheckCommand).Path
}
else {
    $cppcheck = Get-Command -Name $CppcheckCommand -ErrorAction SilentlyContinue
    if ($null -ne $cppcheck) {
        $cppcheckPath = $cppcheck.Source
    }
}

if ($null -eq $cppcheckPath -and -not $PSBoundParameters.ContainsKey("CppcheckCommand")) {
    $defaultLocations = @(
        $env:ProgramFiles,
        $env:ProgramW6432
    ) | Where-Object { -not [string]::IsNullOrWhiteSpace($_) } |
        ForEach-Object { Join-Path $_ "Cppcheck\cppcheck.exe" } |
        Select-Object -Unique

    $cppcheckPath = $defaultLocations |
        Where-Object { Test-Path -LiteralPath $_ -PathType Leaf } |
        Select-Object -First 1
}

if ($null -eq $cppcheckPath) {
    [Console]::Error.WriteLine("Cppcheck est introuvable. Ajoutez-le au PATH ou indiquez son exécutable avec -CppcheckCommand.")
    exit 127
}

$python = Get-Command -Name $PythonCommand -ErrorAction SilentlyContinue
if ($null -eq $python) {
    [Console]::Error.WriteLine("Python est introuvable. Installez Python ou indiquez son exécutable avec -PythonCommand.")
    exit 126
}

$misraAddonPath = Join-Path $projectDirectory "sources-downloads\cppcheck-misra\misra.py"
if (-not (Test-Path -LiteralPath $misraAddonPath -PathType Leaf)) {
    [Console]::Error.WriteLine("L'addon MISRA est introuvable : $misraAddonPath")
    exit 3
}

if ([string]::IsNullOrWhiteSpace($ReportPath)) {
    $ReportPath = Join-Path $projectDirectory "reports\cppcheck-misra.xml"
}
elseif (-not [IO.Path]::IsPathRooted($ReportPath)) {
    $ReportPath = Join-Path (Get-Location) $ReportPath
}

$reportDirectory = Split-Path -Parent $ReportPath
New-Item -ItemType Directory -Force $reportDirectory | Out-Null

Write-Host "Cppcheck : $cppcheckPath"
& $cppcheckPath --version
if ($LASTEXITCODE -ne 0) {
    exit $LASTEXITCODE
}

Write-Host "Analyse MISRA C:2012 de $($sourceFiles.Count) fichier(s) dans : $sourceDirectory"
& $cppcheckPath `
    "--addon=$misraAddonPath" `
    "--addon-python=$($python.Source)" `
    --enable=warning,style,performance,portability `
    --std=c11 `
    --quiet `
    --xml `
    --xml-version=2 `
    --error-exitcode=1 `
    $sourceFiles.FullName 2> $ReportPath

Write-Host "Rapport MISRA : $ReportPath"
exit $LASTEXITCODE
