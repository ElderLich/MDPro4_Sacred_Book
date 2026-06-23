# LP Recovery and Effect Damage

LP-changing effects are usually simple at the call site, but they still need
the same activation and resolution discipline as card-moving effects.

MDPro3/YGOPro exposes the core actions as:

```lua
Duel.Damage(player,value,reason,is_step)
Duel.Recover(player,value,reason,is_step)
```

The local define file documents that both functions return the actual LP value
changed. If damage becomes recovery, or recovery becomes damage, the original
function returns `0`. The core binding also clamps negative amounts to `0`.

## Fixed Damage

A fixed damage effect commonly stores the target player and amount during
activation, then reads them at resolution.

```lua
function s.damtg(e,tp,eg,ep,ev,re,r,rp,chk)
    if chk==0 then return true end
    Duel.SetTargetPlayer(1-tp)
    Duel.SetTargetParam(600)
    Duel.SetOperationInfo(0,CATEGORY_DAMAGE,nil,0,1-tp,600)
end

function s.damop(e,tp,eg,ep,ev,re,r,rp)
    local p,d=Duel.GetChainInfo(0,CHAININFO_TARGET_PLAYER,CHAININFO_TARGET_PARAM)
    Duel.Damage(p,d,REASON_EFFECT)
end
```

This pattern appears in local scripts for fixed effect damage. The player and
amount are Chain data, not official card targets.

## Damage Calculated at Resolution

When the amount depends on the current game state, calculate again in the
operation. The activation branch may announce the best known value, but the
operation should use the value required by the card text.

```lua
function s.damtg(e,tp,eg,ep,ev,re,r,rp,chk)
    if chk==0 then return Duel.GetFieldGroupCount(1-tp,LOCATION_HAND,0)>0 end
    Duel.SetTargetPlayer(1-tp)
    local ct=Duel.GetFieldGroupCount(1-tp,LOCATION_HAND,0)
    Duel.SetOperationInfo(0,CATEGORY_DAMAGE,nil,0,1-tp,ct*200)
end

function s.damop(e,tp,eg,ep,ev,re,r,rp)
    local p=Duel.GetChainInfo(0,CHAININFO_TARGET_PLAYER)
    Duel.Damage(p,Duel.GetFieldGroupCount(p,LOCATION_HAND,0)*200,REASON_EFFECT)
end
```

Use this shape for "for each card currently..." effects.

## Recovery From a Target

When recovery depends on a targeted card, select the target during activation
and recheck it during resolution.

```lua
function s.recfilter(c)
    return c:IsFaceup() and c:GetAttack()>0
end

function s.rectg(e,tp,eg,ep,ev,re,r,rp,chk,chkc)
    if chkc then return chkc:IsControler(tp) and chkc:IsLocation(LOCATION_MZONE) and s.recfilter(chkc) end
    if chk==0 then return Duel.IsExistingTarget(s.recfilter,tp,LOCATION_MZONE,0,1,nil) end
    Duel.Hint(HINT_SELECTMSG,tp,HINTMSG_TARGET)
    local g=Duel.SelectTarget(tp,s.recfilter,tp,LOCATION_MZONE,0,1,1,nil)
    Duel.SetOperationInfo(0,CATEGORY_RECOVER,nil,0,tp,math.ceil(g:GetFirst():GetAttack()/2))
end

function s.recop(e,tp,eg,ep,ev,re,r,rp)
    local tc=Duel.GetFirstTarget()
    if tc and tc:IsRelateToEffect(e) and tc:IsFaceup() and tc:GetAttack()>0 then
        Duel.Recover(tp,math.ceil(tc:GetAttack()/2),REASON_EFFECT)
    end
end
```

The operation rechecks face-up state and ATK because the targeted monster may
have changed before resolution.

## Multiple Players

If a card changes both players' LP, decide whether the actions are sequential
or part of a stepped process.

Sequential calls are simple:

```lua
Duel.Damage(1-tp,500,REASON_EFFECT)
Duel.Recover(tp,500,REASON_EFFECT)
```

For a split recovery/damage process, the local API exposes `is_step=true` and
`Duel.RDComplete()`.

```lua
Duel.Damage(0,500,REASON_EFFECT,true)
Duel.Damage(1,500,REASON_EFFECT,true)
Duel.RDComplete()
```

Use stepped LP changes only when the script needs the timing behavior of a
combined process. The define comments explicitly say `Duel.RDComplete()` is
required after stepped `Damage` or `Recover` calls.

## Categories and Operation Info

Match the effect category to the action:

```lua
e1:SetCategory(CATEGORY_DAMAGE)
e1:SetCategory(CATEGORY_RECOVER)
```

Then announce the operation with `Duel.SetOperationInfo`. This helps the engine
and client understand what the Chain Link intends to do.

```lua
Duel.SetOperationInfo(0,CATEGORY_DAMAGE,nil,0,1-tp,1200)
Duel.SetOperationInfo(0,CATEGORY_RECOVER,nil,0,tp,1000)
```

If the amount is not known until resolution, announce the best legal estimate
or the visible value used by local scripts, then recalculate in the operation.

## Return Values

Both `Duel.Damage` and `Duel.Recover` return an integer.

```lua
local dealt=Duel.Damage(1-tp,1000,REASON_EFFECT)
if dealt>0 then
    -- follow-up that cares about actual damage dealt
end
```

Use the return value when the next part of the effect depends on actual LP
changed, not the intended amount.

Useful API pages:

- [`Duel.Damage`](/api/functions/Duel/Damage)
- [`Duel.Recover`](/api/functions/Duel/Recover)
- [`Duel.RDComplete`](/api/functions/Duel/RDComplete)
- [`Duel.SetTargetPlayer`](/api/functions/Duel/SetTargetPlayer)
- [`Duel.SetTargetParam`](/api/functions/Duel/SetTargetParam)
- [`Duel.GetChainInfo`](/api/functions/Duel/GetChainInfo)
