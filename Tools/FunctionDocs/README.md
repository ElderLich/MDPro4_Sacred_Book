# Function Docs Generator

Generates YGOPro Lua API documentation from the local card scripting workspace and the side-project data files.

## Sources

- `D:\Programs\GitHub\ygopro-core\lib*.cpp`: authoritative core Lua bindings for `Card`, `Duel`, `Effect`, `Group`, and `Debug`.
- `Define/def.lua`: EmmyLua-style signatures, return types, parameters, and Chinese descriptions.
- `Utilities/utility.lua` and `Utilities/procedure.lua`: Lua helper/procedure functions.
- `D:\Programs\GitHub\DataEditorX\DataEditorX\data\lua\_function_english.txt`: existing English descriptions, imported as a legacy baseline where names still match.
- `Utilities/constant.lua`: current constant values and source comments.
- `Rush/Utilities/special.lua` and its `RD*.lua` modules: separately pinned Rush helper signatures, source comments, constants and load order. `RushDuel.Name` has the runtime alias `RD.Name`.
- `D:\Programs\GitHub\DataEditorX\DataEditorX\data\lua\constant.lua`: stale constant comparison.
- `D:\Programs\GitHub\MDPro3_Data\Data\locales\en-US\strings.conf`: category label comparison.

The old `OLD/Utilities` folder is no longer a documentation source. New wording should be reviewed in Sacred Book and regenerated from the structured JSON/tooling here.

## Run

```powershell
python Tools\FunctionDocs\generate_function_docs.py
```

Useful options:

```powershell
python Tools\FunctionDocs\generate_function_docs.py `
  --ygopro-core "D:\Programs\GitHub\ygopro-core" `
  --dataeditorx-data "D:\Programs\GitHub\DataEditorX\DataEditorX\data" `
  --mdpro3-locales "D:\Programs\GitHub\MDPro3_Data\Data\locales"
```

## Outputs

Generated files are written to `Generated/FunctionDocs/`.

- `api_functions.generated.json`: structured source of truth for future editor/wiki integration.
- `_functions.generated.txt`: DataEditorX-compatible Chinese tooltip file.
- `_function_english.generated.txt`: DataEditorX-compatible English tooltip file.
- `wiki/api/functions/`: one markdown page per function, plus an index. The public site adds usage/example sections from local scripts.
- `constants.generated.json`: structured current constants with Chinese/English comments and source metadata.
- `constant_english.generated.lua`: DataEditorX-compatible English constant tooltip file.
- `constants.generated.md`: markdown constant reference.
- `constant_translation_backlog.md`: constants still needing translation/review.
- `function_translation_backlog.md`: function docs still needing translation or first documentation.
- `comparison.generated.json`: machine-readable stale/missing lists.
- `report.md`: human-readable summary.
- `rush/`: separate Rush JSON, constants-only editor Lua, bilingual bullet tooltip files and `wiki/api/` pages. Rush bullet files include both `RushDuel.*` and `RD.*` spellings. Keep Rush constants separate from the standard environment.

Rush signatures support multiline declarations and follow bootstrap load order.
Private underscore helpers are omitted. Reviewed contracts live in
`rush_doc_overrides.json`; other helpers show their source and label unreviewed
types explicitly. Later declarations replace earlier ones, with the shadowed
source recorded in JSON metadata. Plain prose is HTML-escaped and upstream
comments are fenced to prevent examples such as `c<code>.lua` becoming Vue tags.

If the external core is unavailable, native bindings are retained from the
committed JSON snapshot. `Define/def.lua` is not assumed to contain every new API.

## Refresh and verify sources

`python Tools/FunctionDocs/refresh_sources.py` copies exact blobs from the local
standard, define and Rush repository HEADs, without Git's Windows newline
filters. `--check` verifies without writing. Update `UPSTREAM_SOURCES.md` from
its reported counts and hashes. Extra local card scripts cause an error instead
of being removed automatically.

Run `python -m unittest Tools.FunctionDocs.test_rush_function_docs` to check
multiline signatures, alias exports, bootstrap shadowing, constants separation,
factory returns, safe Markdown prose and the native-cache fallback.

## Promote To DataEditorX

After spot-checking the generated text files:

- Copy `_functions.generated.txt` to `D:\Programs\GitHub\DataEditorX\DataEditorX\data\lua\_functions.txt`.
- Copy `_function_english.generated.txt` to `D:\Programs\GitHub\DataEditorX\DataEditorX\data\lua\_function_english.txt`.
- Prefer syncing after spot-checking the most-used generated function entries.
- Copy `constant_english.generated.lua` to `D:\Programs\GitHub\DataEditorX\DataEditorX\data\lua\constant.lua` only if you want English constant tooltips in DataEditorX. Keep a backup if you still need the Chinese comments there.

DataEditorX currently reads `_functions.txt` with `CodeConfig.AddFunction()`, so the generated compatibility files keep the old bullet format. The JSON file is better for a future wiki or a richer DataEditorX integration.
