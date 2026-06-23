# Effect.SetTarget

## Signature

```lua
Effect.SetTarget(Effect e, function targ_func) -> void
```

## Description

Sets e's target callback. For activated effects, this callback performs activation legality checks and records target or operation information.
Target callbacks normally use chk==0 only to answer legality, then use the real activation branch to select official targets with Duel.SelectTarget, record broad targets with Duel.SetTargetCard, or announce operation details with Duel.SetOperationInfo.

## How To Use It

Target callbacks do two jobs for activated effects: answer activation legality during `chk==0`, then record targets and operation information when activation is accepted.

```lua
function s.target(e,tp,eg,ep,ev,re,r,rp,chk,chkc)
    if chkc then return chkc:IsOnField() and chkc:IsControler(1-tp) end
    if chk==0 then
        return Duel.IsExistingTarget(aux.TRUE,tp,0,LOCATION_ONFIELD,1,nil)
    end
    Duel.Hint(HINT_SELECTMSG,tp,HINTMSG_DESTROY)
    Duel.SelectTarget(tp,aux.TRUE,tp,0,LOCATION_ONFIELD,1,1,nil)
    Duel.SetOperationInfo(0,CATEGORY_DESTROY,nil,1,1-tp,LOCATION_ONFIELD)
end
```

Use `Duel.SelectTarget` for cards that are official targets. Use `Duel.SetOperationInfo` so chained cards can see what the effect is expected to do.

## Related Functions

- [Duel.IsExistingTarget](/api/functions/Duel/IsExistingTarget)
- [Duel.SelectTarget](/api/functions/Duel/SelectTarget)
- [Duel.SetOperationInfo](/api/functions/Duel/SetOperationInfo)

## Parameters

- `e` `Effect` - Effect whose target callback is replaced.
- `targ_func` `function` - Callback function stored on e.

## Source

- `D:\Programs\GitHub\ygopro-core\libeffect.cpp:626`
