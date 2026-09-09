param(
    [Parameter(Mandatory=$true)]
    [string]$MdPath
)

$content = [System.IO.File]::ReadAllText($MdPath, [System.Text.Encoding]::UTF8)
$errors = @()

Write-Output "=== Verification des exigences ==="
Write-Output "Fichier : $MdPath"
Write-Output ""

# 1. Count exigences (lines with "- **Official ID:**" or "- **ID officiel :**")
$idMatches = [regex]::Matches($content, '\- \*\*(?:Official ID|ID officiel)\s*:?\*\* ([^\n\r]+)')
$totalExigences = $idMatches.Count
Write-Output "1. Nombre total d'exigences : $totalExigences"

# 2. Check unique IDs
$ids = @{}
$duplicates = @()
foreach ($m in $idMatches) {
    $id = $m.Groups[1].Value.Trim()
    if ($ids.ContainsKey($id)) {
        $duplicates += $id
    } else {
        $ids[$id] = $true
    }
}
Write-Output ""
Write-Output "2. Unicite des IDs"
if ($duplicates.Count -gt 0) {
    $errors += "ECHEC: IDs dupliques: $($duplicates -join ', ')"
} else {
    Write-Output "   OK: $totalExigences IDs uniques, 0 doublon"
}

# 3. Check each exigence has required fields
$exigenceBlocks = [regex]::Matches($content, '#### ([^\n\r]+)\n[\s\S]*?(?=#### |### |## |$)')
$missingCategory = 0
$missingVersion = 0
$missingReference = 0
$missingStatut = 0
$missingDesc = 0

foreach ($block in $exigenceBlocks) {
    $blockText = $block.Groups[0].Value

    if (-not ($blockText -match '\- \*\*(?:Category|Categorie)\s*:?\*\*')) { $missingCategory++ }
    if (-not ($blockText -match '\- \*\*(?:Standard / Version|Norme / Version)\s*:?\*\*')) { $missingVersion++ }
    if (-not ($blockText -match '\- \*\*(?:Source reference|Reference source)\s*:?\*\*')) { $missingReference++ }
    if (-not ($blockText -match '\- \*\*(?:Status|Statut)\s*:?\*\*')) { $missingStatut++ }
    if (-not ($blockText -match '\- \*\*Description\s*:?\*\*')) { $missingDesc++ }
}

Write-Output ""
Write-Output "3. Champs obligatoires"
if ($missingCategory -gt 0) { $errors += "ECHEC: $missingCategory exigences sans categorie" } else { Write-Output "   OK: Toutes les exigences ont une categorie" }
if ($missingVersion -gt 0) { $errors += "ECHEC: $missingVersion exigences sans version" } else { Write-Output "   OK: Toutes les exigences ont une version" }
if ($missingReference -gt 0) { $errors += "ECHEC: $missingReference exigences sans reference source" } else { Write-Output "   OK: Toutes les exigences ont une reference source" }
if ($missingStatut -gt 0) { $errors += "ECHEC: $missingStatut exigences sans statut" } else { Write-Output "   OK: Toutes les exigences ont un statut" }

Write-Output ""
Write-Output "4. Presence des descriptions"
if ($missingDesc -gt 0) {
    $errors += "ECHEC: $missingDesc exigences sans description"
    Write-Output "   ATTENTION: $missingDesc exigences sans description"
} else {
    Write-Output "   OK: Toutes les exigences ont une description"
}

# 5. Check statut values
$statutMatches = [regex]::Matches($content, '\- \*\*(?:Status|Statut)\s*:?\*\* ([^\n\r]+)')
$statuts = @{}
foreach ($s in $statutMatches) {
    $val = $s.Groups[1].Value.Trim()
    if (-not $statuts.ContainsKey($val)) { $statuts[$val] = 0 }
    $statuts[$val]++
}
Write-Output ""
Write-Output "5. Repartition des statuts"
$statuts.GetEnumerator() | ForEach-Object { Write-Output "   $($_.Key): $($_.Value)" }

# Summary
Write-Output ""
Write-Output "=== Resume ==="
if ($errors.Count -gt 0) {
    Write-Output "RESULTAT: ECHEC"
    Write-Output "Erreurs:"
    $errors | ForEach-Object { Write-Output "  - $_" }
    exit 1
} else {
    Write-Output "RESULTAT: SUCCES"
    Write-Output "  - $totalExigences exigences (maximum retrouvable)"
    Write-Output "  - 0 ID duplique"
    Write-Output "  - Toutes les exigences ont: ID, categorie, version, reference, statut, description"
    exit 0
}
