# Card.IsRank

## Signature

```lua
Card.IsRank(Card c, int rank1, [int rank2], [... int]) -> bool
```

## Description

Checks whether c:GetRank() equals any supplied rank value.
Nil rank arguments are skipped. The binding compares the numeric Rank directly; it does not separately require c to be an Xyz Monster, so non-Xyz cards compare as Rank 0.

## Parameters

- `c` `Card`
- `rank1` `int`
- `rank2` `int` optional
- `...` `int` optional

## Returns

- `bool`

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3543`
