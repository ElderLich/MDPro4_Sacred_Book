# RushDuel.GetSZoneCount

Alias: `RD.GetSZoneCount`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.GetSZoneCount(int player, int max) -> int
```

## Description

Returns the available Spell &amp; Trap Zone count capped by max.

## Parameters

- `player` `int`: Player, 0 or 1.
- `max` `int`: Upper bound; required by math.min.

## Returns

- `int`: Capped available zone count.

## Source

`Rush/Utilities/RDFunction.lua:133`

```lua
function RushDuel.GetSZoneCount(player, max)
    local ct = Duel.GetLocationCount(player, LOCATION_SZONE)
    return math.min(ct, max)
end
```

## Used By

Generated from the local `Rush/Scripts/` folder and `rush_cards.cdb`.

No indexed local card script currently calls this function.

This can mean the function is unused in the current script set, is only called through an alias, or is available for future/manual scripts.
