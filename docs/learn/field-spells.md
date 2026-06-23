# Field Spells

Field Spells are Spell Cards that live in the Field Zone. Their scripts usually
combine a simple activation effect with always-on, triggered, or activated
effects that only work while the card remains in `LOCATION_FZONE`.

## Basic Field Spell Shape

Many Field Spells have a normal activation effect and then separate effects
registered on the same card.

```lua
local e1=Effect.CreateEffect(c)
e1:SetType(EFFECT_TYPE_ACTIVATE)
e1:SetCode(EVENT_FREE_CHAIN)
c:RegisterEffect(e1)

local e2=Effect.CreateEffect(c)
e2:SetDescription(aux.Stringid(id,0))
e2:SetType(EFFECT_TYPE_IGNITION)
e2:SetRange(LOCATION_FZONE)
e2:SetCountLimit(1,id)
e2:SetTarget(s.target)
e2:SetOperation(s.operation)
c:RegisterEffect(e2)
```

The activation effect puts the Field Spell onto the field. The second effect is
usable later because `SetRange(LOCATION_FZONE)` says the handler must be in the
Field Zone.

## Field Zone vs Spell & Trap Zone

Use `LOCATION_FZONE` when the script means the Field Zone as a concept:

```lua
e2:SetRange(LOCATION_FZONE)
local fc=Duel.GetFieldCard(tp,LOCATION_FZONE,0)
```

The local core stores the Field Zone inside Spell & Trap Zone internals, and
the define file notes that a Field Spell can appear as Spell & Trap Zone
sequence `5`. You will see older or lower-level local scripts use:

```lua
local fc=Duel.GetFieldCard(tp,LOCATION_SZONE,5)
```

Prefer `LOCATION_FZONE` in learning code unless you are doing raw sequence or
zone-mask work. See [Field zones and sequences](field-zones-and-sequences) for
the sequence details.

## Effects While In The Field Zone

Field Spells can provide continuous field effects, trigger effects, and
activated effects.

```lua
local e1=Effect.CreateEffect(c)
e1:SetType(EFFECT_TYPE_FIELD)
e1:SetCode(EFFECT_UPDATE_ATTACK)
e1:SetRange(LOCATION_FZONE)
e1:SetTargetRange(LOCATION_MZONE,LOCATION_MZONE)
e1:SetTarget(s.atktg)
e1:SetValue(300)
c:RegisterEffect(e1)
```

```lua
local e2=Effect.CreateEffect(c)
e2:SetType(EFFECT_TYPE_FIELD+EFFECT_TYPE_TRIGGER_O)
e2:SetCode(EVENT_PHASE+PHASE_END)
e2:SetRange(LOCATION_FZONE)
e2:SetTarget(s.target)
e2:SetOperation(s.operation)
c:RegisterEffect(e2)
```

Local `c1003840.lua` is a compact example: its activation effect is plain, then
it registers an Ignition Effect and a field Trigger Effect with
`SetRange(LOCATION_FZONE)`.

## Activating Or Placing A Field Spell From The Deck

Some card effects place or activate a Field Spell from the Deck. Local scripts
usually check the candidate's own activation effect before moving it:

```lua
function s.actfilter(c,tp)
    local te=c:GetActivateEffect()
    return c:IsType(TYPE_FIELD) and te and te:IsActivatable(tp,true,true)
end
```

During resolution, the common local pattern is:

```lua
local tc=Duel.SelectMatchingCard(tp,s.actfilter,tp,LOCATION_DECK,0,1,1,nil,tp):GetFirst()
if tc then
    local fc=Duel.GetFieldCard(tp,LOCATION_FZONE,0)
    if fc then
        Duel.SendtoGrave(fc,REASON_RULE)
        Duel.BreakEffect()
    end
    local te=tc:GetActivateEffect()
    if Duel.MoveToField(tc,tp,tp,LOCATION_FZONE,POS_FACEUP,true) then
        te:UseCountLimit(tp,1,true)
        local tep=tc:GetControler()
        local cost=te:GetCost()
        if cost then cost(te,tep,eg,ep,ev,re,r,rp,1) end
        Duel.RaiseEvent(tc,4179255,te,0,tp,tp,Duel.GetCurrentChain())
    end
end
```

This shape is visible in local Dream Mirror scripts such as `c1050355.lua`.
Treat it as an advanced pattern to copy from a matching local script: the
important beginner ideas are that the Field Spell's activation effect must be
activatable, the existing Field Spell is handled by rule, and
`Duel.MoveToField` uses `LOCATION_FZONE`. The numeric event in this pattern is
part of existing local card-script handling for activating a Spell/Trap through
another effect; do not invent a new number for beginner scripts.

## Replacing The Existing Field Spell

When an effect puts a Field Spell into the Field Zone, the previous Field Spell
may need to leave first. Local scripts often do this explicitly so the timing is
clear and a `Duel.BreakEffect()` can separate the actions:

```lua
local fc=Duel.GetFieldCard(tp,LOCATION_FZONE,0)
if fc then
    Duel.SendtoGrave(fc,REASON_RULE)
    Duel.BreakEffect()
end
Duel.MoveToField(tc,tp,tp,LOCATION_FZONE,POS_FACEUP,true)
```

The local core also treats `Duel.MoveToField(..., LOCATION_FZONE, ...)` as a
Field Zone placement and maps it to the correct Spell & Trap Zone slot
internally.

## Checking The Current Environment

Use `Duel.IsEnvironment` when a card cares whether a specific field or
environment code is active.

```lua
if Duel.IsEnvironment(41418852,tp,LOCATION_FZONE) then
    -- Numeron Network is active in this player's Field Zone
end
```

The generated API page notes that the core checks face-up Field Zone cards
first and can also match `EFFECT_CHANGE_ENVIRONMENT` state. Use
`Duel.GetFieldCard` instead when you need the actual card object in the Field
Zone.

## Field Spells With Counters

Field Spells can permit and use counters like other cards.

```lua
function s.initial_effect(c)
    c:EnableCounterPermit(0x6e)
    -- effects
end
```

Local `c97254001.lua` stores counters on a Field Spell, moves another Field
Spell into the Field Zone, then transfers counters if the new card can hold
them. That pattern combines Field Zone replacement with counter scripting, so
keep the two concerns separate when reading it.

## Common Pitfalls

| Mistake | Safer pattern |
| --- | --- |
| Registering later Field Spell effects with `SetRange(LOCATION_SZONE)`. | Use `LOCATION_FZONE` unless you are deliberately writing raw Spell & Trap Zone sequence logic. |
| Placing a Field Spell from the Deck without checking its activation effect. | Use `c:GetActivateEffect()` and `te:IsActivatable(...)` before moving it. |
| Forgetting the existing Field Spell. | Read it with `Duel.GetFieldCard(tp,LOCATION_FZONE,0)` and send it by rule when the local pattern requires explicit replacement. |
| Treating a Field Spell like an Equip Card. | Field Spells do not use `Duel.Equip` or `EFFECT_EQUIP_LIMIT`; they are Field Zone cards with effects in `LOCATION_FZONE`. |
| Using raw sequence `5` everywhere. | Prefer `LOCATION_FZONE`; reserve sequence `5` for zone/sequence lessons. |

Useful API pages:

- [`Duel.MoveToField`](/api/functions/Duel/MoveToField)
- [`Duel.GetFieldCard`](/api/functions/Duel/GetFieldCard)
- [`Duel.IsEnvironment`](/api/functions/Duel/IsEnvironment)
- [`Duel.SendtoGrave`](/api/functions/Duel/SendtoGrave)
- [`Duel.BreakEffect`](/api/functions/Duel/BreakEffect)
- [`Duel.RaiseEvent`](/api/functions/Duel/RaiseEvent)
- [`Duel.GetCurrentChain`](/api/functions/Duel/GetCurrentChain)
- [`Card.GetActivateEffect`](/api/functions/Card/GetActivateEffect)
- [`Effect.UseCountLimit`](/api/functions/Effect/UseCountLimit)
- [`Effect.GetCost`](/api/functions/Effect/GetCost)
- [`Effect.SetRange`](/api/functions/Effect/SetRange)
- [`Effect.SetTargetRange`](/api/functions/Effect/SetTargetRange)
- [`Effect.SetValue`](/api/functions/Effect/SetValue)
