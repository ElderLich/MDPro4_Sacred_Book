# RushDuel.CheckFusionMaterials

Alias: `RD.CheckFusionMaterials`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.CheckFusionMaterials(any group, any fc, any sub, any funcs) -> any
```

## Description

Rush Duel helper declared in `RDFunction.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
检查融合素材 (多组素材使用)
```

## Parameters

- `group` `any`: Type and behavior are not yet reviewed; see the source.
- `fc` `any`: Type and behavior are not yet reviewed; see the source.
- `sub` `any`: Type and behavior are not yet reviewed; see the source.
- `funcs` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDFunction.lua:217`

```lua
function RushDuel.CheckFusionMaterials(group, fc, sub, funcs)
    if #group < #funcs then
        return false
    end
    local sg = Group.CreateGroup()
    return group:IsExists(RushDuel.CheckFusionMaterialsStep, 1, nil, group, sg, fc, sub, table.unpack(funcs))
end
```

## Used By

Generated from the local `Rush/Scripts/` folder and `rush_cards.cdb`.

- Detected in **2** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=rush&mode=code&q=RushDuel.CheckFusionMaterials) with `RushDuel.CheckFusionMaterials`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [YXZ-Cannon Dragon](/examples/rush-cards/120305004) | `120305004` | [Rush/Scripts/c120305004.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120305004.lua) | 4 |
| XYZ-Dragon Cannon | `120305003` | [Rush/Scripts/c120305003.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120305003.lua) | 4 |

## Script Examples

### YXZ-Cannon Dragon (`120305004`)

Source: [Rush/Scripts/c120305004.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120305004.lua)

```lua
function cm.check(g,tp,fc,chkf)
	if g:GetCount()==3 then
		return RD.CheckFusionMaterials(g,fc,true,{cm.matfilter1,cm.matfilter2,cm.matfilter3})
	else
		return RD.CheckFusionMaterials(g,fc,true,{cm.matfilter1,cm.matfilter23})
```

### XYZ-Dragon Cannon (`120305003`)

Source: [Rush/Scripts/c120305003.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120305003.lua)

```lua
function cm.check(g,tp,fc,chkf)
	if g:GetCount()==3 then
		return RD.CheckFusionMaterials(g,fc,true,{cm.matfilter1,cm.matfilter2,cm.matfilter3})
	else
		return RD.CheckFusionMaterials(g,fc,true,{cm.matfilter1,cm.matfilter23})
```
