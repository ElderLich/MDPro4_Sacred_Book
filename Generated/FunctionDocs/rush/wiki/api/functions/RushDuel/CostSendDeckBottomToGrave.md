# RushDuel.CostSendDeckBottomToGrave

Alias: `RD.CostSendDeckBottomToGrave`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.CostSendDeckBottomToGrave(any count, any set_label, any set_object) -> any
```

## Description

Rush Duel helper declared in `RDCost.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
代价: 从卡组下面把卡送去墓地
```

## Parameters

- `count` `any`: Type and behavior are not yet reviewed; see the source.
- `set_label` `any`: Type and behavior are not yet reviewed; see the source.
- `set_object` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDCost.lua:274`

```lua
function RushDuel.CostSendDeckBottomToGrave(count, set_label, set_object)
    return function(e, tp, eg, ep, ev, re, r, rp, chk)
        if chk == 0 then
            return Duel.IsPlayerCanDiscardDeckAsCost(tp, count)
        end
        local dg = RushDuel.GetDeckBottomGroup(tp, count)
        Duel.DisableShuffleCheck()
        if Duel.SendtoGrave(dg, REASON_COST) ~= 0 and (set_label ~= nil or set_object ~= nil) then
            local og = Duel.GetOperatedGroup()
            RushDuel.SetLabelAndObject(e, og, set_label, set_object)
        end
        return true
    end
end
```
