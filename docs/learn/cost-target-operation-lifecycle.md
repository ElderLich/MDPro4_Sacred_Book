# Cost, Target, And Operation Lifecycle

Activated effects usually move through the same script lifecycle: check whether
the effect is legal, pay costs and record activation data, then resolve later
against the current game state.

The important habit is to keep each callback honest. A check branch answers
"can this happen?" A real activation branch spends costs, selects targets, and
stores data. The operation performs the effect after the Chain reaches that
Link.

## Reading Card Text Into Callbacks

Modern card text gives useful punctuation clues:

| Text part | Script home |
| --- | --- |
| Before a colon `:` | activation condition, timing condition, or other explicit requirement |
| Before a semicolon `;` | activation-time procedure, usually cost payment or target selection |
| After the semicolon, or after the colon when there is no semicolon | resolution, usually the operation callback |

This punctuation is a guide, not a substitute for legality checks. The script
still has to check implicit requirements such as available Monster Zones,
whether a card can be added to the hand, whether a target can be affected, or
whether a mandatory part of an optional effect can be attempted.

## Callback Timeline

For a typical activated effect, scripts are written around this sequence:

1. `condition` answers timing and event requirements.
2. `cost` with `chk==0` answers whether the cost can be paid.
3. `target` with `chk==0` answers whether the activation has a legal outcome.
4. The real `cost` branch pays the cost.
5. The real `target` branch selects targets, records target player/param data,
   labels, and operation info.
6. `operation` resolves later and re-checks anything that can change.

Do not move cards, pay LP, remove Xyz Materials, or choose hidden information in
the `chk==0` branch. The engine may call that branch while only testing whether
the effect is available.

## Activation Restrictions Belong With The Activation

If an effect says the player cannot do something for the rest of the turn after
activation, the check and the restriction often live in the cost callback. The
local Red-Eyes Fusion script (`c6172122.lua`) checks whether the player has
already Summoned, then registers the restriction only when the effect is really
activated:

```lua
function c6172122.cost(e,tp,eg,ep,ev,re,r,rp,chk)
    if chk==0 then
        return Duel.GetActivityCount(tp,ACTIVITY_SUMMON)==0
            and Duel.GetActivityCount(tp,ACTIVITY_SPSUMMON)==0
    end
    local e1=Effect.CreateEffect(e:GetHandler())
    e1:SetType(EFFECT_TYPE_FIELD)
    e1:SetCode(EFFECT_CANNOT_SUMMON)
    e1:SetProperty(EFFECT_FLAG_PLAYER_TARGET+EFFECT_FLAG_OATH)
    e1:SetTargetRange(1,0)
    e1:SetReset(RESET_PHASE+PHASE_END)
    Duel.RegisterEffect(e1,tp)
end
```

The important split is the same as an LP cost: check first, apply later. The
restriction is a real effect registered to the player, so creating it during
`chk==0` would leak a restriction from a mere legality probe.

## Cost Can Store Resolution Data

A cost can store an integer label when the amount paid matters later. The
Winged Dragon of Ra (`10000010`) checks whether the player can pay LP, then the
real cost branch stores the paid amount and pays it:

```lua
function c10000010.atkcost(e,tp,eg,ep,ev,re,r,rp,chk)
    local lp=Duel.GetLP(tp)
    if chk==0 then return Duel.CheckLPCost(tp,lp-100,true) end
    e:SetLabel(lp-100)
    Duel.PayLPCost(tp,lp-100,true)
end

function c10000010.atkop(e,tp,eg,ep,ev,re,r,rp)
    local c=e:GetHandler()
    if c:IsFaceup() and c:IsRelateToEffect(e) then
        local e1=Effect.CreateEffect(c)
        e1:SetType(EFFECT_TYPE_SINGLE)
        e1:SetProperty(EFFECT_FLAG_SINGLE_RANGE)
        e1:SetRange(LOCATION_MZONE)
        e1:SetCode(EFFECT_UPDATE_ATTACK)
        e1:SetValue(e:GetLabel())
        e1:SetReset(RESET_EVENT+RESETS_STANDARD+RESET_DISABLE)
        c:RegisterEffect(e1)
    end
end
```

`Duel.CheckLPCost` is the read-side helper. `Duel.PayLPCost` belongs in the
real cost branch because it actually schedules the payment.

## Target Branches Can Store Choices

The target callback is often where a player chooses a mode. `c10000030.lua`
checks two possible outcomes, asks the player which one to use, stores the
choice in `e:SetLabel(op)`, then the operation reads `e:GetLabel()`:

```lua
function c10000030.target1(e,tp,eg,ep,ev,re,r,rp,chk,chkc)
    local b1=Duel.IsExistingTarget(c10000030.filter1,tp,0,LOCATION_MZONE,1,nil)
    local b2=Duel.GetLocationCount(tp,LOCATION_MZONE)>0
        and Duel.IsExistingTarget(c10000030.filter2,tp,0,LOCATION_GRAVE,1,nil,e,tp)
    if chk==0 then return b1 or b2 end
    local op=0
    if b1 and b2 then
        op=Duel.SelectOption(tp,aux.Stringid(10000030,1),aux.Stringid(10000030,2))
    elseif b1 then
        op=Duel.SelectOption(tp,aux.Stringid(10000030,1))
    else
        op=Duel.SelectOption(tp,aux.Stringid(10000030,2))+1
    end
    e:SetLabel(op)
    if op==0 then
        e:SetCategory(CATEGORY_CONTROL)
        Duel.SelectTarget(tp,c10000030.filter1,tp,0,LOCATION_MZONE,1,1,nil)
    else
        e:SetCategory(CATEGORY_SPECIAL_SUMMON)
        Duel.SelectTarget(tp,c10000030.filter2,tp,0,LOCATION_GRAVE,1,1,nil,e,tp)
    end
end

function c10000030.operation1(e,tp,eg,ep,ev,re,r,rp)
    local tc=Duel.GetFirstTarget()
    if e:GetLabel()==0 then
        if tc:IsRelateToEffect(e) then
            Duel.GetControl(tc,tp,PHASE_END,1)
        end
    else
        if tc:IsRelateToEffect(e) then
            Duel.SpecialSummon(tc,0,tp,tp,false,false,POS_FACEUP)
        end
    end
end
```

The operation still checks `tc:IsRelateToEffect(e)`. A stored label remembers
which branch was chosen; it does not prove the target is still usable.

## Target Player And Param

For player-targeted effects, the target callback records the player and amount,
then the operation reads them back from the current Chain. `c10040267.lua` uses
this pattern for effect damage:

```lua
function c10040267.damtg(e,tp,eg,ep,ev,re,r,rp,chk)
    if chk==0 then return true end
    Duel.SetTargetPlayer(1-tp)
    Duel.SetTargetParam(600)
    Duel.SetOperationInfo(0,CATEGORY_DAMAGE,nil,0,1-tp,600)
end

function c10040267.damop(e,tp,eg,ep,ev,re,r,rp)
    local p,d=Duel.GetChainInfo(0,CHAININFO_TARGET_PLAYER,CHAININFO_TARGET_PARAM)
    Duel.Damage(p,d,REASON_EFFECT)
end
```

Use `SetTargetPlayer` and `SetTargetParam` for small Chain-scoped values such
as a player, damage amount, recovery amount, or draw count. Use an effect label
when the data belongs to the effect object rather than to the Chain target
fields.

## Resolution Rechecks

Operation callbacks run after both players had a chance to respond. The field
may no longer match the activation check.

| Activation data | Resolution habit |
| --- | --- |
| A targeted card | Read with `Duel.GetFirstTarget()` or target Group helpers, then check relation. |
| A selected mode | Read `e:GetLabel()` and still re-check cards/zones before acting. |
| Target player/param | Read `Duel.GetChainInfo(0,CHAININFO_TARGET_PLAYER,CHAININFO_TARGET_PARAM)`. |
| A Special Summon outcome | Check zone count and summon legality again if the script can fail gracefully. |
| A card in the handler's location | Check `c:IsRelateToEffect(e)` or the needed location/face-up state. |

## Common Mistakes

Do not pay cost in `chk==0`. For LP, use `Duel.CheckLPCost` first and
`Duel.PayLPCost` only when `chk` is not 0.

Do not select targets in the check branch. Use `Duel.IsExistingTarget` for the
check and `Duel.SelectTarget` for the real activation branch.

Do not assume operation data is still valid. Labels, target player fields, and
operation info remember what was chosen; resolution still needs current-state
checks before moving cards or applying effects.

Relevant API pages:

- [`Effect.SetCost`](/api/functions/Effect/SetCost)
- [`Effect.SetTarget`](/api/functions/Effect/SetTarget)
- [`Effect.SetOperation`](/api/functions/Effect/SetOperation)
- [`Duel.CheckLPCost`](/api/functions/Duel/CheckLPCost)
- [`Duel.PayLPCost`](/api/functions/Duel/PayLPCost)
- [`Duel.SetTargetPlayer`](/api/functions/Duel/SetTargetPlayer)
- [`Duel.SetTargetParam`](/api/functions/Duel/SetTargetParam)
- [`Duel.GetChainInfo`](/api/functions/Duel/GetChainInfo)
- [`Duel.GetActivityCount`](/api/functions/Duel/GetActivityCount)
- [`Duel.RegisterEffect`](/api/functions/Duel/RegisterEffect)
