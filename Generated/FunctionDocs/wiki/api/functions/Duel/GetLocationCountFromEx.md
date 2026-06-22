# Duel.GetLocationCountFromEx

## Signature

```lua
Duel.GetLocationCountFromEx(int player, [int reason_player], [Group|Card|nil targets], [Card|int|nil sc], [int zone]) -> int,int
```

## Description

Returns the usable Monster Zone count for Special Summoning from the Extra Deck, followed by the usable zone mask.
reason_player defaults to the current reason player. targets are treated as leaving the field before the count is checked.

## Parameters

- `player` `int`
- `reason_player` `int` optional
- `targets` `Group|Card|nil` optional
- `sc` `Card|int|nil` optional
- `zone` `int` optional

## Returns

- `int` - Number of usable Monster Zones.
- `int` - Usable zone mask.

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:4938`
