# Duel.SetTargetCard

## Signature

```lua
Duel.SetTargetCard(Card|Group targets) -> void
```

## Description

Stores targets as the target cards for the currently handled Chain.
For non-continuous effects, the core creates Chain relations for those cards and sends the become-target message when the effect has EFFECT_FLAG_CARD_TARGET.
This records broad operation targets; it does not by itself check whether the cards are legal effect targets.

## Parameters

- `targets` `Card|Group` - Card or Group to record as current Chain target cards.

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:5004`
