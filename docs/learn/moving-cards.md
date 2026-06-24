# Functions That Move Cards Across Locations

Movement functions are where many scripting mistakes become visible. The target
or selected group should be legal before activation and still valid at
resolution.

## Common Movement Functions

| Function | Common destination or action |
| --- | --- |
| [`Duel.SendtoHand`](/api/functions/Duel/SendtoHand) | Add cards to the hand. |
| [`Duel.SendtoDeck`](/api/functions/Duel/SendtoDeck) | Return cards to the Deck or Extra Deck. |
| [`Duel.SendtoGrave`](/api/functions/Duel/SendtoGrave) | Send cards to the GY. |
| [`Duel.Remove`](/api/functions/Duel/Remove) | Banish cards. |
| [`Duel.Destroy`](/api/functions/Duel/Destroy) | Destroy cards. |
| [`Duel.Release`](/api/functions/Duel/Release) | Tribute or release cards. |
| [`Duel.DiscardHand`](/api/functions/Duel/DiscardHand) | Discard cards from the hand. |
| [`Duel.SpecialSummon`](/api/functions/Duel/SpecialSummon) | Special Summon a monster. |
| [`Duel.SSet`](/api/functions/Duel/SSet) | Set a Spell/Trap. |
| [`Duel.MSet`](/api/functions/Duel/MSet) | Set a monster. |
| [`Duel.Equip`](/api/functions/Duel/Equip) | Equip one card to another. |
| [`Duel.MoveToField`](/api/functions/Duel/MoveToField) | Move a card to a field location. |
| [`Duel.ReturnToField`](/api/functions/Duel/ReturnToField) | Return a temporarily banished card to the field. |
| [`Duel.Overlay`](/api/functions/Duel/Overlay) | Attach cards as Xyz Materials. |
| [`Duel.SendtoExtraP`](/api/functions/Duel/SendtoExtraP) | Put a Pendulum Card face-up in the Extra Deck. |
| [`Duel.GetControl`](/api/functions/Duel/GetControl) | Change control of cards. |

## Movement Router

Before choosing a function, identify what the card text is really doing.

| Text shape | First question | Usual family |
| --- | --- | --- |
| "add to the hand", "send to the GY", "banish", "shuffle into the Deck" | Which destination is named? | `Duel.SendtoHand`, `Duel.SendtoGrave`, `Duel.Remove`, `Duel.SendtoDeck` |
| "destroy" | Does the text specifically destroy? | `Duel.Destroy` |
| "Tribute", "release" | Is it a cost, effect, or Summon procedure? | `Duel.Release` with the matching reason |
| "discard" | Is it a discard or just send from hand to GY? | `Duel.DiscardHand` or `Duel.SendtoGrave` with discard reason |
| "Special Summon" | Which player summons it, from where, in what position? | `Duel.SpecialSummon` |
| "equip it to..." | Which card becomes the Equip Card? | `Duel.Equip` plus equip-limit effects |
| "place in the Spell & Trap Zone" or "place in the Field Zone" | Is it being moved onto the field as a card type? | `Duel.MoveToField` plus type-changing effects when needed |
| "take control" | How long does control last? | `Duel.GetControl` with reset data |

This keeps "move this card somewhere" from becoming one oversized habit. The
destination, reason, and whether the action places a card onto the field decide
the function.

## Two Movement Families

Most movement mistakes come from treating every destination as the same kind of
action. Split them into two families before writing the filter.

| Family | Examples | What the activation branch usually proves |
| --- | --- | --- |
| Destination or removal action | `Duel.SendtoHand`, `Duel.SendtoGrave`, `Duel.SendtoDeck`, `Duel.Remove`, `Duel.Release`, `Duel.DiscardHand`, `Duel.Destroy` | The card can legally leave its current place for that action, usually with a matching `Card.IsAbleTo*`, `Card.IsReleasable*`, or `Card.IsDiscardable` check. |
| Field placement or field control action | `Duel.SpecialSummon`, `Duel.SSet`, `Duel.MSet`, `Duel.Equip`, `Duel.MoveToField`, `Duel.ReturnToField`, `Duel.GetControl` | There is a usable zone and the card can legally exist there, using checks such as `Duel.GetLocationCount`, `Duel.GetLocationCountFromEx`, `Card.IsCanBeSpecialSummoned`, `Card.IsSSetable`, `Card.IsMSetable`, `not c:IsForbidden()`, `Card.CheckUniqueOnField`, or `Card.IsControlerCanBeChanged`. |

The second family changes the field layout, so it is more sensitive to Chain
changes. A free Monster Zone, Spell & Trap Zone, Field Zone replacement, or
equip target can disappear before resolution. Local scripts commonly check the
zone in `chk==0`, then check again in the operation before moving the card.

## Check The Card Can Move

Movement filters should use the matching "able to" helper when one exists.

| Action | Common filter check |
| --- | --- |
| Add to hand | `c:IsAbleToHand()` |
| Send to GY | `c:IsAbleToGrave()` or `c:IsAbleToGraveAsCost()` |
| Return to Deck | `c:IsAbleToDeck()` or `c:IsAbleToExtra()` depending on the effect |
| Return to Deck/Extra Deck as cost | `c:IsAbleToDeckAsCost()`, `c:IsAbleToExtraAsCost()`, or `c:IsAbleToDeckOrExtraAsCost()` |
| Banish | `c:IsAbleToRemove()` or `c:IsAbleToRemoveAsCost()` |
| Tribute/release | `c:IsReleasableByEffect()` for effects, `c:IsReleasable()` for costs/procedures |
| Discard | `c:IsDiscardable(REASON_EFFECT)` for effects, `c:IsDiscardable(REASON_COST)` or `c:IsDiscardable()` for costs |
| Set Spell/Trap | `c:IsSSetable()` |
| Set monster | `c:IsMSetable(...)` |
| Special Summon | `c:IsCanBeSpecialSummoned(...)` |
| Equip | target is face-up and the Equip Card can legally equip to it |
| Attach as Xyz Material | `c:IsCanOverlay(player)` when that local check applies |
| Change control | `c:IsControlerCanBeChanged(...)` |

Cost filters should use cost-specific helpers where available. A card that can
be sent to the GY by effect is not automatically legal to send as cost.

Destroying is a special case: many effects can be legally activated even if the
chosen card may not actually be destroyed by the resolving effect. Use
`Card.IsDestructable` only when the card text or local pattern specifically
needs that pre-check.

## Targeted Card Pattern

```lua
function s.operation(e,tp,eg,ep,ev,re,r,rp)
    local tc=Duel.GetFirstTarget()
    if tc and tc:IsRelateToEffect(e) then
        Duel.SendtoHand(tc,nil,REASON_EFFECT)
    end
end
```

If the operation has one official target, `Duel.GetFirstTarget()` is usually
the clearest read. Always check relation before moving the target.

## Multi-Target Pattern

```lua
function s.operation(e,tp,eg,ep,ev,re,r,rp)
    local g=Duel.GetTargetsRelateToChain()
    if #g>0 then
        Duel.Destroy(g,REASON_EFFECT)
    end
end
```

For multi-target effects, prefer a relation-aware group helper or filter the
target group yourself.

```lua
local tg=Duel.GetChainInfo(0,CHAININFO_TARGET_CARDS)
local rg=tg:Filter(Card.IsRelateToEffect,nil,e)
```

## Non-Targeting Selection Pattern

Non-targeting effects usually select during operation, not during the target
callback.

```lua
function s.operation(e,tp,eg,ep,ev,re,r,rp)
    Duel.Hint(HINT_SELECTMSG,tp,HINTMSG_REMOVE)
    local g=Duel.SelectMatchingCard(tp,s.filter,tp,LOCATION_GRAVE,0,1,1,nil)
    if #g>0 then
        Duel.Remove(g,POS_FACEUP,REASON_EFFECT)
    end
end
```

Use this when card text says "choose" or performs a selection without targeting.

## Location-To-Location Actions

Many movement functions can move cards from any legal starting location, but
the script still needs to choose the right timing and legality checks.

| Source situation | Typical call |
| --- | --- |
| A card in Deck/GY/banished should go to hand. | `Duel.SendtoHand(g,nil,REASON_EFFECT)` |
| A card should go to the GY without being destroyed. | `Duel.SendtoGrave(g,REASON_EFFECT)` |
| A card should be banished face-up. | `Duel.Remove(g,POS_FACEUP,REASON_EFFECT)` |
| A card should be Tributed/released. | `Duel.Release(g,REASON_EFFECT)` or `Duel.Release(g,REASON_COST)` |
| A card should be discarded. | `Duel.SendtoGrave(g,REASON_DISCARD+REASON_EFFECT)` or `Duel.DiscardHand(...)` |
| A monster should be Special Summoned. | `Duel.SpecialSummon(tc,0,tp,tp,false,false,POS_FACEUP)` |
| A Spell/Trap should be Set. | `Duel.SSet(tp,tc)` |
| A card should become an Equip Card. | `Duel.Equip(tp,eqc,tc)` |
| A card should become a Continuous Spell/Trap. | `Duel.MoveToField(...)` plus `EFFECT_CHANGE_TYPE` when needed |
| A temporarily banished card should return. | `Duel.ReturnToField(tc)` after an earlier temporary `Duel.Remove` flow |
| A Pendulum Card should go face-up to the Extra Deck. | `Duel.SendtoExtraP(tc,tp,REASON_EFFECT)` |
| A card should change controller. | `Duel.GetControl(tc,tp,reset_phase,reset_count)` |

If an action places a card onto the field, check available zones before
activation and again during resolution if the Chain can change them.

Local scripts show the same routing in different card types:

- `c1003840.lua` releases monsters, Special Summons the handler, then returns a
  card to the Deck with `Duel.SendtoDeck`.
- `c10204849.lua` uses `Duel.Equip` for an effect that turns a card into an
  Equip Card.
- `c1050355.lua` uses `Duel.MoveToField` when a card is placed into the Field
  Zone.
- `c99742859.lua` uses `Duel.SpecialSummonStep` and
  `Duel.SpecialSummonComplete` when two monsters are Summoned in one grouped
  process.

## Special Summon Movement

Special Summon checks usually mirror the later summon call.

```lua
function s.spfilter(c,e,tp)
    return c:IsCanBeSpecialSummoned(e,0,tp,false,false,POS_FACEUP,tp)
end

function s.sptg(e,tp,eg,ep,ev,re,r,rp,chk)
    if chk==0 then
        return Duel.GetLocationCount(tp,LOCATION_MZONE)>0
            and Duel.IsExistingMatchingCard(s.spfilter,tp,LOCATION_GRAVE,0,1,nil,e,tp)
    end
    Duel.SetOperationInfo(0,CATEGORY_SPECIAL_SUMMON,nil,1,tp,LOCATION_GRAVE)
end
```

Check zones and summon legality before activation. During resolution, check the
zone again if the effect depends on it.

## Equip and MoveToField

Equip effects often move a card to the Spell & Trap Zone, then register equip
effects and equip limits.

```lua
local tc=Duel.GetFirstTarget()
if c:IsRelateToEffect(e) and tc and tc:IsRelateToEffect(e) then
    Duel.Equip(tp,c,tc)
end
```

`Duel.MoveToField` is used when a card becomes a Continuous Spell/Trap, is put
in a Field Zone, or otherwise moves to a specific field location.

For the full equip flow, see [Equip Spells and Equip Cards](equip-spells).

## Temporary Banish and ReturnToField

`Duel.ReturnToField` is for cards that were temporarily banished, not a generic
"put this card back" helper. The earlier banish should include
`REASON_TEMPORARY`, then a later registered effect returns the same stored card.

Local `c10960419.lua` uses that shape:

```lua
if Duel.Remove(tc,0,REASON_EFFECT+REASON_TEMPORARY)~=0 then
    -- register the delayed return watcher and store tc on it
end
```

The delayed operation then returns the stored card:

```lua
function s.retop(e,tp,eg,ep,ev,re,r,rp)
    local tc=e:GetLabelObject()
    Duel.ReturnToField(tc)
end
```

Do not replace a normal Special Summon, Set, or `MoveToField` action with
`ReturnToField`. Use it when the script has a real temporary-banish lifecycle
to close.

## Change Control

Changing control uses `Duel.GetControl` in this local API, despite the name
reading like a getter.

```lua
function s.ctltg(e,tp,eg,ep,ev,re,r,rp,chk,chkc)
    if chkc then return chkc:IsControler(1-tp) and chkc:IsLocation(LOCATION_MZONE)
        and chkc:IsControlerCanBeChanged() end
    if chk==0 then
        return Duel.IsExistingTarget(Card.IsControlerCanBeChanged,tp,0,LOCATION_MZONE,1,nil)
    end
    Duel.Hint(HINT_SELECTMSG,tp,HINTMSG_CONTROL)
    local g=Duel.SelectTarget(tp,Card.IsControlerCanBeChanged,tp,0,LOCATION_MZONE,1,1,nil)
    Duel.SetOperationInfo(0,CATEGORY_CONTROL,g,1,0,0)
end
```

Do not confuse `IsControlerCanBeChanged` with `IsAbleToChangeControler`. The
former checks whether a control-change action can be applied; the latter is
used by some movement-like actions where controler/possession changes as part
of another operation.

## Return Values

Many movement functions return how many cards moved or whether the action
succeeded. Local scripts often use that return value before applying the next
part of an effect.

```lua
if Duel.SpecialSummon(c,0,tp,tp,false,false,POS_FACEUP)>0 then
    Duel.GetControl(tc,tp)
end
```

Do not assume the intended card moved. Relation checks, immunity, replacement
effects, and zone changes can all affect the final result.

## Reason Matters

The reason flag tells the engine why the move happened: `REASON_EFFECT`,
`REASON_COST`, `REASON_RELEASE`, `REASON_MATERIAL`, and similar constants affect
triggers and replacement effects.

```lua
Duel.SendtoGrave(g,REASON_EFFECT)
Duel.Release(g,REASON_COST)
Duel.SendtoDeck(mat,nil,SEQ_DECKSHUFFLE,REASON_EFFECT+REASON_MATERIAL+REASON_FUSION)
```

Use the reason that matches the card text and mechanic.

Useful API pages:

- [`Duel.SendtoHand`](/api/functions/Duel/SendtoHand)
- [`Duel.SendtoDeck`](/api/functions/Duel/SendtoDeck)
- [`Duel.SendtoGrave`](/api/functions/Duel/SendtoGrave)
- [`Duel.Remove`](/api/functions/Duel/Remove)
- [`Duel.Destroy`](/api/functions/Duel/Destroy)
- [`Duel.Release`](/api/functions/Duel/Release)
- [`Duel.DiscardHand`](/api/functions/Duel/DiscardHand)
- [`Duel.SpecialSummon`](/api/functions/Duel/SpecialSummon)
- [`Duel.SpecialSummonStep`](/api/functions/Duel/SpecialSummonStep)
- [`Duel.SpecialSummonComplete`](/api/functions/Duel/SpecialSummonComplete)
- [`Duel.SSet`](/api/functions/Duel/SSet)
- [`Duel.MSet`](/api/functions/Duel/MSet)
- [`Duel.Equip`](/api/functions/Duel/Equip)
- [`Duel.MoveToField`](/api/functions/Duel/MoveToField)
- [`Duel.ReturnToField`](/api/functions/Duel/ReturnToField)
- [`Duel.Overlay`](/api/functions/Duel/Overlay)
- [`Duel.SendtoExtraP`](/api/functions/Duel/SendtoExtraP)
- [`Duel.GetControl`](/api/functions/Duel/GetControl)
