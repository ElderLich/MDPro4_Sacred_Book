# Special Summon-Only Monster Guide

Some monsters are not Normal Summonable and need a proper Special Summon before
ordinary revive effects can bring them back later. In scripts, that usually
means one or more of these pieces:

| Job | Usual tool | What it protects |
| --- | --- | --- |
| Revive limit | [`Card.EnableReviveLimit`](/api/functions/Card/EnableReviveLimit) | The monster must complete its proper Summon before ordinary Special Summons from the GY, banishment, or similar locations are legal. |
| Built-in procedure | `EFFECT_SPSUMMON_PROC` | The monster can Special Summon itself by a rule procedure, usually from the hand or Extra Deck. |
| Other-Summon restriction | `EFFECT_SPSUMMON_CONDITION` | Other effects cannot Special Summon the monster unless the condition allows that path. |
| Effect-driven proper Summon | [`Duel.SpecialSummon`](/api/functions/Duel/SpecialSummon) plus [`Card.CompleteProcedure`](/api/functions/Card/CompleteProcedure) | An activated effect resolves and deliberately treats the result as the card's proper Summon. |

This guide focuses on Main Deck Special Summon-only monsters. Extra Deck
procedures are covered in the Ritual, Fusion, Synchro, Xyz, Link, and Pendulum
procedure guides.

## The Core Idea

`c:EnableReviveLimit()` does not Summon the monster. It registers an
`EFFECT_REVIVE_LIMIT` effect on that card. The local core then refuses many
ordinary Special Summon attempts while the card has not completed its proper
Summon procedure.

The proper-Summon status is `STATUS_PROC_COMPLETE` in the core. Local
`operations.cpp` sets that status after a successful rule Special Summon
procedure, such as an `EFFECT_SPSUMMON_PROC`. Scripts only need to call
`c:CompleteProcedure()` when a normal resolving effect performs a Summon that
should count as the card's proper Summon.

The core also clears proper-Summon completion when a card is moved to the hand
or Deck. That matches ordinary gameplay expectations: returning a properly
Summoned monster to the hand makes the copy in the hand need its proper
Summon again.

## Basic Hand Procedure

Black Luster Soldier - Envoy of the Beginning (`c72989439.lua`) is a good
local example. It can be Special Summoned from the hand by banishing 1 LIGHT
and 1 DARK monster from the GY.

```lua
function c72989439.initial_effect(c)
    c:EnableReviveLimit()

    local e1=Effect.CreateEffect(c)
    e1:SetDescription(aux.Stringid(72989439,0))
    e1:SetType(EFFECT_TYPE_FIELD)
    e1:SetCode(EFFECT_SPSUMMON_PROC)
    e1:SetProperty(EFFECT_FLAG_CANNOT_DISABLE+EFFECT_FLAG_UNCOPYABLE)
    e1:SetRange(LOCATION_HAND)
    e1:SetCondition(c72989439.spcon)
    e1:SetTarget(c72989439.sptg)
    e1:SetOperation(c72989439.spop)
    c:RegisterEffect(e1)
end
```

The procedure effect is a field effect registered on the monster. It is not an
activated effect and it does not make a Chain Link. The core asks the condition
whether the rule Summon is available, then uses the target and operation pieces
to select and process the procedure cards.

The standard pieces are:

| Piece | Meaning |
| --- | --- |
| `SetCode(EFFECT_SPSUMMON_PROC)` | This is a built-in Special Summon procedure. |
| `SetRange(LOCATION_HAND)` | The procedure is available while this card is in the hand. |
| `EFFECT_FLAG_CANNOT_DISABLE+EFFECT_FLAG_UNCOPYABLE` | The procedure is a card rule hook and should not be disabled or copied like an ordinary effect. |
| `SetCondition` | Checks whether the Summon could currently be performed. |
| `SetTarget` | Lets the player choose required procedure cards when selection is needed. |
| `SetOperation` | Applies the procedure cost or movement, such as banishing or Tributing. |

Many procedure conditions begin with:

```lua
if c==nil then return true end
```

The core can ask the procedure for general availability without a concrete
handler card. When the handler exists, use `c:GetControler()` instead of
assuming `tp` is the controller.

## Selecting Procedure Cards

Black Luster Soldier needs a LIGHT and a DARK monster in the GY. Its filter is
small:

```lua
function c72989439.spcostfilter(c)
    return c:IsAbleToRemoveAsCost() and c:IsAttribute(ATTRIBUTE_LIGHT+ATTRIBUTE_DARK)
end
```

The condition checks zone space, collects the GY candidates, and uses
[`Group.CheckSubGroup`](/api/functions/Group/CheckSubGroup) with
`aux.gfcheck` to prove that a two-card selection can contain one LIGHT and one
DARK monster:

```lua
function c72989439.spcon(e,c)
    if c==nil then return true end
    local tp=c:GetControler()
    if Duel.GetMZoneCount(tp)<=0 then return false end
    local g=Duel.GetMatchingGroup(c72989439.spcostfilter,tp,LOCATION_GRAVE,0,nil)
    return g:CheckSubGroup(aux.gfcheck,2,2,Card.IsAttribute,ATTRIBUTE_LIGHT,ATTRIBUTE_DARK)
end
```

The target branch asks the player to choose the exact pair, keeps that Group
alive, and stores it on the procedure effect:

```lua
function c72989439.sptg(e,tp,eg,ep,ev,re,r,rp,chk,c)
    local g=Duel.GetMatchingGroup(c72989439.spcostfilter,tp,LOCATION_GRAVE,0,nil)
    Duel.Hint(HINT_SELECTMSG,tp,HINTMSG_REMOVE)
    local sg=g:SelectSubGroup(tp,aux.gfcheck,true,2,2,Card.IsAttribute,ATTRIBUTE_LIGHT,ATTRIBUTE_DARK)
    if sg then
        sg:KeepAlive()
        e:SetLabelObject(sg)
        return true
    else
        return false
    end
end
```

The operation retrieves and deletes that kept-alive Group:

```lua
function c72989439.spop(e,tp,eg,ep,ev,re,r,rp,c)
    local sg=e:GetLabelObject()
    Duel.Remove(sg,POS_FACEUP,REASON_SPSUMMON)
    sg:DeleteGroup()
end
```

Use `REASON_SPSUMMON` for procedure material movement when the movement is part
of the Summon itself. Use `REASON_COST` for ordinary activated-effect costs.

## Revealing Cards For A Procedure

Blue-Eyes Alternative White Dragon (`c38517737.lua`) uses the same hand
procedure structure, but its requirement is revealing Blue-Eyes White Dragon in
the hand instead of moving cards from the GY.

```lua
function c38517737.initial_effect(c)
    c:EnableReviveLimit()

    local e1=Effect.CreateEffect(c)
    e1:SetType(EFFECT_TYPE_FIELD)
    e1:SetCode(EFFECT_SPSUMMON_PROC)
    e1:SetProperty(EFFECT_FLAG_CANNOT_DISABLE+EFFECT_FLAG_UNCOPYABLE)
    e1:SetRange(LOCATION_HAND)
    e1:SetCountLimit(1,38517737+EFFECT_COUNT_CODE_OATH)
    e1:SetCondition(c38517737.spcon)
    e1:SetTarget(c38517737.sptg)
    e1:SetOperation(c38517737.spop)
    c:RegisterEffect(e1)
end
```

Two details are worth copying carefully:

| Detail | Why it matters |
| --- | --- |
| `SetCountLimit(1,38517737+EFFECT_COUNT_CODE_OATH)` | The once-per-turn limit belongs to the procedure itself. Because this is not an activated effect, the oath count code is the clean local pattern for the card's text. |
| `aux.EnableChangeCode(c,89631139,LOCATION_MZONE+LOCATION_GRAVE)` | After it is on the field or in the GY, the card is treated as Blue-Eyes White Dragon. That identity change is separate from the Summon procedure. |

The reveal target stores the chosen hidden card as the procedure's label object:

```lua
function c38517737.spcfilter(c)
    return c:IsCode(89631139) and not c:IsPublic()
end

function c38517737.sptg(e,tp,eg,ep,ev,re,r,rp,chk,c)
    local g=Duel.GetMatchingGroup(c38517737.spcfilter,tp,LOCATION_HAND,0,nil)
    Duel.Hint(HINT_SELECTMSG,tp,HINTMSG_CONFIRM)
    local tc=g:SelectUnselect(nil,tp,false,true,1,1)
    if tc then
        e:SetLabelObject(tc)
        return true
    else
        return false
    end
end

function c38517737.spop(e,tp,eg,ep,ev,re,r,rp,c)
    local g=e:GetLabelObject()
    Duel.ConfirmCards(1-tp,g)
    Duel.ShuffleHand(tp)
end
```

Use [`Duel.ConfirmCards`](/api/functions/Duel/ConfirmCards) when the procedure
requires revealing a private card. Use [`Duel.ShuffleHand`](/api/functions/Duel/ShuffleHand)
after revealing from the hand so the opponent cannot keep tracking the exact
hand position.

## Condition-Only Procedures

Some Special Summon-only monsters need no target or operation because their
Summon condition is just a game-state check.

Dark Armed Dragon (`c65192027.lua`) can be Special Summoned from the hand when
you have exactly 3 DARK monsters in the GY:

```lua
function c65192027.spcon(e,c)
    if c==nil then return true end
    return Duel.GetLocationCount(c:GetControler(),LOCATION_MZONE)>0
        and Duel.GetMatchingGroupCount(Card.IsAttribute,c:GetControler(),LOCATION_GRAVE,0,nil,ATTRIBUTE_DARK)==3
end
```

Judgment Dragon (`c57774843.lua`) uses the same shape but counts different
Lightsworn monster names:

```lua
function c57774843.spfilter(c)
    return c:IsSetCard(0x38) and c:IsType(TYPE_MONSTER)
end

function c57774843.spcon(e,c)
    if c==nil then return true end
    if Duel.GetLocationCount(c:GetControler(),LOCATION_MZONE)<=0 then return false end
    local g=Duel.GetMatchingGroup(c57774843.spfilter,c:GetControler(),LOCATION_GRAVE,0,nil)
    local ct=g:GetClassCount(Card.GetCode)
    return ct>3
end
```

Condition-only procedures still need `EnableReviveLimit` when the monster is a
Special Summon-only monster. A successful rule procedure will mark the monster
as properly Summoned.

## Blocking Other Special Summons

Use `EFFECT_SPSUMMON_CONDITION` when the card's text does not allow ordinary
effects to Special Summon it by other methods.

Dark Armed Dragon uses an always-false condition, then separately registers its
own hand procedure:

```lua
local e1=Effect.CreateEffect(c)
e1:SetType(EFFECT_TYPE_SINGLE)
e1:SetProperty(EFFECT_FLAG_CANNOT_DISABLE+EFFECT_FLAG_UNCOPYABLE)
e1:SetCode(EFFECT_SPSUMMON_CONDITION)
e1:SetValue(aux.FALSE)
c:RegisterEffect(e1)

local e2=Effect.CreateEffect(c)
e2:SetType(EFFECT_TYPE_FIELD)
e2:SetCode(EFFECT_SPSUMMON_PROC)
e2:SetProperty(EFFECT_FLAG_CANNOT_DISABLE+EFFECT_FLAG_UNCOPYABLE)
e2:SetRange(LOCATION_HAND)
e2:SetCondition(c65192027.spcon)
c:RegisterEffect(e2)
```

The first effect blocks ordinary effect-based Special Summons. The second
effect is still the monster's own rule procedure.

Older local scripts sometimes register `EFFECT_SPSUMMON_CONDITION` without
`SetValue(aux.FALSE)`. Judgment Dragon and The Winged Dragon of Ra - Immortal
Phoenix (`c10000090.lua`) use that shape. Treat both as restriction hooks and
do not remove them casually; they are part of how those scripts keep unrelated
Special Summon effects from bypassing the card text.

## Summoning To The Opponent's Field

Lava Golem (`c102380.lua`) is a Special Summon-only monster whose procedure
Summons it to the opponent's field by Tributing monsters they control. It uses
`EFFECT_FLAG_SPSUM_PARAM` and [`Effect.SetTargetRange`](/api/functions/Effect/SetTargetRange):

```lua
local e1=Effect.CreateEffect(c)
e1:SetDescription(aux.Stringid(102380,0))
e1:SetType(EFFECT_TYPE_FIELD)
e1:SetCode(EFFECT_SPSUMMON_PROC)
e1:SetProperty(EFFECT_FLAG_CANNOT_DISABLE+EFFECT_FLAG_UNCOPYABLE+EFFECT_FLAG_SPSUM_PARAM)
e1:SetRange(LOCATION_HAND)
e1:SetTargetRange(POS_FACEUP,1)
e1:SetCondition(c102380.spcon)
e1:SetTarget(c102380.sptg)
e1:SetOperation(c102380.spop)
c:RegisterEffect(e1)
```

With `EFFECT_FLAG_SPSUM_PARAM`, `SetTargetRange` no longer means "which
locations are affected." Its first value is the allowed Summon position and
its second value is the destination player. `SetTargetRange(POS_FACEUP,1)`
means this procedure Summons the monster face-up to the opponent's field.

Lava Golem also registers an `EFFECT_SPSUMMON_COST` hook:

```lua
local e3=Effect.CreateEffect(c)
e3:SetType(EFFECT_TYPE_SINGLE)
e3:SetCode(EFFECT_SPSUMMON_COST)
e3:SetProperty(EFFECT_FLAG_CANNOT_DISABLE)
e3:SetCost(c102380.spcost)
e3:SetOperation(c102380.spcop)
c:RegisterEffect(e3)
```

The local core checks `EFFECT_SPSUMMON_COST` during Special Summon processing.
For Lava Golem, the cost hook checks that the player has not Normal Summoned
this turn and then registers temporary effects that stop that player from
Normal Summoning or Setting for the rest of the turn.

## Effect-Driven Proper Summons

Sometimes a resolving effect performs the card's proper Summon instead of using
an `EFFECT_SPSUMMON_PROC`. In that case, the script should:

1. Check legality with [`Card.IsCanBeSpecialSummoned`](/api/functions/Card/IsCanBeSpecialSummoned).
2. Resolve with matching [`Duel.SpecialSummon`](/api/functions/Duel/SpecialSummon) parameters.
3. Call [`Card.CompleteProcedure`](/api/functions/Card/CompleteProcedure) only if the successful Summon is meant to satisfy the card's proper Summon.

Flowerdino (`c10851853.lua`) blocks unrelated Special Summons with
`EFFECT_SPSUMMON_CONDITION`, then has a trigger effect in the hand that properly
Special Summons itself:

```lua
function s.target1(e,tp,eg,ep,ev,re,r,rp,chk)
    local c=e:GetHandler()
    if chk==0 then return Duel.GetLocationCount(tp,LOCATION_MZONE)>0
        and c:IsCanBeSpecialSummoned(e,0,tp,true,false) end
    Duel.SetOperationInfo(0,CATEGORY_SPECIAL_SUMMON,c,1,0,0)
end

function s.activate1(e,tp,eg,ep,ev,re,r,rp)
    local c=e:GetHandler()
    if c:IsRelateToEffect(e) and Duel.SpecialSummon(c,0,tp,tp,true,false,POS_FACEUP)>0 then
        c:CompleteProcedure()
    end
end
```

Notice the match:

| Check | Resolution |
| --- | --- |
| `c:IsCanBeSpecialSummoned(e,0,tp,true,false)` | `Duel.SpecialSummon(c,0,tp,tp,true,false,POS_FACEUP)` |

The effect intentionally uses `nocheck=true` because the card's own Special
Summon condition blocks other methods. It keeps `nolimit=false`, so the revive
limit still matters. After the successful Summon, `CompleteProcedure()` marks
this as the card's proper Summon.

Drytron scripts use the same completion idea through shared local helpers in
`utility.lua`:

```lua
if Duel.SpecialSummon(c,0,tp,tp,false,true,POS_FACEUP_DEFENSE)~=0 then
    c:CompleteProcedure()
    func(e,tp)
end
```

The helper's `nolimit` value is not a shortcut. It is computed from the card
type because the Drytron card text permits Special Summoning Ritual Monsters
and other eligible monsters in that archetype's specific way. Copy the pattern
only when your effect text truly performs a proper Summon that should bypass
the revive-limit check during that resolution.

## `nocheck` And `nolimit`

Both `Card.IsCanBeSpecialSummoned` and `Duel.SpecialSummon` take `nocheck` and
`nolimit`:

| Argument | What it skips | Safe beginner default |
| --- | --- | --- |
| `nocheck` | The card's `EFFECT_SPSUMMON_CONDITION` and other Summoning-condition checks. | `false` |
| `nolimit` | The revive-limit/proper-Summon completion check. | `false` |

Use `true` only when the card text and local script pattern justify it.
Examples:

| Pattern | Common values | Why |
| --- | --- | --- |
| Ordinary revive effect | `false,false` | Respect both the Summon condition and revive limit. |
| Fusion/Ritual/Synchro/Xyz/Link procedure effect | usually `false,false` with the proper `SUMMON_TYPE_*`, then `CompleteProcedure()` | The effect is performing the proper Summon and should still pass normal legality. |
| Self effect that is the card's own proper Summon despite a blocking `EFFECT_SPSUMMON_CONDITION` | sometimes `true,false`, then `CompleteProcedure()` | The card's own effect is allowed to ignore its own general Special Summon restriction, but the revive limit still applies. |
| Explicit local helper that knows a Special Summon-only monster is allowed by that effect | sometimes `nolimit=true`, then `CompleteProcedure()` | The helper must be written around the exact card text, like the Drytron helper. |

If you pass `true,true` because the Summon "doesn't work otherwise," stop and
verify the card text. That combination can easily bypass the mechanic the
script was supposed to enforce.

## Procedure Versus Activated Effect

An `EFFECT_SPSUMMON_PROC` is a rule procedure. Its target and operation
callbacks are not the same as an activated effect's target and operation:

| Rule procedure | Activated effect |
| --- | --- |
| Does not start a Chain Link. | Starts or resolves as part of a Chain Link. |
| Uses procedure callback shapes with the handler card passed as `c` in many local scripts. | Uses the usual `e,tp,eg,ep,ev,re,r,rp,chk` target shape and operation shape. |
| Uses procedure reasons such as `REASON_SPSUMMON` for material movement. | Uses `REASON_COST`, `REASON_EFFECT`, or a material reason depending on the text. |
| Core marks proper completion after the successful rule procedure. | Script calls `CompleteProcedure()` when the effect performs the proper Summon. |

When a card says "You can Special Summon this card..." from the hand without
activating an effect, expect an `EFFECT_SPSUMMON_PROC`. When a card says "You
can activate this effect; Special Summon this card...", expect a normal
activated effect that calls `Duel.SpecialSummon`.

## Common Pitfalls

| Mistake | Better habit |
| --- | --- |
| Forgetting `c:EnableReviveLimit()` on a Special Summon-only monster. | Put it near the top of `initial_effect`, before the Summon procedure or restriction hooks. |
| Calling `CompleteProcedure()` inside a normal `EFFECT_SPSUMMON_PROC` operation. | Let the core complete successful rule procedures. Use `CompleteProcedure()` for effect-driven proper Summons. |
| Using `Duel.SpecialSummon` for a built-in hand procedure. | Register an `EFFECT_SPSUMMON_PROC` when the Summon is a rule procedure and should not create a Chain Link. |
| Skipping `Duel.GetLocationCount` or `Duel.GetMZoneCount`. | Check usable Monster Zone space in the condition or activation check before offering the Summon. |
| Losing a selected Group from a procedure target. | Use `sg:KeepAlive()`, store it with `SetLabelObject`, and delete it in operation. |
| Using `REASON_COST` for procedure material movement. | Use `REASON_SPSUMMON` when the movement is part of the rule Special Summon procedure. |
| Treating `EFFECT_FLAG_SPSUM_PARAM` target ranges as locations. | With that flag, `SetTargetRange` stores Summon position and destination player. |
| Setting `nocheck` or `nolimit` to true to force a Summon. | Match the card text and local examples; true values deliberately bypass engine checks. |
| Completing an ordinary revive as if it were a proper Summon. | Only call `CompleteProcedure()` when the resolving effect is the proper Summon method. |
| Assuming proper-Summon status survives returning to the hand or Deck. | Local core clears `STATUS_PROC_COMPLETE` when the card moves to the hand or Deck. |

## Useful API Pages

- [`Card.EnableReviveLimit`](/api/functions/Card/EnableReviveLimit)
- [`Card.CompleteProcedure`](/api/functions/Card/CompleteProcedure)
- [`Card.IsCanBeSpecialSummoned`](/api/functions/Card/IsCanBeSpecialSummoned)
- [`Card.IsSpecialSummonableCard`](/api/functions/Card/IsSpecialSummonableCard)
- [`Card.IsSpecialSummonable`](/api/functions/Card/IsSpecialSummonable)
- [`Card.IsSummonType`](/api/functions/Card/IsSummonType)
- [`Duel.SpecialSummon`](/api/functions/Duel/SpecialSummon)
- [`Duel.SpecialSummonRule`](/api/functions/Duel/SpecialSummonRule)
- [`Duel.ConfirmCards`](/api/functions/Duel/ConfirmCards)
- [`Duel.ShuffleHand`](/api/functions/Duel/ShuffleHand)
- [`Duel.GetLocationCount`](/api/functions/Duel/GetLocationCount)
- [`Duel.GetMZoneCount`](/api/functions/Duel/GetMZoneCount)
- [`Duel.GetMatchingGroup`](/api/functions/Duel/GetMatchingGroup)
- [`Duel.GetMatchingGroupCount`](/api/functions/Duel/GetMatchingGroupCount)
- [`Duel.Remove`](/api/functions/Duel/Remove)
- [`Duel.Release`](/api/functions/Duel/Release)
- [`Effect.SetTargetRange`](/api/functions/Effect/SetTargetRange)
- [`Effect.SetLabelObject`](/api/functions/Effect/SetLabelObject)
- [`Effect.GetLabelObject`](/api/functions/Effect/GetLabelObject)
- [`Group.CheckSubGroup`](/api/functions/Group/CheckSubGroup)
- [`Group.SelectSubGroup`](/api/functions/Group/SelectSubGroup)
- [`Group.GetClassCount`](/api/functions/Group/GetClassCount)
- [`Group.KeepAlive`](/api/functions/Group/KeepAlive)
- [`Group.DeleteGroup`](/api/functions/Group/DeleteGroup)
