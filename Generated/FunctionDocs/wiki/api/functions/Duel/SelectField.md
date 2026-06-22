# Duel.SelectField

## Signature

```lua
Duel.SelectField(int player, int count, int location1, int location2, int filter, [int desc]) -> int|nil
```

## Description

Lets player select count field zones from location1/location2 after applying filter as unavailable zones.
When desc is supplied, the core shows it as a selection hint. The return value is a bitmask of selected zones from player's viewpoint.

## Parameters

- `player` `int`
- `count` `int`
- `location1` `int`
- `location2` `int`
- `filter` `int`
- `desc` `int` optional

## Returns

- `int|nil` - Selected zone bitmask, or nil if player is invalid.

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:5027`
