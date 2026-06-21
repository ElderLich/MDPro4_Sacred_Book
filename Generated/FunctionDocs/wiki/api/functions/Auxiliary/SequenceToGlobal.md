# Auxiliary.SequenceToGlobal

## Signature

```lua
Auxiliary.SequenceToGlobal(int p, int loc, int seq) -> int
```

## Description

Converts a player's local Monster Zone or Spell & Trap Zone sequence into a global zone bit. Invalid players, locations, or sequences return 0.

## Parameters

- `p` `int`
- `loc` `int`
- `seq` `int`

## Returns

- `int` - The global zone bit, or 0 for invalid input.

## Source

- `Utilities/utility.lua:1487`
