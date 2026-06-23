# Duel.SelectDisableField

## Signature

```lua
Duel.SelectDisableField(int player, int count, int location1, int location2, int filter) -> int
```

## Description

Lets player select count available field zones from the requested own-side and opponent-side locations, then returns the selected zone bitmask.
location1 applies to player's field and location2 applies to the opponent's field. The core clamps count to the available number of zones and returns no value if no zone can be selected.
The returned mask uses player-relative bits: own Monster Zone seq, own Spell & Trap Zone seq+8, opponent Monster Zone seq+16, and opponent Spell & Trap Zone seq+24.

## Parameters

- `player` `int` - Player who selects zones and whose viewpoint defines the returned mask.
- `count` `int` - Number of zones to select. The core reduces this to the number of available zones if needed.
- `location1` `int` - Selectable locations on player's field, usually LOCATION_MZONE and/or LOCATION_SZONE.
- `location2` `int` - Selectable locations on the opponent's field, usually LOCATION_MZONE and/or LOCATION_SZONE.
- `filter` `int` - Player-relative mask of zones that cannot be selected.

## Returns

- `int` - Selected zone bitmask, or no return value if no zone can be selected.

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:5028`
