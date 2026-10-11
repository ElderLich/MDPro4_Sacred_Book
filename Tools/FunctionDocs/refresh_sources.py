"""Copy pinned Git blobs without checkout/CRLF/archive filters, then verify them.

This uses local repository HEADs only. It never fetches, removes local files, or
modifies the upstream repositories. Review and update UPSTREAM_SOURCES.md after
a refresh. Pass --check to verify the current snapshot without writing files.
"""
from __future__ import annotations

import argparse
import hashlib
import io
import json
import re
import subprocess
from pathlib import Path


def git(repo, *args, **kwargs):
    return subprocess.check_output(["git", "-c", f"safe.directory={repo.as_posix()}", *args], cwd=repo, **kwargs)


def refresh(repo, workspace, mapping, check):
    tree = git(repo, "ls-tree", "-r", "HEAD").decode().splitlines()
    entries = {line.split("\t", 1)[1]: line.split()[2] for line in tree}
    selected = [(source, destination, entries[source]) for source, destination in mapping(entries)]
    raw = git(repo, "cat-file", "--batch", input="".join(blob + "\n" for _, _, blob in selected).encode())
    stream = io.BytesIO(raw)
    manifest = []
    hashes = {}
    for source, destination, expected in selected:
        blob, kind, size = stream.readline().decode().split()
        data = stream.read(int(size))
        assert stream.read(1) == b"\n"
        actual = hashlib.sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest()
        assert kind == "blob" and blob == expected == actual, source
        target = workspace / destination
        if not check and (not target.exists() or target.read_bytes() != data):
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(data)
        if not target.exists() or target.read_bytes() != data:
            raise ValueError(f"Snapshot differs from upstream blob: {destination}")
        if re.fullmatch(r"c\d+\.lua", target.name):
            manifest.append(f"{target.name} {blob}")
        else:
            hashes[destination] = hashlib.sha256(data).hexdigest()
    card_destinations = {str(Path(destination).parent) for _, destination, _ in selected if re.fullmatch(r"c\d+\.lua", Path(destination).name)}
    expected_paths = {destination for _, destination, _ in selected}
    for folder in card_destinations:
        extra = {p.relative_to(workspace).as_posix() for p in (workspace / folder).glob("c*.lua")} - expected_paths
        if extra:
            raise ValueError(f"Extra local card scripts require review: {sorted(extra)}")
    return {
        "commit": git(repo, "rev-parse", "HEAD").decode().strip(),
        "card_script_count": len(manifest),
        "card_manifest_sha256": hashlib.sha256("\n".join(sorted(manifest)).encode()).hexdigest() if manifest else None,
        "file_sha256": hashes,
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--workspace", type=Path, default=Path.cwd())
    parser.add_argument("--scripts", type=Path, default=Path(r"D:\Programs\GitHub\ygopro-scripts"))
    parser.add_argument("--define", type=Path, default=Path(r"D:\Programs\GitHub\ygopro-scripts-define"))
    parser.add_argument("--rush", type=Path, default=Path(r"D:\Programs\GitHub\ygopro-rush-duel"))
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    workspace = args.workspace.resolve()
    def standard(entries):
        return [(name, f"Scripts/{name}") for name in entries if re.fullmatch(r"c\d+\.lua", name)] + [
            (name, f"Utilities/{name}") for name in ("constant.lua", "utility.lua", "procedure.lua")]
    def rush(entries):
        result = [("LICENSE", "Rush/LICENSE")]
        for name in entries:
            if name.startswith("script/") and name.endswith(".lua") and name.count("/") == 1:
                folder = "Scripts" if re.fullmatch(r"c\d+\.lua", Path(name).name) else "Utilities"
                result.append((name, f"Rush/{folder}/{Path(name).name}"))
        return result
    summary = {
        "scripts": refresh(args.scripts, workspace, standard, args.check),
        "define": refresh(args.define, workspace, lambda entries: [(name, f"Define/{name}") for name in ("def.lua", "cards.lua")], args.check),
        "rush": refresh(args.rush, workspace, rush, args.check),
    }
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
