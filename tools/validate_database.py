#!/usr/bin/env python3
"""Read-only checks for the Rich Presence image database.

Run from the repository root:
    python tools/validate_database.py
"""
from collections import Counter
from pathlib import Path
import json
import sys

ROOT = Path(__file__).resolve().parent.parent
TITLES = ROOT / "titles.json"
ICONS = ROOT / "icons"

def main():
    problems = []
    duplicate_keys = []
    def load_pairs(pairs):
        result = {}
        for key, value in pairs:
            if key in result:
                duplicate_keys.append(key)
            result[key] = value
        return result

    try:
        with TITLES.open(encoding="utf-8") as file:
            entries = json.load(file, object_pairs_hook=load_pairs)
    except (OSError, json.JSONDecodeError) as exc:
        print(f"ERROR: unable to read titles.json: {exc}")
        return 1

    if not isinstance(entries, dict):
        print("ERROR: titles.json must be a JSON object")
        return 1

    for name in duplicate_keys:
        problems.append(f"Duplicate title key: {name!r}")

    missing = []
    for title, icon in entries.items():
        if not isinstance(title, str) or not title.strip():
            problems.append(f"Invalid title: {title!r}")
        if not isinstance(icon, str) or not icon.lower().endswith(".jpg"):
            problems.append(f"Invalid JPEG filename for {title!r}: {icon!r}")
            continue
        if Path(icon).name != icon or "/" in icon or "\\\\" in icon:
            problems.append(f"Unsafe icon filename for {title!r}: {icon!r}")
            continue
        if not (ICONS / icon).is_file():
            missing.append((title, icon))

    print(f"Checked {len(entries)} game mappings.")
    print(f"Missing referenced icons: {len(missing)}")
    for title, icon in missing[:25]:
        print(f"  MISSING {title!r} -> {icon}")
    if len(missing) > 25:
        print(f"  ... and {len(missing) - 25} more")
    for problem in problems:
        print(f"ERROR: {problem}")
    return 1 if problems or missing else 0

if __name__ == "__main__":
    sys.exit(main())
