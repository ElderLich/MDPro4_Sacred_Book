# Card.IsAbleToRemove

## Signature

```lua
Card.IsAbleToRemove(Card c, [int player], [int pos], [int reason]) -> bool
```

## Description

Checks whether c can be banished by player in position pos for reason.
player defaults to the current reason player, pos defaults to POS_FACEUP, and reason defaults to REASON_EFFECT.

## Parameters

- `c` `Card`
- `player` `int` optional
- `pos` `int` optional
- `reason` `int` optional

## Returns

- `bool`

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3643`
