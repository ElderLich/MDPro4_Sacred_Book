# Duel.CheckTiming

## Signature

```lua
Duel.CheckTiming(int timing) -> bool
```

## Description

Returns whether the current core hint-timing masks contain timing for either player.
This is a prompt-window helper, not a full activation legality check; no indexed local card script currently calls it directly.
Use ordinary type/code/range, condition, cost, and target checks for real legality. See the Chain Timing And Activation Windows learning guide for full patterns.

## Parameters

- `timing` `int` - TIMING_* mask to test against the current core hint timing.

## Returns

- `bool` - True if timing is present in either player's current hint timing mask.

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:4897`
