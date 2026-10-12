# RushDuel.AddSummonProcedureOne

Alias: `RD.AddSummonProcedureOne`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.AddSummonProcedureOne(any card, any desc, any condition, any filter, any operation) -> any
```

## Description

Rush Duel helper declared in `RDSummon.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
添加解放1只的妥协召唤手续
```

## Parameters

- `card` `any`: Type and behavior are not yet reviewed; see the source.
- `desc` `any`: Type and behavior are not yet reviewed; see the source.
- `condition` `any`: Type and behavior are not yet reviewed; see the source.
- `filter` `any`: Type and behavior are not yet reviewed; see the source.
- `operation` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDSummon.lua:45`

```lua
function RushDuel.AddSummonProcedureOne(card, desc, condition, filter, operation)
    local e1 = Effect.CreateEffect(card)
    e1:SetDescription(desc)
    e1:SetType(EFFECT_TYPE_SINGLE)
    e1:SetCode(EFFECT_SUMMON_PROC)
    e1:SetProperty(EFFECT_FLAG_CANNOT_DISABLE + EFFECT_FLAG_UNCOPYABLE)
    e1:SetCondition(RushDuel.SummonProcedureConditionOne(filter, condition))
    e1:SetOperation(RushDuel.SummonProcedureOperationOne(filter, operation))
    e1:SetValue(SUMMON_TYPE_ADVANCE + SUMMON_VALUE_ONE + SUMMON_VALUE_SELF)
    card:RegisterEffect(e1)
    return e1
end
```

## Used By

Generated from the local `Rush/Scripts/` folder and `rush_cards.cdb`.

- Detected in **32** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=rush&mode=code&q=RushDuel.AddSummonProcedureOne) with `RushDuel.AddSummonProcedureOne`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Plasmatic Model Tool Ceto | `120301069` | [Rush/Scripts/c120301069.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120301069.lua) | 1 |
| Darklord Zerato | `120228000` | [Rush/Scripts/c120228000.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120228000.lua) | 1 |
| Animagica Shooter | `120277032` | [Rush/Scripts/c120277032.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120277032.lua) | 1 |
| Freewind | `120290017` | [Rush/Scripts/c120290017.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120290017.lua) | 1 |
| Battletested Gaia The Fierce Knight | `120249032` | [Rush/Scripts/c120249032.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120249032.lua) | 1 |
| Rising Unit | `120304026` | [Rush/Scripts/c120304026.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120304026.lua) | 1 |
| Limlith the Skysavior Princess | `120301045` | [Rush/Scripts/c120301045.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120301045.lua) | 1 |
| Animagica Whip | `120277031` | [Rush/Scripts/c120277031.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120277031.lua) | 1 |
| Cyber Dragon Rakete | `120278006` | [Rush/Scripts/c120278006.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120278006.lua) | 1 |
| Lindorm the Mega Monarch | `120291002` | [Rush/Scripts/c120291002.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120291002.lua) | 1 |
| Dynamajesty Dino Dynakaiser | `120277019` | [Rush/Scripts/c120277019.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120277019.lua) | 1 |
| Peace Lovely Ángel | `120260040` | [Rush/Scripts/c120260040.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120260040.lua) | 1 |
| Cyber Search Dragon | `120109022` | [Rush/Scripts/c120109022.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120109022.lua) | 1 |
| Cybersepice Nutmeg | `120261018` | [Rush/Scripts/c120261018.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120261018.lua) | 1 |
| Abysskite Kaleido-Karen | `120290011` | [Rush/Scripts/c120290011.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120290011.lua) | 1 |
| Infernoclad Dragon - Flagal | `120304019` | [Rush/Scripts/c120304019.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120304019.lua) | 1 |
| Cyber Assault Dragon | `120231022` | [Rush/Scripts/c120231022.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120231022.lua) | 1 |
| Volcano Black Dragon | `120283041` | [Rush/Scripts/c120283041.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120283041.lua) | 1 |
| Infinite Heavy Cavalry Buildragoon | `120264015` | [Rush/Scripts/c120264015.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120264015.lua) | 1 |
| Royal Rebel's Falsetto | `120306005` | [Rush/Scripts/c120306005.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120306005.lua) | 1 |
| Abysskite Ulti-Ange | `120283036` | [Rush/Scripts/c120283036.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120283036.lua) | 1 |
| Lostream Nereides | `120109068` | [Rush/Scripts/c120109068.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120109068.lua) | 1 |
| Mordorne the Skullcrag Knight | `120298004` | [Rush/Scripts/c120298004.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120298004.lua) | 1 |
| Mega Star Monarch Estrome | `120244019` | [Rush/Scripts/c120244019.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120244019.lua) | 1 |
| ...and 8 more |  |  |  |

## Script Examples

### Plasmatic Model Tool Ceto (`120301069`)

Source: [Rush/Scripts/c120301069.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120301069.lua)

```lua
	RD.AddCodeList(c,list)
	--Summon Procedure
	RD.AddSummonProcedureOne(c,aux.Stringid(m,0),nil,cm.sumfilter)
	--Special Summon
	local e1=Effect.CreateEffect(c)
```

### Darklord Zerato (`120228000`)

Source: [Rush/Scripts/c120228000.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120228000.lua)

```lua
function cm.initial_effect(c)
	--Summon Procedure
	RD.AddSummonProcedureOne(c,aux.Stringid(m,0),cm.sumcon,cm.sumfilter)
	--Destroy
	local e1=Effect.CreateEffect(c)
```

### Animagica Shooter (`120277032`)

Source: [Rush/Scripts/c120277032.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120277032.lua)

```lua
function cm.initial_effect(c)
	--Summon Procedure
	RD.AddSummonProcedureOne(c,aux.Stringid(m,0),nil,cm.sumfilter)
	--Position
	local e1=Effect.CreateEffect(c)
```
