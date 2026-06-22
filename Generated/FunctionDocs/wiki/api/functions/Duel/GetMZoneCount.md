# Duel.GetMZoneCount

## Signature

```lua
Duel.GetMZoneCount(int player, [Group|Card targets], [int use_player], [int reason], [int zone]) -> int,int
```

## Description

Returns the number of usable Monster Zones for player after targets leave, plus the usable zone mask.
use_player, reason, and zone are used by effects that restrict where monsters can be placed.

## Parameters

- `player` `int`
- `targets` `Group|Card` optional
- `use_player` `int` optional
- `reason` `int` optional
- `zone` `int` optional - default: 0xff

## Returns

- `int`
- `int` - zone

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:4936`
