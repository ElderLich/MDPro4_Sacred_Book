# RushDuel.IsCanAnnounceFusionMaterialCode

Alias: `RD.IsCanAnnounceFusionMaterialCode`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.IsCanAnnounceFusionMaterialCode(any card, any target) -> any
```

## Description

Rush Duel helper declared in `RDCondition.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
条件: 可以宣言融合素材的卡名
```

## Parameters

- `card` `any`: Type and behavior are not yet reviewed; see the source.
- `target` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDCondition.lua:184`

```lua
function RushDuel.IsCanAnnounceFusionMaterialCode(card, target)
    local codes = RushDuel.GetAnnouncableFusionMaterialCodes(card, target)
    return #codes > 0
end
```

## Used By

Generated from the local `Rush/Scripts/` folder and `rush_cards.cdb`.

- Detected in **6** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=rush&mode=code&q=RushDuel.IsCanAnnounceFusionMaterialCode) with `RushDuel.IsCanAnnounceFusionMaterialCode`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [The Noodle Art of Flavor Shift](/examples/rush-cards/120300053) | `120300053` | [Rush/Scripts/c120300053.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120300053.lua) | 1 |
| Variable Stellariser | `120277007` | [Rush/Scripts/c120277007.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120277007.lua) | 1 |
| Accel Wonder Dark | `120285005` | [Rush/Scripts/c120285005.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120285005.lua) | 1 |
| Rare Dragorite | `120294008` | [Rush/Scripts/c120294008.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120294008.lua) | 1 |
| Phantasm Maskmaster | `120271028` | [Rush/Scripts/c120271028.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120271028.lua) | 1 |
| Elemental HERO Prisma | `120272065` | [Rush/Scripts/c120272065.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120272065.lua) | 1 |

## Script Examples

### The Noodle Art of Flavor Shift (`120300053`)

Source: [Rush/Scripts/c120300053.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120300053.lua)

```lua
end
function cm.filter(c,fc)
	return c:IsFaceup() and RD.IsCanAnnounceFusionMaterialCode(c,fc)
end
function cm.condition(e,tp,eg,ep,ev,re,r,rp)
```

### Variable Stellariser (`120277007`)

Source: [Rush/Scripts/c120277007.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120277007.lua)

```lua
function cm.costfilter(c,e)
	return c:IsType(TYPE_FUSION) and c:IsLevel(9) and c:IsRace(RACE_GALAXY)
		and RD.IsCanAnnounceFusionMaterialCode(e:GetHandler(),c)
end
cm.cost=RD.CostShowExtra(cm.costfilter,1,1,nil,Group.GetFirst)
```

### Accel Wonder Dark (`120285005`)

Source: [Rush/Scripts/c120285005.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120285005.lua)

```lua
function cm.costfilter(c,e)
	return c:IsType(TYPE_FUSION) and c:IsAttribute(ATTRIBUTE_DARK) and c:IsRace(RACE_SPELLCASTER)
		and RD.IsDefense(c,2100) and RD.IsCanAnnounceFusionMaterialCode(e:GetHandler(),c)
end
cm.cost=RD.CostShowExtra(cm.costfilter,1,1,nil,Group.GetFirst)
```
