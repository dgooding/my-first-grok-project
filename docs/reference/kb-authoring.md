---
title: Knowledge Base Authoring
description: How to write articles that work well in MkDocs
tags:
  - reference
  - documentation
  - mkdocs
---

# Knowledge Base Authoring Guidelines

!!! info "STD-KB-004 · v1.0"
    Consistent structure makes search and navigation delightful.

## Why structure matters

MkDocs shines when articles use clear titles, short procedures, and consistent headings — exactly what you see across this sample site.

## Article template

1. **Title** — task-oriented (e.g. *Reset your VPN client*)
2. **Summary** — 1–2 sentences
3. **Before you begin** — prerequisites
4. **Steps** — numbered, one action each
5. **Result** — what success looks like
6. **Related articles** — links

## Style rules

- Active voice, second person (*you*)
- Screenshots only when the UI is non-obvious
- Risk callouts with admonitions (`!!! warning`, `!!! danger`)
- Review quarterly or after major product changes

## MkDocs learning tip

Map each source heading to `##` / `###`, turn bullets into Markdown lists, and place pages under topic folders like `how-to/` and `policies/`.
