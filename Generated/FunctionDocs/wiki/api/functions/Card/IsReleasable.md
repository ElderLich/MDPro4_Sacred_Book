# Card.IsReleasable

## Signature

```lua
Card.IsReleasable(Card c, [int reason]) -> bool
```

## Description

Checks whether c can be Released for a non-Summon reason by the current reason player.
reason defaults to REASON_COST. The core rejects cards being Summoned, Xyz Materials, cards in the GY or banished, Spell/Trap Cards in the hand, cards the player cannot release, and cards affected by EFFECT_UNRELEASABLE_NONSUM.

## Parameters

- `c` `Card`
- `reason` `int` optional - default: REASON_COST

## Returns

- `bool`

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3650`
