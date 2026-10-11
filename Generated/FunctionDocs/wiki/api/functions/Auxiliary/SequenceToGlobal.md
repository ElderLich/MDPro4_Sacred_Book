# Auxiliary.SequenceToGlobal

## Signature

```lua
Auxiliary.SequenceToGlobal(int p, int loc, int seq) -> int
```

## Description

Converts a player's local Monster Zone or Spell & Trap Zone sequence into a global zone bit. Invalid players, locations, or sequences return 0.
Monster Zone bits are shifted by 16*p+seq; Spell & Trap Zone bits are shifted by 16*p+seq+8.

## Parameters

- `p` `int` - Player whose local field sequence is converted.
- `loc` `int` - LOCATION_MZONE or LOCATION_SZONE.
- `seq` `int` - Sequence inside loc. Monster Zone sequences up to 6 are accepted; Spell & Trap Zone sequences up to 4 are accepted.

## Returns

- `int` - The global zone bit, or 0 for invalid input.

## Source

- `Utilities/utility.lua:1490`
