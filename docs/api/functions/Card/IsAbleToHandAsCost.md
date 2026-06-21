# Card.IsAbleToHandAsCost

## Signature

```lua
Card.IsAbleToHandAsCost(Card c) -> bool
```

## Description

Checks whether c can be returned to the hand as a cost.
This uses c's actual return destination and returns false when the card would go somewhere other than the player's hand, such as the Extra Deck.

## Parameters

- `c` `Card`

## Returns

- `bool`

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3589`
