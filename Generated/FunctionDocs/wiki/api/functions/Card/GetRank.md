# Card.GetRank

## Signature

```lua
Card.GetRank(Card c) -> int
```

## Description

Returns c's current Rank.
Non-Xyz cards return 0. Xyz Monsters outside the Monster Zone return their original Rank; in the Monster Zone, Rank-changing effects are applied and the result is at least 1.

## Parameters

- `c` `Card`

## Returns

- `int`

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3457`
