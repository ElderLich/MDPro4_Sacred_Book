# Duel.CalculateDamage

## Signature

```lua
Duel.CalculateDamage(Card attacker, Card|nil attack_target, [bool new_attack]) -> void
```

## Description

Starts damage calculation between attacker and attack_target, or a direct attack when attack_target is nil.
new_attack is optional and is passed to the damage-step processor. If attacker and attack_target are the same card, the binding returns no value and does not start damage calculation.

## Parameters

- `attacker` `Card`
- `attack_target` `Card|nil`
- `new_attack` `bool` optional - default: false

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:4921`
