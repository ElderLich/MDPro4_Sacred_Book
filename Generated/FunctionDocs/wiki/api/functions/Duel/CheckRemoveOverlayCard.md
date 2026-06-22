# Duel.CheckRemoveOverlayCard

## Signature

```lua
Duel.CheckRemoveOverlayCard(int player, int s, int o, int count, int reason) -> bool
```

## Description

Checks whether player can remove at least count Xyz Materials from the specified own/opponent field locations for reason.
s marks locations on player's own field and o marks locations on the opponent's field, from player's perspective. Applicable replacement effects can satisfy the check.

## Parameters

- `player` `int`
- `s` `int`
- `o` `int`
- `count` `int`
- `reason` `int`

## Returns

- `bool`

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:5017`
