# Gemini Monsters

Gemini Monsters are written with the official word "Gemini", but the local
MDPro3/YGOPro constants and helpers still use the older "Dual" names. That is
why scripts check `TYPE_DUAL`, register `EFFECT_DUAL_SUMMONABLE`, and test
`SUMMON_TYPE_DUAL`.

The important gameplay split is simple:

| State | Script meaning |
| --- | --- |
| Not in Dual State | The monster is treated as a Normal Monster while face-up in the Monster Zone or in the GY. |
| In Dual State | The monster has gained its Gemini effects. |

Use official wording when explaining cards, but use the local constants when
writing scripts. There is no local `TYPE_GEMINI` constant.

## The Standard Setup

Most Gemini Monsters begin with
[`aux.EnableDualAttribute`](/api/functions/Auxiliary/EnableDualAttribute):

```lua
function s.initial_effect(c)
    aux.EnableDualAttribute(c)

    local e1=Effect.CreateEffect(c)
    e1:SetType(EFFECT_TYPE_IGNITION)
    e1:SetRange(LOCATION_MZONE)
    e1:SetCondition(aux.IsDualState)
    e1:SetTarget(s.target)
    e1:SetOperation(s.operation)
    c:RegisterEffect(e1)
end
```

The helper registers the standard local Gemini package:

| Helper piece | What it does |
| --- | --- |
| `EFFECT_DUAL_SUMMONABLE` | Allows the core to offer the face-up monster as a Normal Summon target again. |
| `EFFECT_ADD_TYPE` with `TYPE_NORMAL` | Treats the monster as Normal while it is not in Dual State. |
| `EFFECT_REMOVE_TYPE` with `TYPE_EFFECT` | Removes Effect Monster type while it is not in Dual State. |

Local `procedure.lua` applies those type changes in
`LOCATION_MZONE+LOCATION_GRAVE`, and only while the monster is face-up and not
already in Dual State.

Gemini Soldier (`c68366996.lua`) is a clean local example: it calls
`aux.EnableDualAttribute(c)` first, then gives the monster battle protection and
a Deck Special Summon trigger only while `aux.IsDualState` is true.

## Reading Dual State

There are two common checks:

| Check | Use it when |
| --- | --- |
| [`aux.IsDualState`](/api/functions/Auxiliary/IsDualState) | You need an Effect condition for the handler. It also checks that the handler is not disabled. |
| [`Card.IsDualState`](/api/functions/Card/IsDualState) | You are filtering or inspecting a Card object directly. |

Effects that only work after the monster has gained its Gemini effects usually
use the helper directly:

```lua
local e1=Effect.CreateEffect(c)
e1:SetType(EFFECT_TYPE_SINGLE)
e1:SetProperty(EFFECT_FLAG_SINGLE_RANGE)
e1:SetRange(LOCATION_MZONE)
e1:SetCode(EFFECT_INDESTRUCTABLE_COUNT)
e1:SetCondition(aux.IsDualState)
e1:SetCountLimit(1)
e1:SetValue(s.indval)
c:RegisterEffect(e1)
```

For filters, check the Card object:

```lua
function s.gemini_filter(c)
    return c:IsFaceup() and c:IsType(TYPE_DUAL) and not c:IsDualState()
end
```

Gemini Booster (`c18096222.lua`) uses that shape before calling
[`Card.EnableDualState`](/api/functions/Card/EnableDualState) on the selected
monster.

## Making A Gemini Gain Its Effects

Normal Summoning a face-up Gemini Monster again is handled by the core when the
card has `EFFECT_DUAL_SUMMONABLE` and is not already affected by
`EFFECT_DUAL_STATUS`. The resulting Summon type is `SUMMON_TYPE_DUAL`.

Some card effects say that a Gemini Monster is treated as having been Normal
Summoned again. Those scripts do not perform a Normal Summon. They apply the
state directly:

```lua
function s.operation(e,tp,eg,ep,ev,re,r,rp)
    local tc=Duel.GetFirstTarget()
    if tc and tc:IsRelateToEffect(e) then
        tc:EnableDualState()
    end
end
```

Gemini Ablation (`c80758812.lua`) shows the safer version for a monster Special
Summoned during resolution:

```lua
local tc=g:GetFirst()
if tc and Duel.SpecialSummonStep(tc,0,tp,tp,false,false,POS_FACEUP) then
    tc:EnableDualState()
end
Duel.SpecialSummonComplete()
```

[`Card.EnableDualState`](/api/functions/Card/EnableDualState) registers
`EFFECT_DUAL_STATUS` with a client hint. It does not Summon the monster, spend
a Normal Summon, or make a Chain Link by itself. Use it only when the card text
really grants the gained-effect state.

## Checking For A Gemini Summon

If a card cares that a monster was Normal Summoned again as a Gemini Monster,
check the Summon type:

```lua
function s.sumcon(e,tp,eg,ep,ev,re,r,rp)
    return e:GetHandler():IsSummonType(SUMMON_TYPE_DUAL)
end
```

Use [`Card.IsSummonType`](/api/functions/Card/IsSummonType) for that question.
Do not infer Gemini Summon history from `IsDualState()` alone. A card effect
can enable Dual State without performing a Summon, and a monster can lose or
reset effects later.

## Searching Gemini Cards And Support

Use `TYPE_DUAL` for actual Gemini Monsters:

```lua
function s.spfilter(c,e,tp)
    return c:IsType(TYPE_DUAL)
        and c:IsCanBeSpecialSummoned(e,0,tp,false,false)
end
```

Support Spells and Traps that mention Gemini Monsters can mark their text type
for local search helpers:

```lua
s.has_text_type=TYPE_DUAL

function s.thfilter(c)
    return c:IsType(TYPE_SPELL+TYPE_TRAP)
        and aux.IsTypeInText(c,TYPE_DUAL)
        and c:IsAbleToHand()
end
```

Geminize Lord Golknight (`c72305034.lua`) uses
[`aux.IsTypeInText`](/api/functions/Auxiliary/IsTypeInText) this way when it
searches Gemini-related Spell/Trap Cards.

## Common Mistakes

| Mistake | Better pattern |
| --- | --- |
| Using `TYPE_GEMINI`. | Use local `TYPE_DUAL`. |
| Forgetting `aux.EnableDualAttribute(c)`. | Register it before the monster's Gemini-only effects. |
| Checking only `c:IsDualState()` in an Effect condition. | Use `aux.IsDualState` so disabled handlers do not keep applying Gemini-only effects. |
| Assuming Special Summon makes a Gemini Monster gain its effects. | It stays not in Dual State unless the script calls `EnableDualState()` or it is Normal Summoned again. |
| Treating `EnableDualState()` as a Summon. | It only applies `EFFECT_DUAL_STATUS`; it does not spend or create a Normal Summon. |

The mental model is: `TYPE_DUAL` finds the subtype, `aux.EnableDualAttribute`
gives the card the local Gemini rules, and Dual State decides whether its
Gemini effects are live.
