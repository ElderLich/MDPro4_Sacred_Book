# Card.IsAbleToHand

## Signature

```lua
Card.IsAbleToHand(Card c, [int player]) -> bool
```

## Description

Checks whether c can be returned or added to the hand by the current reason player.
An optional player argument can be passed when a specific player is performing the action.

## Parameters

- `c` `Card`
- `player` `int` optional - default: reason player

## Returns

- `bool`

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3639`
