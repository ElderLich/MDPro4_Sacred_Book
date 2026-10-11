# RushDuel.CostSendHandSubToGrave

Alias: `RD.CostSendHandSubToGrave`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.CostSendHandSubToGrave(any filter, any check, any min, any max, any set_label_before, any set_object_before, any set_label_after, any set_object_after) -> any
```

## Description

Rush Duel helper declared in `RDCost.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
代价: 把手卡送去墓地 (子卡片组)
```

## Parameters

- `filter` `any`: Type and behavior are not yet reviewed; see the source.
- `check` `any`: Type and behavior are not yet reviewed; see the source.
- `min` `any`: Type and behavior are not yet reviewed; see the source.
- `max` `any`: Type and behavior are not yet reviewed; see the source.
- `set_label_before` `any`: Type and behavior are not yet reviewed; see the source.
- `set_object_before` `any`: Type and behavior are not yet reviewed; see the source.
- `set_label_after` `any`: Type and behavior are not yet reviewed; see the source.
- `set_object_after` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDCost.lua:306`

```lua
function RushDuel.CostSendHandSubToGrave(filter, check, min, max, set_label_before, set_object_before, set_label_after,
    set_object_after)
    local cost = RushDuel.CostSendGroupToGrave(filter, check, LOCATION_HAND, min, max, true, false, false,
        set_label_before, set_object_before, set_label_after, set_object_after)
    return RushDuel.NoCostCheck(cost, EFFECT_NO_COST_SEND_HAND_TO_GRAVE)
end
```

## Used By

Generated from the local `Rush/Scripts/` folder and `rush_cards.cdb`.

- Detected in **7** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=rush&mode=code&q=RushDuel.CostSendHandSubToGrave) with `RushDuel.CostSendHandSubToGrave`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Conduction Alchemicalizer Suirai | `120254042` | [Rush/Scripts/c120254042.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120254042.lua) | 1 |
| Destructor Wyrm Bakhamut | `120247040` | [Rush/Scripts/c120247040.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120247040.lua) | 1 |
| Secret Alteration | `120257053` | [Rush/Scripts/c120257053.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120257053.lua) | 1 |
| Fire Wrath | `120205052` | [Rush/Scripts/c120205052.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120205052.lua) | 1 |
| Pair Production | `120150018` | [Rush/Scripts/c120150018.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120150018.lua) | 1 |
| Jest of the Cosmos Princess | `120261058` | [Rush/Scripts/c120261058.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120261058.lua) | 1 |
| Dosodon | `120199033` | [Rush/Scripts/c120199033.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120199033.lua) | 1 |

## Script Examples

### Conduction Alchemicalizer Suirai (`120254042`)

Source: [Rush/Scripts/c120254042.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120254042.lua)

```lua
	return g:IsExists(cm.costfilter,1,nil)
end
cm.cost=RD.CostSendHandSubToGrave(Card.IsAbleToGraveAsCost,cm.check,1,3,function(g)
	local sg=g:Filter(Card.IsType,nil,TYPE_MONSTER)
	return g:GetSum(Card.GetLevel),sg:GetClassCount(Card.GetRace)
```

### Destructor Wyrm Bakhamut (`120247040`)

Source: [Rush/Scripts/c120247040.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120247040.lua)

```lua
	return Duel.GetFieldGroupCount(tp,LOCATION_FZONE,LOCATION_FZONE)>0
end
cm.cost=RD.CostSendHandSubToGrave(Card.IsAbleToGraveAsCost,cm.check,2,2)
function cm.target(e,tp,eg,ep,ev,re,r,rp,chk)
	if chk==0 then return Duel.IsExistingMatchingCard(cm.desfilter,tp,0,LOCATION_MZONE,1,nil) end
```

### Secret Alteration (`120257053`)

Source: [Rush/Scripts/c120257053.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120257053.lua)

```lua
	return g:IsExists(cm.costfilter,2,nil)
end
cm.cost=RD.CostSendHandSubToGrave(Card.IsAbleToGraveAsCost,cm.check,3,3)
function cm.target(e,tp,eg,ep,ev,re,r,rp,chk)
	if chk==0 then return Duel.IsPlayerCanDraw(tp,3) end
```
