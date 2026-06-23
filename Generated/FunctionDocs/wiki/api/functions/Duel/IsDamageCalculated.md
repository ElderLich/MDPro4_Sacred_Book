# Duel.IsDamageCalculated

## Signature

```lua
Duel.IsDamageCalculated() -> bool
```

## Description

Returns whether damage calculation has been performed in the current battle/damage-step state.
Use it with Duel.GetCurrentPhase in Damage Step conditions, especially for ATK/DEF-changing effects that stop being legal after damage calculation.

## Returns

- `bool` - true after damage calculation has been performed in the current battle timing.

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:4956`
