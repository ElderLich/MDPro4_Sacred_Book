# Duel.GetLocationCountFromEx

## Signature

```lua
Duel.GetLocationCountFromEx(int player, [int reason_player], [Group|Card|nil targets], [Card|int sc], [int zone]) -> int
```

## Description

Return the number of available slots on player's field [after targets leave due to reason_player] for Special Summoning card sc from the Extra Deck in zone

## Parameters

- `player` `int`
- `reason_player` `int` optional - default: player
- `targets` `Group|Card|nil` optional
- `sc` `Card|int` optional
- `zone` `int` optional - default: 0xff

## Returns

- `int`

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:4938`
