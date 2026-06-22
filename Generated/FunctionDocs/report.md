# Function Docs Refresh Report

Generated: 2026-06-22T19:37:27+00:00

## Outputs

- `Generated/FunctionDocs/api_functions.generated.json`
- `Generated/FunctionDocs/_functions.generated.txt`
- `Generated/FunctionDocs/_function_english.generated.txt`
- `Generated/FunctionDocs/constants.generated.json`
- `Generated/FunctionDocs/constant_english.generated.lua`
- `Generated/FunctionDocs/constants.generated.md`
- `Generated/FunctionDocs/constant_translation_backlog.md`
- `Generated/FunctionDocs/function_translation_backlog.md`
- `Generated/FunctionDocs/comparison.generated.json`
- `Generated/FunctionDocs/report.md`
- `Generated/FunctionDocs/wiki/index.md`
- `Generated/FunctionDocs/wiki/api/index.md`
- `Generated/FunctionDocs/wiki/api/functions/index.md`
- `Generated/FunctionDocs/wiki/api/constants.md`
- `Generated/FunctionDocs/wiki/.vitepress/config.mts`

## Function Sources

- Generated functions: 998
- Core-bound functions: 611
- Lua helper functions: 376
- Stub-only functions: 11
- Core-bound functions without stub docs: 0
- Existing DataEditorX `_functions.txt`: 998
- Existing DataEditorX `_function_english.txt`: 998
- Added versus DataEditorX `_functions.txt`: 0
- Dropped versus DataEditorX `_functions.txt`: 0

## Namespaces

- `Auxiliary`: 363
- `Card`: 286
- `Debug`: 11
- `Duel`: 229
- `Effect`: 55
- `Global`: 1
- `Group`: 45
- `bit`: 8

## English Coverage

- `imported_from_dataeditorx`: 202
- `translated_exact`: 796

## Core Binding Gaps

Core-bound functions that were not documented by `Define/def.lua`:

- None

Documented stubs that do not appear in this core binding scan:

- `Card.branded_fusion_check`
- `Card.cyber_fusion_check`
- `Card.destruction_swordsman_fusion_check`
- `Card.hero_fusion_check`
- `Card.mat_filter`
- `Card.mat_group_check`
- `Card.red_eyes_fusion_check`
- `Card.synchro_fusion_check`
- `Card.ultimate_fusion_check`
- `Card.zw_equip_monster`
- `Group.ForEach`

## Return Signature Audit

Lua helper docs that still render as `void` while their source body contains a `return`:

- Count: 0

- None

## Compatibility Findings

- DataEditorX currently consumes `_functions.txt` through `CodeConfig.AddFunction()`, so the generated bullet text keeps that format.
- The structured JSON is the better source for a future wiki or richer editor integration.
- `MySyntaxHighlighter.cs` also hardcodes many function names, so editor highlighting will remain stale until it is changed to read generated data.

## Constant Findings

- DataEditorX constants: 858
- Local utility constants: 858
- Missing in DataEditorX: 0
- Changed values: 0
- Removed from local: 0
- Effect creator active `EFFECT_*` names: 289
- Effect creator commented `EFFECT_*` names: 6
- Effect creator effect-code names: 256
- Effect creator property names: 33
- Local `EFFECT_*` constants: 320
- Local effect-code constants: 261
- Local effect-property constants: 40
- `effect_creator_settings.txt` missing effect-code constants: 0
- `effect_creator_settings.txt` missing effect-property constants: 0
- Reserved/internal effect-code constants intentionally ignored: 5
- Internal property constants intentionally ignored: 7
- Unknown active effect creator names: 0
- Generated constant docs: 858

Constant English status:

- `existing_english`: 4
- `from_project_cache`: 792
- `reviewed_english`: 7
- `translated_exact`: 28
- `translated_name`: 27

Examples missing in DataEditorX constants:


Examples changed constant values:


## Category Findings

- DataEditorX English categories: 36
- MDPro3 English category labels: 32
- Category mismatches: 0

## Added Function Examples


## Dropped DataEditorX Function Examples


## Recommended Next Steps

1. Review the generated compatibility text files and copy them into DataEditorX only after spot-checking tooltips.
2. Replace the hardcoded function regex lists in `MySyntaxHighlighter.cs` with generated namespace lists.
3. Translate missing English entries from the JSON source instead of editing `_function_english.txt` by hand.
4. Use the generated markdown tree as the seed for a VitePress wiki like scrapi-book, but keep this project's core-specific API separate.
