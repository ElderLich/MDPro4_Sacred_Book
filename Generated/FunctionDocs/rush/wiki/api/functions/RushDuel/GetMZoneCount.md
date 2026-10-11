# RushDuel.GetMZoneCount

Alias: `RD.GetMZoneCount`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.GetMZoneCount(int player, int max) -> int
```

## Description

Returns the available Monster Zone count capped by max, with the helper's special one-zone restriction applied when effect 59822133 affects the player.

## Parameters

- `player` `int`: Player, 0 or 1.
- `max` `int`: Upper bound; required by math.min.

## Returns

- `int`: Capped available zone count.

## Source

`Rush/Utilities/RDFunction.lua:125`

```lua
function RushDuel.GetMZoneCount(player, max)
    local ct = Duel.GetLocationCount(player, LOCATION_MZONE)
    if Duel.IsPlayerAffectedByEffect(player, 59822133) then
        ct = math.min(ct, 1)
    end
    return math.min(ct, max)
end
```
