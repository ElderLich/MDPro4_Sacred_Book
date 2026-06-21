# Duel.GetFirstMatchingCard

## Signature

```lua
Duel.GetFirstMatchingCard([function|nil f], int player, int s, int o, [Card|Group|nil ex], ... any) -> Card
```

## Description

Filter function to return to the specified location to meet the filter condition f and not equal to the first card ex
The sixth parameter starts as an extra parameter

## Parameters

- `f` `function|nil` optional
- `player` `int`
- `s` `int`
- `o` `int`
- `ex` `Card|Group|nil` optional
- `...` `any`

## Returns

- `Card`

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:4971`
