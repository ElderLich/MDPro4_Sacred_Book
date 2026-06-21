# Duel.GetSZoneCount

## Signature

```lua
Duel.GetSZoneCount(int player, [Group|Card targets], [int use_player], [int reason], [int zone]) -> int,int
```

## Description

Returns the number of available Spell & Trap Zones for player after targets leave, optionally restricted by zone. The Field Zone is not included.
The additional use_player and reason parameters are used by effects that restrict zones, such as Kaiser Colosseum.

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

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:4937`
