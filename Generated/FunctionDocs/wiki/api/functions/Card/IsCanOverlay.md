# Card.IsCanOverlay

## Signature

```lua
Card.IsCanOverlay(Card c, [int player]) -> bool
```

## Description

Checks whether c can be used as Xyz Material by player.
player defaults to the current reason player. The core rejects Tokens, forbidden cards in invalid states, and cards controlled by the other player that cannot change control.

## Parameters

- `c` `Card`
- `player` `int` optional - default: current reason player

## Returns

- `bool`

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3693`
