# Card.IsLinkSummonable

## Signature

```lua
Card.IsLinkSummonable(Card c, Group|nil materials, [Card|nil lcard], [int minc], [int maxc]) -> bool
```

## Description

Checks whether Link Monster c can be Link Summoned by the current reason player.
Optional materials, lcard, minc, and maxc restrict the Link Material pool and material count used by the core check.

## Parameters

- `c` `Card`
- `materials` `Group|nil`
- `lcard` `Card|nil` optional
- `minc` `int` optional - default: 0
- `maxc` `int` optional - default: 0

## Returns

- `bool`

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3578`
