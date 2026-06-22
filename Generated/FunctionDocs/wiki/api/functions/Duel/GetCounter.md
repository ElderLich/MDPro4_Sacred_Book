# Duel.GetCounter

## Signature

```lua
Duel.GetCounter(int player, int s, int o, int countertype) -> int|nil
```

## Description

Returns the total number of countertype counters in player-relative locations s and o.

## Parameters

- `player` `int`
- `s` `int`
- `o` `int`
- `countertype` `int`

## Returns

- `int|nil` - Counter count, or nil if player is invalid.

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:4879`
