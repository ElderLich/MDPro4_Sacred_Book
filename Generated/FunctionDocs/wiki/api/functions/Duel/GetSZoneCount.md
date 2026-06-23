# Duel.GetSZoneCount

## Signature

```lua
Duel.GetSZoneCount(int player, [Card|Group|nil targets], [int use_player], [int reason], [int zone]) -> int,int
```

## Description

Returns the number of available Spell & Trap Zones for player after targets leave, optionally restricted by zone. The Field Zone is not included.
The additional use_player and reason parameters are used by effects that restrict zones, such as Kaiser Colosseum.

## Parameters

- `player` `int` - Player whose Spell & Trap Zones are checked.
- `targets` `Card|Group|nil` optional - Card or Group treated as leaving the field before the count is checked.
- `use_player` `int` optional - Player treated as placing the card. Defaults to the current reason player.
- `reason` `int` optional - Placement reason. Defaults to LOCATION_REASON_TOFIELD.
- `zone` `int` optional - Spell & Trap Zone mask to restrict the count. Defaults to 0xff.

## Returns

- `int` - Usable Spell & Trap Zone count after targets are ignored.
- `int` - Usable Spell & Trap Zone mask.

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:4937`
