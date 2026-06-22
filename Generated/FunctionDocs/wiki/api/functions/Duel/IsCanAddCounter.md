# Duel.IsCanAddCounter

## Signature

```lua
Duel.IsCanAddCounter(int player, [int countertype], [int count], [Card c]) -> bool
```

## Description

With only player, checks whether player is not forbidden from placing counters.
With countertype, count, and c, checks whether player can place that many counters of countertype on c.

## Parameters

- `player` `int`
- `countertype` `int` optional
- `count` `int` optional
- `c` `Card` optional

## Returns

- `bool`

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:4876`
