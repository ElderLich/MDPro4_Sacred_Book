# Duel.IsCanRemoveCounter

## Signature

```lua
Duel.IsCanRemoveCounter(int player, int s, int o, int countertype, int count, int reason) -> bool
```

## Description

Checks whether the player player can remove count objects of the countertype type on the farm for reason reasons
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

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:4878`
