# Spell Card Patterns

Spell Cards are usually script-light at the card-activation layer. The card
activation creates a Chain Link with `EFFECT_TYPE_ACTIVATE`; the real work is
then decided by the Spell type and by the callbacks attached to that activation
effect.

Equip and Field Spells have their own focused lessons:

- [Equip Spells and Equip Cards](equip-spells)
- [Field Spells](field-spells)
- [Quick-Play Spells](quick-play-spells)
- [Ritual Procedure Guide](ritual-procedure)

This page covers the remaining Spell Card shapes: Normal Spells, Continuous
Spells, Quick-Play Spells, Ritual Spells, and effects that activate or copy a
Spell from another place.

## The Shared Activation Shape

Most Spell Cards begin like this:

```lua
local e1=Effect.CreateEffect(c)
e1:SetCategory(CATEGORY_DRAW)
e1:SetType(EFFECT_TYPE_ACTIVATE)
e1:SetCode(EVENT_FREE_CHAIN)
e1:SetTarget(s.target)
e1:SetOperation(s.activate)
c:RegisterEffect(e1)
```

Local core behavior normalizes `EFFECT_TYPE_ACTIVATE` into a field activation
effect and gives it the normal hand, Spell & Trap Zone, and Field Zone
activation range. In ordinary Spell scripts, you usually do not write
`SetRange` on the activation effect itself.

The card's printed type then changes the rules around that activation. The
local core reports Spell activation speed like this:

| Spell Card type | Activation speed | Script consequence |
| --- | --- | --- |
| Normal Spell | Spell Speed 1 | Usually `EVENT_FREE_CHAIN`, activated in an open state. |
| Continuous Spell | Spell Speed 1 | Activation places the card face-up; later effects use `SetRange(LOCATION_SZONE)`. |
| Equip Spell | Spell Speed 1 | Activation equips a monster and registers equip limits/equip effects. |
| Field Spell | Spell Speed 1 | Activation places the card in the Field Zone; later effects use `LOCATION_FZONE`. |
| Quick-Play Spell | Spell Speed 2 | Same activation type, but the card type `TYPE_QUICKPLAY` makes it fast. |
| Ritual Spell | Spell Speed 1 | The operation normally performs a Ritual Summon procedure. |

Do not confuse `TYPE_QUICKPLAY` with `EFFECT_TYPE_QUICK_O`. A Quick-Play Spell's
card activation is still `EFFECT_TYPE_ACTIVATE`; the card type is what makes
that activation Spell Speed 2.

## Normal Spells

Normal Spells usually resolve once and then leave the field by normal
Spell/Trap activation handling. Their scripts are often the cleanest examples
of target and operation flow.

Pot of Greed (`c55144522.lua`) shows a player-targeted draw effect:

```lua
function s.target(e,tp,eg,ep,ev,re,r,rp,chk)
    if chk==0 then return Duel.IsPlayerCanDraw(tp,2) end
    Duel.SetTargetPlayer(tp)
    Duel.SetTargetParam(2)
    Duel.SetOperationInfo(0,CATEGORY_DRAW,nil,0,tp,2)
end

function s.activate(e,tp,eg,ep,ev,re,r,rp)
    local p,d=Duel.GetChainInfo(0,CHAININFO_TARGET_PLAYER,CHAININFO_TARGET_PARAM)
    Duel.Draw(p,d,REASON_EFFECT)
end
```

Monster Reborn (`c83764718.lua`) shows the other common Normal Spell shape:
target a card in the GY, then recheck relation and Summon legality at
resolution.

```lua
function s.target(e,tp,eg,ep,ev,re,r,rp,chk,chkc)
    if chkc then return chkc:IsLocation(LOCATION_GRAVE) and s.filter(chkc,e,tp) end
    if chk==0 then
        return Duel.GetLocationCount(tp,LOCATION_MZONE)>0
            and Duel.IsExistingTarget(s.filter,tp,LOCATION_GRAVE,LOCATION_GRAVE,1,nil,e,tp)
    end
    Duel.Hint(HINT_SELECTMSG,tp,HINTMSG_SPSUMMON)
    local g=Duel.SelectTarget(tp,s.filter,tp,LOCATION_GRAVE,LOCATION_GRAVE,1,1,nil,e,tp)
    Duel.SetOperationInfo(0,CATEGORY_SPECIAL_SUMMON,g,1,0,0)
end

function s.activate(e,tp,eg,ep,ev,re,r,rp)
    local tc=Duel.GetFirstTarget()
    if tc:IsRelateToEffect(e) and aux.NecroValleyFilter()(tc) then
        Duel.SpecialSummon(tc,0,tp,tp,false,false,POS_FACEUP)
    end
end
```

Normal Spells are a good place to learn the activation/resolution split because
there is usually no persistent field behavior to distract from the Chain Link.

## Continuous Spells

A Continuous Spell normally has a small activation effect and then one or more
separate effects that work while the card remains face-up in the Spell & Trap
Zone.

```lua
local e1=Effect.CreateEffect(c)
e1:SetType(EFFECT_TYPE_ACTIVATE)
e1:SetCode(EVENT_FREE_CHAIN)
c:RegisterEffect(e1)

local e2=Effect.CreateEffect(c)
e2:SetType(EFFECT_TYPE_FIELD)
e2:SetRange(LOCATION_SZONE)
e2:SetCode(EFFECT_UPDATE_ATTACK)
e2:SetTargetRange(LOCATION_MZONE,0)
e2:SetValue(300)
c:RegisterEffect(e2)
```

Use [Effects That Apply Continuously](continuous-effects) for the deeper
continuous-effect rules. The important Spell-specific habit is that the
activation and the lasting behavior are separate effect objects.

## Quick-Play Spells

Quick-Play Spells still use `EFFECT_TYPE_ACTIVATE`, but their card type makes
the activation Spell Speed 2. Local `c5318639.lua` uses this normal shape:

```lua
local e1=Effect.CreateEffect(c)
e1:SetCategory(CATEGORY_DESTROY)
e1:SetType(EFFECT_TYPE_ACTIVATE)
e1:SetCode(EVENT_FREE_CHAIN)
e1:SetHintTiming(0,TIMING_END_PHASE+TIMING_EQUIP)
e1:SetProperty(EFFECT_FLAG_CARD_TARGET)
e1:SetTarget(s.target)
e1:SetOperation(s.activate)
c:RegisterEffect(e1)
```

`SetHintTiming` is not a legality check. It tells the client when this fast
effect is worth offering to the player. The real legality still belongs in the
condition, cost, and target callbacks.

The local core also enforces special activation restrictions for Quick-Play
Spells:

- a Quick-Play Spell Set this turn needs an effect such as
  `EFFECT_QP_ACT_IN_SET_TURN` to be activated that same turn;
- a Quick-Play Spell activated from the hand during the opponent's turn needs
  an effect such as `EFFECT_QP_ACT_IN_NTPHAND`.

Most beginner Quick-Play Spell scripts do not create those exceptions. They
write the normal activation effect and let the core enforce the card-type rule.

Use [Quick-Play Spells](quick-play-spells) for the focused timing, prompt,
targeting, and relation-check guide.

## Ritual Spells

A Ritual Spell is a Spell activation whose operation performs a Ritual Summon.
Use the [Ritual Procedure Guide](ritual-procedure) for the full material and
Summon flow, because material checks, required Levels, replacement material, and
`SUMMON_TYPE_RITUAL` all interact. For this classification pass, remember the
shape:

1. the card activation is still `EFFECT_TYPE_ACTIVATE`;
2. the target branch checks whether the Ritual Monster and materials are
   available;
3. the operation releases or sends the materials, then Special Summons the
   Ritual Monster with `SUMMON_TYPE_RITUAL`.

Local procedure helpers in `procedure.lua` use that same idea internally, with
`Duel.ReleaseRitualMaterial` and `Duel.SpecialSummon(...,SUMMON_TYPE_RITUAL,...)`
appearing in the Ritual procedure flow.

## Activating A Spell Through Another Effect

Some cards do not simply activate themselves. They check whether another Spell
Card can be activated, then reuse that card's activation effect or its
callbacks.

Use `Card.GetActivateEffect` when you only need the registered activation
effect. Use `Card.CheckActivateEffect` when you need to know whether that
activation effect is currently legal.

Transonic Bird (`c34072799.lua`) is a local advanced example. It sends a Ritual
Spell from the Deck as cost, stores that Spell's activation effect, then calls
the stored target and operation callbacks:

```lua
function s.cfilter(c)
    return c:GetType()==TYPE_SPELL+TYPE_RITUAL
        and c:IsAbleToGraveAsCost()
        and c:CheckActivateEffect(true,true,false)~=nil
end

local te=g:GetFirst():CheckActivateEffect(true,true,false)
e:SetLabelObject(te)
local tg=te:GetTarget()
if tg then tg(e,tp,eg,ep,ev,re,r,rp,1) end
```

That pattern is powerful, but easy to misuse. Copy it from a matching local
script when a card text really says to apply another Spell's activation effect.

## Common Pitfalls

| Mistake | Safer pattern |
| --- | --- |
| Adding `SetRange(LOCATION_HAND)` to every Spell activation. | Let `EFFECT_TYPE_ACTIVATE` use the core's activation range unless the local pattern needs something special. |
| Writing a Quick-Play Spell as `EFFECT_TYPE_QUICK_O`. | Use `EFFECT_TYPE_ACTIVATE`; `TYPE_QUICKPLAY` makes the card activation fast. |
| Treating `SetHintTiming` as permission to activate. | Use target/condition checks for legality; use hint timing for client prompts. |
| Making a Continuous Spell's lasting effect part of the activation effect. | Register the activation effect first, then separate `LOCATION_SZONE` effects. |
| Copying a Ritual Spell's operation without checking activation legality. | Use `CheckActivateEffect` and copy a proven local pattern. |

Useful API pages:

- [`Effect.SetType`](/api/functions/Effect/SetType)
- [`Effect.SetCode`](/api/functions/Effect/SetCode)
- [`Effect.SetHintTiming`](/api/functions/Effect/SetHintTiming)
- [`Card.GetActivateEffect`](/api/functions/Card/GetActivateEffect)
- [`Card.CheckActivateEffect`](/api/functions/Card/CheckActivateEffect)
- [`Card.CancelToGrave`](/api/functions/Card/CancelToGrave)
- [`Duel.SetOperationInfo`](/api/functions/Duel/SetOperationInfo)
- [`Duel.GetChainInfo`](/api/functions/Duel/GetChainInfo)
- [`Duel.SpecialSummon`](/api/functions/Duel/SpecialSummon)
- [`Duel.ReleaseRitualMaterial`](/api/functions/Duel/ReleaseRitualMaterial)
