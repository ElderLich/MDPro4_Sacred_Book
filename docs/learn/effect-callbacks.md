# Conditions, Costs, Activation Procedures, and Resolution

Activated effects usually delegate work to callbacks.

```lua
e1:SetCondition(s.condition)
e1:SetCost(s.cost)
e1:SetTarget(s.target)
e1:SetOperation(s.operation)
```

The common callback arguments are:

| Name | Meaning |
| --- | --- |
| `e` | The effect being checked or resolving. |
| `tp` | The player activating or controlling the effect context. |
| `eg` | Event group, when an event gives cards to the callback. |
| `ep` | Event player. |
| `ev` | Event value. |
| `re` | Related effect that caused the event. |
| `r` | Reason flags. |
| `rp` | Reason player. |
| `chk` | Target/cost legality check flag. |
| `chkc` | Re-target check for target effects. |

## Condition

Conditions answer whether the effect may be considered.

```lua
function s.condition(e,tp,eg,ep,ev,re,r,rp)
  return Duel.IsMainPhase()
end
```

## Cost

Costs must be payable while `chk==0`, then paid when `chk` is not `0`.

```lua
function s.cost(e,tp,eg,ep,ev,re,r,rp,chk)
  if chk==0 then return Duel.CheckReleaseGroup(tp,s.cfilter,1,nil) end
  local g=Duel.SelectReleaseGroup(tp,s.cfilter,1,1,nil)
  Duel.Release(g,REASON_COST)
end
```

## Target

Targets check activation legality and declare operation info.

```lua
function s.target(e,tp,eg,ep,ev,re,r,rp,chk,chkc)
  if chk==0 then return Duel.IsPlayerCanDraw(tp,1) end
  Duel.SetOperationInfo(0,CATEGORY_DRAW,nil,0,tp,1)
end
```

## Operation

Operations resolve the effect. Re-check that affected cards are still related to
the effect before moving or modifying them.

```lua
function s.operation(e,tp,eg,ep,ev,re,r,rp)
  Duel.Draw(tp,1,REASON_EFFECT)
end
```

Relevant API pages:

- [`Duel.SetOperationInfo`](/api/functions/Duel/SetOperationInfo)
- [`Duel.Draw`](/api/functions/Duel/Draw)
- [`Duel.Release`](/api/functions/Duel/Release)
