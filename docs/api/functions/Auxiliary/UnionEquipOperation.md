# Auxiliary.UnionEquipOperation

## Signature

```lua
Auxiliary.UnionEquipOperation(function equip_filter) -> function
```

## Description

Returns the operation function for the shared modern Union equip effect. It equips the handler to the selected target, or sends the handler to the Graveyard by rule if the target is no longer valid.

## Parameters

- `equip_filter` `function`

## Returns

- `function` - Operation function for the shared Union equip effect.

## Source

- `Utilities/utility.lua:408`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

No indexed local card script currently calls this function.

This can mean the function is unused in the current script set, is only called through an alias, or is available for future/manual scripts.
