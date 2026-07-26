# Upstream Source Provenance

Sacred Book vendors card scripts, Lua constants/helpers, and editor signatures so
the generated guide is reproducible without requiring every upstream repository
at site-build time. Refreshes should preserve the upstream files byte-for-byte;
Sacred Book-specific explanations belong in `Tools/FunctionDocs/` or the site
generator rather than in the vendored files.

## Current snapshot

| Source | Commit | Sacred Book inputs |
| --- | --- | --- |
| [Fluorohydride/ygopro-scripts](https://github.com/Fluorohydride/ygopro-scripts) | `b605741f9bcf114bdc9087e264de2130736e27e0` | `Scripts/c*.lua`, `Utilities/constant.lua`, `Utilities/utility.lua`, `Utilities/procedure.lua` |
| [mercury233/ygopro-scripts-define](https://github.com/mercury233/ygopro-scripts-define) | `4c37fb75997603e25dce464baf1737893a74f569` | `Define/def.lua`, `Define/cards.lua` |
| [Fluorohydride/ygopro-core](https://github.com/Fluorohydride/ygopro-core) | `8b020270e752c56a5df52a8f827f094837be5b64` | `libcard.cpp`, `libduel.cpp`, `libeffect.cpp`, `libgroup.cpp`, and `libdebug.cpp` are read by `Tools/FunctionDocs/generate_function_docs.py`; they are not vendored |

Snapshot verification on 2026-07-26:

- `Scripts/` contains 13,414 card scripts, with no missing, extra, or
  content-different `c<number>.lua` files relative to the recorded
  `ygopro-scripts` commit.
- The sorted card-script manifest SHA-256 is
  `23278cb40d69587b59eade9ec75871611431819e4cb53e2a663d30ddb7b0718b`.
  The manifest format is one `<filename> <git-blob-id>` line per card script,
  sorted by filename and joined with LF without a final LF.
- Vendored non-card file SHA-256 values:

| File | SHA-256 |
| --- | --- |
| `Utilities/constant.lua` | `993db9f754e7924f51f886e06e2d63ee9e63f43b1f43a10e2794fba7d4646e91` |
| `Utilities/utility.lua` | `f76d5191f7e487605aade4e2ef01f0ea71d95a9709ba187bc750f73c74a374fb` |
| `Utilities/procedure.lua` | `64e510643688d192e1b2ad4c979e131df93401a519fbcf6493bdf5d42b8ebd3c` |
| `Define/def.lua` | `2380db279de093ab67b4a6ec0575d12c2e65770355e2a5955dabbdad43944023` |
| `Define/cards.lua` | `8bbc780834ab67d76abaf3bf2617741d69671ee9a2c7840f8a5b562980b2de31` |

## Refresh method

For an incremental `ygopro-scripts` refresh, collect the union of paths touched
by every commit after the previously recorded boundary, then copy each path's
content from the new upstream HEAD. Do not rely only on
`git diff <old>..HEAD`: a file can change and later be reverted, and its final
state still needs to be restored locally.

The 2026-07-26 refresh covered all 26 commits after
`7e4e8bc2f4dc1b1edaf05bc31ddd91d09e597e45`. Across those commits, 174 Lua
paths were touched (173 card scripts and `constant.lua`); 19 card scripts were
changed and later reverted before HEAD.

After copying, verify:

1. The upstream and local `c<number>.lua` filename sets are identical.
2. Their Git blob IDs are identical file by file.
3. `constant.lua`, `utility.lua`, and `procedure.lua` hashes match upstream.
4. `Define/def.lua` and `Define/cards.lua` hashes match
   `ygopro-scripts-define`.
5. Run the function-doc generator to a temporary `--out` directory before
   regenerating the committed `Generated/` and `docs/` trees.
