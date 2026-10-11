# RushDuel.OnlyFusionSummon

Alias: `RD.OnlyFusionSummon`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.OnlyFusionSummon(any card) -> any
```

## Description

Rush Duel helper declared in `RDBase.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
创建效果: 这张卡不用融合术召唤不能特殊召唤
```

## Parameters

- `card` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDBase.lua:87`

```lua
function RushDuel.OnlyFusionSummon(card)
    local e1 = Effect.CreateEffect(card)
    e1:SetType(EFFECT_TYPE_SINGLE)
    e1:SetCode(EFFECT_SPSUMMON_CONDITION)
    e1:SetProperty(EFFECT_FLAG_CANNOT_DISABLE + EFFECT_FLAG_UNCOPYABLE)
    e1:SetValue(Auxiliary.fuslimit)
    card:RegisterEffect(e1)
    local e2 = Effect.CreateEffect(card)
    e2:SetType(EFFECT_TYPE_SINGLE)
    e2:SetCode(EFFECT_ONLY_FUSION_SUMMON)
    e2:SetProperty(EFFECT_FLAG_CANNOT_DISABLE + EFFECT_FLAG_UNCOPYABLE)
    card:RegisterEffect(e2)
    return e1, e2
end
```

## Used By

Generated from the local `Rush/Scripts/` folder and `rush_cards.cdb`.

- Detected in **10** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=rush&mode=code&q=RushDuel.OnlyFusionSummon) with `RushDuel.OnlyFusionSummon`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Elemental HERO Heliosphere | `120283029` | [Rush/Scripts/c120283029.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120283029.lua) | 1 |
| Elemental HERO Thunder Giant | `120263003` | [Rush/Scripts/c120263003.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120263003.lua) | 1 |
| Elemental HERO Plasma Vice | `120300066` | [Rush/Scripts/c120300066.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120300066.lua) | 1 |
| Elemental HERO Burst Wingman | `120263002` | [Rush/Scripts/c120263002.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120263002.lua) | 1 |
| Elemental HERO Mariner | `120272047` | [Rush/Scripts/c120272047.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120272047.lua) | 1 |
| Elemental HERO Voltic Wingman | `120277065` | [Rush/Scripts/c120277065.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120277065.lua) | 1 |
| Elemental HERO Shining Flare Wingman | `120264000` | [Rush/Scripts/c120264000.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120264000.lua) | 1 |
| Five-Headed Dragon | `120238001` | [Rush/Scripts/c120238001.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120238001.lua) | 1 |
| Elemental HERO Flame Wingman | `120263001` | [Rush/Scripts/c120263001.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120263001.lua) | 1 |
| Elemental HERO Mudballman | `120109042` | [Rush/Scripts/c120109042.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120109042.lua) | 1 |

## Script Examples

### Elemental HERO Heliosphere (`120283029`)

Source: [Rush/Scripts/c120283029.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120283029.lua)

```lua
	RD.AddFusionProcedure(c,list[1],list[2],list[3])
	--Only Fusion Summon
	RD.OnlyFusionSummon(c)
	--Draw
	local e1=Effect.CreateEffect(c)
```

### Elemental HERO Thunder Giant (`120263003`)

Source: [Rush/Scripts/c120263003.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120263003.lua)

```lua
	RD.AddFusionProcedure(c,list[1],list[2])
	--Only Fusion Summon
	RD.OnlyFusionSummon(c)
	--Destroy
	local e1=Effect.CreateEffect(c)
```

### Elemental HERO Plasma Vice (`120300066`)

Source: [Rush/Scripts/c120300066.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120300066.lua)

```lua
	RD.AddFusionProcedure(c,list[1],list[2])
	--Only Fusion Summon
	RD.OnlyFusionSummon(c)
	--Destroy
	local e1=Effect.CreateEffect(c)
```
