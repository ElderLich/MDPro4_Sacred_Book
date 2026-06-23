# Counters

Counters are visible numbers placed on cards. Spell Counters, Kaiju Counters,
Guard Counters, A-Counters, Predator Counters, and many archetype counters all
use the same core shape: a card must be allowed to hold that counter type, an
effect adds or removes a count, and later effects read the count.

Do not confuse card counters with Counter Trap Cards. Counter Traps use
`TYPE_COUNTER`; card counters use functions such as
[`Card.AddCounter`](/api/functions/Card/AddCounter).

## The Basic Pattern

Most counter cards follow this order:

1. Permit the card to hold the counter type.
2. Optionally set a maximum count.
3. Add counters in an operation.
4. Read or remove those counters later.

```lua
function s.initial_effect(c)
    c:EnableCounterPermit(0x1)
    c:SetCounterLimit(0x1,4)

    local e1=Effect.CreateEffect(c)
    e1:SetCategory(CATEGORY_COUNTER)
    e1:SetType(EFFECT_TYPE_SINGLE+EFFECT_TYPE_TRIGGER_F)
    e1:SetCode(EVENT_SUMMON_SUCCESS)
    e1:SetTarget(s.cttg)
    e1:SetOperation(s.ctop)
    c:RegisterEffect(e1)
end

function s.cttg(e,tp,eg,ep,ev,re,r,rp,chk)
    if chk==0 then return true end
    Duel.SetOperationInfo(0,CATEGORY_COUNTER,nil,1,0,0x1)
end

function s.ctop(e,tp,eg,ep,ev,re,r,rp)
    local c=e:GetHandler()
    if c:IsRelateToEffect(e) then
        c:AddCounter(0x1,1)
    end
end
```

That shape is based on Defender, the Magical Knight (`c2525268.lua`), which
permits Spell Counters (`0x1`), limits itself to 1 Spell Counter, and adds one
when it is Normal Summoned.

## Counter Types

Counter types are integer IDs. Local scripts usually use hexadecimal values:

| Counter type | Common local use |
| --- | --- |
| `0x1` | Spell Counters |
| `0x37` | Kaiju Counters |
| `0x54` | The World Legacy's counters |
| `0x100e`, `0x1019`, and similar values | Counter IDs that include extra flag bits. |

Always pass the same counter type to every related function. A card that holds
`0x1` counters does not have `0x37` counters.

The local constants also define `COUNTER_WITHOUT_PERMIT = 0x1000`. The core
uses that flag to allow a counter type to be placed without an
`EFFECT_COUNTER_PERMIT` effect. `COUNTER_NEED_ENABLE` is present in
`constant.lua` but marked `N/A` and commented out in the local core header, so
do not build new Sacred Book examples around it.

## Permitting Counters

[`Card.EnableCounterPermit`](/api/functions/Card/EnableCounterPermit) registers
the permit effect that lets a card hold a counter type:

```lua
c:EnableCounterPermit(0x1)
```

If you omit the location, the local binding chooses a default:

| Card kind | Default permit range |
| --- | --- |
| Monster | `LOCATION_MZONE` |
| Non-monster | `LOCATION_SZONE+LOCATION_FZONE` |

Pendulum Monsters often need an explicit range because they can exist in either
the Monster Zone or Pendulum Zone. Magical Abductor (`c10239627.lua`) uses:

```lua
c:EnableCounterPermit(0x1,LOCATION_PZONE+LOCATION_MZONE)
```

The permit can also take a condition callback, but most beginner scripts only
need the counter type and location.

## Counter Limits

[`Card.SetCounterLimit`](/api/functions/Card/SetCounterLimit) creates an
`EFFECT_COUNTER_LIMIT` for one counter type:

```lua
c:SetCounterLimit(0x37,5)
```

The Kaiju Files (`c11163040.lua`) uses that pattern to cap Kaiju Counters at
5. Arcane Barrier (`c17896384.lua`) caps Spell Counters at 4.

Limits are checked by
[`Card.IsCanAddCounter`](/api/functions/Card/IsCanAddCounter) and
[`Card.AddCounter`](/api/functions/Card/AddCounter). If the addition would go
over the limit, a normal add fails.

## Adding Several Counters With `singly`

The fourth argument to `Card.AddCounter` is `singly`. When it is true, the core
allows a partial add up to the remaining limit.

The World Legacy (`c92562411.lua`) counts how many face-up Level 5 or higher
monsters went from the Monster Zone to the GY, then tries to add that many
counters one by one up to its limit of 7:

```lua
function c92562411.ctop(e,tp,eg,ep,ev,re,r,rp)
    local ct=eg:FilterCount(c92562411.ctfilter,nil)
    if ct>0 then
        e:GetHandler():AddCounter(0x54,ct,true)
    end
end
```

Without `true`, adding 3 counters to a card that only has 2 free counter slots
would fail. With `true`, the core can add the 2 that fit.

## Checking Before You Add

Use the check that matches the question you are asking:

| Question | Function |
| --- | --- |
| Can this face-up card currently receive these counters? | [`Card.IsCanAddCounter`](/api/functions/Card/IsCanAddCounter) |
| Does this card have a counter permit at all, even if it is not currently face-up on the field? | [`Card.IsCanHaveCounter`](/api/functions/Card/IsCanHaveCounter) |
| Is the player allowed to place counters, ignoring the card's own permit and limit checks? | [`Duel.IsCanAddCounter`](/api/functions/Duel/IsCanAddCounter) |

For targets already on the field, local scripts usually filter with
`Card.IsCanAddCounter`:

```lua
Duel.SelectTarget(tp,Card.IsCanAddCounter,tp,LOCATION_MZONE,LOCATION_MZONE,1,1,nil,0x1019,1)
```

For cards that will be Special Summoned and then receive a counter, the card is
not face-up on the field yet. Servant of Endymion (`c92559258.lua`) combines
the permit check with the player-level check:

```lua
function c92559258.spfilter(c,e,tp)
    return c:IsAttackAbove(1000) and c:IsCanHaveCounter(0x1)
        and Duel.IsCanAddCounter(tp,0x1,1,c)
        and c:IsCanBeSpecialSummoned(e,0,tp,false,false)
end
```

After the cards are Special Summoned, the script adds the counters:

```lua
for tc in aux.Next(g) do
    tc:AddCounter(0x1,1)
end
```

## Adding Counters At Resolution

Counter effects still need ordinary resolution discipline. Recheck that the
card is related to the effect, and recheck `IsCanAddCounter` when the target
could have changed.

Power of the Guardians (`c1118137.lua`) adds one Spell Counter to itself when
the equipped monster battles:

```lua
function c1118137.ctop(e,tp,eg,ep,ev,re,r,rp)
    if e:GetHandler():IsRelateToEffect(e) then
        e:GetHandler():AddCounter(0x1,1)
    end
end
```

Servant of Endymion adds counters to every eligible card you control:

```lua
local g=Duel.GetMatchingGroup(Card.IsCanAddCounter,tp,LOCATION_ONFIELD,0,c,0x1,1)
if c:IsRelateToEffect(e) then g:AddCard(c) end
for tc in aux.Next(g) do
    if tc:IsCanAddCounter(0x1,1) then
        tc:AddCounter(0x1,1)
    end
end
```

That second check inside the loop is not wasted. A card can stop being a legal
recipient between target checking and resolution.

## Reading Counters

[`Card.GetCounter`](/api/functions/Card/GetCounter) returns how many counters
of one type are on one card:

```lua
function c10239627.atkval(e,c)
    return e:GetHandler():GetCounter(0x1)*100
end
```

Magical Abductor uses this for its ATK gain while it is in the Monster Zone.
Power of the Guardians uses the same pattern for its equip bonus:

```lua
function c1118137.atkval(e,c)
    return e:GetHandler():GetCounter(0x1)*500
end
```

[`Duel.GetCounter`](/api/functions/Duel/GetCounter) totals counters of one
type across field locations:

```lua
local ct=Duel.GetCounter(tp,1,0,0x1)
```

The `s` and `o` parameters are location masks from the chosen player's
perspective: `s` for that player's field and `o` for the opponent's field.
Local scripts often use `1,0` for your field, or `1,1` for both sides.

Sharp edge: in this local core, `Card.GetCounter(c,0)` returns the number of
different counter types currently on `c`, not the total number of all counters
on that card. Use a real counter type when you need a count.

## Removing Counters From One Card

Use [`Card.IsCanRemoveCounter`](/api/functions/Card/IsCanRemoveCounter) in the
cost or target check, then
[`Card.RemoveCounter`](/api/functions/Card/RemoveCounter) when you actually
pay or resolve the removal:

```lua
function c10239627.thcost(e,tp,eg,ep,ev,re,r,rp,chk)
    local c=e:GetHandler()
    if chk==0 then return c:IsCanRemoveCounter(tp,0x1,3,REASON_COST) end
    c:RemoveCounter(tp,0x1,3,REASON_COST)
end
```

That pattern removes 3 Spell Counters from Magical Abductor itself. Use
`REASON_COST` for costs, and `REASON_EFFECT` for removal performed by the
effect's resolution.

`Card.RemoveCounter(c,player,0,count,reason)` is a special local binding path:
when `countertype` is `0`, it clears every counter type on that card and
returns no Lua value. For normal scripts, prefer a specific counter type.

## Removing Counters From The Field

[`Duel.RemoveCounter`](/api/functions/Duel/RemoveCounter) removes counters from
allowed field locations. It can prompt the player to choose which cards supply
the counters.

Defender, the Magical Knight protects face-up Spellcaster monsters by removing
one Spell Counter for each monster that would be destroyed:

```lua
function c2525268.destg(e,tp,eg,ep,ev,re,r,rp,chk)
    if chk==0 then
        local count=eg:FilterCount(c2525268.dfilter,nil)
        e:SetLabel(count)
        return count>0 and Duel.IsCanRemoveCounter(tp,1,0,0x1,count,REASON_COST)
    end
    return Duel.SelectEffectYesNo(tp,e:GetHandler(),96)
end

function c2525268.desop(e,tp,eg,ep,ev,re,r,rp)
    Duel.RemoveCounter(tp,1,0,0x1,e:GetLabel(),REASON_COST)
end
```

Power of the Guardians also uses field-wide removal for its destroy
replacement:

```lua
Duel.RemoveCounter(tp,1,0,0x1,1,REASON_EFFECT+REASON_REPLACE)
```

There is no public `Duel.SelectCounter` Lua function in this local binding. The
selection is an internal processor used by `Duel.RemoveCounter`.

## Removal Replacement

`EFFECT_RCOUNTER_REPLACE + countertype` is a continuous effect code that can
replace counter removal. Magical Citadel of Endymion (`c39910367.lua`) uses it
for Spell Counters:

```lua
local e4=Effect.CreateEffect(c)
e4:SetDescription(aux.Stringid(39910367,0))
e4:SetType(EFFECT_TYPE_CONTINUOUS+EFFECT_TYPE_FIELD)
e4:SetCode(EFFECT_RCOUNTER_REPLACE+0x1)
e4:SetRange(LOCATION_FZONE)
e4:SetCountLimit(1)
e4:SetCondition(c39910367.rcon)
e4:SetOperation(c39910367.rop)
c:RegisterEffect(e4)
```

Its condition checks that the removal is for a cost paid by its owner and that
Magical Citadel has enough counters to replace that removal:

```lua
function c39910367.rcon(e,tp,eg,ep,ev,re,r,rp)
    return re:IsActivated() and bit.band(r,REASON_COST)~=0
        and ep==e:GetOwnerPlayer()
        and e:GetHandler():GetCounter(0x1)>=ev
end
```

The operation removes the counters from Magical Citadel instead:

```lua
function c39910367.rop(e,tp,eg,ep,ev,re,r,rp)
    e:GetHandler():RemoveCounter(ep,0x1,ev,REASON_EFFECT)
end
```

The local core looks for these replacement effects when checking and resolving
counter removal.

## Counter Events

The core raises typed events by adding the counter type to the base event:

| Event shape | Meaning |
| --- | --- |
| `EVENT_ADD_COUNTER + countertype` | Counters of that type were added. |
| `EVENT_REMOVE_COUNTER + countertype` | Counters of that type were removed. |

`Card.AddCounter` raises the add-counter event after writing the counter
change. The local remove-counter processor raises the remove-counter event
after typed removal is processed.

Most beginner scripts do not need to raise these events manually. Prefer the
counter APIs unless you are working on a very unusual manual counter movement.

## Counter Lifecycle

Counters are attached to the card's current on-field state. In the local core,
ordinary counters are cleared when the card moves to the hand, Deck, GY,
banished zone, overlay state, changes monster/Spell & Trap status, returns to
the field, or is turned face-down. On disable resets, permit-based counters are
also removed, while `COUNTER_WITHOUT_PERMIT` counters are preserved.

If a card effect needs to preserve a counter count while moving itself, record
the count before the move and add it back afterward. Servant of Endymion stores
its Spell Counter count before it leaves the Monster Zone, then restores those
counters if it is placed into the Pendulum Zone:

```lua
function c92559258.regop(e,tp,eg,ep,ev,re,r,rp)
    e:GetLabelObject():SetLabel(e:GetHandler():GetCounter(0x1))
end

function c92559258.penop(e,tp,eg,ep,ev,re,r,rp)
    local c=e:GetHandler()
    local ct=e:GetLabel()
    if c:IsRelateToEffect(e) and Duel.MoveToField(c,tp,tp,LOCATION_PZONE,POS_FACEUP,true)
        and ct>0 then
        c:AddCounter(0x1,ct)
    end
end
```

## Common Pitfalls

| Mistake | Better habit |
| --- | --- |
| Calling `AddCounter` without permitting that counter type. | Register `EnableCounterPermit` first, unless the counter type intentionally uses `COUNTER_WITHOUT_PERMIT`. |
| Using the default permit range on a Pendulum Monster that needs counters in both zones. | Pass `LOCATION_PZONE+LOCATION_MZONE` explicitly. |
| Treating `Duel.IsCanAddCounter` as a full card legality check. | Use `Card.IsCanAddCounter` for face-up cards already on the field; combine `Card.IsCanHaveCounter` with `Duel.IsCanAddCounter` for cards that will receive counters after being placed or Summoned. |
| Forgetting counter limits. | Use `SetCounterLimit`, and use `AddCounter(..., true)` when partial addition up to the limit is correct. |
| Reading `Card.GetCounter(c,0)` as a total count. | Pass the exact counter type; local `0` returns the number of counter types. |
| Removing counters from the wrong place. | Use `Card.RemoveCounter` for one known card and `Duel.RemoveCounter` for a field-wide pool. |
| Expecting counters to survive card movement. | Record the count before the move and restore it after the card reaches the new valid zone. |

## Useful API Pages

- [`Card.EnableCounterPermit`](/api/functions/Card/EnableCounterPermit)
- [`Card.SetCounterLimit`](/api/functions/Card/SetCounterLimit)
- [`Card.AddCounter`](/api/functions/Card/AddCounter)
- [`Card.RemoveCounter`](/api/functions/Card/RemoveCounter)
- [`Card.GetCounter`](/api/functions/Card/GetCounter)
- [`Card.IsCanAddCounter`](/api/functions/Card/IsCanAddCounter)
- [`Card.IsCanRemoveCounter`](/api/functions/Card/IsCanRemoveCounter)
- [`Card.IsCanHaveCounter`](/api/functions/Card/IsCanHaveCounter)
- [`Duel.IsCanAddCounter`](/api/functions/Duel/IsCanAddCounter)
- [`Duel.RemoveCounter`](/api/functions/Duel/RemoveCounter)
- [`Duel.IsCanRemoveCounter`](/api/functions/Duel/IsCanRemoveCounter)
- [`Duel.GetCounter`](/api/functions/Duel/GetCounter)
- [`Duel.SetOperationInfo`](/api/functions/Duel/SetOperationInfo)
- [`Duel.MoveToField`](/api/functions/Duel/MoveToField)
- [`Effect.SetCode`](/api/functions/Effect/SetCode)
- [`Effect.SetRange`](/api/functions/Effect/SetRange)
