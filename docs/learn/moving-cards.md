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

## Resolution Pattern

```lua
local tc=Duel.GetFirstTarget()
if tc and tc:IsRelateToEffect(e) then
  Duel.SendtoHand(tc,nil,REASON_EFFECT)
end
```

For groups:

```lua
local tg=Duel.GetChainInfo(0,CHAININFO_TARGET_CARDS)
local rg=tg:Filter(Card.IsRelateToEffect,nil,e)
if rg:GetCount()>0 then
  Duel.SendtoDeck(rg,nil,SEQ_DECKSHUFFLE,REASON_EFFECT)
end
```

## Reason Matters

The reason flag tells the engine why the move happened: `REASON_EFFECT`,
`REASON_COST`, `REASON_RELEASE`, and similar constants affect triggers and
replacement effects. Check [constants](/api/constants) when the reason matters.
