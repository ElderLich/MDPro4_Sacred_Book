# Card.GetHandSynchro

## Signature

```lua
Card.GetHandSynchro(Card c) -> Effect|nil,function|nil,int|nil,int|nil
```

## Description

Returns the hand-Synchro enabling effect on c, its target function, and the min/max hand-material counts.
Only Monster Zone cards are checked. EFFECT_HAND_SYNCHRO has priority, then EFFECT_TUNER_MATERIAL_LIMIT with LOCATION_HAND.

## Parameters

- `c` `Card`

## Returns

- `Effect|nil` - Hand Synchro enabling effect.
- `function|nil` - Effect target function.
- `int|nil` - Minimum hand-material count.
- `int|nil` - Maximum hand-material count.

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3550`
