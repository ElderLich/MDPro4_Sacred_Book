# Duel.SelectDisableField

## Signature

```lua
Duel.SelectDisableField(int player, int count, int location1, int location2, int filter) -> int
```

## Description

Lets player select count available field zones from the requested own-side and opponent-side locations, then returns the selected zone bitmask.
location1 applies to player's field and location2 applies to the opponent's field. The core clamps count to the available number of zones and returns no value if no zone can be selected.

## Parameters

- `player` `int`
- `count` `int`
- `location1` `int`
- `location2` `int`
- `filter` `int`

## Returns

- `int` - Selected zone bitmask.

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:5028`
