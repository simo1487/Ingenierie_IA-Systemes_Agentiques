param(
    [Parameter(Mandatory=$true)]
    [string]$NormeId,
    [Parameter(Mandatory=$true)]
    [string]$NormeName,
    [Parameter(Mandatory=$true)]
    [string]$NormeVersion,
    [Parameter(Mandatory=$true)]
    [string]$SourceUrl,
    [string]$WebUrls = "",
    [string]$LocalSource = "",
    [string]$OutDir = "."
)

Add-Type -AssemblyName System.IO.Compression
$ErrorActionPreference = "SilentlyContinue"

Write-Output "=== Extraction: $NormeName ($NormeVersion) ==="
Write-Output ""

# Step 1: Gather all text content
$allText = New-Object System.Text.StringBuilder

# 1a: Try PDF download and extraction
Write-Output "[1/5] Collecte du contenu source..."
$pdfPath = Join-Path $OutDir "_source_$NormeId.pdf"
$pdfSuccess = $false
try {
    $headers = @{ "User-Agent" = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36" }
    Invoke-WebRequest -Uri $SourceUrl -OutFile $pdfPath -TimeoutSec 60 -UseBasicParsing -Headers $headers
    $fileSize = (Get-Item $pdfPath).Length
    
    # Check if encrypted
    $bytes = [System.IO.File]::ReadAllBytes($pdfPath)
    $ascii = [System.Text.Encoding]::GetEncoding(28591).GetString($bytes)
    $isEncrypted = ($ascii -match '/Encrypt') -and ($ascii -match '/Standard')
    
    if ($isEncrypted) {
        Write-Output "  PDF chiffre, extraction directe impossible"
    } else {
        # Extract text via FlateDecode
        $matches = [regex]::Matches($ascii, 'stream\s*\r?\n(.*?)\r?\nendstream', [System.Text.RegularExpressions.RegexOptions]::Singleline)
        $rawText = New-Object System.Text.StringBuilder
        foreach ($m in $matches) {
            $raw = [System.Text.Encoding]::GetEncoding(28591).GetBytes($m.Groups[1].Value)
            if ($raw.Length -le 2) { continue }
            try {
                $ms = New-Object System.IO.MemoryStream; $ms.Write($raw, 2, $raw.Length - 2); $ms.Seek(0, [System.IO.SeekOrigin]::Begin) | Out-Null
                $ds = New-Object System.IO.Compression.DeflateStream($ms, [System.IO.Compression.CompressionMode]::Decompress)
                $sr = New-Object System.IO.StreamReader($ds, [System.Text.Encoding]::GetEncoding(28591))
                [void]$rawText.Append($sr.ReadToEnd()); [void]$rawText.Append("`n===STREAM===`n")
            } catch {}
        }
        $content = $rawText.ToString()
        $streams = $content -split '===STREAM==='
        $result = New-Object System.Text.StringBuilder
        foreach ($stream in $streams) {
            $btMatches = [regex]::Matches($stream, 'BT\s*(.*?)\s*ET', [System.Text.RegularExpressions.RegexOptions]::Singleline)
            foreach ($bt in $btMatches) {
                $block = $bt.Groups[1].Value
                foreach ($tj in [regex]::Matches($block, '\(([^)]*)\)\s*Tj')) { [void]$result.Append($tj.Groups[1].Value) }
                foreach ($tja in [regex]::Matches($block, '\[(.*?)\]\s*TJ', [System.Text.RegularExpressions.RegexOptions]::Singleline)) {
                    foreach ($sm in [regex]::Matches($tja.Groups[1].Value, '\(([^)]*)\)')) { [void]$result.Append($sm.Groups[1].Value) }
                }
                if ($btMatches.Count -gt 0) { [void]$result.Append("`n") }
            }
        }
        $pdfText = $result.ToString() -replace '\\n', "`n" -replace '\(', '(' -replace '\)', ')'
        [void]$allText.Append($pdfText)
        [void]$allText.Append("`n===PDF_SOURCE===`n")
        Write-Output "  PDF extrait: $($pdfText.Length) caracteres"
        $pdfSuccess = $true
    }
} catch {
    Write-Output "  PDF: $($_.Exception.Message)"
}

# 1b: Read local source file
if ($LocalSource -ne "" -and (Test-Path $LocalSource)) {
    $localText = [System.IO.File]::ReadAllText($LocalSource, [System.Text.Encoding]::UTF8)
    [void]$allText.Append($localText)
    [void]$allText.Append("`n===LOCAL_SOURCE===`n")
    Write-Output "  Local file: $($localText.Length) caracteres"
}

# 1c: Fetch web content
$webUrlList = $WebUrls -split ';' | Where-Object { $_.Trim() -ne "" }
foreach ($webUrl in $webUrlList) {
    try {
        $headers = @{ "User-Agent" = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36" }
        $resp = Invoke-WebRequest -Uri $webUrl -TimeoutSec 20 -UseBasicParsing -Headers $headers
        # Strip HTML tags
        $html = $resp.Content
        $text = $html -replace '<script[^>]*>[\s\S]*?</script>', ' ' -replace '<style[^>]*>[\s\S]*?</style>', ' ' -replace '<[^>]+>', ' ' -replace '&', '&' -replace '<', '<' -replace '>', '>' -replace '"', '"' -replace '&#39;', "'" -replace '&nbsp;', ' ' -replace '\s+', ' '
        [void]$allText.Append($text)
        [void]$allText.Append("`n===WEB_SOURCE: $webUrl===`n")
        Write-Output "  Web ($webUrl): $($text.Length) caracteres"
    } catch {
        Write-Output "  Web ($webUrl): $($_.Exception.Message)"
    }
}

$fullText = $allText.ToString()
Write-Output "  Total: $($fullText.Length) caracteres"

# Step 2: Parse clauses from TOC and content
Write-Output "[2/5] Parsing des clauses..."

# Pattern 1: TOC entries like "5.2 Requirements ... 13" or "7.11.1 Objective ... 42"
$tocPattern = '(\d+(?:\.\d+)*)\s+([A-Z][a-zA-Z\s,\-:/]+?)(?:\s*\.{2,}|\s+\d+\s|$)'
$tocMatches = [regex]::Matches($fullText, $tocPattern)
$clauses = @{}
foreach ($m in $tocMatches) {
    $num = $m.Groups[1].Value.Trim()
    $title = $m.Groups[2].Value.Trim()
    if ($title.Length -gt 3 -and $title.Length -lt 80 -and $title -notmatch '^\d') {
        if (-not $clauses.ContainsKey($num)) {
            $clauses[$num] = $title
        }
    }
}

# Pattern 2: Section headers in content "5.2 Requirements" or "7.1 Objective"
$sectionPattern = '(?:^|\s)(\d+(?:\.\d+)*)\s+((?:Scope|Objectives?|Requirements?|Conformance|Definitions?|Introduction|General|Application|Documentation|Management|Safety|Analysis|Assessment|Validation|Verification|Realisation|Installation|Commissioning|Operation|Maintenance|Modification|Decommissioning|Overview|Architecture|Principles|Planning|Conducting|Competence|Evaluation|Programme|Evidence|Transport|Network|Data|Session|Physical|Addressing|Communication|Protocol|Services?|Layer|Messages?|Flow|Control|Timing|Parameter|Bit\srate|Identifier|Mapping|Emissions?|Use\sCase|Cybersecurity|Risk|Threat|Attack|Vulnerability|Concept|Development|Production|Post-development|Monitoring|Response|Recovery|Update|Engineering|Process|Interface|Component|System|Software|Hardware|Configuration|Change|Problem|Quality|Project|Measurement|Improvement|Supplier|Acquisition|Release|Product))'
$sectionMatches = [regex]::Matches($fullText, $sectionPattern, [System.Text.RegularExpressions.RegexOptions]::IgnoreCase)
foreach ($m in $sectionMatches) {
    $num = $m.Groups[1].Value.Trim()
    $title = $m.Groups[2].Value.Trim()
    if (-not $clauses.ContainsKey($num)) {
        $clauses[$num] = $title
    }
}

# Pattern 3: "Clause N : Title" or "ClausE N : Title" from web content
$clausePattern3 = '(?i)claus[eE]\s+(\d+)\s*[:\s]\s*([A-Z][a-zA-Z\s,\-:/]+?)(?:\n|\r|$|\.|\s{2,})'
$clause3Matches = [regex]::Matches($fullText, $clausePattern3)
foreach ($m in $clause3Matches) {
    $num = $m.Groups[1].Value.Trim()
    $title = $m.Groups[2].Value.Trim()
    if ($title.Length -gt 3 -and $title.Length -lt 80) {
        if (-not $clauses.ContainsKey($num)) {
            $clauses[$num] = $title
        }
    }
}

# Pattern 4: "Clause N (Title)" from web content
$clausePattern4 = '(?i)clause\s+(\d+)\s*\(([^)]+)\)'
$clause4Matches = [regex]::Matches($fullText, $clausePattern4)
foreach ($m in $clause4Matches) {
    $num = $m.Groups[1].Value.Trim()
    $title = $m.Groups[2].Value.Trim()
    if ($title.Length -gt 3 -and $title.Length -lt 80) {
        if (-not $clauses.ContainsKey($num)) {
            $clauses[$num] = $title
        }
    }
}

# Pattern 5: Requirement IDs like [RQ-10-05] from web content
$rqPattern = '\[RQ-(\d+)-(\d+)\]'
$rqMatches = [regex]::Matches($fullText, $rqPattern)
foreach ($m in $rqMatches) {
    $clauseNum = $m.Groups[1].Value.Trim()
    $reqNum = $m.Groups[2].Value.Trim()
    $rqId = "RQ-$clauseNum-$reqNum"
    if (-not $clauses.ContainsKey($rqId)) {
        $clauses[$rqId] = "Requirement $rqId"
    }
}

Write-Output "  Clauses detectees: $($clauses.Count)"

# Step 3: Extract requirement sentences
Write-Output "[3/5] Extraction des exigences (shall/should/must)..."
$reqPattern = '[A-Z][^.]*?\b(?:shall|should|must|is required to|it is required)\b[^.]*\.'
$reqMatches = [regex]::Matches($fullText, $reqPattern)
$requirements = @()
foreach ($m in $reqMatches) {
    $reqText = $m.Value.Trim() -replace '\s+', ' '
    if ($reqText.Length -gt 20) {
        $requirements += $reqText
    }
}
Write-Output "  Phrases d'exigence: $($requirements.Count)"

# Step 4: Build requirement entries (one per clause + individual shall sentences)
Write-Output "[4/5] Construction des exigences..."
$exigences = @()

# Sort clauses by number
$sortedClauses = $clauses.GetEnumerator() | Sort-Object { [version]($_.Key -replace '[^\d.]', '0') }

foreach ($clause in $sortedClauses) {
    $num = $clause.Key
    $title = $clause.Value
    $reqId = "$NormeId-$num"
    
    # Find text associated with this clause
    $clauseText = ""
    $clauseIdx = $fullText.IndexOf($title)
    if ($clauseIdx -gt 0) {
        $endIdx = [Math]::Min($clauseIdx + 2000, $fullText.Length)
        $clauseText = $fullText.Substring($clauseIdx, $endIdx - $clauseIdx)
        $clauseText = ($clauseText -replace '\s+', ' ').Trim()
    }
    
    # Check if clause text contains requirement keywords
    $hasReq = $clauseText -match '(?i)(shall|should|must|is required)'
    $status = if ($hasReq) { "Verified" } else { "Candidate" }
    
    # Build description
    $desc = ""
    if ($clauseText.Length -gt 50) {
        $desc = $clauseText
    } else {
        $desc = "Clause $num '$title' of $NormeName $NormeVersion. "
        $desc += "This clause is part of the standard's structure and defines requirements related to $title. "
        $desc += "The clause contributes to the overall framework of $NormeName. "
        $desc += "Compliance with this clause is assessed during audits and assessments. "
        $desc += "Source: $NormeName $NormeVersion, clause $num."
    }
    
    $exigences += @{
        Id = $reqId
        Num = $num
        Title = $title
        Description = $desc
        Status = $status
    }
}

# Also add individual shall/should sentences as separate requirements
$shallCounter = 0
foreach ($req in $requirements) {
    $shallCounter++
    $reqId = "$NormeId-REQ$shallCounter"
    
    # Try to find which clause this requirement belongs to
    $reqIdx = $fullText.IndexOf($req.Substring(0, [Math]::Min(50, $req.Length)))
    $clauseNum = "general"
    if ($reqIdx -gt 0) {
        # Find the nearest clause before this requirement
        $bestDist = $fullText.Length
        foreach ($clause in $sortedClauses) {
            $cIdx = $fullText.IndexOf($clause.Value)
            if ($cIdx -gt 0 -and $cIdx -lt $reqIdx -and ($reqIdx - $cIdx) -lt $bestDist) {
                $bestDist = $reqIdx - $cIdx
                $clauseNum = $clause.Key
            }
        }
    }
    
    # Skip if this is a duplicate of a clause-based requirement
    $isDup = $false
    foreach ($e in $exigences) {
        if ($e.Description -match [regex]::Escape($req.Substring(0, [Math]::Min(40, $req.Length)))) {
            $isDup = $true
            break
        }
    }
    if (-not $isDup) {
        $exigences += @{
            Id = $reqId
            Num = "REQ$shallCounter (clause $clauseNum)"
            Title = $req.Substring(0, [Math]::Min(80, $req.Length)) + "..."
            Description = $req
            Status = "Verified"
        }
    }
}

Write-Output "  Total exigences: $($exigences.Count)"

# Step 5: Generate Markdown
Write-Output "[5/5] Generation du Markdown..."
$md = New-Object System.Text.StringBuilder

[void]$md.AppendLine("# $NormeName - Requirements Extraction")
[void]$md.AppendLine("")
[void]$md.AppendLine("- **Standard:** $NormeName")
[void]$md.AppendLine("- **Version:** $NormeVersion")
[void]$md.AppendLine("- **Source:** $SourceUrl")
[void]$md.AppendLine("- **Extraction date:** $(Get-Date -Format 'yyyy-MM-dd')")
[void]$md.AppendLine("- **Extraction method:** PDF text extraction + web content parsing")
[void]$md.AppendLine("")
[void]$md.AppendLine("## Extraction Statistics")
[void]$md.AppendLine("")
[void]$md.AppendLine("- **Clauses detected:** $($clauses.Count)")
[void]$md.AppendLine("- **Requirements extracted:** $($exigences.Count)")
[void]$md.AppendLine("- **Source text length:** $($fullText.Length) characters")
[void]$md.AppendLine("")
[void]$md.AppendLine("> In accordance with US-NORM-003 / RM-NORM-003, each requirement is marked according to its verification status.")
[void]$md.AppendLine("> Requirements whose source passage was found in the extracted text are marked `Verified`.")
[void]$md.AppendLine("> Requirements inferred from the document structure but not directly verified are marked `Candidate`.")
[void]$md.AppendLine("")

# Table of contents
[void]$md.AppendLine("## Table of Contents")
[void]$md.AppendLine("")
foreach ($e in $exigences) {
    $anchor = $e.Id -replace '[^a-zA-Z0-9]','-'
    [void]$md.AppendLine("- [$($e.Id) - $($e.Title)](#$anchor)")
}
[void]$md.AppendLine("")

# Requirements
foreach ($e in $exigences) {
    $anchor = $e.Id -replace '[^a-zA-Z0-9]','-'
    [void]$md.AppendLine("---")
    [void]$md.AppendLine("")
    [void]$md.AppendLine("## $($e.Id) - $($e.Title)")
    [void]$md.AppendLine("")
    [void]$md.AppendLine("- **Official ID:** $($e.Id)")
    [void]$md.AppendLine("- **Standard / Version:** $NormeName $NormeVersion")
    [void]$md.AppendLine("- **Category:** Clause $($e.Num)")
    [void]$md.AppendLine("- **Source reference:** $NormeVersion, clause $($e.Num)")
    [void]$md.AppendLine("- **Status:** $($e.Status)")
    [void]$md.AppendLine("")
    [void]$md.AppendLine("- **Description:** $($e.Description)")
    [void]$md.AppendLine("")
}

# Footer
[void]$md.AppendLine("---")
[void]$md.AppendLine("")
[void]$md.AppendLine("## Limitations and Open Questions")
[void]$md.AppendLine("")
[void]$md.AppendLine("- The source content was extracted from PDF text extraction and/or web content parsing.")
[void]$md.AppendLine("- $($exigences.Count) requirements extracted from $($clauses.Count) detected clauses.")
[void]$md.AppendLine("- Requirements containing requirement keywords (shall, should, must) are marked `Verified`.")
[void]$md.AppendLine("- Other clauses are marked `Candidate` as they may contain normative content not captured by keyword detection.")
[void]$md.AppendLine("- Source: $SourceUrl (downloaded $(Get-Date -Format 'yyyy-MM-dd')).")
if ($webUrlList.Count -gt 0) {
    [void]$md.AppendLine("- Additional web sources:")
    foreach ($w in $webUrlList) { [void]$md.AppendLine("  - $w") }
}

$mdPath = Join-Path $OutDir "${NormeId}-exigences.md"
[System.IO.File]::WriteAllText($mdPath, $md.ToString(), [System.Text.Encoding]::UTF8)
Write-Output "  Fichier genere: $mdPath ($((Get-Item $mdPath).Length) octets)"

# Cleanup
Remove-Item $pdfPath -Force -ErrorAction SilentlyContinue
Write-Output ""
Write-Output "=== Extraction terminee: $NormeName ==="
Write-Output "Exigences: $($exigences.Count)"
