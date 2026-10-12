# RushDuel.CostChangePosition

Alias: `RD.CostChangePosition`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.CostChangePosition(any filter, any min, any max, any position, any except_self, any set_label_before, any set_object_before, any set_label_after, any set_object_after) -> any
```

## Description

Rush Duel helper declared in `RDCost.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
代价: 改变怪兽的表示形式
```

## Parameters

- `filter` `any`: Type and behavior are not yet reviewed; see the source.
- `min` `any`: Type and behavior are not yet reviewed; see the source.
- `max` `any`: Type and behavior are not yet reviewed; see the source.
- `position` `any`: Type and behavior are not yet reviewed; see the source.
- `except_self` `any`: Type and behavior are not yet reviewed; see the source.
- `set_label_before` `any`: Type and behavior are not yet reviewed; see the source.
- `set_object_before` `any`: Type and behavior are not yet reviewed; see the source.
- `set_label_after` `any`: Type and behavior are not yet reviewed; see the source.
- `set_object_after` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDCost.lua:497`

```lua
function RushDuel.CostChangePosition(filter, min, max, position, except_self, set_label_before, set_object_before,
    set_label_after, set_object_after)
    local action = RushDuel._private_action_change_position(position, set_label_before, set_object_before,
        set_label_after, set_object_after)
    return RushDuel._private_cost_select_match(HINTMSG_POSCHANGE, filter, LOCATION_MZONE, 0, min, max, except_self,
        action)
end
```

## Used By

Generated from the local `Rush/Scripts/` folder and `rush_cards.cdb`.

- Detected in **9** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=rush&mode=code&q=RushDuel.CostChangePosition) with `RushDuel.CostChangePosition`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Moonforce Ziggy](/examples/rush-cards/120300014) | `120300014` | [Rush/Scripts/c120300014.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120300014.lua) | 1 |
| Super Soldier Radiance | `120293042` | [Rush/Scripts/c120293042.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120293042.lua) | 1 |
| Luna Moonforce Alba | `120300038` | [Rush/Scripts/c120300038.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120300038.lua) | 1 |
| Dragon Remover | `120261035` | [Rush/Scripts/c120261035.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120261035.lua) | 1 |
| Yamiluna the Dark Devotee | `120246046` | [Rush/Scripts/c120246046.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120246046.lua) | 1 |
| Lostream Nemora | `120309037` | [Rush/Scripts/c120309037.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120309037.lua) | 1 |
| Asbolus the Star Knight | `120190002` | [Rush/Scripts/c120190002.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120190002.lua) | 1 |
| Draco the Doctor | `120294003` | [Rush/Scripts/c120294003.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120294003.lua) | 1 |
| Bonded Bowing | `120140010` | [Rush/Scripts/c120140010.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120140010.lua) | 1 |

## Script Examples

### Moonforce Ziggy (`120300014`)

Source: [Rush/Scripts/c120300014.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120300014.lua)

```lua
	return c:IsType(TYPE_MONSTER) and c:IsAbleToDeck()
end
cm.cost=RD.CostChangePosition(cm.costfilter,1,1)
function cm.target(e,tp,eg,ep,ev,re,r,rp,chk)
	if chk==0 then return Duel.IsExistingMatchingCard(cm.filter,tp,0,LOCATION_MZONE,1,nil) end
```

### Super Soldier Radiance (`120293042`)

Source: [Rush/Scripts/c120293042.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120293042.lua)

```lua
end
cm.cost1=RD.CostSendHandToDeckBottom(cm.costfilter1,1,1,false)
cm.cost2=RD.CostChangePosition(cm.costfilter2,1,1)
cm.cost=RD.CostChoose(HINTMSG_TODECK,cm.cost1,HINTMSG_POSCHANGE,cm.cost2)
function cm.target(e,tp,eg,ep,ev,re,r,rp,chk)
```

### Luna Moonforce Alba (`120300038`)

Source: [Rush/Scripts/c120300038.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120300038.lua)

```lua
		and not Duel.IsExistingMatchingCard(cm.confilter,tp,LOCATION_GRAVE,0,6,nil)
end
cm.cost=RD.CostChangePosition(cm.costfilter,1,1)
function cm.operation(e,tp,eg,ep,ev,re,r,rp)
	local c=e:GetHandler()
```
