# Duel.IsExistingTarget

## Signature

```lua
Duel.IsExistingTarget([function|nil f], int player, int s, int o, int count, [Card|Group|nil ex], ... any) -> bool
```

## Description

Filter function to check whether there is at least the specified number of positions to meet the filter conditions f and not equal ex
And can become a card of an object that is currently being processed
The seventh argument starts as an extra parameter

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

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:4985`
