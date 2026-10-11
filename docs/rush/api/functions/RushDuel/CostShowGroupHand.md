# RushDuel.CostShowGroupHand

Alias: `RD.CostShowGroupHand`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.CostShowGroupHand(any filter, any check, any min, any max, any set_label, any set_object) -> any
```

## Description

Rush Duel helper declared in `RDCost.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
代价: 把手卡给对方观看 (子卡片组)
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

`Rush/Utilities/RDCost.lua:215`

```lua
function RushDuel.CostShowGroupHand(filter, check, min, max, set_label, set_object)
    return RushDuel._private_cost_select_group(HINTMSG_CONFIRM, filter, check, LOCATION_HAND, 0, min, max, true,
        function(g, e, tp, eg, ep, ev, re, r, rp)
            RushDuel.SetLabelAndObject(e, g, set_label, set_object)
            Duel.ConfirmCards(1 - tp, g)
            Duel.ShuffleHand(tp)
        end)
end
```

## Used By

Generated from the local `Rush/Scripts/` folder and `rush_cards.cdb`.

- Detected in **4** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=rush&mode=code&q=RushDuel.CostShowGroupHand) with `RushDuel.CostShowGroupHand`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Spiritualization Training](/examples/rush-cards/120301020) | `120301020` | [Rush/Scripts/c120301020.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120301020.lua) | 1 |
| Animagica Witch | `120257031` | [Rush/Scripts/c120257031.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120257031.lua) | 1 |
| Data Eater | `120261038` | [Rush/Scripts/c120261038.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120261038.lua) | 1 |
| Deep Sea Dragon Bat Eel | `120239041` | [Rush/Scripts/c120239041.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120239041.lua) | 1 |

## Script Examples

### Spiritualization Training (`120301020`)

Source: [Rush/Scripts/c120301020.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120301020.lua)

```lua
	return RD.IsPlayerNoActivateInThisTurn(tp,list[1])
end
cm.cost=RD.CostShowGroupHand(cm.costfilter,cm.costcheck,2,2,function(g)
	return g:GetFirst():GetAttribute()
end)
```

### Animagica Witch (`120257031`)

Source: [Rush/Scripts/c120257031.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120257031.lua)

```lua
	return Duel.IsPlayerCanDraw(tp,g:GetCount())
end
cm.cost=RD.CostShowGroupHand(cm.costfilter,cm.costcheck,1,2,Group.GetCount)
function cm.target(e,tp,eg,ep,ev,re,r,rp,chk)
	if chk==0 then return true end
```

### Data Eater (`120261038`)

Source: [Rush/Scripts/c120261038.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120261038.lua)

```lua
	return c:IsAbleToDeck()
end
cm.cost=RD.CostShowGroupHand(cm.costfilter,cm.costcheck,2,2)
function cm.target(e,tp,eg,ep,ev,re,r,rp,chk)
	if chk==0 then return Duel.IsExistingMatchingCard(cm.tdfilter,tp,0,LOCATION_GRAVE,2,nil) end
```
