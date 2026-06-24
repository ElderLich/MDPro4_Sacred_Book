# Trap Card Patterns

Trap Cards share the same card-activation effect shape as Spells, but their
timing rules are different. Normal Traps and Continuous Traps activate at Spell
Speed 2. Counter Traps activate at Spell Speed 3.

In script terms, all of those card activations still use
`EFFECT_TYPE_ACTIVATE`; the Trap's card type decides the activation speed.

## The Shared Trap Activation Shape

```lua
local e1=Effect.CreateEffect(c)
e1:SetCategory(CATEGORY_DISABLE)
e1:SetType(EFFECT_TYPE_ACTIVATE)
e1:SetProperty(EFFECT_FLAG_CARD_TARGET)
e1:SetCode(EVENT_FREE_CHAIN)
e1:SetTarget(s.target)
e1:SetOperation(s.activate)
c:RegisterEffect(e1)
```

Local core behavior treats `TYPE_TRAP` activations as Spell Speed 2 and
`TYPE_COUNTER` activations as Spell Speed 3. It also checks whether a Trap is
being activated from the hand or during the turn it was Set.

Those exceptions are not written into the activation effect itself. They are
usually granted as separate single effects:

| Exception | Common effect code |
| --- | --- |
| Activate a Trap from the hand | `EFFECT_TRAP_ACT_IN_HAND` |
| Activate a Trap during the turn it was Set | `EFFECT_TRAP_ACT_IN_SET_TURN` |

## Normal Traps

A Normal Trap often looks like a Quick-Play Spell from the callback point of
view: target branch, operation branch, relation checks, and optional hint
timing.

Infinite Impermanence (`c10045474.lua`) uses a normal activation effect and a
separate hand-activation permission:

```lua
local e1=Effect.CreateEffect(c)
e1:SetCategory(CATEGORY_DISABLE)
e1:SetType(EFFECT_TYPE_ACTIVATE)
e1:SetProperty(EFFECT_FLAG_CARD_TARGET)
e1:SetCode(EVENT_FREE_CHAIN)
e1:SetHintTiming(0,TIMINGS_CHECK_MONSTER)
e1:SetTarget(s.target)
e1:SetOperation(s.activate)
c:RegisterEffect(e1)

local e2=Effect.CreateEffect(c)
e2:SetType(EFFECT_TYPE_SINGLE)
e2:SetCode(EFFECT_TRAP_ACT_IN_HAND)
e2:SetCondition(s.handcon)
c:RegisterEffect(e2)
```

The activation target still follows ordinary targeting rules:

```lua
function s.target(e,tp,eg,ep,ev,re,r,rp,chk,chkc)
    if chkc then
        return chkc:IsLocation(LOCATION_MZONE)
            and chkc:IsControler(1-tp)
            and aux.NegateMonsterFilter(chkc)
    end
    if chk==0 then
        return Duel.IsExistingTarget(aux.NegateMonsterFilter,tp,0,LOCATION_MZONE,1,nil)
    end
    Duel.Hint(HINT_SELECTMSG,tp,HINTMSG_DISABLE)
    Duel.SelectTarget(tp,aux.NegateMonsterFilter,tp,0,LOCATION_MZONE,1,1,nil)
end
```

Trap Trick (`c80101899.lua`) shows the Set-from-Deck pattern. It checks
`IsSSetable`, Sets the matching Trap, then grants that Set card
`EFFECT_TRAP_ACT_IN_SET_TURN`.

```lua
function s.setfilter(c,code)
    return c:IsCode(code) and c:IsSSetable()
end

if tc2 and Duel.SSet(tp,tc2)~=0 then
    local e1=Effect.CreateEffect(c)
    e1:SetType(EFFECT_TYPE_SINGLE)
    e1:SetCode(EFFECT_TRAP_ACT_IN_SET_TURN)
    e1:SetProperty(EFFECT_FLAG_SET_AVAILABLE)
    e1:SetReset(RESET_EVENT+RESETS_STANDARD)
    tc2:RegisterEffect(e1)
end
```

This is a good example of separating the movement action from the later
activation exception. `Duel.SSet` places the card; the single effect changes
when the newly Set Trap may be activated.

## Continuous Traps

A Continuous Trap usually has a small activation effect, then separate effects
that work while the card remains face-up in the Spell & Trap Zone.

```lua
local e0=Effect.CreateEffect(c)
e0:SetType(EFFECT_TYPE_ACTIVATE)
e0:SetCode(EVENT_FREE_CHAIN)
c:RegisterEffect(e0)

local e1=Effect.CreateEffect(c)
e1:SetDescription(aux.Stringid(id,0))
e1:SetType(EFFECT_TYPE_QUICK_O)
e1:SetCode(EVENT_FREE_CHAIN)
e1:SetRange(LOCATION_SZONE)
e1:SetCountLimit(1,EFFECT_COUNT_CODE_SINGLE)
e1:SetHintTiming(0,TIMING_END_PHASE)
e1:SetTarget(s.target)
e1:SetOperation(s.operation)
c:RegisterEffect(e1)
```

Cyberdark Invasion (`c1157683.lua`) uses this structure: one activation effect
places the Continuous Trap face-up, then two Quick Effects are registered with
`SetRange(LOCATION_SZONE)`.

Mind Scan (`c34298391.lua`) is a newer Continuous Trap example with a different
shape: it has a small activation effect, a continuous hand-reveal effect, a
continuous Set-card inspection effect using `EFFECT_REVEAL_ONFIELD`, and a
separate once-per-turn Quick Effect. See the
[Mind Scan case study](/examples/mind-scan) for the full pattern.

For Continuous Traps, `EFFECT_TYPE_ACTIVATE` is not the same thing as the
card's later face-up effects. The activation effect gets the card onto the
field. The later effects describe what the face-up Trap can do.

## Counter Traps

Counter Traps still register `EFFECT_TYPE_ACTIVATE`, but `TYPE_COUNTER` makes
their activation Spell Speed 3 in the local core.

Chaos Trap Hole (`c11593137.lua`) is a compact local summon-negation pattern:

```lua
local e1=Effect.CreateEffect(c)
e1:SetCategory(CATEGORY_DISABLE_SUMMON+CATEGORY_REMOVE)
e1:SetType(EFFECT_TYPE_ACTIVATE)
e1:SetCode(EVENT_SUMMON)
e1:SetCondition(s.condition)
e1:SetCost(s.cost)
e1:SetTarget(s.target)
e1:SetOperation(s.activate)
c:RegisterEffect(e1)

local e2=e1:Clone()
e2:SetCode(EVENT_FLIP_SUMMON)
c:RegisterEffect(e2)

local e3=e1:Clone()
e3:SetCode(EVENT_SPSUMMON)
c:RegisterEffect(e3)
```

The operation negates the Summon, then banishes the Summoned monster:

```lua
function s.activate(e,tp,eg,ep,ev,re,r,rp)
    local g=eg:Filter(s.filter,nil)
    Duel.NegateSummon(g)
    Duel.Remove(g,POS_FACEUP,REASON_EFFECT)
end
```

Counter Traps that negate card or effect activations usually listen to
`EVENT_CHAINING`, check the Chain Link with `Duel.IsChainNegatable(ev)`, then
call `Duel.NegateActivation(ev)` during resolution.

Do not use `Duel.NegateSummon` for Chain Link negation. Summon negation and
activation negation are different timing families.

## Trap Cards Leaving Or Staying

Normal Traps and other non-continuous Spell/Trap Cards activated on the field
are normally confirmed to go to the GY after their Chain handling. The generated
API page for `Card.CancelToGrave` documents the local helper used by scripts
that need to keep such a card on the field or make a replacement pattern work.

Most Trap scripts do not call `CancelToGrave`. Use it only when a matching
local script pattern needs to override the normal post-activation destination.

## Common Pitfalls

| Mistake | Safer pattern |
| --- | --- |
| Writing a Counter Trap as `EFFECT_TYPE_QUICK_O`. | Use `EFFECT_TYPE_ACTIVATE`; `TYPE_COUNTER` gives the card activation Spell Speed 3. |
| Putting Continuous Trap effects inside the activation effect. | Register a small activation effect, then separate `LOCATION_SZONE` effects. |
| Setting a Trap from the Deck and assuming it can activate immediately. | Grant `EFFECT_TRAP_ACT_IN_SET_TURN` only when the card text allows it. |
| Letting a Trap activate from the hand by target logic alone. | Add an `EFFECT_TRAP_ACT_IN_HAND` single effect with its own condition. |
| Using `Duel.NegateSummon` to answer an activated effect. | Use `Duel.NegateActivation` for Chain Link activation negation. |

Useful API pages:

- [`Effect.SetType`](/api/functions/Effect/SetType)
- [`Effect.SetCode`](/api/functions/Effect/SetCode)
- [`Effect.SetHintTiming`](/api/functions/Effect/SetHintTiming)
- [`Card.IsSSetable`](/api/functions/Card/IsSSetable)
- [`Card.CancelToGrave`](/api/functions/Card/CancelToGrave)
- [`Duel.SSet`](/api/functions/Duel/SSet)
- [`Duel.NegateSummon`](/api/functions/Duel/NegateSummon)
- [`Duel.NegateActivation`](/api/functions/Duel/NegateActivation)
- [`Duel.IsChainNegatable`](/api/functions/Duel/IsChainNegatable)
- [`Effect.GetActiveType`](/api/functions/Effect/GetActiveType)
