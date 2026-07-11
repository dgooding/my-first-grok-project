---
title: Convert a file library to Markdown and build this site
description: Tools and end-to-end steps to convert Word/PDF libraries into Markdown and publish an MkDocs Material knowledge base
tags:
  - guide
  - mkdocs
  - conversion
---

# Convert a file library to Markdown (and rebuild this site)

This guide covers two things:

1. **How to turn a whole folder of documents into Markdown**
2. **How to build a site like this project** — MkDocs Material, structure, search, Git, and GitHub Pages

Use it when you have Word, PDF, HTML, or similar files and want a searchable docs site.

---

## Part 1 — Convert an entire document library to Markdown

### Recommended apps

| Tool | Best for | Notes |
|------|----------|--------|
| **[Pandoc](https://pandoc.org/)** | Word (`.docx`), HTML, RTF to Markdown | Industry standard CLI; easy to batch |
| **[Microsoft MarkItDown](https://github.com/microsoft/markitdown)** | Mixed DOCX, PDF, PPTX, XLSX, HTML | Strong whole-library converter |
| **[Docling](https://github.com/DS4SD/docling)** | Complex PDFs | Heavier install; good layout recovery |
| **LibreOffice + Pandoc** | Legacy `.doc` | Convert to `.docx` first, then Pandoc |

**Practical picks**

- Word-heavy folders → **Pandoc**
- Mixed Office + PDF → **MarkItDown**
- Scanned or messy PDFs → **Docling**, then clean Markdown

!!! tip "Treat a file share as the source library"
    Copy or export files into one folder tree, then batch-convert into `docs/`.

### Option A — Pandoc

=== "Windows (winget)"

    ```powershell
    winget install --id JohnMacFarlane.Pandoc -e
    pandoc --version
    ```

=== "Installer"

    Download from [pandoc.org/installing.html](https://pandoc.org/installing.html), open a new terminal, run `pandoc --version`.

**One file**

```powershell
pandoc ".\source\password-reset.docx" -t gfm -o ".\docs\how-to\password-reset.md"
```

**Whole folder** (script in this repo)

```powershell
cd ~\MKDocs-figuring-out-stuff
.\scripts\convert-with-pandoc.ps1 -SourceDir ".\sample-data\word" -OutDir ".\docs\imported"
```

### Option B — MarkItDown

```powershell
cd ~\MKDocs-figuring-out-stuff
.\.venv\Scripts\Activate.ps1
pip install "markitdown[all]"
.\scripts\convert-with-markitdown.ps1 -SourceDir ".\sample-data" -OutDir ".\docs\imported"
```

### After conversion

| Check | Action |
|-------|--------|
| Titles | One `#` H1 per page |
| Tables | Fix broken pipes |
| Lists | Real Markdown lists |
| Images | Store under `docs/assets/` and fix image paths |
| Nav | Add each page under `nav:` in `mkdocs.yml` |
| Names | Prefer `kebab-case.md` |

!!! warning "Review before publish"
    Run `mkdocs serve` and click through pages before deploying.

### Suggested layout

```text
docs/
  index.md
  getting-started/
  how-to/
  policies/
  reference/
  guides/
  showcase/     # optional demos (header star on this site)
  imported/     # temp conversion drop zone
  assets/
sample-data/    # original Word/PDF sources
```

---

## Part 2 — How this site was built

### 1. Project and venv

```powershell
mkdir ~\MKDocs-figuring-out-stuff
cd ~\MKDocs-figuring-out-stuff
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
```

### 2. Install packages

```powershell
pip install mkdocs mkdocs-material pymdown-extensions `
  mkdocs-git-revision-date-localized-plugin
pip freeze > requirements.txt
```

### 3. Configure Material

```powershell
mkdocs new .
```

Then configure `mkdocs.yml` for Material theme, palette, and plugins. Important for the header search bar:

```yaml
plugins:
  - material/search
```

This repo also uses:

- `docs/stylesheets/extra.css` — styling  
- `overrides/main.html` — announcement bar  
- `overrides/partials/header.html` — header star to the showcase  

### 4. Content

Author Markdown under `docs/`, or convert from `sample-data/` then clean and file under the right folders.

### 5. Navigation

```yaml
nav:
  - Home: index.md
  - Getting started:
      - Overview: getting-started/overview.md
  - Guides:
      - Convert files to Markdown: guides/convert-files-to-markdown.md
  - How-to:
      - Password reset: how-to/password-reset.md
```

### 6. Preview and build

```powershell
mkdocs serve   # http://127.0.0.1:8000/  — press / to search
mkdocs build   # output → site/
```

### 7. GitHub Pages

```yaml
site_url: https://YOUR_USER.github.io/MKDocs-figuring-out-stuff/
repo_url: https://github.com/YOUR_USER/MKDocs-figuring-out-stuff
```

```powershell
git add -A
git commit -m "Update docs"
git push
mkdocs gh-deploy --force
```

GitHub → **Settings → Pages** → Deploy from branch → `gh-pages` / root.

Live example: https://dgooding.github.io/MKDocs-figuring-out-stuff/

---

## Quick commands

```powershell
cd ~\MKDocs-figuring-out-stuff
.\.venv\Scripts\Activate.ps1
mkdocs serve
.\scripts\convert-with-pandoc.ps1 -SourceDir ".\sample-data\word" -OutDir ".\docs\imported"
mkdocs gh-deploy --force
```

## Related

- [Knowledge base authoring](../reference/kb-authoring.md)
- [Service desk overview](../getting-started/overview.md)
- [Home](../index.md)

## Repo paths

| Path | Role |
|------|------|
| `sample-data/word/` | Example Word sources |
| `sample-data/pdf/` | Example PDF sources |
| `docs/` | Live Markdown content |
| `mkdocs.yml` | Site configuration |
| `scripts/convert-with-pandoc.ps1` | Batch Word conversion |
| `scripts/convert-with-markitdown.ps1` | Batch mixed conversion |
| `.github/workflows/deploy-docs.yml` | CI deploy on push |
