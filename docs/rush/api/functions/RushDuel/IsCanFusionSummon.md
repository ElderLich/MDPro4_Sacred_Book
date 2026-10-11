# RushDuel.IsCanFusionSummon

Alias: `RD.IsCanFusionSummon`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.IsCanFusionSummon(any e, any tp, any pos, any matfilter, any spfilter, any exfilter, any s_range, any o_range, any mat_check, any including_self, any self_leave, any except) -> any
```

## Description

Rush Duel helper declared in `RDFusion.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
判断条件: 是否可以进行融合召唤
```

## Parameters

- `e` `any`: Type and behavior are not yet reviewed; see the source.
- `tp` `any`: Type and behavior are not yet reviewed; see the source.
- `pos` `any`: Type and behavior are not yet reviewed; see the source.
- `matfilter` `any`: Type and behavior are not yet reviewed; see the source.
- `spfilter` `any`: Type and behavior are not yet reviewed; see the source.
- `exfilter` `any`: Type and behavior are not yet reviewed; see the source.
- `s_range` `any`: Type and behavior are not yet reviewed; see the source.
- `o_range` `any`: Type and behavior are not yet reviewed; see the source.
- `mat_check` `any`: Type and behavior are not yet reviewed; see the source.
- `including_self` `any`: Type and behavior are not yet reviewed; see the source.
- `self_leave` `any`: Type and behavior are not yet reviewed; see the source.
- `except` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDFusion.lua:528`

```lua
function RushDuel.IsCanFusionSummon(e, tp, pos, matfilter, spfilter, exfilter, s_range, o_range, mat_check, including_self, self_leave, except)
    RushDuel.FusionExtraChecker = RushDuel.FusionCheckLocation(e, self_leave, mat_check)
    local fusionable = RushDuel.GetFusionSummonData(e, tp, pos, matfilter, spfilter, exfilter, s_range, o_range, including_self, self_leave, except)
    RushDuel.FusionExtraChecker = nil
    return fusionable
end
```

## Used By

Generated from the local `Rush/Scripts/` folder and `rush_cards.cdb`.

- Detected in **2** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=rush&mode=code&q=RushDuel.IsCanFusionSummon) with `RushDuel.IsCanFusionSummon`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Void Dust Fusion | `120277052` | [Rush/Scripts/c120277052.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120277052.lua) | 1 |
| Darkness Dwarf | `120253003` | [Rush/Scripts/c120253003.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120253003.lua) | 1 |

## Script Examples

### Void Dust Fusion (`120277052`)

Source: [Rush/Scripts/c120277052.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120277052.lua)

```lua
	return c:IsAttribute(ATTRIBUTE_DARK) and c:IsRace(RACE_GALAXY) and c:IsType(TYPE_NORMAL)
		and c:IsAbleToDeckOrExtraAsCost()
		and RD.IsCanFusionSummon(e,tp,POS_FACEUP,aux.FALSE,cm.spfilter,cm.matfilter,LOCATION_GRAVE,0,cm.matcheck,false,false,c)
end
function cm.matfilter(c)
```

### Darkness Dwarf (`120253003`)

Source: [Rush/Scripts/c120253003.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120253003.lua)

```lua
function cm.costfilter(c,e,tp)
	return c:IsFaceup() and c:IsRace(RACE_GALAXY) and c:IsAbleToGraveAsCost()
		and RD.IsCanFusionSummon(e,tp,POS_FACEUP,cm.matfilter,cm.spfilter,nil,0,0,nil,true,false,c)
end
cm.cost=RD.CostSendMZoneToGrave(cm.costfilter,1,1,true)
```
