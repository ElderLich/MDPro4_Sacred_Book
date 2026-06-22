# Card.IsAbleToRemoveAsCost

## Signature

```lua
Card.IsAbleToRemoveAsCost(Card c, [int pos]) -> bool
```

## Description

Checks whether c can be banished as a cost by the current reason player.
pos controls the banished position and defaults to POS_FACEUP.

## Parameters

- `c` `Card`
- `pos` `int` optional - default: POS_FACEUP

## Returns

- `bool`

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3594`
