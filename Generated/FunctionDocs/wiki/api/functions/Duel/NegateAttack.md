# Duel.NegateAttack

## Signature

```lua
Duel.NegateAttack() -> bool
```

## Description

Attempts to negate the current attack and returns whether the attack was successfully negated.
The core fails if there is no valid current attacker, if the attacker moved or changed field ID, if the attacker cannot attack, if the Damage Step state blocks attack negation, or if the attacker is not affected by the resolving effect.

## Returns

- `bool`

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:4960`
