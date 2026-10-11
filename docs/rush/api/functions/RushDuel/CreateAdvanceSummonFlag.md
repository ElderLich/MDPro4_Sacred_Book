# RushDuel.CreateAdvanceSummonFlag

Alias: `RD.CreateAdvanceSummonFlag`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.CreateAdvanceSummonFlag(any card, any flag) -> any
```

## Description

Rush Duel helper declared in `RDSummon.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
记录攻击表示上级召唤的状态
```

## Parameters

- `card` `any`: Type and behavior are not yet reviewed; see the source.
- `flag` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDSummon.lua:289`

```lua
function RushDuel.CreateAdvanceSummonFlag(card, flag)
    local e1 = Effect.CreateEffect(card)
    e1:SetType(EFFECT_TYPE_SINGLE + EFFECT_TYPE_CONTINUOUS)
    e1:SetCode(EVENT_SUMMON_SUCCESS)
    e1:SetProperty(EFFECT_FLAG_CANNOT_DISABLE)
    e1:SetLabel(flag)
    e1:SetCondition(RushDuel.AdvanceSummonFlagCondition)
    e1:SetOperation(RushDuel.AdvanceSummonFlagOperation)
    card:RegisterEffect(e1)
    return e1
end
```

## Used By

Generated from the local `Rush/Scripts/` folder and `rush_cards.cdb`.

- Detected in **5** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=rush&mode=code&q=RushDuel.CreateAdvanceSummonFlag) with `RushDuel.CreateAdvanceSummonFlag`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Transam Prime Armor Nova | `120257008` | [Rush/Scripts/c120257008.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120257008.lua) | 1 |
| God Maju Garzett | `120261043` | [Rush/Scripts/c120261043.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120261043.lua) | 1 |
| Volcalize Ifrit | `120272004` | [Rush/Scripts/c120272004.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120272004.lua) | 1 |
| Maju Garzett | `120238004` | [Rush/Scripts/c120238004.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120238004.lua) | 1 |
| Great Maju Garzett | `120238019` | [Rush/Scripts/c120238019.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120238019.lua) | 1 |

## Script Examples

### Transam Prime Armor Nova (`120257008`)

Source: [Rush/Scripts/c120257008.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120257008.lua)

```lua
	RD.AddPrimeSummonProcedure(c,aux.Stringid(m,0),1800)
	RD.AddSummonProcedureThree(c,aux.Stringid(m,1))
	RD.CreateAdvanceSummonFlag(c,20257008)
	--Atk Up
	local e1=Effect.CreateEffect(c)
```

### God Maju Garzett (`120261043`)

Source: [Rush/Scripts/c120261043.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120261043.lua)

```lua
function cm.initial_effect(c)
	RD.AddSummonProcedureThree(c,aux.Stringid(m,0),nil,cm.sumfilter)
	RD.CreateAdvanceSummonFlag(c,20261043)
	--Atk Up
	local e1=Effect.CreateEffect(c)
```

### Volcalize Ifrit (`120272004`)

Source: [Rush/Scripts/c120272004.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120272004.lua)

```lua
cm.name="化学火山化火巨灵"
function cm.initial_effect(c)
	RD.CreateAdvanceSummonFlag(c,20272004)
	--Atk Up
	local e1=Effect.CreateEffect(c)
```
