# Duel.CheckReleaseGroup

## Signature

```lua
Duel.CheckReleaseGroup(int player, [function|nil f], int count, [Card|Group|nil ex], ... any) -> bool
```

## Description

Checks whether player can release at least count cards matching f, excluding ex.
Extra arguments after ex are passed to f after the Card argument. This helper uses REASON_COST.

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
