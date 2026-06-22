# Duel.RemoveOverlayCard

## Signature

```lua
Duel.RemoveOverlayCard(int player, int s, int o, int min, int max, int reason) -> int
```

## Description

Lets player remove between min and max Xyz Materials from the specified own/opponent field locations for reason.
s marks locations on player's own field and o marks locations on the opponent's field, from player's perspective. The return value is the number of materials removed.

## Parameters

- `player` `int`
- `s` `int`
- `o` `int`
- `min` `int`
- `max` `int`
- `reason` `int`

## Returns

- `int`

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:5018`
