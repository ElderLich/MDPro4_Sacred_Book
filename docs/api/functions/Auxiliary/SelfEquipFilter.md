# Auxiliary.SelfEquipFilter

## Signature

```lua
Auxiliary.SelfEquipFilter(Card c, int id) -> bool
```

## Description

Returns true if c has a flag with id, used by Auxiliary.IsSelfEquip to identify cards equipped by their own effect.

## Parameters

- `c` `Card`
- `id` `int`

## Returns

- `bool` - true if c has the flag id.

## Source

- `Utilities/utility.lua:1961`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

No indexed local card script currently calls this function.

This can mean the function is unused in the current script set, is only called through an alias, or is available for future/manual scripts.
