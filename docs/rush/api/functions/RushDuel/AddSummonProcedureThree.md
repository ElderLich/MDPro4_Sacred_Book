# RushDuel.AddSummonProcedureThree

Alias: `RD.AddSummonProcedureThree`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.AddSummonProcedureThree(any card, any desc, any condition, any filter, any operation) -> any
```

## Description

Rush Duel helper declared in `RDSummon.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
添加解放3只的妥协召唤手续
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

`Rush/Utilities/RDSummon.lua:116`

```lua
function RushDuel.AddSummonProcedureThree(card, desc, condition, filter, operation)
    local e1 = Effect.CreateEffect(card)
    e1:SetDescription(desc)
    e1:SetType(EFFECT_TYPE_SINGLE)
    e1:SetCode(EFFECT_SUMMON_PROC)
    e1:SetProperty(EFFECT_FLAG_CANNOT_DISABLE + EFFECT_FLAG_UNCOPYABLE)
    e1:SetCondition(RushDuel.SummonProcedureConditionThree(filter, condition))
    e1:SetOperation(RushDuel.SummonProcedureOperationThree(filter, operation))
    e1:SetValue(SUMMON_TYPE_ADVANCE + SUMMON_VALUE_THREE + SUMMON_VALUE_SELF)
    card:RegisterEffect(e1)
    local mt = getmetatable(card)
    if mt.is_can_triple_tribute == nil then
        mt.is_can_triple_tribute = true
    end
    return e1
end
```

## Used By

Generated from the local `Rush/Scripts/` folder and `rush_cards.cdb`.

- Detected in **8** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=rush&mode=code&q=RushDuel.AddSummonProcedureThree) with `RushDuel.AddSummonProcedureThree`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Galactica Supreme Oblivion | `120245003` | [Rush/Scripts/c120245003.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120245003.lua) | 1 |
| Voidvelg Divine Requiem | `120109037` | [Rush/Scripts/c120109037.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120109037.lua) | 1 |
| Darkness Transam Crisis | `120253004` | [Rush/Scripts/c120253004.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120253004.lua) | 7 |
| Transam Prime Armor Nova | `120257008` | [Rush/Scripts/c120257008.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120257008.lua) | 1 |
| God Maju Garzett | `120261043` | [Rush/Scripts/c120261043.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120261043.lua) | 1 |
| Magnet Citadel Jar | `120260027` | [Rush/Scripts/c120260027.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120260027.lua) | 1 |
| Beast King Barbaros | `120300000` | [Rush/Scripts/c120300000.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120300000.lua) | 1 |
| Gilford the Lightning | `120235000` | [Rush/Scripts/c120235000.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120235000.lua) | 1 |

## Script Examples

### Galactica Supreme Oblivion (`120245003`)

Source: [Rush/Scripts/c120245003.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120245003.lua)

```lua
function cm.initial_effect(c)
	--Summon Procedure
	RD.AddSummonProcedureThree(c,aux.Stringid(m,0))
	--Destroy
	local e1=Effect.CreateEffect(c)
```

### Voidvelg Divine Requiem (`120109037`)

Source: [Rush/Scripts/c120109037.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120109037.lua)

```lua
function cm.initial_effect(c)
	--Summon Procedure
	RD.AddSummonProcedureThree(c,aux.Stringid(m,0))
	--Destroy
	local e1=Effect.CreateEffect(c)
```

### Darkness Transam Crisis (`120253004`)

Source: [Rush/Scripts/c120253004.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120253004.lua)

```lua
function cm.initial_effect(c)
	--Summon Procedure
	RD.AddSummonProcedureThree(c,aux.Stringid(m,2),nil,cm.sumfilter(ATTRIBUTE_LIGHT))
	RD.AddSummonProcedureThree(c,aux.Stringid(m,3),nil,cm.sumfilter(ATTRIBUTE_DARK))
	RD.AddSummonProcedureThree(c,aux.Stringid(m,4),nil,cm.sumfilter(ATTRIBUTE_FIRE))
```
