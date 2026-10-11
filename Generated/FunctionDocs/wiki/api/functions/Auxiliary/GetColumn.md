# Auxiliary.GetColumn

## Signature

```lua
Auxiliary.GetColumn(Card c, [int p]) -> int
```

## Description

Returns c's column index from player p's viewpoint, or NULL_VALUE when c has no field column.
The local helper maps ordinary Monster Zones and Spell & Trap Zones to columns 0-4; Extra Monster Zone sequences 5 and 6 map to columns 1 and 3.

## Parameters

- `c` `Card` - Card whose field column is checked.
- `p` `int` optional - Viewpoint player. Defaults to 0.

## Returns

- `int` - Column index from p's viewpoint, or NULL_VALUE if c has no field column.

## Source

- `Utilities/utility.lua:705`
