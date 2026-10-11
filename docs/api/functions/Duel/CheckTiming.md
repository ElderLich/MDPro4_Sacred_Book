# Duel.CheckTiming

## Signature

```lua
Duel.CheckTiming(int timing) -> bool
```

## Description

Returns whether the current core hint-timing masks contain timing for either player.
This is a prompt-window helper, not a full activation legality check; no indexed local card script currently calls it directly.
Use ordinary type/code/range, condition, cost, and target checks for real legality. See the Chain Timing And Activation Windows learning guide for full patterns.
Pair this with Effect.SetHintTiming when an optional effect needs to be visible only during specific timing windows.

## How To Use It

Use this in optional trigger or Quick Effect conditions when the effect should only be offered during specific client timing windows.

```lua
return Duel.CheckTiming(TIMING_END_PHASE)
```

This checks the current hint-timing masks from the duel state. `Effect.SetHintTiming` controls when an effect asks to be shown; `Duel.CheckTiming` answers whether the current window matches.

## Related Functions

- [Effect.SetHintTiming](/api/functions/Effect/SetHintTiming)
- [Duel.GetCurrentChain](/api/functions/Duel/GetCurrentChain)
- [Duel.IsChainSolving](/api/functions/Duel/IsChainSolving)

## Parameters

- `timing` `int` - TIMING_* mask to test against the current core hint timing.

## Returns

- `bool` - True if timing is present in either player's current hint timing mask.

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:4897`

## Guided Examples

Learn how to use this function in context:

- [Chain Timing And Activation Windows](/learn/chain-timing-and-activation-windows)

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

No indexed local card script currently calls this function.

This can mean the function is unused in the current script set, is only called through an alias, or is available for future/manual scripts.
