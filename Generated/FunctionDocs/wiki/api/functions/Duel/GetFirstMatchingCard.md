# Duel.GetFirstMatchingCard

## Signature

```lua
Duel.GetFirstMatchingCard([function|nil f], int player, int s, int o, [Card|Group|nil ex], [... any]) -> Card|nil
```

## Description

Returns the first card in the specified locations that satisfies f and is not excluded by ex.
f may be nil. ex may be a Card, a Group, or nil, and extra arguments after ex are passed to f. Returns nil when no matching card is found.

## Parameters

- `f` `function|nil` optional
- `player` `int`
- `s` `int`
- `o` `int`
- `ex` `Card|Group|nil` optional
- `...` `any` optional

## Returns

- `Card|nil`

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:4971`
