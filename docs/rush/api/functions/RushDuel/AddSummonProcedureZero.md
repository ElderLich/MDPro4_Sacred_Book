# RushDuel.AddSummonProcedureZero

Alias: `RD.AddSummonProcedureZero`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.AddSummonProcedureZero(any card, any desc, any condition, any operation) -> any
```

## Description

Rush Duel helper declared in `RDSummon.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
添加不用解放的妥协召唤手续
```

## Parameters

- `card` `any`: Type and behavior are not yet reviewed; see the source.
- `desc` `any`: Type and behavior are not yet reviewed; see the source.
- `condition` `any`: Type and behavior are not yet reviewed; see the source.
- `operation` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDSummon.lua:19`

```lua
function RushDuel.AddSummonProcedureZero(card, desc, condition, operation)
    local e1 = Effect.CreateEffect(card)
    e1:SetDescription(desc)
    e1:SetType(EFFECT_TYPE_SINGLE)
    e1:SetCode(EFFECT_SUMMON_PROC)
    e1:SetProperty(EFFECT_FLAG_CANNOT_DISABLE + EFFECT_FLAG_UNCOPYABLE)
    e1:SetCondition(RushDuel.SummonProcedureConditionZero(condition))
    if operation ~= nil then
        e1:SetOperation(operation)
    end
    e1:SetValue(SUMMON_VALUE_ZERO + SUMMON_VALUE_SELF)
    card:RegisterEffect(e1)
    return e1
end
```

## Used By

Generated from the local `Rush/Scripts/` folder and `rush_cards.cdb`.

- Detected in **14** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=rush&mode=code&q=RushDuel.AddSummonProcedureZero) with `RushDuel.AddSummonProcedureZero`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Preferlyre](/examples/rush-cards/120283046) | `120283046` | [Rush/Scripts/c120283046.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120283046.lua) | 1 |
| OuTerverSe Byugyuwazzo | `120290006` | [Rush/Scripts/c120290006.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120290006.lua) | 1 |
| Twilight Companion - Dralia | `120304068` | [Rush/Scripts/c120304068.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120304068.lua) | 1 |
| Scissor Hercules | `120298038` | [Rush/Scripts/c120298038.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120298038.lua) | 1 |
| Voidalfr Antromeda | `120300005` | [Rush/Scripts/c120300005.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120300005.lua) | 1 |
| Special Operative Flavor Inspector | `120300017` | [Rush/Scripts/c120300017.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120300017.lua) | 1 |
| Supreme Machine Burning Overlord | `120260069` | [Rush/Scripts/c120260069.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120260069.lua) | 1 |
| Stratohammer Mjolnir | `120287071` | [Rush/Scripts/c120287071.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120287071.lua) | 1 |
| Leogun the Golden-Haired Magical Beast | `120294029` | [Rush/Scripts/c120294029.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120294029.lua) | 1 |
| Hybridrive Barriertail | `120264008` | [Rush/Scripts/c120264008.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120264008.lua) | 1 |
| Double Cannon Armor | `120298037` | [Rush/Scripts/c120298037.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120298037.lua) | 1 |
| All Lovely Goddess | `120260039` | [Rush/Scripts/c120260039.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120260039.lua) | 1 |
| Cyber Shark | `120253021` | [Rush/Scripts/c120253021.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120253021.lua) | 1 |
| Swift Gaia the Fierce Knight | `120102005` | [Rush/Scripts/c120102005.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120102005.lua) | 1 |

## Script Examples

### Preferlyre (`120283046`)

Source: [Rush/Scripts/c120283046.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120283046.lua)

```lua
	RD.AddCodeList(c,list)
	--Summon Procedure
	RD.AddSummonProcedureZero(c,aux.Stringid(m,0),cm.sumcon)
	--Draw
	local e1=Effect.CreateEffect(c)
```

### OuTerverSe Byugyuwazzo (`120290006`)

Source: [Rush/Scripts/c120290006.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120290006.lua)

```lua
	RD.AddCodeList(c,list)
	--Summon Procedure
	RD.AddSummonProcedureZero(c,aux.Stringid(m,0),cm.sumcon)
	--Change Code
	RD.EnableChangeCode(c,list[1],LOCATION_GRAVE)
```

### Twilight Companion - Dralia (`120304068`)

Source: [Rush/Scripts/c120304068.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120304068.lua)

```lua
function cm.initial_effect(c)
	--Summon Procedure
	RD.AddSummonProcedureZero(c,aux.Stringid(m,0),cm.sumcon)
	--Atk Up
	local e1=Effect.CreateEffect(c)
```
