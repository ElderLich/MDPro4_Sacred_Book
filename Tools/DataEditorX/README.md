# DataEditorX reference promotion

After regenerating and reviewing function contracts, copy the standard and
Rush tooltip files into the editor's data folder:

```powershell
python Tools/DataEditorX/sync_editor_data.py --destination "D:\Programs\GitHub\DataEditorX\DataEditorX\data"
python Tools/DataEditorX/sync_editor_data.py --destination "D:\Programs\GitHub\DataEditorX\DataEditorX\data" --check
```

The command copies six files byte-for-byte and prints their SHA-256 hashes.
It reads all source files before writing; `--check` verifies without changing
the editor. Other editor settings and data are preserved.

The editor loads Rush functions and constants from separate optional files.
`_rush_functions.txt` and `_rush_function_english.txt` include both the
`RushDuel.Name` spelling and `RD.Name` bootstrap alias. `rush_constant.lua`
contains tooltip assignments only; it is not a replacement for the game's
Rush bootstrap. This separation also keeps Rush entries out of the standard
reference generator's legacy-description baseline.
