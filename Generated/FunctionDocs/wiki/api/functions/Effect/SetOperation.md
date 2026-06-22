# Effect.SetOperation

## Signature

```lua
Effect.SetOperation(Effect e, nil|function op_func) -> void
```

## Description

Sets e's operation callback. Passing nil clears the operation.

## How To Use It

The operation callback performs the effect when the Chain resolves.

For targeted cards, retrieve the target and re-check that it is still related to the resolving effect before applying the action:

```lua
function s.operation(e,tp,eg,ep,ev,re,r,rp)
    local tc=Duel.GetFirstTarget()
    if tc and tc:IsRelateToEffect(e) then
        Duel.Destroy(tc,REASON_EFFECT)
    end
end
```

Passing nil to `SetOperation` clears the operation. That is occasionally useful for effects whose category or target data is enough and no resolution callback is needed.

## Related Functions

- [Effect.SetTarget](/api/functions/Effect/SetTarget)
- [Duel.GetFirstTarget](/api/functions/Duel/GetFirstTarget)
- [Duel.GetTargetsRelateToChain](/api/functions/Duel/GetTargetsRelateToChain)

## Parameters

- `e` `Effect`
- `op_func` `nil|function`

## Source

- `D:\Programs\GitHub\ygopro-core\libeffect.cpp:629`
