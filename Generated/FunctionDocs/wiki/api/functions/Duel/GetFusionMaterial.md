# Duel.GetFusionMaterial

## Signature

```lua
Duel.GetFusionMaterial(int player, [int location]) -> Group,Group
```

## Description

Returns two Groups for player: all currently usable Fusion Material candidates, then the base material pool from the requested locations.
location defaults to LOCATION_HAND + LOCATION_MZONE. Extra Fusion Material effects in the Spell & Trap Zone or GY are added to the first returned Group, while the second Group contains only cards from location.

## Parameters

- `player` `int` - Player whose Fusion Material pool is collected.
- `location` `int` optional - Location mask for the base pool; default: LOCATION_HAND + LOCATION_MZONE.

## Returns

- `Group` - All currently usable Fusion Material candidates, including extra Fusion Material effects.
- `Group` - Base material pool from the requested locations only.

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:5000`
