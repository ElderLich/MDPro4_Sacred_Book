# Equip Spells and Equip Cards

Equip scripting has two sides:

1. The card must become equipped to a monster.
2. The Equip Card registers effects that apply while it remains equipped.

MDPro3/YGOPro exposes the equip action through `Duel.Equip`. Local utility
scripts also provide `Auxiliary.AddEquipSpellEffect`, which builds the common
Equip Spell activation effect and `EFFECT_EQUIP_LIMIT` for you.

## Manual Equip Spell Pattern

The local script style for a basic Equip Spell is:

```lua
local e1=Effect.CreateEffect(c)
e1:SetCategory(CATEGORY_EQUIP)
e1:SetType(EFFECT_TYPE_ACTIVATE)
e1:SetCode(EVENT_FREE_CHAIN)
e1:SetProperty(EFFECT_FLAG_CARD_TARGET+EFFECT_FLAG_CONTINUOUS_TARGET)
e1:SetTarget(s.target)
e1:SetOperation(s.operation)
c:RegisterEffect(e1)
```

The target function selects a face-up monster and announces that the card will
be equipped.

```lua
function s.eqfilter(c)
    return c:IsFaceup() and c:IsSetCard(0x1034)
end

function s.target(e,tp,eg,ep,ev,re,r,rp,chk,chkc)
    if chkc then return chkc:IsLocation(LOCATION_MZONE) and s.eqfilter(chkc) end
    if chk==0 then
        return Duel.IsExistingTarget(s.eqfilter,tp,LOCATION_MZONE,LOCATION_MZONE,1,nil)
    end
    Duel.Hint(HINT_SELECTMSG,tp,HINTMSG_EQUIP)
    Duel.SelectTarget(tp,s.eqfilter,tp,LOCATION_MZONE,LOCATION_MZONE,1,1,nil)
    Duel.SetOperationInfo(0,CATEGORY_EQUIP,e:GetHandler(),1,0,0)
end
```

During resolution, recheck both the Equip Card and the target monster.

```lua
function s.operation(e,tp,eg,ep,ev,re,r,rp)
    local c=e:GetHandler()
    local tc=Duel.GetFirstTarget()
    if c:IsRelateToEffect(e) and tc and tc:IsRelateToEffect(e) and tc:IsFaceup() then
        Duel.Equip(tp,c,tc)
    end
end
```

This is the same shape used by local Equip Spell scripts such as the one that
registers an ATK bonus and an equip limit after its activation effect.

## Rules-Facing Script Notes

Equip Cards are unusually sensitive to the difference between "this card is
legally equipped" and "this card's continuous effect is currently applying."
Keep these ideas separate:

| Topic | Script consequence |
| --- | --- |
| Activation and targeting | Normal Equip Spell activation targets a face-up monster and uses continuous targeting flags. |
| Equip legality | `EFFECT_EQUIP_LIMIT` or Union state decides which monster the card may remain equipped to. |
| Effect application | `EFFECT_TYPE_EQUIP` applies effects to the equipped monster while the equip state is valid. |
| Leaving the field | Equip effects stop applying when the Equip Card is no longer equipped/face-up in the expected state. |
| Negation | A negated activation does not complete the equip operation; negated continuous equip effects do not apply their bonus. |

The script should not treat a failed stat bonus as the same thing as an illegal
equip target. For example, a monster might be unaffected by a continuous equip
modifier while the Equip Card itself is still legally equipped. The equip limit
answers the legal-target question.

## Equip Effects

An Equip Card's bonus is usually an `EFFECT_TYPE_EQUIP` effect. It applies to
the equipped monster, not to the Equip Card itself.

```lua
local e2=Effect.CreateEffect(c)
e2:SetType(EFFECT_TYPE_EQUIP)
e2:SetCode(EFFECT_UPDATE_ATTACK)
e2:SetValue(800)
c:RegisterEffect(e2)
```

Dynamic equip values use a value function. Local scripts use this for Equip
Cards whose bonus depends on counters, equipped state, or other live data.

```lua
function s.atkval(e,c)
    return e:GetHandler():GetCounter(0x1)*500
end
```

## Equip Limits

Most Equip Cards also register `EFFECT_EQUIP_LIMIT` as a single effect. The
limit tells the engine which equipped monster remains legal for that card.

```lua
local e3=Effect.CreateEffect(c)
e3:SetType(EFFECT_TYPE_SINGLE)
e3:SetCode(EFFECT_EQUIP_LIMIT)
e3:SetProperty(EFFECT_FLAG_CANNOT_DISABLE)
e3:SetValue(s.eqlimit)
c:RegisterEffect(e3)

function s.eqlimit(e,c)
    return c:IsSetCard(0x1034)
end
```

`Card.CheckEquipTarget(c1,c2)` checks whether `c2` is a valid equipped monster
for `c1`; the local define comments note that this is determined by
`EFFECT_EQUIP_LIMIT` or Union state.

```lua
function s.filter(c,e,tp,ec)
    return c:IsSetCard(0x207a)
        and c:IsCanBeEffectTarget(e)
        and c:CheckEquipTarget(ec)
end
```

Use `CheckEquipTarget` when a script is moving an existing Equip Card to a new
monster or choosing a target for a card that already has equip-limit logic.

## `Auxiliary.AddEquipSpellEffect`

The local `utility.lua` helper `Auxiliary.AddEquipSpellEffect` creates a common
Equip Spell activation effect with:

- `CATEGORY_EQUIP`
- `EFFECT_TYPE_ACTIVATE`
- `EVENT_FREE_CHAIN`
- `EFFECT_FLAG_CARD_TARGET+EFFECT_FLAG_CONTINUOUS_TARGET`
- a target function using `Duel.IsExistingTarget` and `Duel.SelectTarget`
- an operation that calls `Duel.Equip`
- an `EFFECT_EQUIP_LIMIT` effect on the Equip Card

Use the helper when the card follows that normal shape. Write the activation
manually when the card has unusual targeting, delayed equipping, multiple
possible equipped monsters, or extra state to store.

## Cards Equipped by Effects

Monsters can also become Equip Cards through card effects. Those scripts still
use the same core ideas:

- move or equip the card with `Duel.Equip` or a helper that wraps it
- register an equip limit or Union limit
- register `EFFECT_TYPE_EQUIP` bonuses or replacement effects
- recheck that the card and target are still related to the resolving effect

If a monster is moved into the Spell & Trap Zone as a Continuous Spell/Trap
instead of becoming equipped, that is a different action. Local scripts use
`Duel.MoveToField` and then register a type-changing effect such as
`EFFECT_CHANGE_TYPE`.

```lua
Duel.MoveToField(tc,tp,tp,LOCATION_SZONE,POS_FACEUP,true)
local e1=Effect.CreateEffect(e:GetHandler())
e1:SetType(EFFECT_TYPE_SINGLE)
e1:SetCode(EFFECT_CHANGE_TYPE)
e1:SetProperty(EFFECT_FLAG_CANNOT_DISABLE)
e1:SetReset(RESET_EVENT+RESETS_STANDARD)
e1:SetValue(TYPE_SPELL+TYPE_CONTINUOUS)
tc:RegisterEffect(e1)
```

That pattern creates a Continuous Spell/Trap style card on the field. It is not
the same as `Duel.Equip`.

## Activated Effects On Equip Cards

An Equip Card can have activated effects in addition to its equip modifiers.
Those effects use their own `SetType`, `SetRange`, and callbacks.

```lua
local e1=Effect.CreateEffect(c)
e1:SetDescription(aux.Stringid(id,0))
e1:SetType(EFFECT_TYPE_IGNITION)
e1:SetRange(LOCATION_SZONE)
e1:SetTarget(s.target)
e1:SetOperation(s.operation)
c:RegisterEffect(e1)
```

When an activated effect needs the currently equipped monster, read it from the
Equip Card.

```lua
local ec=e:GetHandler():GetEquipTarget()
if ec and ec:IsFaceup() then
    -- use the equipped monster
end
```

When the effect needs the monster that was equipped before the Equip Card left
the field, local scripts use `Card.GetPreviousEquipTarget`.

```lua
local ec=e:GetHandler():GetPreviousEquipTarget()
```

This is useful for "if this equipped card is sent..." style effects.

## Continuous Card Targets

Equip state is not the only long-term relationship a card can keep. Some local
scripts use card targets for continuous relationships and read them with
`GetFirstCardTarget`.

```lua
local tc=e:GetHandler():GetFirstCardTarget()
```

Use the equip APIs for true equip relationships. Use card-target APIs only when
the local script pattern or the card text establishes a continuous target that
is not simply "this card is equipped to that monster."

## Summon-Then-Equip Effects

Some effects Special Summon a monster, then equip a card to that monster. These
effects should only register the equip limit after `Duel.Equip` succeeds.

```lua
if Duel.SpecialSummon(tc,0,tp,tp,false,false,POS_FACEUP)>0
    and Duel.Equip(tp,c,tc) then
    local e1=Effect.CreateEffect(c)
    e1:SetType(EFFECT_TYPE_SINGLE)
    e1:SetCode(EFFECT_EQUIP_LIMIT)
    e1:SetProperty(EFFECT_FLAG_CANNOT_DISABLE)
    e1:SetValue(s.eqlimit)
    c:RegisterEffect(e1)
end
```

If the later card text destroys or sends the equipped monster when the Equip
Card leaves, store or read the relevant equip/card target relationship and
recheck it during that later operation.

## Stepped Equip

The local define file shows optional stepped behavior:

```lua
Duel.Equip(player,c1,c2,up,is_step)
Duel.EquipComplete()
```

When `is_step` is true, the equip process is split and must be completed with
`Duel.EquipComplete()`. This is for scripts that need several equip operations
to finish as one process. Most ordinary Equip Spells call `Duel.Equip` without
the stepped argument.

## Common Pitfalls

| Mistake | Safer pattern |
| --- | --- |
| Equipping without checking the Spell & Trap Zone or target relation. | Check activation legality, then recheck `IsRelateToEffect` in operation. |
| Registering only the ATK/DEF bonus. | Also register `EFFECT_EQUIP_LIMIT` when the card needs a legal equipped monster. |
| Treating an Equip effect as `EFFECT_TYPE_SINGLE`. | Use `EFFECT_TYPE_EQUIP` for effects applied to the equipped monster. |
| Moving a monster to the Spell & Trap Zone when the card should be equipped. | Use `Duel.Equip` for equip state; use `Duel.MoveToField` for Continuous Spell/Trap state. |

Useful API pages:

- [`Duel.Equip`](/api/functions/Duel/Equip)
- [`Duel.EquipComplete`](/api/functions/Duel/EquipComplete)
- [`Card.GetEquipTarget`](/api/functions/Card/GetEquipTarget)
- [`Card.GetPreviousEquipTarget`](/api/functions/Card/GetPreviousEquipTarget)
- [`Card.GetEquipGroup`](/api/functions/Card/GetEquipGroup)
- [`Card.CheckEquipTarget`](/api/functions/Card/CheckEquipTarget)
- [`Card.GetFirstCardTarget`](/api/functions/Card/GetFirstCardTarget)
- [`Effect.SetType`](/api/functions/Effect/SetType)
- [`Effect.SetValue`](/api/functions/Effect/SetValue)
