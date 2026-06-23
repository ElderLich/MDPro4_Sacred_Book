# Tribute Summon Materials

Tribute Summon scripts sit between ordinary Normal Summons and effect
resolution. The engine asks how many Tributes the monster needs, gathers cards
that can be Tributed, gives some of those cards a Tribute value, then releases
the selected material cards with `REASON_SUMMON+REASON_MATERIAL`.

This page focuses on cards that are treated as multiple Tributes, such as
Egyptian God Slime, and the nearby mechanics that often appear in the same
scripts.

## Where This Fits

| Need | Common tool |
| --- | --- |
| A card counts as 2 Tributes for certain Tribute Summons | `EFFECT_DOUBLE_TRIBUTE` on the card being Tributed. |
| A card can stand in for a 3-Tribute monster, like Egyptian God Slime | A custom Summon/Set procedure that selects and releases that card. |
| A monster needs 3 Tributes by rule | `EFFECT_LIMIT_SUMMON_PROC` with `Duel.CheckTribute(c,3)` and `Duel.SelectTribute(tp,c,3,3)`. |
| A monster needs fewer Tributes this turn | `EFFECT_DECREASE_TRIBUTE` or `EFFECT_DECREASE_TRIBUTE_SET`. |
| A monster can only be Tribute Summoned with certain Tributes | `EFFECT_TRIBUTE_LIMIT`. |
| A card needs to remember what was Tributed | `EFFECT_MATERIAL_CHECK` and `Card.GetMaterial`. |

Local constant files also define `EFFECT_TRIPLE_TRIBUTE`, but it is marked
`N/A` in `constant.lua` and is commented out in the local core header. The
verified MDPro3/YGOPro path for "treated as 3 Tributes" is a custom Summon
procedure, not a generic triple-Tribute effect code.

## The Core Model

For ordinary Tribute Summons, the core starts from the monster's Level:

| Monster Level | Base Tribute requirement |
| --- | --- |
| Level 1-4 | 0 Tributes |
| Level 5-6 | 1 Tribute |
| Level 7 or higher | 2 Tributes |

[`Card.GetTributeRequirement`](/api/functions/Card/GetTributeRequirement)
returns the current minimum and maximum Tribute counts after reduction effects
are considered:

```lua
local minc,maxc=c:GetTributeRequirement()
```

The current maximum can matter. A reduction effect may allow a monster to be
Tribute Summoned with fewer Tributes while still allowing the normal number.

When the core builds the Tribute candidate list, each releasable card gets a
`release_param`:

| Candidate state | Tribute value used by selection |
| --- | --- |
| Ordinary releasable monster | `1` |
| A monster affected by `EFFECT_DOUBLE_TRIBUTE` for the monster being Summoned | `2` |

That is why [`Duel.GetTributeCount`](/api/functions/Duel/GetTributeCount) can
return a number larger than the size of
[`Duel.GetTributeGroup`](/api/functions/Duel/GetTributeGroup). The count is a
Tribute value total, not just a card count.

## Simple Double-Tribute Monsters

Kaiser Sea Horse (`c17444133.lua`) is the cleanest pattern:

```lua
function c17444133.initial_effect(c)
    local e1=Effect.CreateEffect(c)
    e1:SetType(EFFECT_TYPE_SINGLE)
    e1:SetCode(EFFECT_DOUBLE_TRIBUTE)
    e1:SetValue(c17444133.condition)
    c:RegisterEffect(e1)
end

function c17444133.condition(e,c)
    return c:IsAttribute(ATTRIBUTE_LIGHT)
end
```

The value function receives the monster that would be Tribute Summoned as `c`.
Return `true` when this card should count as 2 Tributes for that monster.

Double Coston (`c44436472.lua`) is the DARK version:

```lua
function c44436472.condition(e,c)
    return c:IsAttribute(ATTRIBUTE_DARK)
end
```

The effect is on the card being Tributed, not on the monster being Summoned.
The core checks it while building the Tribute list with the target monster as
the argument.

## Temporary Double-Tribute Effects

The First Monarch (`c8522996.lua`) becomes a Trap Monster, lets the player
declare an Attribute, changes itself to that Attribute, then registers a
temporary double-Tribute effect:

```lua
local e2=Effect.CreateEffect(c)
e2:SetType(EFFECT_TYPE_SINGLE)
e2:SetCode(EFFECT_DOUBLE_TRIBUTE)
e2:SetProperty(EFFECT_FLAG_CANNOT_DISABLE)
e2:SetValue(c8522996.condition)
e2:SetReset(RESET_EVENT+RESETS_STANDARD)
c:RegisterEffect(e2)
```

Its condition compares the monster being Tribute Summoned with The First
Monarch's current Attribute:

```lua
function c8522996.condition(e,c)
    return c:IsAttribute(e:GetHandler():GetAttribute())
end
```

This is the same mechanic as Kaiser Sea Horse. The difference is duration: the
effect is created later and resets when the Trap Monster leaves its valid
state.

## Egyptian God Slime

Egyptian God Slime (`c42166000.lua`) is not implemented with
`EFFECT_TRIPLE_TRIBUTE`. The local script gives Egyptian God Slime a marker
effect, then registers custom Normal Summon and Set procedures while it is on
the field.

First, the marker:

```lua
local e0=Effect.CreateEffect(c)
e0:SetType(EFFECT_TYPE_SINGLE)
e0:SetCode(42166000)
c:RegisterEffect(e0)
```

Then the Summon procedure:

```lua
local e3=Effect.CreateEffect(c)
e3:SetDescription(aux.Stringid(42166000,0))
e3:SetType(EFFECT_TYPE_FIELD)
e3:SetCode(EFFECT_LIMIT_SUMMON_PROC)
e3:SetRange(LOCATION_MZONE)
e3:SetTargetRange(LOCATION_HAND,0)
e3:SetCondition(c42166000.ttcon)
e3:SetTarget(c42166000.RequireSummon)
e3:SetOperation(c42166000.ttop)
e3:SetValue(SUMMON_TYPE_ADVANCE)
c:RegisterEffect(e3)
```

`SetTargetRange(LOCATION_HAND,0)` means this field procedure applies to
monsters in your hand. `RequireSummon` lists the monsters that may use Egyptian
God Slime as the whole 3-Tribute procedure, including the Egyptian Gods:

```lua
function c42166000.RequireSummon(e,c)
    return c:IsCode(10000000,10000010,10000020,10000080,21208154,57793869,62180201,57761191)
end
```

The condition asks whether an Egyptian God Slime marker is available and
whether releasing it would open a Monster Zone:

```lua
function c42166000.ttfilter(c,tp)
    return c:IsHasEffect(42166000) and c:IsReleasable(REASON_SUMMON)
        and Duel.GetMZoneCount(tp,c)>0
end

function c42166000.ttcon(e,c,minc)
    if c==nil then return true end
    local tp=c:GetControler()
    return minc<=3 and Duel.IsExistingMatchingCard(c42166000.ttfilter,tp,LOCATION_MZONE,0,1,nil,tp)
end
```

The operation selects exactly one Egyptian God Slime, records it as material,
and releases it as Summon material:

```lua
function c42166000.ttop(e,tp,eg,ep,ev,re,r,rp,c)
    Duel.Hint(HINT_SELECTMSG,tp,HINTMSG_RELEASE)
    local g=Duel.SelectMatchingCard(tp,c42166000.ttfilter,tp,LOCATION_MZONE,0,1,1,nil,tp)
    c:SetMaterial(g)
    Duel.Release(g,REASON_SUMMON+REASON_MATERIAL)
end
```

That is the key lesson: "treated as 3 Tributes" is modeled by a custom
procedure that replaces the normal 3-Tribute selection for specific monsters.
It is not the same as a generic `release_param=3` effect.

Egyptian God Slime also has a second custom procedure for monsters that can be
Tribute Summoned by Tributing 3 monsters, where one Egyptian God Slime counts
as 3 of a larger requirement. That procedure combines an ordinary
[`Duel.SelectTribute`](/api/functions/Duel/SelectTribute) selection with one
selected Egyptian God Slime, merges the groups, records the material, and
releases all of them.

## Three-Tribute Monsters

Slifer the Sky Dragon (`c10000020.lua`) shows the ordinary "this monster needs
3 Tributes" shape:

```lua
local e1=Effect.CreateEffect(c)
e1:SetDescription(aux.Stringid(10000020,2))
e1:SetProperty(EFFECT_FLAG_CANNOT_DISABLE+EFFECT_FLAG_UNCOPYABLE)
e1:SetType(EFFECT_TYPE_SINGLE)
e1:SetCode(EFFECT_LIMIT_SUMMON_PROC)
e1:SetCondition(c10000020.ttcon)
e1:SetOperation(c10000020.ttop)
e1:SetValue(SUMMON_TYPE_ADVANCE)
c:RegisterEffect(e1)
```

The condition and operation use the Tribute APIs directly:

```lua
function c10000020.ttcon(e,c,minc)
    if c==nil then return true end
    return minc<=3 and Duel.CheckTribute(c,3)
end

function c10000020.ttop(e,tp,eg,ep,ev,re,r,rp,c)
    local g=Duel.SelectTribute(tp,c,3,3)
    c:SetMaterial(g)
    Duel.Release(g,REASON_SUMMON+REASON_MATERIAL)
end
```

Use this pattern when the monster itself has a nonstandard Tribute Summon
requirement. Use the Egyptian God Slime pattern when another card on the field
creates an alternate procedure for that monster.

## Reducing Tribute Requirements

Amarylease (`c18988391.lua`) registers a temporary field effect that reduces
the Tribute requirement for monsters in the hand:

```lua
local e1=Effect.CreateEffect(e:GetHandler())
e1:SetType(EFFECT_TYPE_FIELD)
e1:SetCode(EFFECT_DECREASE_TRIBUTE)
e1:SetTargetRange(LOCATION_HAND,0)
e1:SetCountLimit(1)
e1:SetValue(0x1)
e1:SetReset(RESET_PHASE+PHASE_END)
Duel.RegisterEffect(e1,tp)
```

The local core reads the value as a packed number:

| Part | Meaning |
| --- | --- |
| low 16 bits, `value & 0xffff` | Amount subtracted from the minimum Tribute count. |
| high 16 bits, `value >> 16` | Amount subtracted from the maximum Tribute count. |

So `0x1` reduces the minimum by 1 but leaves the maximum alone. A Level 7
monster can become Tribute Summonable with 1 Tribute while still allowing 2.

Simorgh, Bird of Ancestry (`c86489182.lua`) returns `0x10001,86489182`:

```lua
function c86489182.decval(e,c)
    return 0x10001,86489182
end
```

That reduces both minimum and maximum by 1. The second returned value is a
duplicate-prevention code; the core uses it so multiple effects with the same
code do not stack repeatedly.

Use `EFFECT_DECREASE_TRIBUTE_SET` for Set procedures. Simorgh, Bird of
Ancestry clones the Summon reduction and changes the code for setting:

```lua
local e4=e3:Clone()
e4:SetCode(EFFECT_DECREASE_TRIBUTE_SET)
c:RegisterEffect(e4)
```

## Restricting Which Tributes Can Be Used

`EFFECT_TRIBUTE_LIMIT` belongs on the monster being Tribute Summoned. Its
value function receives a potential Tribute and returns true when that Tribute
is not allowed.

Simorgh, Bird of Divinity (`c14989021.lua`) can only use WIND monsters as
Tributes:

```lua
local e2=Effect.CreateEffect(c)
e2:SetType(EFFECT_TYPE_SINGLE)
e2:SetCode(EFFECT_TRIBUTE_LIMIT)
e2:SetValue(c14989021.tlimit)
c:RegisterEffect(e2)

function c14989021.tlimit(e,c)
    return not c:IsAttribute(ATTRIBUTE_WIND)
end
```

Read the predicate carefully. Because the function returns `not WIND`, it is
not saying "this is a good Tribute"; it is saying "this candidate is forbidden
by the limit."

## Remembering Tributed Materials

After a Tribute Summon, scripts can inspect the recorded material group with
[`Card.GetMaterial`](/api/functions/Card/GetMaterial). The procedure or core
must call [`Card.SetMaterial`](/api/functions/Card/SetMaterial) before the
release for this to be useful.

Simorgh, Bird of Ancestry uses `EFFECT_MATERIAL_CHECK` to remember whether all
Tributed monsters were WIND:

```lua
local e6=Effect.CreateEffect(c)
e6:SetType(EFFECT_TYPE_SINGLE)
e6:SetCode(EFFECT_MATERIAL_CHECK)
e6:SetValue(c86489182.valcheck)
e6:SetLabelObject(e5)
c:RegisterEffect(e6)

function c86489182.valcheck(e,c)
    local g=c:GetMaterial()
    if g:FilterCount(Card.IsAttribute,nil,ATTRIBUTE_WIND)==#g and #g>0 then
        e:GetLabelObject():SetLabel(1)
    else
        e:GetLabelObject():SetLabel(0)
    end
end
```

Hardened Armed Dragon (`c68473226.lua`) shows a different memory pattern. It
checks `EVENT_BE_PRE_MATERIAL`, confirms it was used for a Tribute Summon with
`r==REASON_SUMMON`, then grants protection to the monster that used it as
material.

## Tribute APIs In Custom Procedures

Use the Tribute APIs when writing a custom Tribute Summon procedure:

| Function | Use |
| --- | --- |
| [`Duel.GetTributeGroup`](/api/functions/Duel/GetTributeGroup) | Get the actual candidate cards. |
| [`Duel.GetTributeCount`](/api/functions/Duel/GetTributeCount) | Count available Tribute value, including cards that count as 2 Tributes. |
| [`Duel.CheckTribute`](/api/functions/Duel/CheckTribute) | Check whether a Tribute selection from `min` to `max` exists. |
| [`Duel.SelectTribute`](/api/functions/Duel/SelectTribute) | Ask the player to choose Tributes for the monster. |
| [`Card.SetMaterial`](/api/functions/Card/SetMaterial) | Record selected Tributes as Summon materials. |
| [`Duel.Release`](/api/functions/Duel/Release) | Release selected Tributes with `REASON_SUMMON+REASON_MATERIAL`. |

The local define notes for `Duel.GetTributeCount` explicitly warn that the
count may not equal the number of cards in `Duel.GetTributeGroup`, because some
cards can be used as multiple Tributes.

## Common Pitfalls

| Mistake | Better habit |
| --- | --- |
| Using `EFFECT_DOUBLE_TRIBUTE` on the monster being Tribute Summoned. | Put it on the card that will be Tributed, and make the value function inspect the monster being Summoned. |
| Treating `EFFECT_TRIPLE_TRIBUTE` as a usable local mechanic. | Use a custom procedure; locally that constant is `N/A` and not implemented in the verified core path. |
| Assuming a double-Tribute card counts as 2 for every release. | The verified core double-Tribute path is Tribute Summon selection. Ordinary costs and effect releases use actual cards unless a script customizes them. |
| Forgetting `Card.SetMaterial` before releasing custom Tribute material. | Record the selected group first, then release it with `REASON_SUMMON+REASON_MATERIAL`. |
| Confusing a reduced requirement with a larger Tribute value. | `EFFECT_DECREASE_TRIBUTE` changes what the monster needs; `EFFECT_DOUBLE_TRIBUTE` changes what a candidate contributes. |
| Reading `EFFECT_TRIBUTE_LIMIT` backwards. | Its value function returns true for a forbidden candidate, as shown by Simorgh, Bird of Divinity. |
| Using `Duel.SelectMatchingCard` for ordinary Tribute selection. | Use `Duel.SelectTribute` when you need the core to respect Tribute value, Tribute limits, extra releases, and zone constraints. |
| Forgetting Set procedures. | Use `EFFECT_LIMIT_SET_PROC`, `EFFECT_SET_PROC`, or `EFFECT_DECREASE_TRIBUTE_SET` when the card text also affects Setting. |

## Useful API Pages

- [`Card.GetTributeRequirement`](/api/functions/Card/GetTributeRequirement)
- [`Card.SetMaterial`](/api/functions/Card/SetMaterial)
- [`Card.GetMaterial`](/api/functions/Card/GetMaterial)
- [`Card.IsReleasable`](/api/functions/Card/IsReleasable)
- [`Card.IsSummonType`](/api/functions/Card/IsSummonType)
- [`Duel.GetTributeGroup`](/api/functions/Duel/GetTributeGroup)
- [`Duel.GetTributeCount`](/api/functions/Duel/GetTributeCount)
- [`Duel.CheckTribute`](/api/functions/Duel/CheckTribute)
- [`Duel.SelectTribute`](/api/functions/Duel/SelectTribute)
- [`Duel.Release`](/api/functions/Duel/Release)
- [`Duel.Summon`](/api/functions/Duel/Summon)
- [`Duel.MSet`](/api/functions/Duel/MSet)
- [`Duel.GetMZoneCount`](/api/functions/Duel/GetMZoneCount)
- [`Duel.GetLocationCount`](/api/functions/Duel/GetLocationCount)
- [`Effect.SetValue`](/api/functions/Effect/SetValue)
- [`Effect.SetTargetRange`](/api/functions/Effect/SetTargetRange)
- [`Effect.SetLabelObject`](/api/functions/Effect/SetLabelObject)
- [`Effect.GetLabelObject`](/api/functions/Effect/GetLabelObject)
- [`Group.Merge`](/api/functions/Group/Merge)
- [`Group.CheckSubGroup`](/api/functions/Group/CheckSubGroup)
