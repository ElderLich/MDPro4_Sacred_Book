# Card.IsAttackable

## Signature

```lua
Card.IsAttackable(Card c) -> bool
```

## Description

Checks whether c currently satisfies the core's basic attack-capable conditions.
The card must be face-up Attack Position, or face-up Defense Position with EFFECT_DEFENSE_ATTACK, and it must not be forbidden, unable to attack, attack-disabled, or under a skipped Battle Phase. This does not check attack-announcement costs.

## Parameters

- `c` `Card`

## Returns

- `bool`

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3601`
