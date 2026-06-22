# Duel.ChangeAttackTarget

## Signature

```lua
Duel.ChangeAttackTarget(Card|nil target) -> bool
```

## Description

Changes the current attack target to target, or to a direct attack when target is nil, and returns whether the change succeeded.
The current attacker must exist, be able to attack, and not have its attack canceled. A card target must be one of the current legal attack targets; direct attack requires that the attacker is not forbidden from attacking directly.

## Parameters

- `target` `Card|nil`

## Returns

- `bool`

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:4920`
