# Duel.RemoveCounter

## Signature

```lua
Duel.RemoveCounter(int player, int s, int o, int countertype, int count, int reason) -> bool
```

## Description

Causes the player player to remove count objects of the countertype type present on the farm for reason reasons. The return value indicates success
S represents the position of the player's own removable pointer, o represents the position of the opponent's removable pointer for the player

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
