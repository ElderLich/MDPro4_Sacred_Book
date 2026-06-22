# Effect.SetCountLimit

## Signature

```lua
Effect.SetCountLimit(Effect e, int count, [int code]) -> void
```

## Description

Sets how many times e can be used before its count limit is spent.
If count is 0, the core treats it as 1. Effects that share a nonzero code share the same usage count. EFFECT_COUNT_CODE_CHAIN is stored together with EFFECT_COUNT_CODE_SINGLE.

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
- `code` `int` optional - Shared count-limit code. Effects with the same nonzero code share usage.

## Source

- `D:\Programs\GitHub\ygopro-core\libeffect.cpp:617`
