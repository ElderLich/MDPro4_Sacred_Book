# Card.IsXyzSummonable

## Signature

```lua
Card.IsXyzSummonable(Card c, [Group|nil materials], [int minc], [int maxc]) -> bool
```

## Description

Checks whether Xyz Monster c can be Xyz Summoned by the current reason player with an optional material group and min/max constraints.

## Parameters

- `c` `Card`
- `materials` `Group|nil` optional
- `minc` `int` optional
- `maxc` `int` optional

## Returns

- `bool`

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3577`
