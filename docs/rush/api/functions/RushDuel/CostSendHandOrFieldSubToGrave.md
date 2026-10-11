# RushDuel.CostSendHandOrFieldSubToGrave

Alias: `RD.CostSendHandOrFieldSubToGrave`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.CostSendHandOrFieldSubToGrave(any filter, any check, any min, any max, any except_self, any set_label_before, any set_object_before, any set_label_after, any set_object_after) -> any
```

## Description

Rush Duel helper declared in `RDCost.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
代价: 把手卡·场上的卡送去墓地 (子卡片组)
```

## Parameters

- `filter` `any`: Type and behavior are not yet reviewed; see the source.
- `check` `any`: Type and behavior are not yet reviewed; see the source.
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

`Rush/Utilities/RDCost.lua:343`

```lua
function RushDuel.CostSendHandOrFieldSubToGrave(filter, check, min, max, except_self, set_label_before,
    set_object_before, set_label_after, set_object_after)
    return RushDuel.CostSendGroupToGrave(filter, check, LOCATION_HAND + LOCATION_ONFIELD, min, max, except_self, false,
        false, set_label_before, set_object_before, set_label_after, set_object_after)
end
```

## Used By

Generated from the local `Rush/Scripts/` folder and `rush_cards.cdb`.

- Detected in **3** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=rush&mode=code&q=RushDuel.CostSendHandOrFieldSubToGrave) with `RushDuel.CostSendHandOrFieldSubToGrave`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Sacred Tower in Collapse | `120290064` | [Rush/Scripts/c120290064.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120290064.lua) | 1 |
| Certain Death Promotion | `120272055` | [Rush/Scripts/c120272055.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120272055.lua) | 1 |
| Monumenthes Festival -The Isyria Seance- | `120300046` | [Rush/Scripts/c120300046.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120300046.lua) | 1 |

## Script Examples

### Sacred Tower in Collapse (`120290064`)

Source: [Rush/Scripts/c120290064.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120290064.lua)

```lua
	return eg:IsExists(cm.confilter,1,nil,1-tp)
end
cm.cost=RD.CostSendHandOrFieldSubToGrave(cm.costfilter,cm.check,2,2,true)
function cm.target(e,tp,eg,ep,ev,re,r,rp,chk)
	if chk==0 then return true end
```

### Certain Death Promotion (`120272055`)

Source: [Rush/Scripts/c120272055.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120272055.lua)

```lua
	return g:GetClassCount(Card.GetLocation)==g:GetCount()
end
cm.cost=RD.CostSendHandOrFieldSubToGrave(cm.costfilter,cm.check,2,2,true)
function cm.target(e,tp,eg,ep,ev,re,r,rp,chk)
	if chk==0 then return Duel.IsExistingMatchingCard(nil,tp,0,LOCATION_ONFIELD,1,nil) end
```

### Monumenthes Festival -The Isyria Seance- (`120300046`)

Source: [Rush/Scripts/c120300046.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120300046.lua)

```lua
	return g:GetClassCount(Card.GetCode)==g:GetCount()
end
cm.cost=RD.CostSendHandOrFieldSubToGrave(cm.costfilter,cm.check,3,3,true)
```
