# RushDuel.CostSendDeckTopAnyToGrave

Alias: `RD.CostSendDeckTopAnyToGrave`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.CostSendDeckTopAnyToGrave(any desc, any min, any max, any set_label, any set_object) -> any
```

## Description

Rush Duel helper declared in `RDCost.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
代价: 从卡组上面把任意数量的卡送去墓地
```

## Parameters

- `desc` `any`: Type and behavior are not yet reviewed; see the source.
- `min` `any`: Type and behavior are not yet reviewed; see the source.
- `max` `any`: Type and behavior are not yet reviewed; see the source.
- `set_label` `any`: Type and behavior are not yet reviewed; see the source.
- `set_object` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDCost.lua:253`

```lua
function RushDuel.CostSendDeckTopAnyToGrave(desc, min, max, set_label, set_object)
    return function(e, tp, eg, ep, ev, re, r, rp, chk)
        if chk == 0 then
            return Duel.IsPlayerCanDiscardDeckAsCost(tp, min)
        end
        local ops = {}
        for i = min, max do
            if Duel.IsPlayerCanDiscardDeckAsCost(tp, i) then
                table.insert(ops, i)
            end
        end
        Duel.Hint(HINT_SELECTMSG, tp, desc)
        local count = Duel.AnnounceNumber(tp, table.unpack(ops))
        if Duel.DiscardDeck(tp, count, REASON_COST) ~= 0 and (set_label ~= nil or set_object ~= nil) then
            local og = Duel.GetOperatedGroup()
            RushDuel.SetLabelAndObject(e, og, set_label, set_object)
        end
        return true
    end
end
```
