# Auxiliary.GetGlobalColumn

## Signature

```lua
Auxiliary.GetGlobalColumn(int p, int location, int sequence) -> int
```

## Description

Returns the column index for location and sequence from player 0's viewpoint. For player 1, the local column is mirrored. Invalid locations/sequences return NULL_VALUE.

## Parameters

- `p` `int`
- `location` `int`
- `sequence` `int`

## Returns

- `int` - The global column index, or NULL_VALUE for invalid input.

## Source

- `Utilities/utility.lua:658`
