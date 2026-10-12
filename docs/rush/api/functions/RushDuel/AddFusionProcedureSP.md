# RushDuel.AddFusionProcedureSP

Alias: `RD.AddFusionProcedureSP`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.AddFusionProcedureSP(any card, any sub, any insf, any matfilter, any matcheck, any min, any max) -> any
```

## Description

Rush Duel helper declared in `RDFusion.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
添加融合手续: 指定条件, 不固定数量
```

## Parameters

- `card` `any`: Type and behavior are not yet reviewed; see the source.
- `sub` `any`: Type and behavior are not yet reviewed; see the source.
- `insf` `any`: Type and behavior are not yet reviewed; see the source.
- `matfilter` `any`: Type and behavior are not yet reviewed; see the source.
- `matcheck` `any`: Type and behavior are not yet reviewed; see the source.
- `min` `any`: Type and behavior are not yet reviewed; see the source.
- `max` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDFusion.lua:49`

```lua
function RushDuel.AddFusionProcedureSP(card, sub, insf, matfilter, matcheck, min, max)
    if card:IsStatus(STATUS_COPYING_EFFECT) then
        return
    end
    local insf = (insf ~= false)
    local sub = (sub ~= false)
    local funcs = {}
    return RushDuel.CreateFusionProcedure(card, sub, insf, funcs, matfilter, min, max, matcheck)
end
```

## Used By

Generated from the local `Rush/Scripts/` folder and `rush_cards.cdb`.

- Detected in **5** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=rush&mode=code&q=RushDuel.AddFusionProcedureSP) with `RushDuel.AddFusionProcedureSP`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [YXZ-Cannon Dragon](/examples/rush-cards/120305004) | `120305004` | [Rush/Scripts/c120305004.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120305004.lua) | 1 |
| Tamabot King Golem | `120285039` | [Rush/Scripts/c120285039.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120285039.lua) | 1 |
| XYZ-Dragon Cannon | `120305003` | [Rush/Scripts/c120305003.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120305003.lua) | 1 |
| Deep Space Yggdrago | `120260007` | [Rush/Scripts/c120260007.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120260007.lua) | 1 |
| Blue-Eyes Ultimate Dragon | `120252001` | [Rush/Scripts/c120252001.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120252001.lua) | 1 |

## Script Examples

### YXZ-Cannon Dragon (`120305004`)

Source: [Rush/Scripts/c120305004.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120305004.lua)

```lua
	RD.AddCodeList(c,list)
	--Fusion Material
	RD.AddFusionProcedureSP(c,true,true,cm.matfilter,cm.check,2,3)
	RD.SetFusionMaterial(c,{list[1],list[2],list[3]},3,3)
	--Union Fusion
```

### Tamabot King Golem (`120285039`)

Source: [Rush/Scripts/c120285039.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120285039.lua)

```lua
	RD.AddCodeList(c,list)
	--Fusion Material
	RD.AddFusionProcedureSP(c,true,true,cm.matfilter,cm.check,2,3)
	RD.SetFusionMaterial(c,{list[1]},3,3)
	--Indes
```

### XYZ-Dragon Cannon (`120305003`)

Source: [Rush/Scripts/c120305003.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120305003.lua)

```lua
	RD.AddCodeList(c,list)
	--Fusion Material
	RD.AddFusionProcedureSP(c,true,true,cm.matfilter,cm.check,2,3)
	RD.SetFusionMaterial(c,{list[1],list[2],list[3]},3,3)
	--Union Fusion
```
