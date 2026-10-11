# Card.EnableReviveLimit

## Signature

```lua
Card.EnableReviveLimit(Card c) -> void
```

## Description

Marks c as needing to be properly Summoned before ordinary Special Summon effects can bring it back from public locations.
The core registers an EFFECT_REVIVE_LIMIT effect on c. Pair this with the card's proper Summon procedure or with an effect that calls CompleteProcedure after a successful proper Summon.
Local core handling clears the completed-procedure status when the card moves to the hand or Deck.

## Parameters

- `c` `Card` - Card that should require a proper Summon before ordinary revive effects can Special Summon it.

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3623`
