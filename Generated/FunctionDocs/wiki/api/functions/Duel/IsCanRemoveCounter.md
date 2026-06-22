# Duel.IsCanRemoveCounter

## Signature

```lua
Duel.IsCanRemoveCounter(int player, int s, int o, int countertype, int count, int reason) -> bool
```

## Description

Checks whether player can remove count counters of countertype for reason from the selected field locations.
s marks locations on player's own field and o marks locations on the opponent's field, from player's perspective.

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

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:4878`
