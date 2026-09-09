$ErrorActionPreference = 'Stop'

$repoRoot = git rev-parse --show-toplevel
Set-Location $repoRoot

$cppcheck = "C:\Program Files\Cppcheck\cppcheck.exe"
if (-not (Test-Path $cppcheck)) {
    Write-Error "cppcheck introuvable : $cppcheck"
    exit 1
}

$files = git diff --cached --name-only --diff-filter=ACMRTUXB
$cFiles = $files | Where-Object { $_ -match '\.c$' }

if (-not $cFiles) {
    Write-Host "Aucun fichier .c modifie : push autorise."
    exit 0
}

Write-Host "Verification CPPCheck sur les fichiers .c modifies :"
foreach ($file in $cFiles) {
    Write-Host "- $file"
}

$fail = $false
foreach ($file in $cFiles) {
    & $cppcheck --error-exitcode=1 --enable=all --std=c11 $file
    if ($LASTEXITCODE -ne 0) {
        $fail = $true
    }
}

if ($fail) {
    Write-Host "" 
    Write-Host "Push bloque : des erreurs cppcheck ont ete detectees sur des fichiers .c modifies." -ForegroundColor Red
    exit 1
}

Write-Host "" 
Write-Host "cppcheck OK : le push peut continuer." -ForegroundColor Green
exit 0
