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

- `Utilities/utility.lua:601`
