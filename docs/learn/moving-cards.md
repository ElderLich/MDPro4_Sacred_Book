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
| [`Duel.SpecialSummon`](/api/functions/Duel/SpecialSummon) | Special Summon a monster. |
| [`Duel.SSet`](/api/functions/Duel/SSet) | Set a Spell/Trap. |
| [`Duel.MSet`](/api/functions/Duel/MSet) | Set a monster. |
| [`Duel.Equip`](/api/functions/Duel/Equip) | Equip one card to another. |
| [`Duel.MoveToField`](/api/functions/Duel/MoveToField) | Move a card to a field location. |
| [`Duel.Overlay`](/api/functions/Duel/Overlay) | Attach cards as Xyz Materials. |

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
