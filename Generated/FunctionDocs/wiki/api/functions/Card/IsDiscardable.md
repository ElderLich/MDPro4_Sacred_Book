# Card.IsDiscardable

## Signature

```lua
Card.IsDiscardable(Card c, [int reason]) -> bool
```

## Description

Checks whether c can be discarded for reason.
This is only a check: sending a card from the hand to the Graveyard with REASON_DISCARD does not by itself make that card unable to be discarded.

## Parameters

- `c` `Card`
- `reason` `int` optional - default: REASON_COST

## Returns

- `bool`

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3652`
