[CmdletBinding()]
param(
    [string]$CppcheckCommand = "cppcheck"
)

$ErrorActionPreference = "Stop"
$sourceDirectory = $PSScriptRoot
$sourceFiles = Get-ChildItem -Path $sourceDirectory -Recurse -File |
    Where-Object { $_.Extension -in ".c", ".cc", ".cpp", ".cxx" }

if ($sourceFiles.Count -eq 0) {
    [Console]::Error.WriteLine("Aucun fichier C ou C++ à analyser dans : $sourceDirectory")
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

Write-Host "Cppcheck : $cppcheckPath"
& $cppcheckPath --version
if ($LASTEXITCODE -ne 0) {
    exit $LASTEXITCODE
}

Write-Host "Analyse de $($sourceFiles.Count) fichier(s) dans : $sourceDirectory"
& $cppcheckPath `
    --enable=warning,style,performance,portability `
    --std=c11 `
    --error-exitcode=1 `
    $sourceFiles.FullName

exit $LASTEXITCODE
