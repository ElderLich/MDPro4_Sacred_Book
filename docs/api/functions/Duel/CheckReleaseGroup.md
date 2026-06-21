# Duel.CheckReleaseGroup

## Signature

```lua
Duel.CheckReleaseGroup(int player, [function|nil f], int count, [Card|Group|nil ex], ... any) -> bool
```

## Description

Check if the player has at least count of cards that meet the filter condition f and are not equal to ex (non-superior summons)
The fifth parameter starts as an extra parameter

## Parameters

- `player` `int`
- `f` `function|nil` optional
- `count` `int`
- `ex` `Card|Group|nil` optional
- `...` `any`

## Returns

- `bool`

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:4976`
