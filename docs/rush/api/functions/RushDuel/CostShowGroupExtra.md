# RushDuel.CostShowGroupExtra

Alias: `RD.CostShowGroupExtra`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.CostShowGroupExtra(any filter, any check, any min, any max, any set_label, any set_object) -> any
```

## Description

Rush Duel helper declared in `RDCost.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
代价: 把额外卡组给对方观看 (子卡片组)
```

## Parameters

- `filter` `any`: Type and behavior are not yet reviewed; see the source.
- `check` `any`: Type and behavior are not yet reviewed; see the source.
- `min` `any`: Type and behavior are not yet reviewed; see the source.
- `max` `any`: Type and behavior are not yet reviewed; see the source.
- `set_label` `any`: Type and behavior are not yet reviewed; see the source.
- `set_object` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDCost.lua:232`

```lua
function RushDuel.CostShowGroupExtra(filter, check, min, max, set_label, set_object)
    return RushDuel._private_cost_select_group(HINTMSG_CONFIRM, filter, check, LOCATION_EXTRA, 0, min, max, false,
        function(g, e, tp, eg, ep, ev, re, r, rp)
            RushDuel.SetLabelAndObject(e, g, set_label, set_object)
            Duel.ConfirmCards(1 - tp, g)
        end)
end
```

## Used By

Generated from the local `Rush/Scripts/` folder and `rush_cards.cdb`.

- Detected in **2** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=rush&mode=code&q=RushDuel.CostShowGroupExtra) with `RushDuel.CostShowGroupExtra`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Ciela, the Knight of Skysavior | `120235024` | [Rush/Scripts/c120235024.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120235024.lua) | 1 |
| Dankus, the Knight of Skysavior | `120235025` | [Rush/Scripts/c120235025.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120235025.lua) | 1 |

## Script Examples

### Ciela, the Knight of Skysavior (`120235024`)

Source: [Rush/Scripts/c120235024.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120235024.lua)

```lua
	return g:GetClassCount(Card.GetLinkCode)==g:GetCount()
end
cm.cost=RD.CostShowGroupExtra(cm.costfilter,cm.costcheck,1,5,Group.GetCount)
function cm.target(e,tp,eg,ep,ev,re,r,rp,chk)
	if chk==0 then return Duel.IsExistingMatchingCard(Card.IsFaceup,tp,0,LOCATION_MZONE,1,nil) end
```

### Dankus, the Knight of Skysavior (`120235025`)

Source: [Rush/Scripts/c120235025.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120235025.lua)

```lua
	return g:GetClassCount(Card.GetLinkCode)==g:GetCount()
end
cm.cost=RD.CostShowGroupExtra(cm.costfilter,cm.costcheck,1,5,Group.GetCount)
function cm.operation(e,tp,eg,ep,ev,re,r,rp)
	local c=e:GetHandler()
```
