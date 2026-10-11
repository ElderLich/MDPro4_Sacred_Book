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

## Used By

Generated from the local `Rush/Scripts/` folder and `rush_cards.cdb`.

- Detected in **2** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=rush&mode=code&q=RushDuel.CostSendDeckTopAnyToGrave) with `RushDuel.CostSendDeckTopAnyToGrave`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Card Trooper | `120109044` | [Rush/Scripts/c120109044.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120109044.lua) | 1 |
| Vi-FRND | `120246059` | [Rush/Scripts/c120246059.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120246059.lua) | 1 |

## Script Examples

### Card Trooper (`120109044`)

Source: [Rush/Scripts/c120109044.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120109044.lua)

```lua
	return Duel.GetFieldGroupCount(tp,LOCATION_DECK,0)>9
end
cm.cost=RD.CostSendDeckTopAnyToGrave(aux.Stringid(m,1),1,3,Group.GetCount)
function cm.operation(e,tp,eg,ep,ev,re,r,rp)
	local c=e:GetHandler()
```

### Vi-FRND (`120246059`)

Source: [Rush/Scripts/c120246059.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120246059.lua)

```lua
	return c:IsCode(list[1],list[2],list[3],list[4],list[5])
end
cm.cost=RD.CostSendDeckTopAnyToGrave(aux.Stringid(m,1),1,5)
function cm.operation(e,tp,eg,ep,ev,re,r,rp)
	local c=e:GetHandler()
```
