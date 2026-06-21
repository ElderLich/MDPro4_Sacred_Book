# Duel.CheckReleaseGroupEx

## Signature

```lua
Duel.CheckReleaseGroupEx(int player, [function|nil f], int count, int reason, bool use_hand, [Card|Group|nil ex], ... any) -> bool
```

## Description

Check whether there are at least count cards that can satisfy the filter condition f and are not equal to ex. (For non-superior summoning)

## Parameters

- `player` `int`
- `f` `function|nil` optional
- `count` `int`
- `reason` `int`
- `use_hand` `bool`
- `ex` `Card|Group|nil` optional
- `...` `any`

## Returns

- `bool`

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:4978`
