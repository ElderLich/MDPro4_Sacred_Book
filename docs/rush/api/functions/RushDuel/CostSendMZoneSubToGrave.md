# RushDuel.CostSendMZoneSubToGrave

Alias: `RD.CostSendMZoneSubToGrave`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.CostSendMZoneSubToGrave(any filter, any check, any min, any max, any except_self, any set_label_before, any set_object_before, any set_label_after, any set_object_after) -> any
```

## Description

Rush Duel helper declared in `RDCost.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
代价: 把怪兽送去墓地 (子卡片组)
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

`Rush/Utilities/RDCost.lua:319`

```lua
function RushDuel.CostSendMZoneSubToGrave(filter, check, min, max, except_self, set_label_before, set_object_before,
    set_label_after, set_object_after)
    return RushDuel.CostSendGroupToGrave(filter, check, LOCATION_MZONE, min, max, except_self, false, false,
        set_label_before, set_object_before, set_label_after, set_object_after)
end
```

## Used By

Generated from the local `Rush/Scripts/` folder and `rush_cards.cdb`.

- Detected in **8** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=rush&mode=code&q=RushDuel.CostSendMZoneSubToGrave) with `RushDuel.CostSendMZoneSubToGrave`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Necromaid Timer](/examples/rush-cards/120294014) | `120294014` | [Rush/Scripts/c120294014.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120294014.lua) | 1 |
| Soul Drake | `120252007` | [Rush/Scripts/c120252007.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120252007.lua) | 1 |
| Celeb Rose Warlock | `120254046` | [Rush/Scripts/c120254046.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120254046.lua) | 1 |
| Dragonic Geist | `120261029` | [Rush/Scripts/c120261029.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120261029.lua) | 1 |
| Darkness Ri-chair-al | `120151027` | [Rush/Scripts/c120151027.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120151027.lua) | 1 |
| Black Luster Jersitual | `120228046` | [Rush/Scripts/c120228046.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120228046.lua) | 1 |
| Medea's Secret Remedy | `120285061` | [Rush/Scripts/c120285061.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120285061.lua) | 1 |
| Shadow Flower Wish | `120205048` | [Rush/Scripts/c120205048.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120205048.lua) | 1 |

## Script Examples

### Necromaid Timer (`120294014`)

Source: [Rush/Scripts/c120294014.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120294014.lua)

```lua
	return Duel.GetMZoneCount(tp,g)>0
end
cm.cost=RD.CostSendMZoneSubToGrave(cm.costfilter,cm.costcheck,2,2,false)
function cm.target(e,tp,eg,ep,ev,re,r,rp,chk)
	if chk==0 then return (e:IsCostChecked() or Duel.GetMZoneCount(tp)>0)
```

### Soul Drake (`120252007`)

Source: [Rush/Scripts/c120252007.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120252007.lua)

```lua
		and RD.IsCanBeSpecialSummoned(c,e,tp,POS_FACEUP)
end
cm.cost=RD.CostSendMZoneSubToGrave(cm.costfilter,cm.costcheck,2,2,false)
function cm.target(e,tp,eg,ep,ev,re,r,rp,chk)
	if chk==0 then return Duel.IsExistingMatchingCard(cm.spfilter,tp,LOCATION_GRAVE,0,1,nil,e,tp) end
```

### Celeb Rose Warlock (`120254046`)

Source: [Rush/Scripts/c120254046.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120254046.lua)

```lua
	return c:IsCode(list[2]) and RD.IsCanBeSpecialSummoned(c,e,tp,POS_FACEUP)
end
cm.cost=RD.CostSendMZoneSubToGrave(cm.costfilter,cm.costcheck,1,2,false)
function cm.target(e,tp,eg,ep,ev,re,r,rp,chk)
	if chk==0 then return Duel.IsExistingMatchingCard(cm.spfilter1,tp,LOCATION_GRAVE,0,1,nil,e,tp) end
```
