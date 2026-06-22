# Duel.IsAbleToEnterBP

## Signature

```lua
Duel.IsAbleToEnterBP() -> bool
```

## Description

Checks whether the current turn player can still enter the Battle Phase.
The core requires the duel to allow first-turn attacks or not be turn 1, the current phase to be before PHASE_BATTLE_START, and the turn player not to be affected by EFFECT_CANNOT_BP.

## Returns

- `bool`

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:5071`
