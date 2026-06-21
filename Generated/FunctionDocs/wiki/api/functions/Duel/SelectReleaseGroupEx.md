# Duel.SelectReleaseGroupEx

## Signature

```lua
Duel.SelectReleaseGroupEx(int player, [function|nil f], int min, int max, int reason, bool use_hand, [Card|Group|nil ex], ... any) -> Group
```

## Description

Filter function, allowing the player player from the field · hand card selection min-max Zhang does not equal ex to meet the conditions of f can be liberated card (non-superior call)

## Parameters

- `player` `int`
- `f` `function|nil` optional
- `min` `int`
- `max` `int`
- `reason` `int`
- `use_hand` `bool`
- `ex` `Card|Group|nil` optional
- `...` `any`

## Returns

- `Group`

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:4979`
