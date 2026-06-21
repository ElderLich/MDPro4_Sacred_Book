# Auxiliary.GetGlobalRow

## Signature

```lua
Auxiliary.GetGlobalRow(int p, int location, int sequence) -> int
```

## Description

Returns the row index for location and sequence from player 0's viewpoint. For player 1, the local row is mirrored. Invalid locations/sequences return NULL_VALUE.

## Parameters

- `p` `int`
- `location` `int`
- `sequence` `int`

## Returns

- `int` - The global row index, or NULL_VALUE for invalid input.

## Source

- `Utilities/utility.lua:621`
