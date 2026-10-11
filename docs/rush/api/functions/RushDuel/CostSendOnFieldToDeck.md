# RushDuel.CostSendOnFieldToDeck

Alias: `RD.CostSendOnFieldToDeck`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.CostSendOnFieldToDeck(any filter, any min, any max, any except_self, any set_label_before, any set_object_before, any set_label_after, any set_object_after) -> any
```

## Description

Rush Duel helper declared in `RDCost.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
代价: 让场上的卡返回卡组
```

## Parameters

- `filter` `any`: Type and behavior are not yet reviewed; see the source.
- `min` `any`: Type and behavior are not yet reviewed; see the source.
- `max` `any`: Type and behavior are not yet reviewed; see the source.
- `except_self` `any`: Type and behavior are not yet reviewed; see the source.
- `set_label_before` `any`: Type and behavior are not yet reviewed; see the source.
- `set_object_before` `any`: Type and behavior are not yet reviewed; see the source.
- `set_label_after` `any`: Type and behavior are not yet reviewed; see the source.
- `set_object_after` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDCost.lua:407`

```lua
function RushDuel.CostSendOnFieldToDeck(filter, min, max, except_self, set_label_before, set_object_before,
    set_label_after, set_object_after)
    return RushDuel.CostSendMatchToDeckSort(filter, LOCATION_ONFIELD, min, max, except_self, SEQ_DECKSHUFFLE, true,
        false, set_label_before, set_object_before, set_label_after, set_object_after)
end
```

## Used By

Generated from the local `Rush/Scripts/` folder and `rush_cards.cdb`.

- Detected in **1** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=rush&mode=code&q=RushDuel.CostSendOnFieldToDeck) with `RushDuel.CostSendOnFieldToDeck`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Coil Dragon of Desolation | `120192011` | [Rush/Scripts/c120192011.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120192011.lua) | 1 |

## Script Examples

### Coil Dragon of Desolation (`120192011`)

Source: [Rush/Scripts/c120192011.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120192011.lua)

```lua
	return c:IsFaceup() and c:IsLocation(LOCATION_FZONE) and c:IsAbleToDeckAsCost()
end
cm.cost=RD.CostSendOnFieldToDeck(cm.costfilter,1,1)
function cm.target(e,tp,eg,ep,ev,re,r,rp,chk)
	if chk==0 then return true end
```
