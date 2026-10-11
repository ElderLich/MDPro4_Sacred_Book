# RushDuel.CheckUnionEquip

Alias: `RD.CheckUnionEquip`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.CheckUnionEquip(any e, any c, any ec) -> any
```

## Description

Rush Duel helper declared in `RDUnion.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
检查是否可以同盟装备
```

## Parameters

- `e` `any`: Type and behavior are not yet reviewed; see the source.
- `c` `any`: Type and behavior are not yet reviewed; see the source.
- `ec` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDUnion.lua:72`

```lua
function RushDuel.CheckUnionEquip(e, c, ec)
    local effects = {ec:IsHasEffect(EFFECT_UNION_TARGET)}
    for i, effect in ipairs(effects) do
        local value = effect:GetValue()
        if value(c, effect, e) then
            return true
        end
    end
    return false
end
```

## Used By

Generated from the local `Rush/Scripts/` folder and `rush_cards.cdb`.

- Detected in **3** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=rush&mode=code&q=RushDuel.CheckUnionEquip) with `RushDuel.CheckUnionEquip`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Lostream Shell | `120309039` | [Rush/Scripts/c120309039.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120309039.lua) | 1 |
| UMP Sky Forbia | `120306017` | [Rush/Scripts/c120306017.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120306017.lua) | 1 |
| The Lauan Adventurers Are Go!! | `120306050` | [Rush/Scripts/c120306050.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120306050.lua) | 1 |

## Script Examples

### Lostream Shell (`120309039`)

Source: [Rush/Scripts/c120309039.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120309039.lua)

```lua
function cm.exfilter(c,e,tc)
	return c:IsType(TYPE_UNION) and c:IsAttribute(ATTRIBUTE_WIND) and c:IsRace(RACE_SEASERPENT)
		and RD.CheckUnionEquip(e,tc,c)
end
cm.cost=RD.CostSendHandToGrave(cm.costfilter,1,1)
```

### UMP Sky Forbia (`120306017`)

Source: [Rush/Scripts/c120306017.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120306017.lua)

```lua
function cm.filter(c,e,tc)
	return c:IsType(TYPE_UNION) and c:IsAttribute(ATTRIBUTE_WIND) and c:IsRace(RACE_PLANT)
		and RD.CheckUnionEquip(e,tc,c)
end
function cm.condition(e,tp,eg,ep,ev,re,r,rp)
```

### The Lauan Adventurers Are Go!! (`120306050`)

Source: [Rush/Scripts/c120306050.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120306050.lua)

```lua
function cm.exfilter(c,e,tc)
	return c:IsType(TYPE_UNION) and c:IsAttribute(ATTRIBUTE_WIND) and c:IsRace(RACE_PLANT)
		and RD.CheckUnionEquip(e,tc,c)
end
cm.cost=RD.CostSendMatchToDeckSort(cm.costfilter,LOCATION_ONFIELD,1,1,true,SEQ_DECKBOTTOM,true,true)
```
