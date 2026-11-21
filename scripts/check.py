#!/usr/bin/env python3
"""Check that every local file the site's HTML and CSS refer to exists."""

import re
import sys
from pathlib import Path

SITE = Path(__file__).resolve().parent.parent / "site"
HTML_REF = re.compile(r'(?:href|src|data-src)="([^"#]+)"')
CSS_REF = re.compile(r'url\("([^"]+)"\)')
EXTERNAL = ("http://", "https://", "mailto:")


def local_refs(path: Path) -> list[str]:
    pattern = CSS_REF if path.suffix == ".css" else HTML_REF
    refs = pattern.findall(path.read_text(encoding="utf-8"))
    return [ref for ref in refs if not ref.startswith(EXTERNAL) and ref != "/"]


def main() -> int:
    missing = []
    for page in [*SITE.glob("*.html"), *SITE.glob("*.css")]:
        for ref in local_refs(page):
            target = SITE / ref.lstrip("/")
            if not target.is_file():
                missing.append(f"{page.name}: {ref}")
    for line in missing:
        print(f"missing: {line}")
    if not missing:
        print("all local references resolve")
    return 1 if missing else 0


if __name__ == "__main__":
    sys.exit(main())
