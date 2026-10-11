# RushDuel.AddFusionProcedureRep

Alias: `RD.AddFusionProcedureRep`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.AddFusionProcedureRep(any card, any sub, any insf, any func, any min, any max, ... any) -> any
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
- `func` `any`: Type and behavior are not yet reviewed; see the source.
- `min` `any`: Type and behavior are not yet reviewed; see the source.
- `max` `any`: Type and behavior are not yet reviewed; see the source.
- `...` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDFusion.lua:37`

```lua
function RushDuel.AddFusionProcedureRep(card, sub, insf, func, min, max, ...)
    if card:IsStatus(STATUS_COPYING_EFFECT) then
        return
    end
    local vals = {...}
    -- 融合素材
    local codes, funcs = RushDuel.MakeFusionMaterial(card, table.unpack(vals))
    RushDuel.SetFusionMaterialData(card, codes, #funcs + min, #funcs + max)
    return RushDuel.CreateFusionProcedure(card, sub, insf, funcs, func, min, max, nil)
end
```

## Used By

Generated from the local `Rush/Scripts/` folder and `rush_cards.cdb`.

- Detected in **4** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=rush&mode=code&q=RushDuel.AddFusionProcedureRep) with `RushDuel.AddFusionProcedureRep`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Princess Cosmos the Cosmic Trickster | `120293043` | [Rush/Scripts/c120293043.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120293043.lua) | 1 |
| Eternum Voidvelg Requiem | `120300032` | [Rush/Scripts/c120300032.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120300032.lua) | 1 |
| Chimeratech Crush Dragon | `120283031` | [Rush/Scripts/c120283031.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120283031.lua) | 1 |
| Chimeratech Overdragon | `120278001` | [Rush/Scripts/c120278001.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120278001.lua) | 1 |

## Script Examples

### Princess Cosmos the Cosmic Trickster (`120293043`)

Source: [Rush/Scripts/c120293043.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120293043.lua)

```lua
	RD.AddCodeList(c,list)
	--Fusion Material
	RD.AddFusionProcedureRep(c,true,true,cm.matfilter,2,63,list[1])
	-- Fusion Flag
	RD.CreateFusionSummonFlag(c,20293043)
```

### Eternum Voidvelg Requiem (`120300032`)

Source: [Rush/Scripts/c120300032.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120300032.lua)

```lua
	RD.AddCodeList(c,list)
	--Fusion Material
	RD.AddFusionProcedureRep(c,true,true,cm.matfilter,1,63,list[1])
	--Cannot To Hand & Deck & Extra
	local e1=Effect.CreateEffect(c)
```

### Chimeratech Crush Dragon (`120283031`)

Source: [Rush/Scripts/c120283031.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120283031.lua)

```lua
	RD.AddCodeList(c,list)
	--Fusion Material
	RD.AddFusionProcedureRep(c,true,true,cm.matfilter,2,63,list[1])
	-- Fusion Flag
	RD.CreateFusionSummonFlag(c,20283031)
```
