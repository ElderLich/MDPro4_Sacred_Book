# Duel.AnnounceNumber

## Signature

```lua
Duel.AnnounceNumber(int player, int number1, [int number2], [... int]) -> int,int
```

## Description

Lets player choose one of the supplied numbers.
Returns the selected number and the core's 0-based option index for that number.

## Parameters

- `player` `int`
- `number1` `int`
- `number2` `int` optional
- `...` `int` optional

## Returns

- `int` - Selected number.
- `int` - 0-based option index selected by the core.

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:5034`
