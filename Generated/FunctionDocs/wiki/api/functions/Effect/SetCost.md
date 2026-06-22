# Effect.SetCost

## Signature

```lua
Effect.SetCost(Effect e, function cost_func) -> void
```

## Description

Sets e's cost callback. For activated effects, the callback checks whether the cost can be paid and then pays it.
Cost callbacks should only test legality when chk is 0; irreversible payment belongs in the nonzero chk branch.

## How To Use It

Cost callbacks usually have two phases. When `chk==0`, only answer whether the cost can be paid. When `chk` is not 0, actually pay the cost.

```lua
function s.cost(e,tp,eg,ep,ev,re,r,rp,chk)
    if chk==0 then return Duel.CheckLPCost(tp,1000) end
    Duel.PayLPCost(tp,1000)
end
```

Do not perform irreversible actions during the `chk==0` check. The engine may call that branch just to test activation legality.

## Related Functions

- [Duel.CheckLPCost](/api/functions/Duel/CheckLPCost)
- [Duel.PayLPCost](/api/functions/Duel/PayLPCost)
- [Effect.IsCostChecked](/api/functions/Effect/IsCostChecked)

## Parameters

- `e` `Effect`
- `cost_func` `function`

## Source

- `D:\Programs\GitHub\ygopro-core\libeffect.cpp:627`
