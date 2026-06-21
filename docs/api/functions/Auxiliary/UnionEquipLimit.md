# Auxiliary.UnionEquipLimit

## Signature

```lua
Auxiliary.UnionEquipLimit(function filter) -> function
```

## Description

Returns an Equip Limit value function for modern Union monsters. It allows cards controlled by the handler's player that satisfy filter, and also keeps the current equip target legal.

## Parameters

- `filter` `function`

## Returns

- `function` - Equip Limit value function.

## Source

- `Utilities/utility.lua:391`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

No indexed local card script currently calls this function.

This can mean the function is unused in the current script set, is only called through an alias, or is available for future/manual scripts.
