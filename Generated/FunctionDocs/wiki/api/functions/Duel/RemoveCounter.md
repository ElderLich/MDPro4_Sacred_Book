# Duel.RemoveCounter

## Signature

```lua
Duel.RemoveCounter(int player, int s, int o, int countertype, int count, int reason) -> bool
```

## Description

Lets player remove count counters of countertype from the selected field locations for reason and returns whether removal succeeded.
s marks locations on player's own field and o marks locations on the opponent's field, from player's perspective. The core can offer applicable counter-removal replacement effects before removing counters.

## Parameters

- `player` `int`
- `s` `int`
- `o` `int`
- `countertype` `int`
- `count` `int`
- `reason` `int`

## Returns

- `bool`

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:4877`
