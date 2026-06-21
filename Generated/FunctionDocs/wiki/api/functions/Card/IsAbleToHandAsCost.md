# Card.IsAbleToHandAsCost

## Signature

```lua
Card.IsAbleToHandAsCost(Card c) -> bool
```

## Description

Check whether c can be sent as the cost of hand cards
Note: This function appends the actual destination of c to Card.IsAbleToHand
This function returns false when c is sent to the other hand (if the retraction loop is applicable, or c is a blend, cohomology, and oversize)

## Parameters

- `c` `Card`

## Returns

- `bool`

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3589`
