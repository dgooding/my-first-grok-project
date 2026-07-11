"""Full site audit: links, nav, encoding, config consistency."""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
link_re = re.compile(r"\[([^\]]*)\]\(([^)]+)\)")


def main() -> None:
    md_files = list(DOCS.rglob("*.md"))
    print(f"PAGES: {len(md_files)}")
    issues = []
    for p in md_files:
        raw = p.read_bytes()
        if raw.startswith(b"\xef\xbb\xbf"):
            issues.append((str(p.relative_to(ROOT)), "BOM", "UTF-8 BOM present"))
        text = raw.decode("utf-8-sig")
        if "\ufffd" in text or "???" in text or "Γ" in text:
            issues.append((str(p.relative_to(ROOT)), "ENCODING", "suspicious characters"))
        for m in link_re.finditer(text):
            href = m.group(2).strip()
            if " " in href and not href.startswith("<"):
                href = href.split()[0].strip('"')
            if href.startswith(("#", "http://", "https://", "mailto:", "javascript:")):
                continue
            href_path = href.split("#")[0].split("?")[0]
            if not href_path or href_path == "...":
                issues.append((str(p.relative_to(ROOT)), href, "BAD_HREF"))
                continue
            target = (p.parent / href_path).resolve()
            try:
                rel = target.relative_to(DOCS.resolve()).as_posix()
            except ValueError:
                issues.append((str(p.relative_to(ROOT)), href, "outside docs"))
                continue
            ok = (
                target.is_file()
                or target.with_suffix(".md").is_file()
                or (target.is_dir() and (target / "index.md").is_file())
                or (DOCS / f"{rel}.md").is_file()
                or (DOCS / rel / "index.md").is_file()
            )
            if not ok:
                issues.append((str(p.relative_to(ROOT)), href, "MISSING"))

    yml = (ROOT / "mkdocs.yml").read_text(encoding="utf-8")
    nav_section = yml.split("nav:", 1)[1] if "nav:" in yml else ""
    nav_files = re.findall(r":\s*([A-Za-z0-9_./-]+\.md)", nav_section)
    for f in nav_files:
        if not (DOCS / f).is_file():
            issues.append(("mkdocs.yml", f, "NAV_MISSING"))

    for p in sorted(x.relative_to(DOCS).as_posix() for x in md_files):
        if p == "index.md":
            continue
        if p not in nav_files:
            print("ORPHAN_OK_IF_INTENTIONAL:", p)

    # assets
    for asset in ["assets/logo.svg", "assets/favicon.svg", "stylesheets/extra.css", "javascripts/mathjax.js"]:
        if not (DOCS / asset).is_file():
            issues.append(("docs", asset, "ASSET_MISSING"))

    print(f"ISSUES: {len(issues)}")
    for i in issues:
        print(" -", i)

    # header search check
    header = (ROOT / "overrides/partials/header.html").read_text(encoding="utf-8")
    if "material/search" in header and "material/search" not in yml and "\n  - search" in yml:
        print("WARN: header expects material/search but yml may use different plugin")
    if "material/search" in yml:
        print("OK: material/search configured")


if __name__ == "__main__":
    main()
