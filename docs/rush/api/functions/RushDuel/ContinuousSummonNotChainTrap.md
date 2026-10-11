# RushDuel.ContinuousSummonNotChainTrap

Alias: `RD.ContinuousSummonNotChainTrap`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.ContinuousSummonNotChainTrap(any card, any flag, any filter) -> any
```

## Description

Rush Duel helper declared in `RDContinuous.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
永续效果: 召唤·特殊召唤时, 对方不能把陷阱卡发动
```

## Parameters

- `card` `any`: Type and behavior are not yet reviewed; see the source.
- `flag` `any`: Type and behavior are not yet reviewed; see the source.
- `filter` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDContinuous.lua:20`

```lua
function RushDuel.ContinuousSummonNotChainTrap(card, flag, filter)
	local e1 = Effect.CreateEffect(card)
	e1:SetType(EFFECT_TYPE_FIELD + EFFECT_TYPE_CONTINUOUS)
	e1:SetCode(EVENT_SUMMON_SUCCESS)
	e1:SetRange(LOCATION_MZONE)
	e1:SetCondition(function(e, tp, eg, ep, ev, re, r, rp)
        return eg:IsExists(filter, 1, nil, e, tp, eg, ep, ev, re, r, rp)
    end)
	e1:SetOperation(function(e, tp, eg, ep, ev, re, r, rp)
        if Duel.GetCurrentChain() == 0 then
            Duel.SetChainLimitTillChainEnd(RushDuel.AttachSummonNotChainTrapLimit)
        elseif Duel.GetCurrentChain() == 1 then
            local c=e:GetHandler()
            c:RegisterFlagEffect(flag,RESET_EVENT+RESETS_STANDARD,0,1)
            local e1 = Effect.CreateEffect(c)
            e1:SetType(EFFECT_TYPE_FIELD+EFFECT_TYPE_CONTINUOUS)
            e1:SetCode(EVENT_CHAINING)
            e1:SetOperation(function(e)
                e:GetHandler():ResetFlagEffect(flag)
                e:Reset()
            end)
            Duel.RegisterEffect(e1,tp)
        end
    end)
	card:RegisterEffect(e1)
	local e2=e1:Clone()
	e2:SetCode(EVENT_SPSUMMON_SUCCESS)
	card:RegisterEffect(e2)
	local e3=Effect.CreateEffect(card)
	e3:SetType(EFFECT_TYPE_FIELD + EFFECT_TYPE_CONTINUOUS)
	e3:SetCode(EVENT_CHAIN_END)
	e3:SetRange(LOCATION_MZONE)
	e3:SetOperation(function(e, tp, eg, ep, ev, re, r, rp)
        local c=e:GetHandler()
        if c:GetFlagEffect(flag) ~= 0 then
            Duel.SetChainLimitTillChainEnd(RushDuel.AttachSummonNotChainTrapLimit)
        end
        c:ResetFlagEffect(flag)
    end)
	card:RegisterEffect(e3)
    return e1, e2, e3
end
```

## Used By

Generated from the local `Rush/Scripts/` folder and `rush_cards.cdb`.

- Detected in **3** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=rush&mode=code&q=RushDuel.ContinuousSummonNotChainTrap) with `RushDuel.ContinuousSummonNotChainTrap`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Isyria, Deity of the Monumenthes | `120300037` | [Rush/Scripts/c120300037.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120300037.lua) | 1 |
| Animagica Double Saber | `120277030` | [Rush/Scripts/c120277030.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120277030.lua) | 1 |
| Harpie Lady 2 &amp; 3 | `120279003` | [Rush/Scripts/c120279003.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120279003.lua) | 1 |

## Script Examples

### Isyria, Deity of the Monumenthes (`120300037`)

Source: [Rush/Scripts/c120300037.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120300037.lua)

```lua
	c:RegisterEffect(e2)
	--Cannot Activate
	local e3,e4,e5=RD.ContinuousSummonNotChainTrap(c,20300037,cm.filter)
	--Atk Up
	local e6=Effect.CreateEffect(c)
```

### Animagica Double Saber (`120277030`)

Source: [Rush/Scripts/c120277030.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120277030.lua)

```lua
function cm.initial_effect(c)
	--Cannot Activate
	local e1,e2,e3=RD.ContinuousSummonNotChainTrap(c,20277030,cm.filter)
	--Level Up
	local e4=Effect.CreateEffect(c)
```

### Harpie Lady 2 & 3 (`120279003`)

Source: [Rush/Scripts/c120279003.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120279003.lua)

```lua
	RD.EnableContactFusion(c,aux.Stringid(m,0))
	--Cannot Activate
	local e1,e2,e3=RD.ContinuousSummonNotChainTrap(c,20279003,cm.filter)
	--Continuous Effect
	RD.AddContinuousEffect(c,e1,e2,e3,RD.EnableChangeCode(c,list[2],LOCATION_MZONE))
```
