# Auxiliary.GetLocalColumn

## Signature

```lua
Auxiliary.GetLocalColumn(int location, int sequence) -> int
```

## Description

Returns the local column index for a Spell & Trap Zone or Monster Zone sequence. Extra Monster Zone sequences 5 and 6 map to columns 1 and 3; invalid inputs return NULL_VALUE.

## Parameters

- `location` `int`
- `sequence` `int`

## Returns

- `int` - The local column index, or NULL_VALUE for invalid input.

## Source

- `Utilities/utility.lua:633`
