# Upstream Source Provenance

Sacred Book vendors card scripts, Lua constants/helpers, and editor signatures so
the generated guide is reproducible without requiring every upstream repository
at site-build time. Refreshes should preserve the upstream files byte-for-byte;
Sacred Book-specific explanations belong in `Tools/FunctionDocs/` or the site
generator rather than in the vendored files.

## Current snapshot (2026-10-11)

These are the newest commits in the supplied local repositories; this refresh
did not fetch remote branches.

| Source | Commit | Sacred Book inputs |
| --- | --- | --- |
| [Fluorohydride/ygopro-scripts](https://github.com/Fluorohydride/ygopro-scripts) | `14745a5a3908861bba65d79cf9c542605c83d9cb` | `Scripts/c*.lua`, `Utilities/constant.lua`, `Utilities/utility.lua`, `Utilities/procedure.lua` |
| [mercury233/ygopro-scripts-define](https://github.com/mercury233/ygopro-scripts-define) | `4c37fb75997603e25dce464baf1737893a74f569` | `Define/def.lua`, `Define/cards.lua` |
| [Fluorohydride/ygopro-core](https://github.com/Fluorohydride/ygopro-core) | `c4ccbab40702e4af6da4f4ad1d7a04c3ea80ad02` | `libcard.cpp`, `libduel.cpp`, `libeffect.cpp`, `libgroup.cpp`, and `libdebug.cpp` are read by `Tools/FunctionDocs/generate_function_docs.py`; they are not vendored |
| [mycard/ygopro-rush-duel](https://git.moenext.com/mycard/ygopro-rush-duel) | `6916047c1d6a1bc850e779fb15f4ea0d94b1e6ee` | `Rush/Scripts/c*.lua`, `Rush/Utilities/*.lua`, `Rush/LICENSE` |

This refresh covers 41 standard-script commits after `b605741f9bcf114bdc9087e264de2130736e27e0` and nine core commits after `8b020270e752c56a5df52a8f827f094837be5b64`. The standard commits touch 633 Lua paths: 631 card scripts, `constant.lua`, and `utility.lua`. The complete final snapshot was copied and verified. The defines repository has not advanced.

| Corpus | Card scripts | Sorted Git-blob manifest SHA-256 |
| --- | ---: | --- |
| Standard | 13,572 | `c724354ce8e1930485a774c9eeba3a96ed5e9b4d86c58970b3f5f9ceb19d6e4f` |
| Rush | 3,071 | `b901e053a85e5ca2b736a4ac3c6295ad0c1b8269daaee3b5b72d4d987a57a5b9` |

Both filename sets and every file's blob ID match upstream. The Rush snapshot also includes 20 non-card Lua files: 18 `RD*.lua` modules, `special.lua`, and optional `pick.lua` rules. Each manifest uses the format described below.

| File | SHA-256 of upstream Git blob bytes |
| --- | --- |
| `Utilities/constant.lua` | `7f739d54f8346a1021cfe5f991e1520c186e75a20c2be808ab54ca8484aacffc` |
| `Utilities/utility.lua` | `e0f24e14336aca7f81f675e9b9250c81a5603b821b59b7f82bc8013c464c293d` |
| `Utilities/procedure.lua` | `aae9067432e47ab1082ae27ff5dbf5a2d9688950d3af40f333d0859b3493d3b0` |
| `Define/def.lua` | `b100499105e48ed61bf6e365493320a48ad21bad3683483909bee319c87df139` |
| `Define/cards.lua` | `1d9583cdf26291cc08040edb8409de418c704aa13f7e1505d6b57f6b21f6847d` |
| `Rush/Utilities/special.lua` | `519901a29467ec497414ec503631fee5c38623c366f3df15bf20c3346eb4e077` |

Older raw hashes below used Windows working-copy line endings. The current verifier reads Git blobs directly, so unchanged helpers/defines can have different raw hashes while their Git blob IDs remain unchanged.

Both databases were refreshed from `D:\Programs\GitHub\MDPro3_Data\Data\locales\en-US` and passed SQLite integrity checks. Database counts can exceed script counts because alternate artwork and cards without standalone effects share scripts.

| Destination | Rows | SHA-256 |
| --- | ---: | --- |
| `cards.cdb` | 15,019 | `e0f148dbeed76f3162c2b2e24cc01ae833e1349d8045d20ee4c359416b02640c` |
| `rush_cards.cdb` | 4,076 | `9f4af00c22c61900d4eccc02264d9195c85ce84a0cb17be24a6e6453d382a1f7` |

The reference now includes five new Card APIs (`GetCardType`, `IsCardType`, `IsAllCardTypes`, `GetPreviousCardTypeOnField`, `IsPreviousCardTypeOnField`), card-type effects 377–379, three new `Auxiliary` helpers, and corrected `HINTMSG_NUMBER`/`HINTMSG_LVRANK` spellings. Deprecated `HINGMSG_*` aliases remain available. The SetCode catalog includes the new effects.

Rush has its own 441 public helper references and 65 constants; 32 common entrypoints have reviewed English descriptions and returns. Other entries expose their source and explicitly mark unreviewed types. The generator follows bootstrap load order and records the later Ritual `ConfirmCardFilter` definition superseding the identical Fusion definition. Rush type bits are kept separate: Legend `0x8` and Maximum `0x8000` overlap standard type bits.

## Historical verification (2026-07-26)

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

Prefer the reproducible full-snapshot tool, which avoids Windows checkout and archive newline filters:

```powershell
python Tools/FunctionDocs/refresh_sources.py
python Tools/FunctionDocs/refresh_sources.py --check
python -m unittest Tools.FunctionDocs.test_rush_function_docs
```

It reads local HEADs with `git cat-file --batch`, verifies exact blob contents and filename sets, and prints hashes. Unexpected local scripts cause an error instead of being removed. A fresh Windows checkout may convert line endings; run the refresh before the strict `--check` in that case. Update the pins above from its output.

The reference generator retains native bindings from the committed API JSON when external core sources are unavailable, so CI does not lose new APIs absent from the unchanged stubs. Rush outputs remain separate under `Generated/FunctionDocs/rush/`.

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
