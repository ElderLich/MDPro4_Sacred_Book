# Effect.SetCategory

## Signature

```lua
Effect.SetCategory(Effect e, int cate) -> void
```

## Description

Sets e's operation category flags, such as CATEGORY_DESTROY, CATEGORY_TOHAND, or CATEGORY_SPECIAL_SUMMON.
Categories describe what the effect may do; known operation details should still be recorded with Duel.SetOperationInfo in the Target callback.

## How To Use It

Categories tell the engine and response checks what kind of action the effect may perform.

```lua
e1:SetCategory(CATEGORY_DESTROY+CATEGORY_TOHAND)
```

The category is not the actual operation. If the affected cards, player, or count are known during targeting, also call `Duel.SetOperationInfo` in the Target callback.

## Related Functions

- [Duel.SetOperationInfo](/api/functions/Duel/SetOperationInfo)
- [Duel.GetOperationInfo](/api/functions/Duel/GetOperationInfo)

## Parameters

- `e` `Effect`
- `cate` `int`

## Source

- `D:\Programs\GitHub\ygopro-core\libeffect.cpp:623`
