# Duel.GetMZoneCount

## Signature

```lua
Duel.GetMZoneCount(int player, [Card|Group|nil targets], [int use_player], [int reason], [int zone]) -> int,int
```

## Description

Returns the number of usable Monster Zones for player after targets leave, plus the usable zone mask.
use_player, reason, and zone are used by effects that restrict where monsters can be placed.

## Parameters

- `player` `int` - Player whose Monster Zones are checked.
- `targets` `Card|Group|nil` optional - Card or Group treated as leaving the field before the count is checked.
- `use_player` `int` optional - Player treated as placing the monster. Defaults to the current reason player.
- `reason` `int` optional - Placement reason. Defaults to LOCATION_REASON_TOFIELD.
- `zone` `int` optional - Monster Zone mask to restrict the count. Defaults to 0xff.

## Returns

- `int` - Usable Monster Zone count after targets are ignored.
- `int` - Usable Monster Zone mask.

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:4936`
