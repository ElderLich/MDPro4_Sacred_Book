# Duel.GetUsableMZoneCount

## Signature

```lua
Duel.GetUsableMZoneCount(int player, [int use_player]) -> int|nil
```

## Description

Returns how many Monster Zones player can use for a monster entering the field.
use_player defaults to the current reason player and is used for zone-limit checks involving the acting player.

## Parameters

- `player` `int`
- `use_player` `int` optional - default: current reason player

## Returns

- `int|nil` - Usable Monster Zone count, or nil if player is invalid.

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:4939`
