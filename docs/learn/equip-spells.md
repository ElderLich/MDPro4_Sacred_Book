# Equip Spells and Equip Cards

Equip scripting has two sides:

1. The card must become equipped to a monster.
2. The Equip Card registers effects that apply while it remains equipped.

MDPro3/YGOPro exposes the equip action through `Duel.Equip`. Local utility
scripts also provide `Auxiliary.AddEquipSpellEffect`, which builds the common
Equip Spell activation effect and `EFFECT_EQUIP_LIMIT` for you.

Some outside examples use helper names that do not exist in this local script
set. In MDPro3, the standard Equip Spell helper is
`Auxiliary.AddEquipSpellEffect`, and many cards still write the activation,
equip limit, and operation by hand when the card has extra state to manage.

## Pick The Equip Shape First

Before writing the filter, decide what kind of equip flow the card actually
uses.

| Card text shape | Local pattern to start from |
| --- | --- |
| "Activate this card by targeting 1 face-up monster..." | Use `Auxiliary.AddEquipSpellEffect` or the manual activation pattern below. |
| "Special Summon that target, then equip this card to it" | Target the monster in its source location, Special Summon it, then call `Duel.Equip` and register a limit during resolution. |
| "Equip 1 appropriate card from your GY/Deck/banished cards" | Select or target the card to become equipped, check zone availability, `CheckEquipTarget`, uniqueness, and forbidden state before `Duel.Equip`. |
| "Equip several cards at once" | Use stepped `Duel.Equip(..., true, true)` calls, then finish with `Duel.EquipComplete()`. |
| "Place this monster in the Spell & Trap Zone as a Continuous Spell" | Use `Duel.MoveToField` and type-changing effects instead of equip APIs. |

This first choice prevents a common beginner mistake: writing every "put in
the Spell & Trap Zone" effect as an Equip Spell. Equip state is a relationship
between two cards; `MoveToField` is just a field-placement action.

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

## Activation Shapes

Not every effect that equips a card uses the same target shape.

| Shape | Targeting pattern | Equip timing |
| --- | --- | --- |
| Ordinary Equip Spell activation | `EFFECT_FLAG_CARD_TARGET+EFFECT_FLAG_CONTINUOUS_TARGET`, `Duel.SelectTarget` on a face-up monster | `Duel.Equip` during the activation's operation |
| Effect that Special Summons, then equips itself | Usually targets the monster in the GY/banished/other source location, without `EFFECT_FLAG_CONTINUOUS_TARGET` | Special Summon first, then `Duel.Equip` and register the equip limit |
| Monster or Trap becoming an Equip Card | Often non-activation or monster-effect flow | `Duel.Equip` changes the card into equip state and the script adds limits/effects |
| Existing Equip Card moving to a new monster | Target or select the new monster and check `CheckEquipTarget` | `Duel.Equip` changes the equip relationship |

An effect does not target just because it will equip something. In script
terms, targeting comes from the effect property and target APIs. `Duel.Equip`
creates the equip relationship during resolution; it does not retroactively
make a non-targeting effect into an activation-time targeting effect.

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

## What The Core Handles

Local core behavior does a lot of equip housekeeping for scripts:

- If `Duel.Equip` cannot keep the Equip Card on the field because the target is
  not a face-up monster or there is no usable Spell & Trap Zone, the Equip Card
  is sent to the GY by rule.
- When a card becomes equipped and it was not already an Equip Spell, the core
  adds the temporary type-change support needed for equip state.
- If the equipped monster leaves the field or the equip relationship is lost,
  local core destroys the Equip Card with `REASON_RULE+REASON_LOST_TARGET`.
- If the equipped monster remains but no longer satisfies `EFFECT_EQUIP_LIMIT`,
  the core destroys the Equip Card by rule during adjustment.

That means ordinary equip scripts do not need to manually poll the equipped
monster every frame. They do need to register the correct equip limit and use
the correct reason checks when a later trigger cares why the Equip Card left.

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

`EFFECT_TYPE_EQUIP` is already tied to equip state, so a normal equip modifier
does not need `SetRange(LOCATION_SZONE)`. If the equipped monster cannot use a
particular continuous value, such as a DEF update on a Link Monster, the
modifier simply has no useful result for that monster; it is not automatically
the same as an illegal equip target.

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

## Target Filter vs Equip Limit

The activation target filter and the equip-limit function answer different
questions.

| Function | When it is checked | Question |
| --- | --- | --- |
| Target filter | Activation or selection time | "Can this monster be chosen for this effect right now?" |
| Equip limit | While the card is equipped | "May this Equip Card remain equipped to this monster?" |

The local `Auxiliary.AddEquipSpellEffect` helper can keep those aligned for a
normal Equip Spell. It builds the activation target from the filter, registers
`EFFECT_EQUIP_LIMIT`, and rechecks the limit before `Duel.Equip`.

When the equip flow is unusual, write the checks by hand. Local `c11802691.lua`
checks the candidate Equip Card with `CheckEquipTarget`, `CheckUniqueOnField`,
and `IsForbidden` before offering the player a choice between equipping it and
sending it to the GY. Local `c10204849.lua` registers a temporary equip limit
only after the target monster is Special Summoned and `Duel.Equip` has been
called during resolution.

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

Local `c11913700.lua` shows the common lost-target trigger shape:

```lua
function s.spcon(e,tp,eg,ep,ev,re,r,rp)
    local ec=e:GetHandler():GetPreviousEquipTarget()
    return e:GetHandler():IsReason(REASON_LOST_TARGET)
        and ec and not ec:IsLocation(LOCATION_ONFIELD+LOCATION_OVERLAY)
end
```

Use `GetPreviousEquipTarget` for this kind of trigger because by the time the
Equip Card is in the GY, `GetEquipTarget` no longer describes the old
relationship.

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

Local `c10204849.lua` uses this category: it targets a monster in the GY,
Special Summons it, then equips the Spell to that monster and registers the
equip limit during resolution. That is why the activation effect uses ordinary
card targeting for the GY monster, not the continuous target flag used by a
normal Equip Spell activation.

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
to finish as one process.

Local `c10613952.lua` uses this shape after selecting several cards from the
GY: it checks the available Spell & Trap Zones, equips each selected card with
`Duel.Equip(tp,tc,c,true,true)`, then calls `Duel.EquipComplete()` once after
the loop. Most ordinary Equip Spells call `Duel.Equip` without the stepped
argument.

## Local Scripts To Read

These scripts are useful when you need a concrete local pattern instead of a
generic template.

| Script | Why it is useful |
| --- | --- |
| `c1435851.lua` | Small ordinary Equip Spell using the local `aux.AddEquipSpellEffect` helper. |
| `c10204849.lua` | Targets a monster, Special Summons it, equips the Spell to it, then registers `EFFECT_EQUIP_LIMIT` during resolution. |
| `c10613952.lua` | Equips several cards with stepped `Duel.Equip` calls and finishes with `Duel.EquipComplete()`. |
| `c11802691.lua` | Checks `CheckEquipTarget`, `CheckUniqueOnField`, and `IsForbidden` before equipping cards chosen from another location. |
| `c11913700.lua` | Uses `GetPreviousEquipTarget` for a lost-target trigger after the Equip Card leaves the field. |

When you see an equip helper name that is not in the local API, use this table
as the starting point. The MDPro3 scripts above show the behavior that exists
in this repository.

## Common Pitfalls

| Mistake | Safer pattern |
| --- | --- |
| Equipping without checking the Spell & Trap Zone or target relation. | Check activation legality, then recheck `IsRelateToEffect` in operation. |
| Letting the target filter and equip limit drift apart accidentally. | Keep them aligned through `Auxiliary.AddEquipSpellEffect`, or document the reason and recheck the limit before `Duel.Equip`. |
| Choosing a card to become an Equip Card without zone and field-state checks. | Check `Duel.GetLocationCount`, `CheckUniqueOnField`, `IsForbidden`, and `CheckEquipTarget` when the local pattern does. |
| Registering only the ATK/DEF bonus. | Also register `EFFECT_EQUIP_LIMIT` when the card needs a legal equipped monster. |
| Treating an Equip effect as `EFFECT_TYPE_SINGLE`. | Use `EFFECT_TYPE_EQUIP` for effects applied to the equipped monster. |
| Moving a monster to the Spell & Trap Zone when the card should be equipped. | Use `Duel.Equip` for equip state; use `Duel.MoveToField` for Continuous Spell/Trap state. |
| Checking `GetEquipTarget` after the Equip Card has already left the field. | Use `GetPreviousEquipTarget` in leave-field or sent-to-GY triggers. |
| Assuming a non-applying equip bonus means the equip itself is illegal. | Separate equip legality from whether a specific continuous effect can affect that monster. |

Useful API pages:

- [`Duel.Equip`](/api/functions/Duel/Equip)
- [`Duel.EquipComplete`](/api/functions/Duel/EquipComplete)
- [`Duel.MoveToField`](/api/functions/Duel/MoveToField)
- [`Card.GetEquipTarget`](/api/functions/Card/GetEquipTarget)
- [`Card.GetPreviousEquipTarget`](/api/functions/Card/GetPreviousEquipTarget)
- [`Card.GetEquipGroup`](/api/functions/Card/GetEquipGroup)
- [`Card.CheckEquipTarget`](/api/functions/Card/CheckEquipTarget)
- [`Card.GetFirstCardTarget`](/api/functions/Card/GetFirstCardTarget)
- [`Effect.SetType`](/api/functions/Effect/SetType)
- [`Effect.SetValue`](/api/functions/Effect/SetValue)
