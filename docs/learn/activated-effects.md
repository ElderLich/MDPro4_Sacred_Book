# Activated Effects

Activated effects are effects that create a Chain Link. The activation and the
resolution are separate moments: the player activates the effect, costs and
targets are handled, other effects may be chained, and only later does the
operation resolve.

This distinction is the reason most activated effects are written with the
same callback shape:

```lua
e1:SetCondition(s.condition)
e1:SetCost(s.cost)
e1:SetTarget(s.target)
e1:SetOperation(s.operation)
```

Not every effect needs every callback. A simple effect may only need `target`
and `operation`; a continuous effect may use none of them.

## The Chain Link Shape

An activated effect usually has four practical layers.

| Layer | Job |
| --- | --- |
| Type and timing | `SetType`, `SetCode`, `SetRange`, and properties decide when the effect may be activated. |
| Legality | `condition`, `cost`, and `target` answer whether activation is legal right now. |
| Activation data | The non-check branch selects targets, stores labels, and announces operation info. |
| Resolution | `operation` performs the action if the required cards and zones are still valid. |

The target and cost functions receive `chk`. When `chk==0`, the engine is only
asking if the effect can be activated. Do not pay costs, select cards, or move
cards in that branch.

## Common Activated Types

| Effect type | Typical use |
| --- | --- |
| `EFFECT_TYPE_ACTIVATE` | Activating a Spell/Trap Card. |
| `EFFECT_TYPE_IGNITION` | Optional Main Phase effects the turn player chooses to activate. |
| `EFFECT_TYPE_TRIGGER_O` | Optional effects that activate after an event. |
| `EFFECT_TYPE_TRIGGER_F` | Mandatory effects that activate after an event. |
| `EFFECT_TYPE_QUICK_O` | Optional fast effects that can be chained at the right timing. |
| `EFFECT_TYPE_QUICK_F` | Mandatory fast effects that the engine should force when their timing is reached. |

These are usually combined with `EFFECT_TYPE_SINGLE` or `EFFECT_TYPE_FIELD`
when the effect belongs to a monster or watches events from a range.

The `_O` suffix means optional. The `_F` suffix means forced or mandatory.
That suffix changes the legality habit: optional effects usually need a real
legal outcome in `chk==0`, while mandatory triggers often activate because the
event happened and then resolve as much as they can.

Trigger effects are Spell Speed 1 unless another rule or card text says
otherwise. Quick effects are Spell Speed 2 and are the usual script form for
monster "(Quick Effect)" text. If multiple Trigger Effects want to activate at
the same time, the Duel engine handles the Chain-building order; the script's
job is to declare the correct type, event code, range, and optional/mandatory
status.

```lua
local e1=Effect.CreateEffect(c)
e1:SetDescription(aux.Stringid(id,0))
e1:SetCategory(CATEGORY_DESTROY)
e1:SetType(EFFECT_TYPE_IGNITION)
e1:SetProperty(EFFECT_FLAG_CARD_TARGET)
e1:SetRange(LOCATION_MZONE)
e1:SetCountLimit(1,id)
e1:SetTarget(s.destg)
e1:SetOperation(s.desop)
c:RegisterEffect(e1)
```

## Activation Is Not Resolution

Scripts should check activation legality before the Chain Link is created, then
check the live game state again during resolution.

```lua
function s.destg(e,tp,eg,ep,ev,re,r,rp,chk,chkc)
    if chkc then return chkc:IsLocation(LOCATION_MZONE) and s.filter(chkc) end
    if chk==0 then
        return Duel.IsExistingTarget(s.filter,tp,0,LOCATION_MZONE,1,nil)
    end
    Duel.Hint(HINT_SELECTMSG,tp,HINTMSG_DESTROY)
    local g=Duel.SelectTarget(tp,s.filter,tp,0,LOCATION_MZONE,1,1,nil)
    Duel.SetOperationInfo(0,CATEGORY_DESTROY,g,1,0,0)
end

function s.desop(e,tp,eg,ep,ev,re,r,rp)
    local tc=Duel.GetFirstTarget()
    if tc and tc:IsRelateToEffect(e) then
        Duel.Destroy(tc,REASON_EFFECT)
    end
end
```

`Duel.SelectTarget` registers official Chain targets. `Duel.GetFirstTarget`
reads them at resolution. `Card.IsRelateToEffect` protects the operation from a
target that left the place the effect expected.

## Quick Effect Legality

Quick Effects need both the correct type and the correct timing checks. A
typical response effect uses `EFFECT_TYPE_QUICK_O`, an event such as
`EVENT_CHAINING`, a range, and a condition that inspects the Chain Link being
answered.

Cyber Dragon Infinity (`c10443957.lua`) is a compact local example:

```lua
e3:SetCategory(CATEGORY_NEGATE+CATEGORY_DESTROY)
e3:SetType(EFFECT_TYPE_QUICK_O)
e3:SetCode(EVENT_CHAINING)
e3:SetProperty(EFFECT_FLAG_DAMAGE_STEP+EFFECT_FLAG_DAMAGE_CAL)
e3:SetRange(LOCATION_MZONE)
e3:SetCondition(c10443957.discon)
e3:SetCost(c10443957.discost)
e3:SetTarget(c10443957.distg)
e3:SetOperation(c10443957.disop)

function c10443957.discon(e,tp,eg,ep,ev,re,r,rp)
    return not e:GetHandler():IsStatus(STATUS_BATTLE_DESTROYED)
        and Duel.IsChainNegatable(ev)
end
```

The condition is not doing the whole timing job by itself. `SetType`,
`SetCode`, `SetRange`, and `SetProperty` make the effect available at the broad
timing; the condition rejects the current Chain Link when this particular card
should not respond.

## Optional Trigger Effects

Optional triggers should only activate when their effect can make a legal
attempt. They usually check the event group, location, and available action.

```lua
function s.thcon(e,tp,eg,ep,ev,re,r,rp)
    return eg:IsExists(Card.IsControler,1,nil,tp)
end

function s.thtg(e,tp,eg,ep,ev,re,r,rp,chk)
    if chk==0 then
        return Duel.IsExistingMatchingCard(s.thfilter,tp,LOCATION_DECK,0,1,nil)
    end
    Duel.SetOperationInfo(0,CATEGORY_TOHAND,nil,1,tp,LOCATION_DECK)
end
```

When the text targets, the target callback should include a `chkc` branch. When
the text does not target, the operation often selects the card at resolution
instead.

## Mandatory Trigger Effects

Mandatory triggers are different. Once their event happens, they normally
activate even if part of the later action may fail. For that reason, the
legality branch can be very small.

```lua
function s.mandtarg(e,tp,eg,ep,ev,re,r,rp,chk)
    if chk==0 then return true end
    Duel.SetOperationInfo(0,CATEGORY_DAMAGE,nil,0,1-tp,500)
end
```

The operation still needs resolution checks. Mandatory activation does not make
an impossible action become possible.

## Spell/Trap Activation

Spell and Trap Cards that activate normally use `EFFECT_TYPE_ACTIVATE` and a
timing code such as `EVENT_FREE_CHAIN`.

```lua
local e1=Effect.CreateEffect(c)
e1:SetCategory(CATEGORY_DRAW)
e1:SetType(EFFECT_TYPE_ACTIVATE)
e1:SetCode(EVENT_FREE_CHAIN)
e1:SetTarget(s.drtg)
e1:SetOperation(s.drop)
c:RegisterEffect(e1)
```

For Equip Spells, Field Spells, and Continuous Spells/Traps, the activation
effect may only place the card on the field; the card's continuous effects are
registered as separate effects on the same handler.

For the card-type differences, continue into [Spell Card Patterns](spell-card-patterns)
and [Trap Card Patterns](trap-card-patterns).

## Quick Checklist

Before an activated effect is finished, check:

1. Does `SetType` match the effect's timing and Chain behavior?
2. Does `SetRange` match where the handler must be to activate?
3. Does the `chk==0` branch only check legality?
4. If the effect targets, does it use `Duel.SelectTarget` and relation checks?
5. Does `SetOperationInfo` describe the action that can really happen?
6. Does the operation recheck targets, zones, and summoned card legality?

Related lessons:

- [Activation legality](activation-legality)
- [Spell Card Patterns](spell-card-patterns)
- [Trap Card Patterns](trap-card-patterns)
- [Targeting flow](targeting-flow)
- [Cost, target, and operation lifecycle](cost-target-operation-lifecycle)
- [EFFECT_TYPE constants and templates](effect-types)

Relevant API pages:

- [`Effect.SetType`](/api/functions/Effect/SetType)
- [`Effect.SetCode`](/api/functions/Effect/SetCode)
- [`Effect.SetProperty`](/api/functions/Effect/SetProperty)
- [`Duel.IsChainNegatable`](/api/functions/Duel/IsChainNegatable)
- [`Card.IsStatus`](/api/functions/Card/IsStatus)
