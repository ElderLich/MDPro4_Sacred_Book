# Function Docs Refresh Report

Generated: 2026-06-21T09:57:29+00:00

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
- `Generated/FunctionDocs/wiki/api/functions/index.md`

## Function Sources

- Generated functions: 998
- Core-bound functions: 611
- Lua helper functions: 376
- Stub-only functions: 11
- Core-bound functions without stub docs: 0
- Existing DataEditorX `_functions.txt`: 692
- Existing DataEditorX `_function_english.txt`: 762
- Old Utilities `_functions.txt`: 692
- Added versus old `_functions.txt`: 334
- Dropped versus old `_functions.txt`: 28

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

- `existing_english`: 22
- `imported_from_dataeditorx`: 731
- `missing_documentation`: 201
- `translated_exact`: 44

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

## Compatibility Findings

- DataEditorX currently consumes `_functions.txt` through `CodeConfig.AddFunction()`, so the generated bullet text keeps that format.
- The structured JSON is the better source for a future wiki or richer editor integration.
- `MySyntaxHighlighter.cs` also hardcodes many function names, so editor highlighting will remain stale until it is changed to read generated data.

## Constant Findings

- DataEditorX constants: 808
- Local utility constants: 858
- Missing in DataEditorX: 58
- Changed values: 5
- Removed from local: 8
- Effect creator effect names: 263
- Local `EFFECT_*` constants: 320
- `effect_creator_settings.txt` missing local `EFFECT_*`: 61
- Generated constant docs: 858

Constant English status:

- `existing_english`: 4
- `from_old_utility`: 799
- `translated_exact`: 28
- `translated_name`: 27

Examples missing in DataEditorX constants:

- `CATEGORY_HANDES_OPPO`
- `CATEGORY_HANDES_SELF`
- `CATEGORY_MSET`
- `CATEGORY_SSET`
- `DUEL_REVEAL_DECK_SEQ`
- `EFFECT_ACTIVATION_COUNT_LIMIT`
- `EFFECT_COUNT_CODE_CHAIN`
- `EFFECT_DOUBLE_XMATERIAL`
- `EFFECT_EXTRA_SYNCHRO_MATERIAL`
- `EFFECT_FLAG2_REPEAT_UPDATE`
- `EFFECT_FLAG_ACTIVATE_CONDITION`
- `EFFECT_FLAG_CAN_FORBIDDEN`
- `EFFECT_FLAG_COIN`
- `EFFECT_FLAG_COPY`
- `EFFECT_FLAG_DICE`
- `EFFECT_FLAG_EFFECT`
- `EFFECT_FLAG_FUSION_SUMMON`
- `EFFECT_KAISER_COLOSSEUM`
- `EFFECT_REPLACE_DAMAGE`
- `EFFECT_RITUAL_LEVEL_EX`
- `... 38 more`

Examples changed constant values:

- `CATEGORY_HANDES`
- `DOUBLE_DAMAGE`
- `HALF_DAMAGE`
- `MIN_ID`
- `RACE_ALL`

## Category Findings

- DataEditorX English categories: 36
- MDPro3 English category labels: 32
- Category mismatches: 0

## Added Function Examples

- `Auxiliary.AND`
- `Auxiliary.AddBanishRedirect`
- `Auxiliary.AddCodeList`
- `Auxiliary.AddContactFusionProcedure`
- `Auxiliary.AddDrytronSpSummonEffect`
- `Auxiliary.AddEquipSpellEffect`
- `Auxiliary.AddFusionEffectProc`
- `Auxiliary.AddFusionEffectProcUltimate`
- `Auxiliary.AddMaterialCodeList`
- `Auxiliary.AddRitualProcGreater2`
- `Auxiliary.AddRitualProcGreater2Code`
- `Auxiliary.AddRitualProcGreater2Code2`
- `Auxiliary.AddRitualProcUltimate`
- `Auxiliary.AddSetNameMonsterList`
- `Auxiliary.AddThisCardInGraveAlreadyCheck`
- `Auxiliary.AddUrsarcticSpSummonEffect`
- `Auxiliary.AdjacentFilter`
- `Auxiliary.ArcanaCoinOperation`
- `Auxiliary.ArcanaCoinTarget`
- `Auxiliary.ArcanaCondition`
- `Auxiliary.AssaultModeLimit`
- `Auxiliary.AtkEqualsDef`
- `Auxiliary.BESRemoveCondition`
- `Auxiliary.BESRemoveOperation`
- `Auxiliary.BESRemoveTarget`
- `Auxiliary.BanishRedirectCondition`
- `Auxiliary.BecomeOriginalCode`
- `Auxiliary.ChangeBattleDamage`
- `Auxiliary.CheckGroupRecursive`
- `Auxiliary.CheckGroupRecursiveCapture`
- `Auxiliary.CheckGroupRecursiveEach`
- `Auxiliary.CheckXyz2XMaterial`
- `Auxiliary.ContactFusionCondition`
- `Auxiliary.ContactFusionMaterialFilter`
- `Auxiliary.ContactFusionOperation`
- `Auxiliary.ContactFusionSendToDeck`
- `Auxiliary.ContactFusionTarget`
- `Auxiliary.CreateChecks`
- `Auxiliary.CreateMaterialReasonCardRelation`
- `Auxiliary.DarkFusionLimit`
- `... 294 more`

## Dropped Old Function Examples

- `Auxiliary.GetMustMaterialGroup`
- `Auxiliary.disfilter1`
- `Card.GetLinkMarker`
- `Card.GetOriginalLinkMarker`
- `Card.GetRemovedOverlayCount`
- `Card.IsAbleToDecreaseAttackAsCost`
- `Card.IsAbleToDecreaseDefenseAsCost`
- `Card.IsRitualType`
- `Card.IsXyzSummonableByRose`
- `Card.SetCardData`
- `Card.SetEntityCode`
- `Duel.AnnounceCardFilter`
- `Duel.DisableActionCheck`
- `Duel.Exile`
- `Duel.GetCardsInZone`
- `Duel.GetEnvironment`
- `Duel.GetMasterRule`
- `Duel.IsPlayerExtraSummoned`
- `Duel.LoadScript`
- `Duel.MoveTurnCount`
- `Duel.ReadCard`
- `Duel.ResetTimeLimit`
- `Duel.SetMetatable`
- `Duel.SetSummonCancelable`
- `Duel.XyzSummonByRose`
- `Effect.GetCountLimit`
- `Effect.SetOwner`
- `initial_effect`

## Recommended Next Steps

1. Review the generated compatibility text files and copy them into DataEditorX only after spot-checking tooltips.
2. Replace the hardcoded function regex lists in `MySyntaxHighlighter.cs` with generated namespace lists.
3. Translate missing English entries from the JSON source instead of editing `_function_english.txt` by hand.
4. Use the generated markdown tree as the seed for a VitePress wiki like scrapi-book, but keep this project's core-specific API separate.
