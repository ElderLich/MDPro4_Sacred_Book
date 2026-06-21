# Auxiliary.UnionEquipTarget

## Signature

```lua
Auxiliary.UnionEquipTarget(function equip_filter) -> function
```

## Description

Returns the target function for the shared modern Union equip effect. It checks the once-per-turn Union flag, requires an open Spell & Trap Zone, selects a valid target, and registers equip operation info.

## Parameters

- `equip_filter` `function`

## Returns

- `function` - Target function for the shared Union equip effect.

## Source

- `Utilities/utility.lua:396`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

No indexed local card script currently calls this function.

This can mean the function is unused in the current script set, is only called through an alias, or is available for future/manual scripts.
