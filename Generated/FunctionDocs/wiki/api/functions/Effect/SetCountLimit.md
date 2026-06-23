# Effect.SetCountLimit

## Signature

```lua
Effect.SetCountLimit(Effect e, int count, [int code]) -> void
```

## Description

Sets how many times e can be used before its count limit is spent.
If count is 0, the core treats it as 1. Effects that share a nonzero code share the same usage count for the checked player.
EFFECT_COUNT_CODE_OATH uses oath-style rollback on negated activations and failed procedure attempts; EFFECT_COUNT_CODE_DUEL uses the duel-long count map; EFFECT_COUNT_CODE_SINGLE shares usage by handler instance; EFFECT_COUNT_CODE_CHAIN uses the chain count map.

## How To Use It

Use `SetCountLimit` for once-per-turn and shared-count restrictions.

A normal hard once per turn usually uses the card id as the shared code:

```lua
e1:SetCountLimit(1,id)
```

Effects with the same nonzero code share the same count. Special flags such as `EFFECT_COUNT_CODE_OATH`, `EFFECT_COUNT_CODE_DUEL`, `EFFECT_COUNT_CODE_SINGLE`, and `EFFECT_COUNT_CODE_CHAIN` change how that count is scoped. If `count` is 0, MDPro3 stores it as 1.

## Related Functions

- [Effect.CheckCountLimit](/api/functions/Effect/CheckCountLimit)
- [Effect.UseCountLimit](/api/functions/Effect/UseCountLimit)

## Parameters

- `e` `Effect` - Effect whose count limit is set.
- `count` `int` - Maximum uses before the count is spent; 0 is normalized to 1 by the core.
- `code` `int` optional - Shared count-limit code. Effects with the same nonzero code share usage for the checked player; combine a card id with EFFECT_COUNT_CODE_OATH, EFFECT_COUNT_CODE_DUEL, or EFFECT_COUNT_CODE_SINGLE when that special behavior is needed. Passing exactly EFFECT_COUNT_CODE_CHAIN stores it together with EFFECT_COUNT_CODE_SINGLE in this core.

## Source

- `D:\Programs\GitHub\ygopro-core\libeffect.cpp:617`
