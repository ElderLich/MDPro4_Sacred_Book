# Duel.GetTargetCount

## Signature

```lua
Duel.GetTargetCount([function|nil f], int player, int s, int o, [Card|Group|nil ex], ... any) -> int
```

## Description

Basic with Duel.GetMatchingGroupCount, the difference lies in the need to add to determine whether the card is currently being processed by the effect of the object

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

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:4984`
