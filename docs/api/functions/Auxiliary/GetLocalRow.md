# Auxiliary.GetLocalRow

## Signature

```lua
Auxiliary.GetLocalRow(int location, int sequence) -> int
```

## Description

Returns the local row index for a Spell & Trap Zone or Monster Zone sequence. Main Monster Zones are row 1, Extra Monster Zones are row 2, and invalid inputs return NULL_VALUE.

## Parameters

- `location` `int`
- `sequence` `int`

## Returns

- `int` - The local row index, or NULL_VALUE for invalid input.

## Source

- `Utilities/utility.lua:604`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

No indexed local card script currently calls this function.

This can mean the function is unused in the current script set, is only called through an alias, or is available for future/manual scripts.
