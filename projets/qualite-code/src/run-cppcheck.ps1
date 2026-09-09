[CmdletBinding()]
param(
    [string]$CppcheckCommand = "cppcheck",
    [string]$SourceDirectory = ""
)

$ErrorActionPreference = "Stop"
if ([string]::IsNullOrEmpty($SourceDirectory)) {
    $sourceDirectory = $PSScriptRoot
} else {
    $sourceDirectory = $SourceDirectory
}
$sourceFiles = Get-ChildItem -Path $sourceDirectory -Recurse -File |
    Where-Object { $_.Extension -in ".c", ".cc", ".cpp", ".cxx" }

if ($sourceFiles.Count -eq 0) {
    [Console]::Error.WriteLine("Aucun fichier C ou C++ a analyser dans : $sourceDirectory")
    exit 2
}

$cppcheck = Get-Command -Name $CppcheckCommand -ErrorAction SilentlyContinue
if ($null -eq $cppcheck) {
    [Console]::Error.WriteLine("Cppcheck est introuvable. Installez-le ou indiquez son executable avec -CppcheckCommand.")
    exit 127
}

Write-Host "Cppcheck : $($cppcheck.Source)"
& $cppcheck.Source --version
if ($LASTEXITCODE -ne 0) {
    exit $LASTEXITCODE
}

Write-Host "Analyse de $($sourceFiles.Count) fichier(s) dans : $sourceDirectory"
& $cppcheck.Source `
    --enable=warning,style,performance,portability `
    --std=c11 `
    --error-exitcode=1 `
    $sourceFiles.FullName

exit $LASTEXITCODE
