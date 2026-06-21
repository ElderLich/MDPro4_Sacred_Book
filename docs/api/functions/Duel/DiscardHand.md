# Duel.DiscardHand

## Signature

```lua
Duel.DiscardHand(int player, [function|nil f], int min, int max, int reason, [Card|Group|nil ex], ... any) -> int
```

## Description

Filter function allows the player to select and discard the player to meet the screening conditions f soldiers is not equal to ex min-max Zhang card
The seventh argument starts as an extra parameter

## Parameters

- `player` `int`
- `f` `function|nil` optional
- `min` `int`
- `max` `int`
- `reason` `int`
- `ex` `Card|Group|nil` optional
- `...` `any`

## Returns

- `int`

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:4911`
