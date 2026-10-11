# RushDuel.CostSendHandToDeckTopOrBottom

Alias: `RD.CostSendHandToDeckTopOrBottom`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.CostSendHandToDeckTopOrBottom(any filter, any min, any max, any top_desc, any bottom_desc, any confirm, any set_label_before, any set_object_before, any set_label_after, any set_object_after) -> any
```

## Description

Rush Duel helper declared in `RDCost.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
代价: 把手卡返回卡组上面或下面
```

## Parameters

- `filter` `any`: Type and behavior are not yet reviewed; see the source.
- `min` `any`: Type and behavior are not yet reviewed; see the source.
- `max` `any`: Type and behavior are not yet reviewed; see the source.
- `top_desc` `any`: Type and behavior are not yet reviewed; see the source.
- `bottom_desc` `any`: Type and behavior are not yet reviewed; see the source.
- `confirm` `any`: Type and behavior are not yet reviewed; see the source.
- `set_label_before` `any`: Type and behavior are not yet reviewed; see the source.
- `set_object_before` `any`: Type and behavior are not yet reviewed; see the source.
- `set_label_after` `any`: Type and behavior are not yet reviewed; see the source.
- `set_object_after` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDCost.lua:437`

```lua
function RushDuel.CostSendHandToDeckTopOrBottom(filter, min, max, top_desc, bottom_desc, confirm, set_label_before, set_object_before,
    set_label_after, set_object_after)
    return RushDuel.CostSendMatchToDeckTopOrBottom(filter, LOCATION_HAND, min, max, true, top_desc, bottom_desc,
        false, confirm, set_label_before, set_object_before, set_label_after, set_object_after)
end
```

## Used By

Generated from the local `Rush/Scripts/` folder and `rush_cards.cdb`.

- Detected in **1** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=rush&mode=code&q=RushDuel.CostSendHandToDeckTopOrBottom) with `RushDuel.CostSendHandToDeckTopOrBottom`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Shadowforce Explosion | `120300042` | [Rush/Scripts/c120300042.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120300042.lua) | 1 |

## Script Examples

### Shadowforce Explosion (`120300042`)

Source: [Rush/Scripts/c120300042.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120300042.lua)

```lua
	return RD.IsPlayerNoActivateInThisTurn(tp,list[1])
end
cm.cost=RD.CostSendHandToDeckTopOrBottom(Card.IsAbleToDeckAsCost,1,1,aux.Stringid(m,1),aux.Stringid(m,2),false)
function cm.target(e,tp,eg,ep,ev,re,r,rp,chk)
	local g=Duel.GetMatchingGroup(cm.filter,tp,LOCATION_GRAVE,0,nil)
```
