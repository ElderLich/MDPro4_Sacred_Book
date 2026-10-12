# LP Recovery and Effect Damage

LP-changing effects are usually simple at the call site, but they still need
the same activation and resolution discipline as card-moving effects.

MDPro4/YGOPro exposes the core actions as:

```lua
Duel.Damage(player,value,reason,is_step)
Duel.Recover(player,value,reason,is_step)
```

The local define file documents that both functions return the actual LP value
changed. If damage becomes recovery, or recovery becomes damage, the original
function returns `0`. The core binding also clamps negative amounts to `0`.

## What This Page Covers

This page is about effect damage and LP recovery performed by scripts. Battle
damage has its own battle flow and events, even though later trigger effects may
listen for `EVENT_DAMAGE`.

LP changes affect players, not cards. That is why LP scripts often store:

- the target player with `Duel.SetTargetPlayer`
- the amount with `Duel.SetTargetParam`
- the announced category with `Duel.SetOperationInfo`
- event-provided damage/recovery values through callback arguments such as `ev`

`Duel.SetTargetPlayer` and `Duel.SetTargetParam` store Chain data that the
operation can read later. `Duel.SetOperationInfo` announces what the Chain Link
intends to do. They are related, but they are not substitutes for each other.

## Pick The Amount Source

Most LP bugs come from using the wrong source for the number.

| Amount source | When to use it | Operation pattern |
| --- | --- | --- |
| Fixed value | The card text names a number such as 500 or 1000. | Store the player/amount, then call `Duel.Damage` or `Duel.Recover`. |
| Current field or hand state | The text cares about what exists at resolution. | Announce the best visible estimate, then recalculate in the operation. |
| Targeted card value | The amount depends on a monster's ATK/DEF/Level. | Target the card, recheck relation and face-up state, then read the current value. |
| Event value | The trigger passes the amount in `ev`. | Use `ev` unless the card text says to recalculate. |
| Event group count | The text counts cards from the triggering event. | Capture/count the event group instead of counting the field later. |
| Actual LP changed | The next action depends on damage/recovery really happening. | Use the return value from `Duel.Damage` or `Duel.Recover`. |

## Pure LP Effects And Activation Checks

A pure fixed LP effect often has a simple legality branch:

```lua
function s.damtg(e,tp,eg,ep,ev,re,r,rp,chk)
    if chk==0 then return true end
    Duel.SetTargetPlayer(1-tp)
    Duel.SetTargetParam(1000)
    Duel.SetOperationInfo(0,CATEGORY_DAMAGE,nil,0,1-tp,1000)
end
```

There is no card target and no destination to prove, so the activation check
does not need a matching-card search. Local `c102380.lua` uses this kind of
shape for a mandatory fixed-damage trigger.

Add real checks when the LP amount or follow-up action depends on something
that must be legal at activation: a target still needs target legality, a
Special Summon needs an open Monster Zone, and a "destroy, then inflict damage"
effect needs the action that comes first to be legal.

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

When the text separates actions into visible steps, local scripts often insert
`Duel.BreakEffect()` between them. Do not use stepped LP changes for a "then"
sequence that should resolve one action first and the next action afterward.

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

Local `c12694768.lua` uses the simultaneous-damage style:

```lua
Duel.Damage(tp,d,REASON_EFFECT,true)
Duel.Damage(1-tp,d,REASON_EFFECT,true)
Duel.RDComplete()
```

Without `Duel.RDComplete()`, a stepped damage/recovery sequence is incomplete.

The stepped batch can also mix damage and recovery. Local `c37169670.lua`
announces both categories, reads the stored operation info, then finishes the
combined batch:

```lua
local ex1,a1,b1,p1,d1=Duel.GetOperationInfo(0,CATEGORY_DAMAGE)
local ex2,a2,b2,p2,d2=Duel.GetOperationInfo(0,CATEGORY_RECOVER)
Duel.Damage(1-tp,d1,REASON_EFFECT,true)
Duel.Recover(tp,d2,REASON_EFFECT,true)
Duel.RDComplete()
```

Use ordinary sequential calls when the card text and local script pattern want
one LP change to fully happen before the next action. Use stepped calls when the
LP changes belong to one combined damage/recovery process and the script
finishes that process with `Duel.RDComplete()`.

## Event Value Amounts

Some trigger effects use the event value `ev`. Local scripts use this when the
amount should match the damage or recovery from the triggering event.

```lua
function s.sptg(e,tp,eg,ep,ev,re,r,rp,chk)
    if chk==0 then
        return Duel.GetLocationCount(tp,LOCATION_MZONE)>0
            and e:GetHandler():IsCanBeSpecialSummoned(e,0,tp,false,false)
    end
    Duel.SetOperationInfo(0,CATEGORY_SPECIAL_SUMMON,e:GetHandler(),1,0,0)
    Duel.SetOperationInfo(0,CATEGORY_RECOVER,nil,0,tp,ev)
end

function s.spop(e,tp,eg,ep,ev,re,r,rp)
    local c=e:GetHandler()
    if c:IsRelateToEffect(e)
        and Duel.SpecialSummon(c,0,tp,tp,false,false,POS_FACEUP)~=0 then
        Duel.Recover(tp,ev,REASON_EFFECT)
    end
end
```

Do not replace `ev` with a current LP difference unless the card text says to
recalculate. The event value is part of the trigger data.

## Conjuncted Effects

When LP change is tied to another action, write the operation in the same order
as the card text.

For "do A, and if you do, inflict damage", check the result of A first.

```lua
if tc:IsRelateToEffect(e)
    and tc:IsType(TYPE_MONSTER)
    and Duel.Destroy(tc,REASON_EFFECT)~=0 then
    local atk=math.floor(tc:GetTextAttack()/2)
    if atk>0 then
        Duel.Damage(1-tp,atk,REASON_EFFECT)
    end
end
```

For "inflict damage, then optionally do B", use the return value of
`Duel.Damage` or `Duel.Recover` when actual LP changed matters.

```lua
local dealt=Duel.Damage(1-tp,500,REASON_EFFECT)
if dealt>0 and Duel.SelectYesNo(tp,aux.Stringid(id,0)) then
    -- follow-up action
end
```

This is different from simply announcing both categories. Categories describe
the Chain Link; return values and operation checks decide whether the later
action may happen.

## Event Count vs Resolution Count

Two similar card texts can need different amounts:

| Text shape | Script source |
| --- | --- |
| "for each card that was..." | Count the triggering event group or use event data. |
| "for each card currently..." | Recount during resolution. |

Event-group amounts should be captured from `eg` or event data before the field
changes. Resolution amounts should be calculated in the operation.

```lua
local ct=eg:FilterCount(s.filter,nil,tp)
e:SetLabel(ct)
```

```lua
local ct=Duel.GetMatchingGroupCount(s.filter,tp,LOCATION_MZONE,0,nil)
Duel.Recover(tp,ct*500,REASON_EFFECT)
```

The first pattern remembers what triggered the effect. The second pattern asks
what is true now.

## Local Scripts To Read

These scripts show the common LP branches in the local script set:

| Script | LP pattern |
| --- | --- |
| `c99518961.lua` | Stores a player at activation, then calculates hand-based damage again during resolution. |
| `c99427357.lua` | Recovers LP from a targeted monster's current ATK after relation and face-up checks. |
| `c13313278.lua` | Uses the event value `ev` as the recovery amount. |
| `c12694768.lua` | Applies simultaneous damage to both players with stepped `Duel.Damage` and `Duel.RDComplete()`. |
| `c37169670.lua` | Reads announced damage/recovery operation info and resolves a mixed stepped batch. |
| `c49407319.lua` | Uses sequential damage and return values to decide whether the follow-up damage happens. |
| `c12950294.lua` | Uses `Duel.BreakEffect()`, then damage return value, then recovery from actual damage dealt. |

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
- [`Duel.SetOperationInfo`](/api/functions/Duel/SetOperationInfo)
- [`Duel.GetOperationInfo`](/api/functions/Duel/GetOperationInfo)
- [`Duel.GetChainInfo`](/api/functions/Duel/GetChainInfo)
- [`Duel.BreakEffect`](/api/functions/Duel/BreakEffect)
