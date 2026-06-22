#!/usr/bin/env python3
"""Validate internal markdown links in the Sacred Book docs trees."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path
from urllib.parse import unquote, urlsplit


DEFAULT_ROOTS = [
    Path("docs"),
    Path("Generated") / "FunctionDocs" / "wiki",
]

INLINE_LINK_RE = re.compile(r"(?<!!)\[[^\]\n]*(?:\][^\[\]\n]*)*]\(([^)\s]+)(?:\s+\"[^\"]*\")?\)")
REFERENCE_LINK_RE = re.compile(r"^\s{0,3}\[[^\]]+]:\s*(\S+)")
HTML_LINK_RE = re.compile(r"""<a\s+[^>]*href=["']([^"']+)["']""", re.IGNORECASE)
HEADING_RE = re.compile(r"^\s{0,3}(#{1,6})\s+(.+?)\s*#*\s*$")


def strip_code_blocks(text: str) -> str:
    lines: list[str] = []
    in_fence = False
    fence_marker = ""
    for line in text.splitlines():
        stripped = line.lstrip()
        if stripped.startswith(("```", "~~~")):
            marker = stripped[:3]
            if not in_fence:
                in_fence = True
                fence_marker = marker
            elif marker == fence_marker:
                in_fence = False
                fence_marker = ""
            lines.append("")
            continue
        lines.append("" if in_fence else line)
    return "\n".join(lines)


def is_external(target: str) -> bool:
    parsed = urlsplit(target)
    if parsed.scheme in {"http", "https", "mailto", "tel"}:
        return True
    if target.startswith("//"):
        return True
    return False


def clean_target(target: str) -> str:
    target = target.strip().strip("<>")
    if target.startswith("<") and target.endswith(">"):
        target = target[1:-1]
    return target


def markdown_links(path: Path) -> list[tuple[int, str]]:
    text = strip_code_blocks(path.read_text(encoding="utf-8", errors="replace"))
    links: list[tuple[int, str]] = []
    for line_number, line in enumerate(text.splitlines(), 1):
        for match in INLINE_LINK_RE.finditer(line):
            links.append((line_number, clean_target(match.group(1))))
        ref_match = REFERENCE_LINK_RE.match(line)
        if ref_match:
            links.append((line_number, clean_target(ref_match.group(1))))
        for match in HTML_LINK_RE.finditer(line):
            links.append((line_number, clean_target(match.group(1))))
    return links


def slugify_heading(text: str) -> str:
    text = re.sub(r"<[^>]+>", "", text)
    text = re.sub(r"`([^`]*)`", r"\1", text)
    text = text.strip().lower()
    text = re.sub(r"[^\w\u3400-\u9fff -]", "", text, flags=re.UNICODE)
    text = re.sub(r"\s+", "-", text)
    return text.strip("-")


def heading_ids(path: Path) -> set[str]:
    text = strip_code_blocks(path.read_text(encoding="utf-8", errors="replace"))
    ids: set[str] = set()
    seen: dict[str, int] = {}
    for line in text.splitlines():
        match = HEADING_RE.match(line)
        if not match:
            continue
        base = slugify_heading(match.group(2))
        if not base:
            continue
        count = seen.get(base, 0)
        seen[base] = count + 1
        ids.add(base if count == 0 else f"{base}-{count}")
    return ids


def candidate_files(path: Path) -> list[Path]:
    if path.suffix:
        return [path]
    return [
        path.with_suffix(".md"),
        path / "index.md",
        path,
    ]


def resolve_target(current_file: Path, root: Path, target: str) -> Path | None:
    split = urlsplit(target)
    target_path = unquote(split.path)
    if not target_path:
        return current_file
    if target_path.startswith("/"):
        public_candidate = root / "public" / target_path.lstrip("/")
        if public_candidate.exists():
            return public_candidate
        base = root / target_path.lstrip("/")
    else:
        base = current_file.parent / target_path
    for candidate in candidate_files(base):
        if candidate.exists():
            return candidate.resolve()
    return None


def validate_root(root: Path) -> list[str]:
    problems: list[str] = []
    root = root.resolve()
    anchor_cache: dict[Path, set[str]] = {}
    for path in sorted(root.rglob("*.md")):
        for line_number, target in markdown_links(path):
            if not target or is_external(target):
                continue
            split = urlsplit(target)
            if split.scheme:
                continue
            resolved = resolve_target(path, root, target)
            rel_path = path.relative_to(root).as_posix()
            if resolved is None:
                problems.append(f"{root.name}/{rel_path}:{line_number}: missing target {target}")
                continue
            if split.fragment and resolved.suffix == ".md":
                anchors = anchor_cache.setdefault(resolved, heading_ids(resolved))
                fragment = unquote(split.fragment).lower()
                if fragment not in anchors:
                    target_rel = resolved.relative_to(root).as_posix()
                    problems.append(
                        f"{root.name}/{rel_path}:{line_number}: missing anchor #{split.fragment} in {target_rel}"
                    )
    return problems


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("roots", nargs="*", type=Path, default=DEFAULT_ROOTS)
    args = parser.parse_args()

    problems: list[str] = []
    for root in args.roots:
        if not root.exists():
            problems.append(f"{root}: docs root does not exist")
            continue
        problems.extend(validate_root(root))

    if problems:
        print("Markdown link validation failed:", file=sys.stderr)
        for problem in problems:
            print(f"- {problem}", file=sys.stderr)
        return 1
    print("Markdown link validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
