# Conditions, Costs, Activation Procedures, and Resolution

Activated effects usually delegate work to callbacks.

```lua
e1:SetCondition(s.condition)
e1:SetCost(s.cost)
e1:SetTarget(s.target)
e1:SetOperation(s.operation)
```

Not every effect uses all four. A simple continuous stat effect might only use
`SetValue`; a simple activated effect might only use `SetTarget` and
`SetOperation`.

## Common Callback Arguments

| Name | Meaning |
| --- | --- |
| `e` | The effect being checked or resolving. |
| `tp` | The player activating the effect or the player used as this effect's context. |
| `eg` | Event group, when an event gives cards to the callback. |
| `ep` | Event player. |
| `ev` | Event value. |
| `re` | Related effect that caused the event. |
| `r` | Reason flags. |
| `rp` | Reason player. |
| `chk` | Cost/target legality check flag. |
| `chkc` | Re-target check for target effects. |

The first eight arguments appear together so often that many scripts keep the
same names even when only one or two are used.

## Condition

Conditions answer whether the effect may be considered.

```lua
function s.condition(e,tp,eg,ep,ev,re,r,rp)
    return Duel.IsMainPhase()
end
```

Use a condition for timing or event requirements: "during the Main Phase",
"when this card is Summoned", "if this card was destroyed by battle", and so on.

Conditions are ordinary Lua expressions, so grouping matters.

```lua
return c:IsDefensePos() and Duel.GetLP(1-tp)>Duel.GetLP(tp)
```

Use parentheses when the card text mixes `and` and `or`.

```lua
return (a or b) and c
return a or (b and c)
```

Be careful with `not`: write the expression you mean.

```lua
return not (Duel.GetLP(tp)>1500)
```

That is clearer than relying on reader memory of Lua operator precedence.

## Cost

Costs have two phases. When `chk==0`, only answer whether the cost can be paid.
When `chk` is not 0, actually pay it.

```lua
function s.cost(e,tp,eg,ep,ev,re,r,rp,chk)
    if chk==0 then return Duel.CheckLPCost(tp,1000) end
    Duel.PayLPCost(tp,1000)
end
```

Do not release, discard, banish, or pay LP in the `chk==0` branch. The engine
may call that branch just to test whether the effect can be activated.

Many cost functions have three practical sections:

```lua
function s.cost(e,tp,eg,ep,ev,re,r,rp,chk)
    local c=e:GetHandler()
    if chk==0 then
        return c:IsDiscardable()
    end
    Duel.SendtoGrave(c,REASON_COST+REASON_DISCARD)
end
```

| Section | Job |
| --- | --- |
| Shared setup | Read `e:GetHandler()`, count cards, or build local values used by both branches. |
| Checking branch | Return whether the cost can be paid. |
| Payment branch | Actually pay the cost. |

Do not hide payment inside a helper that is called from both branches unless
the helper itself also respects `chk`.

## Target

Target callbacks usually do two jobs:

1. During `chk==0`, prove the effect can be activated.
2. During the real activation, select targets and announce operation info.

```lua
function s.target(e,tp,eg,ep,ev,re,r,rp,chk,chkc)
    if chkc then return chkc:IsOnField() and s.filter(chkc) end
    if chk==0 then
        return Duel.IsExistingTarget(s.filter,tp,LOCATION_MZONE,0,1,nil)
    end
    Duel.Hint(HINT_SELECTMSG,tp,HINTMSG_TARGET)
    Duel.SelectTarget(tp,s.filter,tp,LOCATION_MZONE,0,1,1,nil)
    Duel.SetOperationInfo(0,CATEGORY_DESTROY,nil,1,tp,LOCATION_MZONE)
end
```

Use `Duel.IsExistingTarget` and `Duel.SelectTarget` when the effect targets.
Use matching-card functions when the card text does not target.

For activated effects that do not target, the target callback often only checks
whether the later operation has a legal attempt and announces operation info.

```lua
function s.sptg(e,tp,eg,ep,ev,re,r,rp,chk)
    local c=e:GetHandler()
    if chk==0 then
        return Duel.GetLocationCount(tp,LOCATION_MZONE)>0
            and c:IsCanBeSpecialSummoned(e,0,tp,false,false)
    end
    Duel.SetOperationInfo(0,CATEGORY_SPECIAL_SUMMON,c,1,0,0)
end
```

Some effects have no legal manual target recheck. In those cases scripts may
answer `false` in the `chkc` branch.

```lua
if chkc then return false end
```

Use that only when the effect's activation should not accept a manually chosen
target.

For continuous field effects, `SetTarget` has a different job: it filters which
cards in the target range are affected.

```lua
e1:SetType(EFFECT_TYPE_FIELD)
e1:SetCode(EFFECT_UPDATE_ATTACK)
e1:SetTargetRange(LOCATION_MZONE,0)
e1:SetTarget(s.atktg)
e1:SetValue(300)

function s.atktg(e,c)
    return c:IsFaceup() and c:IsSetCard(0x123)
end
```

This target callback does not receive `chk` and does not select official Chain
targets. Always read the effect type and effect code before assuming a callback
signature.

## Operation

Operations resolve the effect. The game state may have changed after activation,
so re-check cards before moving or modifying them.

```lua
function s.operation(e,tp,eg,ep,ev,re,r,rp)
    local tc=Duel.GetFirstTarget()
    if tc and tc:IsRelateToEffect(e) then
        Duel.Destroy(tc,REASON_EFFECT)
    end
end
```

If several target cards were selected, use `Duel.GetTargetsRelateToChain()` or
`Duel.GetChainInfo(0,CHAININFO_TARGET_CARDS):Filter(Card.IsRelateToEffect,nil,e)`
depending on what the script needs to preserve.

## Value

`SetValue` can be a number or a callback. Continuous ATK/DEF effects commonly
use value callbacks when the amount depends on the current field.

```lua
function s.val(e,c)
    return Duel.GetMatchingGroupCount(s.filter,c:GetControler(),LOCATION_MZONE,0,nil)*400
end
```

The arguments depend on the effect code. A value function for a stat modifier
is not the same shape as a value function for an activation restriction or an
equip limit.

## `Duel.SetOperationInfo`

`Duel.SetOperationInfo` tells the engine and UI what the effect intends to do.
It does not perform the action. The actual action belongs in the operation.

```lua
Duel.SetOperationInfo(0,CATEGORY_TOHAND,nil,1,tp,LOCATION_DECK)
```

Use categories that match the real operation: draw, destroy, send to GY, banish,
Special Summon, equip, search, and so on.

Relevant API pages:

- [`Effect.SetCondition`](/api/functions/Effect/SetCondition)
- [`Effect.SetCost`](/api/functions/Effect/SetCost)
- [`Effect.SetTarget`](/api/functions/Effect/SetTarget)
- [`Effect.SetOperation`](/api/functions/Effect/SetOperation)
- [`Duel.SetOperationInfo`](/api/functions/Duel/SetOperationInfo)
