# RushDuel.ValueDoubleTributeLvAttrRace

Alias: `RD.ValueDoubleTributeLvAttrRace`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.ValueDoubleTributeLvAttrRace(any level, any attribute, any race, any ignore) -> any
```

## Description

Rush Duel helper declared in `RDValue.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
效果值: 双重解放 等级/属性/种族
```

## Parameters

- `level` `any`: Type and behavior are not yet reviewed; see the source.
- `attribute` `any`: Type and behavior are not yet reviewed; see the source.
- `race` `any`: Type and behavior are not yet reviewed; see the source.
- `ignore` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDValue.lua:73`

```lua
function RushDuel.ValueDoubleTributeLvAttrRace(level, attribute, race, ignore)
    return RushDuel.ValueDoubleTributeMix(ignore, nil, attribute, nil, level, race, nil, nil)
end
```

## Used By

Generated from the local `Rush/Scripts/` folder and `rush_cards.cdb`.

- Detected in **2** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=rush&mode=code&q=RushDuel.ValueDoubleTributeLvAttrRace) with `RushDuel.ValueDoubleTributeLvAttrRace`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Darkness Doom Giant | `120253035` | [Rush/Scripts/c120253035.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120253035.lua) | 1 |
| Double Twin Dragon | `120231051` | [Rush/Scripts/c120231051.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120231051.lua) | 1 |

## Script Examples

### Darkness Doom Giant (`120253035`)

Source: [Rush/Scripts/c120253035.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120253035.lua)

```lua
end
--To Hand
cm.trival=RD.ValueDoubleTributeLvAttrRace(8,nil,RACE_GALAXY)
function cm.thfilter(c)
	return ((c:IsLevel(7,8) and c:IsRace(RACE_GALAXY)) or c:IsCode(list[2])) and c:IsAbleToHand()
```

### Double Twin Dragon (`120231051`)

Source: [Rush/Scripts/c120231051.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120231051.lua)

```lua
end
--Extra Tribute
cm.trival=RD.ValueDoubleTributeLvAttrRace(7,nil,RACE_DRAGON)
function cm.costfilter(c)
	return c:IsType(TYPE_MONSTER) and c:IsAbleToDeckOrExtraAsCost()
```
