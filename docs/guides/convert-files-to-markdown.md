---
title: Convert a file library to Markdown & build this site
description: Tools and end-to-end steps to convert Word/PDF libraries into Markdown and publish an MkDocs Material knowledge base
tags:
  - guide
  - mkdocs
  - conversion
  - pandoc
  - markitdown
---

# Convert a file library to Markdown (and rebuild this whole site)

This guide covers two things:

1. **How to turn a whole folder (or “database”) of documents into Markdown**
2. **How to build everything in this project** — MkDocs Material site, structure, search, Git, and GitHub Pages

Use it when you have a pile of Word, PDF, HTML, or similar files and want a searchable docs site like this one.

---

## Part 1 — Convert an entire document library to Markdown

### Recommended apps

| Tool | Best for | Notes |
|------|----------|--------|
| **[Pandoc](https://pandoc.org/)** | Word (`.docx`), HTML, RTF, many formats → Markdown | Industry standard CLI. Install once, script batches easily. |
| **[Microsoft MarkItDown](https://github.com/microsoft/markitdown)** | Mixed folders: DOCX, PDF, PPTX, XLSX, images, HTML | Python package; strong “whole library” converter. |
| **[Docling](https://github.com/DS4SD/docling)** (IBM) | Messy PDFs, complex layout | Heavier install; excellent PDF structure recovery. |
| **LibreOffice + Pandoc** | Old `.doc` files | Convert `.doc` → `.docx` first, then Pandoc. |

**Practical pick for most service-desk libraries**

- **Word-heavy folders** → **Pandoc**
- **Mixed Office + PDF dump** → **MarkItDown**
- **Scanned / layout-heavy PDFs** → **Docling** (then clean in Markdown)

!!! tip "There is no perfect one-click database button"
    Treat your shared drive, SharePoint export, or file share as the “database.” Export or copy files into one folder tree, then batch-convert into `docs/`.

---

### Option A — Pandoc (Word / HTML batch)

#### Install

=== "Windows (winget)"

    ```powershell
    winget install --id JohnMacFarlane.Pandoc -e
    pandoc --version
    ```

=== "Windows (installer)"

    Download from [pandoc.org/installing.html](https://pandoc.org/installing.html), then open a **new** terminal and run `pandoc --version`.

#### Convert one file

```powershell
pandoc ".\source\password-reset.docx" -t gfm -o ".\docs\how-to\password-reset.md"
```

- `-t gfm` = GitHub-Flavored Markdown (tables work well in MkDocs)
- For older Markdown: `-t markdown`

#### Convert an entire folder of Word files

Save as `scripts/convert-with-pandoc.ps1` (also in this repo under `scripts/`):

```powershell
param(
  [string]$SourceDir = ".\sample-data\word",
  [string]$OutDir = ".\docs\imported"
)

New-Item -ItemType Directory -Force -Path $OutDir | Out-Null
Get-ChildItem -Path $SourceDir -Filter *.docx -Recurse | ForEach-Object {
  $rel = $_.FullName.Substring((Resolve-Path $SourceDir).Path.Length).TrimStart('\')
  $out = Join-Path $OutDir ($rel -replace '\.docx$', '.md')
  New-Item -ItemType Directory -Force -Path (Split-Path $out) | Out-Null
  Write-Host "Converting $($_.Name) -> $out"
  pandoc $_.FullName -t gfm -o $out --wrap=none
}
Write-Host "Done. Review files under $OutDir then move into docs/ categories."
```

Run:

```powershell
cd ~\MKDocs-figuring-out-stuff
.\scripts\convert-with-pandoc.ps1 -SourceDir ".\sample-data\word" -OutDir ".\docs\imported"
```

#### PDF with Pandoc

Pandoc’s PDF **read** support is limited (often needs `pdftotext` / poppler). Prefer **MarkItDown** or **Docling** for bulk PDF.

---

### Option B — MarkItDown (mixed formats, whole library)

#### Install (in this project’s venv)

```powershell
cd ~\MKDocs-figuring-out-stuff
.\.venv\Scripts\Activate.ps1
pip install "markitdown[all]"
```

#### Convert one file

```powershell
markitdown ".\sample-data\word\01-service-desk-overview.docx" -o ".\docs\imported\overview.md"
```

#### Convert a whole tree

```powershell
# Example: walk every supported file under sample-data
$src = ".\sample-data"
$out = ".\docs\imported"
New-Item -ItemType Directory -Force -Path $out | Out-Null

Get-ChildItem $src -Recurse -File | Where-Object {
  $_.Extension -match '\.(docx|pdf|pptx|html|htm|xlsx|csv|json|xml)$'
} | ForEach-Object {
  $name = [IO.Path]::GetFileNameWithoutExtension($_.Name) + ".md"
  $dest = Join-Path $out $name
  Write-Host "Converting $($_.FullName)"
  markitdown $_.FullName -o $dest
}
```

A ready script lives at `scripts/convert-with-markitdown.ps1`.

---

### After conversion — always clean the Markdown

Automated conversion is **step one**, not the finish line.

| Check | What to do |
|-------|------------|
| Titles | One `#` H1 per page; use `##` / `###` for sections |
| Tables | Confirm pipes align; fix broken cells |
| Lists | Prefer real Markdown lists, not leftover bullet characters |
| Images | Put under `docs/assets/` and fix `![](...)` paths |
| Front matter | Optional YAML at top for title/tags (this site uses it) |
| Nav | Add each new page under `nav:` in `mkdocs.yml` |
| Filenames | `kebab-case.md` (e.g. `password-reset.md`) |

!!! warning "Do not publish raw dumps"
    Run `mkdocs serve`, click through pages, and fix anything agents would stumble on.

---

### Suggested folder layout after import

```text
docs/
  index.md                 # home
  getting-started/
  how-to/
  policies/
  reference/
  guides/                  # meta how-tos (this page)
  imported/                # temp drop zone from converters
  assets/
  stylesheets/
sample-data/               # original Word/PDF sources (optional archive)
```

Move polished files out of `imported/` into the right category folders.

---

## Part 2 — How this site was built (full recipe)

Everything below matches what was set up for **Dan's Service Desk Knowledge Base**.

### 1. Project folder + Python virtual environment

```powershell
mkdir ~\MKDocs-figuring-out-stuff
cd ~\MKDocs-figuring-out-stuff
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
```

### 2. Install MkDocs + Material + useful plugins

```powershell
pip install mkdocs mkdocs-material pymdown-extensions `
  mkdocs-git-revision-date-localized-plugin `
  mkdocs-git-committers-plugin-2
pip freeze > requirements.txt
```

| Package | Why |
|---------|-----|
| `mkdocs` | Static site generator |
| `mkdocs-material` | Modern theme, search, dark mode, cards, tabs |
| `pymdown-extensions` | Admonitions, task lists, better fences |
| `git-revision-date-localized` | “Last updated” from Git history |

### 3. Scaffold the site

```powershell
mkdocs new .
```

Then replace the default config with a Material setup (this repo’s `mkdocs.yml`):

- Theme: Material, light/dark, sticky tabs, **search.suggest / highlight / share**
- Plugins: `search`, `tags`, git revision dates
- Extensions: admonitions, tables, task lists, emoji, tabbed content
- Custom CSS: `docs/stylesheets/extra.css`
- Optional override: `overrides/main.html` (announcement bar)

### 4. Write (or convert) content into Markdown

Two paths used in this project:

1. **Author in Markdown** under `docs/` (fastest for new content)
2. **Keep sources** in `sample-data/word` and `sample-data/pdf`, convert → clean → place under `docs/`

Each article should include:

- Clear H1 title  
- Short intro  
- Numbered procedures where agents must follow steps  
- Tables for severity/SLA matrices  
- Admonitions for warnings (`!!! warning`, `!!! danger`)

### 5. Wire navigation

In `mkdocs.yml`, list every page under `nav:` so the header tabs and sidebar match your IA:

```yaml
nav:
  - Home: index.md
  - Getting started:
      - Overview: getting-started/overview.md
  - How-to:
      - Password reset: how-to/password-reset.md
  - Guides:
      - Convert files to Markdown: guides/convert-files-to-markdown.md
```

### 6. Preview locally

```powershell
cd ~\MKDocs-figuring-out-stuff
.\.venv\Scripts\Activate.ps1
mkdocs serve
```

Open **http://127.0.0.1:8000/**  
Press **`/`** to search. Edit a file under `docs/` and the page reloads.

Build a static copy anytime:

```powershell
mkdocs build
# output → site/
```

### 7. Git + GitHub

```powershell
git init
# add .gitignore with .venv/ and site/
git add .
git commit -m "Initial service desk knowledge base"
```

Create or rename a GitHub repo, then:

```powershell
git remote add origin https://github.com/YOUR_USER/MKDocs-figuring-out-stuff.git
git branch -M master
git push -u origin master
```

Tools used along the way:

- **Git for Windows** — CLI  
- **GitHub Desktop** — visual commits / publish  
- **GitHub CLI (`gh`)** — optional automation  

### 8. Publish with GitHub Pages

In `mkdocs.yml`:

```yaml
site_url: https://YOUR_USER.github.io/MKDocs-figuring-out-stuff/
repo_url: https://github.com/YOUR_USER/MKDocs-figuring-out-stuff
```

Deploy:

```powershell
mkdocs gh-deploy --force
```

That builds the site and pushes the `gh-pages` branch.

GitHub → **Settings → Pages** → Source: **Deploy from a branch** → `gh-pages` / root.

!!! note "Private repos"
    Free GitHub Pages requires a **public** repository (or a paid plan for private Pages).

Live example for this project:

**https://dgooding.github.io/MKDocs-figuring-out-stuff/**

CI option: `.github/workflows/deploy-docs.yml` runs `mkdocs gh-deploy` on every push to `master`.

### 9. Visual polish (what makes it look “real”)

| Feature | How |
|---------|-----|
| Search | Material `search` plugin + `search.suggest` / `highlight` |
| Dark mode | Theme `palette` toggles in `mkdocs.yml` |
| Cards on home | Material grid cards in `docs/index.md` |
| Brand colors | `docs/stylesheets/extra.css` |
| Logo / favicon | `docs/assets/logo.svg`, `favicon.svg` |
| Announcement bar | `overrides/main.html` |
| Tags | YAML `tags:` on pages + `tags` plugin |

### 10. Ongoing workflow for your team

```text
1. Drop new Word/PDF into sample-data/ (or a share export folder)
2. Convert with Pandoc or MarkItDown → docs/imported/
3. Clean headings, tables, links
4. Move into how-to/ / policies/ / reference/
5. Add nav entry in mkdocs.yml
6. mkdocs serve → review
7. git commit && git push  (Actions or gh-deploy publishes)
```

---

## Quick command cheat sheet

```powershell
cd ~\MKDocs-figuring-out-stuff
.\.venv\Scripts\Activate.ps1

# Preview
mkdocs serve

# Build only
mkdocs build

# Convert Word library (Pandoc)
.\scripts\convert-with-pandoc.ps1 -SourceDir ".\path\to\docx-root" -OutDir ".\docs\imported"

# Convert mixed library (MarkItDown)
pip install "markitdown[all]"
.\scripts\convert-with-markitdown.ps1 -SourceDir ".\path\to\files" -OutDir ".\docs\imported"

# Publish
git add -A
git commit -m "Add converted articles"
git push
mkdocs gh-deploy --force
```

---

## Related pages

- [Knowledge base authoring standards](../reference/kb-authoring.md)
- [Service desk overview](../getting-started/overview.md)
- [Home](../index.md)

---

## Source files in this repo

| Path | Role |
|------|------|
| `sample-data/word/` | Example Word SOPs |
| `sample-data/pdf/` | Example PDF policies |
| `docs/` | Live Markdown site content |
| `mkdocs.yml` | Site config, theme, nav, search |
| `scripts/convert-with-pandoc.ps1` | Batch Word → Markdown |
| `scripts/convert-with-markitdown.ps1` | Batch mixed formats → Markdown |
| `scripts/generate_sample_docs.py` | Regenerates sample Word/PDF demos |
| `.github/workflows/deploy-docs.yml` | Auto-deploy on push |
