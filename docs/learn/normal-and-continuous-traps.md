# Normal And Continuous Traps

Normal Traps and Continuous Traps use the same card-activation type, but they
do different jobs after activation.

A Normal Trap usually resolves once and leaves by normal Spell/Trap handling. A
Continuous Trap usually has a small activation effect that turns it face-up,
then separate effects that work from `LOCATION_SZONE` while it remains there.

## Normal Trap Activation Flow

Infinite Impermanence (`c10045474.lua`) begins like an ordinary targeted Trap:

```lua
local e1=Effect.CreateEffect(c)
e1:SetCategory(CATEGORY_DISABLE)
e1:SetType(EFFECT_TYPE_ACTIVATE)
e1:SetProperty(EFFECT_FLAG_CARD_TARGET)
e1:SetCode(EVENT_FREE_CHAIN)
e1:SetHintTiming(0,TIMINGS_CHECK_MONSTER)
e1:SetTarget(c10045474.target)
e1:SetOperation(c10045474.activate)
c:RegisterEffect(e1)
```

The target callback checks the target twice: once for manual target checks
through `chkc`, and once for activation legality through `chk==0`.

```lua
function c10045474.target(e,tp,eg,ep,ev,re,r,rp,chk,chkc)
    if chkc then return chkc:IsLocation(LOCATION_MZONE) and chkc:IsControler(1-tp) and aux.NegateMonsterFilter(chkc) end
    if chk==0 then return Duel.IsExistingTarget(aux.NegateMonsterFilter,tp,0,LOCATION_MZONE,1,nil) end
    Duel.Hint(HINT_SELECTMSG,tp,HINTMSG_DISABLE)
    Duel.SelectTarget(tp,aux.NegateMonsterFilter,tp,0,LOCATION_MZONE,1,1,nil)
end
```

Resolution rechecks the target before registering temporary disable effects:

```lua
local tc=Duel.GetFirstTarget()
if tc:IsFaceup() and tc:IsRelateToEffect(e) and tc:IsCanBeDisabledByEffect(e) then
    Duel.NegateRelatedChain(tc,RESET_TURN_SET)
    -- register EFFECT_DISABLE and EFFECT_DISABLE_EFFECT
end
```

That is the basic Normal Trap habit: legal target at activation, current
relation and state at resolution.

## Hand And Set-Turn Exceptions

Trap activation exceptions are separate effects. Infinite Impermanence grants
hand activation with `EFFECT_TRAP_ACT_IN_HAND`:

```lua
local e2=Effect.CreateEffect(c)
e2:SetDescription(aux.Stringid(10045474,0))
e2:SetType(EFFECT_TYPE_SINGLE)
e2:SetCode(EFFECT_TRAP_ACT_IN_HAND)
e2:SetCondition(c10045474.handcon)
c:RegisterEffect(e2)
```

Trap Trick (`c80101899.lua`) Sets a Normal Trap from the Deck, then grants that
newly Set card same-turn activation:

```lua
if tc2 and Duel.SSet(tp,tc2)~=0 then
    local e1=Effect.CreateEffect(c)
    e1:SetDescription(aux.Stringid(80101899,0))
    e1:SetType(EFFECT_TYPE_SINGLE)
    e1:SetCode(EFFECT_TRAP_ACT_IN_SET_TURN)
    e1:SetProperty(EFFECT_FLAG_SET_AVAILABLE)
    e1:SetReset(RESET_EVENT+RESETS_STANDARD)
    tc2:RegisterEffect(e1)
end
```

Do not hide those permissions inside the target callback. The target callback
answers "is this activation legal now?" The exception effect changes the Trap's
activation rule.

## Continuous Trap Face-Up Effects

Cyberdark Invasion (`c1157683.lua`) shows the common Continuous Trap split:

```lua
local e0=Effect.CreateEffect(c)
e0:SetType(EFFECT_TYPE_ACTIVATE)
e0:SetCode(EVENT_FREE_CHAIN)
c:RegisterEffect(e0)

local e1=Effect.CreateEffect(c)
e1:SetDescription(aux.Stringid(1157683,0))
e1:SetType(EFFECT_TYPE_QUICK_O)
e1:SetCode(EVENT_FREE_CHAIN)
e1:SetRange(LOCATION_SZONE)
e1:SetProperty(EFFECT_FLAG_CARD_TARGET)
e1:SetCountLimit(1,EFFECT_COUNT_CODE_SINGLE)
e1:SetHintTiming(0,TIMING_END_PHASE)
e1:SetTarget(c1157683.eqtg)
e1:SetOperation(c1157683.eqop)
c:RegisterEffect(e1)
```

The activation effect only places the Continuous Trap face-up. The Quick Effect
has its own `SetRange(LOCATION_SZONE)`, target, operation, count limit, and
hint timing.

If a Continuous Trap effect has no `SetRange(LOCATION_SZONE)`, it may not be
limited to the face-up Trap in the Spell & Trap Zone. That is one of the most
common Continuous Trap bugs.

## Continuous Effects And Target Ranges

Some Continuous Traps do not activate again; they continuously apply rules.
Mind Scan (`c34298391.lua`) registers field effects while the Trap is in the
Spell & Trap Zone:

```lua
local e2=Effect.CreateEffect(c)
e2:SetType(EFFECT_TYPE_FIELD)
e2:SetCode(EFFECT_PUBLIC)
e2:SetRange(LOCATION_SZONE)
e2:SetCondition(s.picon)
e2:SetTargetRange(0,LOCATION_HAND)
c:RegisterEffect(e2)

local e3=e2:Clone()
e3:SetCode(EFFECT_REVEAL_ONFIELD)
e3:SetTarget(aux.TargetBoolFunction(Card.IsFacedown))
e3:SetTargetRange(0,LOCATION_ONFIELD)
c:RegisterEffect(e3)
```

`SetRange` says where the Trap must be for the effect to apply.
`SetTargetRange` says which cards or players the effect applies to. They answer
different questions, and Continuous Trap scripts often need both.

## Reset Behavior For Temporary Effects

Continuous Traps often create temporary effects after they resolve. Infinite
Impermanence registers column effects that last until the End Phase:

```lua
local e5=Effect.CreateEffect(c)
e5:SetType(EFFECT_TYPE_FIELD+EFFECT_TYPE_CONTINUOUS)
e5:SetCode(EVENT_CHAIN_SOLVING)
e5:SetOperation(c10045474.disop)
e5:SetReset(RESET_PHASE+PHASE_END)
Duel.RegisterEffect(e5,tp)
```

Mind Scan does the same kind of temporary watcher after the player announces a
card name:

```lua
e1:SetType(EFFECT_TYPE_FIELD+EFFECT_TYPE_CONTINUOUS)
e1:SetCode(EVENT_CHAIN_SOLVING)
e1:SetCondition(s.discon)
e1:SetOperation(s.disop)
e1:SetReset(RESET_PHASE+PHASE_END)
Duel.RegisterEffect(e1,tp)
```

Use `RESET_EVENT+RESETS_STANDARD` when an effect is tied to a specific card's
normal lifecycle. Use `RESET_PHASE+PHASE_END` for a temporary rule that expires
at the end of the turn. Many scripts combine these when a temporary effect is
registered directly onto a card.

## Leaving The Field

Continuous Traps that maintain another card often need cleanup in both
directions. Call of the Haunted (`c97077563.lua`) targets and Special Summons a
monster, then sets the monster as the Trap's card target:

```lua
if c:IsRelateToEffect(e) and tc:IsRelateToEffect(e)
    and Duel.SpecialSummonStep(tc,0,tp,tp,false,false,POS_FACEUP_ATTACK) then
    c:SetCardTarget(tc)
end
Duel.SpecialSummonComplete()
```

It then watches two leave-field cases:

```lua
local e3=Effect.CreateEffect(c)
e3:SetType(EFFECT_TYPE_CONTINUOUS+EFFECT_TYPE_SINGLE)
e3:SetCode(EVENT_LEAVE_FIELD)
e3:SetOperation(c97077563.desop)
c:RegisterEffect(e3)

local e4=Effect.CreateEffect(c)
e4:SetType(EFFECT_TYPE_CONTINUOUS+EFFECT_TYPE_FIELD)
e4:SetRange(LOCATION_SZONE)
e4:SetCode(EVENT_LEAVE_FIELD)
e4:SetCondition(c97077563.descon2)
e4:SetOperation(c97077563.desop2)
c:RegisterEffect(e4)
```

One effect destroys the monster if the Trap leaves. The other destroys the Trap
if the monster is destroyed. This pattern is much safer than trying to fold all
of the cleanup into the original activation operation.

## Normal Vs Continuous Trap Checklist

| Question | Normal Trap habit | Continuous Trap habit |
| --- | --- | --- |
| What does activation do? | Select targets and resolve a one-time action. | Usually just turns the Trap face-up, or starts a relationship. |
| Where does lasting behavior live? | Temporary effects registered during resolution. | Separate effects with `SetRange(LOCATION_SZONE)`. |
| Does it need `SetTargetRange`? | Only for registered field effects. | Often, for field-wide rules from the face-up Trap. |
| Does it need leave-field cleanup? | Usually no. | Often yes, especially if it holds a monster or creates a lasting link. |
| Does it activate from hand or this turn Set? | Only with a separate exception effect. | Same rule; use the matching exception effect. |

## Common Pitfalls

| Mistake | Better pattern |
| --- | --- |
| Putting a Continuous Trap's later Quick Effect inside its activation effect. | Register a small activation effect, then a separate `LOCATION_SZONE` effect. |
| Forgetting `SetRange(LOCATION_SZONE)`. | Add it to face-up Continuous Trap effects. |
| Using `SetRange` instead of `SetTargetRange`. | Use `SetRange` for where the source must be; use `SetTargetRange` for what it affects. |
| Granting hand activation in the target callback. | Register `EFFECT_TRAP_ACT_IN_HAND` with a condition. |
| Setting a Trap and assuming it can activate immediately. | Register `EFFECT_TRAP_ACT_IN_SET_TURN` only when allowed. |
| Forgetting leave-field cleanup. | Add event watchers for the Trap leaving, the linked card leaving, or both. |
| Registering temporary effects with no reset. | Use phase, event, or standard resets that match the card text. |

## Useful API Pages

- [`Effect.SetType`](/api/functions/Effect/SetType)
- [`Effect.SetCode`](/api/functions/Effect/SetCode)
- [`Effect.SetRange`](/api/functions/Effect/SetRange)
- [`Effect.SetTargetRange`](/api/functions/Effect/SetTargetRange)
- [`Effect.SetReset`](/api/functions/Effect/SetReset)
- [`Effect.SetCountLimit`](/api/functions/Effect/SetCountLimit)
- [`Effect.SetHintTiming`](/api/functions/Effect/SetHintTiming)
- [`Duel.IsExistingTarget`](/api/functions/Duel/IsExistingTarget)
- [`Duel.SelectTarget`](/api/functions/Duel/SelectTarget)
- [`Duel.SSet`](/api/functions/Duel/SSet)
- [`Duel.RegisterEffect`](/api/functions/Duel/RegisterEffect)
- [`Duel.SpecialSummonStep`](/api/functions/Duel/SpecialSummonStep)
- [`Duel.SpecialSummonComplete`](/api/functions/Duel/SpecialSummonComplete)
- [`Card.SetCardTarget`](/api/functions/Card/SetCardTarget)
- [`Card.GetFirstCardTarget`](/api/functions/Card/GetFirstCardTarget)
- [`Card.IsRelateToEffect`](/api/functions/Card/IsRelateToEffect)

Related lessons:

- [Trap Card Patterns](trap-card-patterns)
- [Continuous effects](continuous-effects)
- [Reset Flags And Effect Duration](reset-flags-and-duration)
- [Targeting flow](targeting-flow)
- [Common Script Errors And Debugging](common-script-errors-and-debugging)
