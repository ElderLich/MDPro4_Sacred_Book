# Duel.Damage

## Signature

```lua
Duel.Damage(int player, int value, int reason, [bool is_step]) -> int
```

## Description

Deals value effect damage to player for reason and returns the damage actually applied.
If damage is changed into LP recovery or prevented, the return value reflects the final applied damage. With is_step=true, finish the damage/recovery batch with Duel.RDComplete.

## Parameters

- `player` `int`
- `value` `int`
- `reason` `int`
- `is_step` `bool` optional - default: false

## Returns

- `int`

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:4901`
