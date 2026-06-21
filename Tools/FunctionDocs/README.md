# Function Docs Generator

Generates YGOPro Lua API documentation from the local card scripting workspace and the side-project data files.

## Sources

- `D:\Programs\GitHub\ygopro-core\lib*.cpp`: authoritative core Lua bindings for `Card`, `Duel`, `Effect`, `Group`, and `Debug`.
- `Define/def.lua`: EmmyLua-style signatures, return types, parameters, and Chinese descriptions.
- `Utilities/utility.lua` and `Utilities/procedure.lua`: Lua helper/procedure functions.
- `D:\Programs\GitHub\DataEditorX\DataEditorX\data\lua\_function_english.txt`: existing English descriptions, imported where names still match.
- `OLD\Utilities\_functions.txt`: older English scripting guide, imported as a fallback after DataEditorX English.
- `Utilities/constant.lua`: current constant values and source comments.
- `OLD\Utilities\constant.lua`: older English constant comments, imported where names still match.
- `D:\Programs\GitHub\DataEditorX\DataEditorX\data\lua\constant.lua`: stale constant comparison.
- `D:\Programs\GitHub\MDPro3_Data\Data\locales\en-US\strings.conf`: category label comparison.

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
- `constants.generated.json`: structured current constants with Chinese/English comments and source metadata.
- `constant_english.generated.lua`: DataEditorX-compatible English constant tooltip file.
- `constants.generated.md`: markdown constant reference.
- `constant_translation_backlog.md`: constants still needing translation/review.
- `function_translation_backlog.md`: function docs still needing translation or first documentation.
- `wiki/api/functions/`: one markdown page per function, plus an index.
- `comparison.generated.json`: machine-readable stale/missing lists.
- `report.md`: human-readable summary.

## Promote To DataEditorX

After spot-checking the generated text files:

- Copy `_functions.generated.txt` to `D:\Programs\GitHub\DataEditorX\DataEditorX\data\lua\_functions.txt`.
- Copy `_function_english.generated.txt` to `D:\Programs\GitHub\DataEditorX\DataEditorX\data\lua\_function_english.txt`.
- Copy `constant_english.generated.lua` to `D:\Programs\GitHub\DataEditorX\DataEditorX\data\lua\constant.lua` only if you want English constant tooltips in DataEditorX. Keep a backup if you still need the Chinese comments there.

DataEditorX currently reads `_functions.txt` with `CodeConfig.AddFunction()`, so the generated compatibility files keep the old bullet format. The JSON file is better for a future wiki or a richer DataEditorX integration.
