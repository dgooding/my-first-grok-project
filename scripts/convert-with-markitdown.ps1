# Batch-convert mixed Office/PDF files to Markdown with Microsoft MarkItDown.
# Usage:
#   .\.venv\Scripts\Activate.ps1
#   pip install "markitdown[all]"
#   .\scripts\convert-with-markitdown.ps1 -SourceDir ".\sample-data" -OutDir ".\docs\imported"

param(
    [string]$SourceDir = ".\sample-data",
    [string]$OutDir = ".\docs\imported"
)

$ErrorActionPreference = "Stop"

$markitdown = $null
if (Get-Command markitdown -ErrorAction SilentlyContinue) {
    $markitdown = "markitdown"
} elseif (Test-Path ".\.venv\Scripts\markitdown.exe") {
    $markitdown = (Resolve-Path ".\.venv\Scripts\markitdown.exe").Path
} else {
    Write-Error "markitdown not found. Run: pip install `"markitdown[all]`""
}

if (-not (Test-Path $SourceDir)) {
    Write-Error "Source directory not found: $SourceDir"
}

New-Item -ItemType Directory -Force -Path $OutDir | Out-Null

$extensions = @(".docx", ".pdf", ".pptx", ".html", ".htm", ".xlsx", ".csv", ".json", ".xml", ".txt", ".md")
$files = Get-ChildItem -Path $SourceDir -Recurse -File | Where-Object {
    $extensions -contains $_.Extension.ToLowerInvariant()
}

if (-not $files) {
    Write-Warning "No supported files under $SourceDir"
    exit 0
}

$usedNames = @{}
foreach ($file in $files) {
    $base = [IO.Path]::GetFileNameWithoutExtension($file.Name)
    $destName = "$base.md"
    # Avoid overwrites when same filename appears in different folders
    if ($usedNames.ContainsKey($destName)) {
        $destName = "{0}-{1}.md" -f $base, $usedNames[$destName]
        $usedNames[$base]++
    } else {
        $usedNames[$destName] = 1
    }
    $outPath = Join-Path $OutDir $destName
    Write-Host "Converting: $($file.FullName) -> $outPath"
    & $markitdown $file.FullName -o $outPath
}

Write-Host ""
Write-Host "Done. Converted $($files.Count) file(s) into $OutDir"
Write-Host "Review, clean headings/tables, then move pages into docs/ categories and update mkdocs.yml nav."
