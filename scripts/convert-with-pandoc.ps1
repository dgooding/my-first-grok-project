# Batch-convert Word (.docx) files to GitHub-Flavored Markdown with Pandoc.
# Usage:
#   .\scripts\convert-with-pandoc.ps1 -SourceDir ".\sample-data\word" -OutDir ".\docs\imported"

param(
    [string]$SourceDir = ".\sample-data\word",
    [string]$OutDir = ".\docs\imported"
)

$ErrorActionPreference = "Stop"

if (-not (Get-Command pandoc -ErrorAction SilentlyContinue)) {
    Write-Error "pandoc not found. Install with: winget install --id JohnMacFarlane.Pandoc -e"
}

if (-not (Test-Path $SourceDir)) {
    Write-Error "Source directory not found: $SourceDir"
}

$sourceRoot = (Resolve-Path $SourceDir).Path
New-Item -ItemType Directory -Force -Path $OutDir | Out-Null

$files = Get-ChildItem -Path $SourceDir -Filter *.docx -Recurse -File
if (-not $files) {
    Write-Warning "No .docx files under $SourceDir"
    exit 0
}

foreach ($file in $files) {
    $rel = $file.FullName.Substring($sourceRoot.Length).TrimStart('\', '/')
    $outRel = [IO.Path]::ChangeExtension($rel, ".md")
    $outPath = Join-Path $OutDir $outRel
    $outParent = Split-Path $outPath -Parent
    New-Item -ItemType Directory -Force -Path $outParent | Out-Null
    Write-Host "Converting: $rel"
    & pandoc $file.FullName -t gfm -o $outPath --wrap=none
}

Write-Host ""
Write-Host "Done. Converted $($files.Count) file(s) into $OutDir"
Write-Host "Review, clean headings/tables, then move pages into docs/how-to, docs/policies, etc."
Write-Host "Add each page to nav: in mkdocs.yml and run: mkdocs serve"
