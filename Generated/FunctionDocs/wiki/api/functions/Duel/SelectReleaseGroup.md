# Duel.SelectReleaseGroup

## Signature

```lua
Duel.SelectReleaseGroup(int sel_player, [function|nil f], int min, int max, [Card|Group|nil ex], ... any) -> Group
```

## Description

Filter function, allowing players to choose from the field min-max Zhang is not equal to ex to meet the conditions f can be liberated card (non-superior summon)

## Parameters

- `sel_player` `int`
- `f` `function|nil` optional
- `min` `int`
- `max` `int`
- `ex` `Card|Group|nil` optional
- `...` `any`

## Returns

- `Group`

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:4977`
