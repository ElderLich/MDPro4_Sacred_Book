# Duel.IsExistingMatchingCard

## Signature

```lua
Duel.IsExistingMatchingCard([function|nil f], int player, int s, int o, int count, [Card|Group|nil ex], ... any) -> bool
```

## Description

Checks whether the specified locations contain at least count cards that satisfy filter f and are not excluded by ex.
s is player's own location mask and o is the opponent's location mask from that player's viewpoint. Extra arguments after ex are passed to f.

## Parameters

- `f` `function|nil` optional
- `player` `int`
- `s` `int`
- `o` `int`
- `count` `int`
- `ex` `Card|Group|nil` optional
- `...` `any`

## Returns

- `bool`

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:4972`
