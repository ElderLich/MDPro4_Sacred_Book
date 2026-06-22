# Duel.GetMatchingGroupCount

## Signature

```lua
Duel.GetMatchingGroupCount([function|nil f], int player, int s, int o, [Card|Group|nil ex], ... any) -> int
```

## Description

Counts cards in the specified locations that satisfy filter f and are not excluded by ex.
Extra arguments after ex are passed to f after the card argument.

## Parameters

- `f` `function|nil` optional
- `player` `int`
- `s` `int`
- `o` `int`
- `ex` `Card|Group|nil` optional
- `...` `any`

## Returns

- `int`

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:4970`
