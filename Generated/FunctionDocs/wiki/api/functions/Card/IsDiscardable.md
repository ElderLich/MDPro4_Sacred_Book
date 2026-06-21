# Card.IsDiscardable

## Signature

```lua
Card.IsDiscardable(Card c, [int reason]) -> bool
```

## Description

Check whether c can be discarded
Note: This function is only used to detect,
REASON_DISCARD as a reason to hand a card to the tomb and will not lead to that card can not be discarded

## Parameters

- `c` `Card`
- `reason` `int` optional - default: REASON_COST

## Returns

- `bool`

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3597`
