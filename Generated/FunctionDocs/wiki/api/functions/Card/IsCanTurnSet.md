# Card.IsCanTurnSet

## Signature

```lua
Card.IsCanTurnSet(Card c) -> bool
```

## Description

Checks whether c can be turned face-down by the current reason player.
The core returns false for Link Monsters, Tokens, already face-down cards, and cards or players affected by EFFECT_CANNOT_TURN_SET.

## Parameters

- `c` `Card` - Card checked for whether it can be turned face-down.

## Returns

- `bool` - True if c can be turned face-down by the current reason player.

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3689`
