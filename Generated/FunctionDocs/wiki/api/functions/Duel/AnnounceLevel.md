# Duel.AnnounceLevel

## Signature

```lua
Duel.AnnounceLevel(int player, [int min], [int max], [int excluded_level1], [... int]) -> int|nil,int|nil
```

## Description

Lets player declare a Level and returns the declared Level plus the zero-based option index.
min and max default to 1 and 12 and are swapped if min is greater than max. Extra level arguments are excluded from the options; if no Levels remain, the binding returns no value.

## Parameters

- `player` `int`
- `min` `int` optional - default: 1
- `max` `int` optional - default: 12
- `excluded_level1` `int` optional
- `...` `int` optional

## Returns

- `int|nil` - Declared Level.
- `int|nil` - Zero-based option index.

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:5031`
