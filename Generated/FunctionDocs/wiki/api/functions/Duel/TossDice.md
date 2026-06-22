# Duel.TossDice

## Signature

```lua
Duel.TossDice(int player, int count1, [int count2]) -> int,...?
```

## Description

Tosses count1 dice for player and, when count2 is supplied, count2 dice for the opponent.
Valid dice results are integers from 1 to 6. Normal script use should keep count1 + count2 at 5 or less; the core rejects count1 &lt;= 0 and count2 &lt; 0.

## Parameters

- `player` `int`
- `count1` `int`
- `count2` `int` optional - default: 0

## Returns

- `int` - First die result.
- `...?` - Additional die results.

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:5037`
