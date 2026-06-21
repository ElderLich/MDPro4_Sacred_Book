# Duel.GetMatchingGroup

## Signature

```lua
Duel.GetMatchingGroup([function|nil f], int player, int s, int o, [Card|Group|nil ex], ... any) -> Group
```

## Description

Filter function to return to the specified location to meet the filter condition f and not equal to the ex card
The sixth parameter starts as an extra parameter

## Parameters

- `f` `function|nil` optional
- `player` `int`
- `s` `int`
- `o` `int`
- `ex` `Card|Group|nil` optional
- `...` `any`

## Returns

- `Group`

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:4969`
