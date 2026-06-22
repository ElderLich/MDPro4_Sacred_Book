# Effect.SetCondition

## Signature

```lua
Effect.SetCondition(Effect e, function con_func) -> void
```

## Description

Sets e's condition callback. The callback decides whether the effect can apply or be activated in the current context.

## How To Use It

Conditions answer whether the effect can apply or be activated in the current context.

Keep condition callbacks side-effect free. They may be called while the engine is only checking legality:

```lua
function s.spcon(e,tp,eg,ep,ev,re,r,rp)
    return e:GetHandler():IsSummonType(SUMMON_TYPE_SPECIAL)
end

e1:SetCondition(s.spcon)
```

For activated effects, costs and targets still get their own legality checks. The condition should describe the timing or state requirement that belongs to the effect itself.

## Related Functions

- [Effect.SetCost](/api/functions/Effect/SetCost)
- [Effect.SetTarget](/api/functions/Effect/SetTarget)
- [Effect.SetOperation](/api/functions/Effect/SetOperation)

## Parameters

- `e` `Effect`
- `con_func` `function`

## Source

- `D:\Programs\GitHub\ygopro-core\libeffect.cpp:625`
