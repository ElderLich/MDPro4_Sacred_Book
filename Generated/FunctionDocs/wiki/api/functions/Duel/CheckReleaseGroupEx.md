# Duel.CheckReleaseGroupEx

## Signature

```lua
Duel.CheckReleaseGroupEx(int player, [function|nil f], int count, int reason, bool use_hand, [Card|Group|nil ex], ... any) -> bool
```

## Description

Checks whether player can release at least count cards matching f, excluding ex, with an explicit reason and optional hand releases.
Extra arguments after ex are passed to f after the Card argument.

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
