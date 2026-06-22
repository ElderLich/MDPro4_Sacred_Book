# Duel.SkipPhase

## Signature

```lua
Duel.SkipPhase(int player, int phase, int reset_flag, int reset_count, [int value]) -> void
```

## Description

Applies a temporary field effect that makes player skip phase.
The phase must be one of PHASE_DRAW, PHASE_STANDBY, PHASE_MAIN1, PHASE_BATTLE, PHASE_MAIN2, or PHASE_END. reset_count values of 0 or less are treated as 1, and value is stored on the generated skip effect.

## Parameters

- `player` `int`
- `phase` `int`
- `reset_flag` `int`
- `reset_count` `int`
- `value` `int` optional - default: 0

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:4955`
