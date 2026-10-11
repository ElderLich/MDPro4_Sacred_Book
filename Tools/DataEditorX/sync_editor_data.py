#!/usr/bin/env python3
"""Promote reviewed Sacred Book references into DataEditorX's tooltip data."""

from __future__ import annotations

import argparse
import hashlib
from pathlib import Path


WORKSPACE = Path(__file__).resolve().parents[2]
GENERATED = WORKSPACE / "Generated" / "FunctionDocs"
FILES = {
    "_functions.generated.txt": "_functions.txt",
    "_function_english.generated.txt": "_function_english.txt",
    "constant_english.generated.lua": "constant.lua",
    "rush/_functions.generated.txt": "_rush_functions.txt",
    "rush/_function_english.generated.txt": "_rush_function_english.txt",
    "rush/constant_english.generated.lua": "rush_constant.lua",
}


def sync(destination: Path, check: bool = False) -> int:
    # Read every input before writing anything, so an incomplete generation
    # cannot leave the editor with only half of the new references.
    contents = {name: (GENERATED / source).read_bytes() for source, name in FILES.items()}
    for name, content in contents.items():
        text = content.decode("utf-8-sig")
        if not text.strip() or (name.endswith(".txt") and "●" not in text):
            raise ValueError(f"Invalid generated reference: {name}")
    lua_dir = destination.resolve() / "lua"
    if not check:
        lua_dir.mkdir(parents=True, exist_ok=True)
    mismatches = 0
    for name, content in contents.items():
        target = lua_dir / name
        identical = target.exists() and target.read_bytes() == content
        if check and not identical:
            print(f"OUT OF DATE: {target}")
            mismatches += 1
        elif not check and not identical:
            target.write_bytes(content)
        print(f"{name}: {hashlib.sha256(content).hexdigest()}")
    return 1 if mismatches else 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--destination", required=True, type=Path, help="DataEditorX/data directory")
    parser.add_argument("--check", action="store_true", help="Verify exact matches without writing")
    args = parser.parse_args()
    return sync(args.destination, args.check)


if __name__ == "__main__":
    raise SystemExit(main())
