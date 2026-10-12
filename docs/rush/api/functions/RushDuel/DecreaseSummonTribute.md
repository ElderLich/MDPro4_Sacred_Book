# RushDuel.DecreaseSummonTribute

Alias: `RD.DecreaseSummonTribute`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.DecreaseSummonTribute(any card, any condition, any value) -> any
```

## Description

Rush Duel helper declared in `RDSummon.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
上级召唤所需的解放数量可以减少
```

## Parameters

- `card` `any`: Type and behavior are not yet reviewed; see the source.
- `condition` `any`: Type and behavior are not yet reviewed; see the source.
- `value` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDSummon.lua:362`

```lua
function RushDuel.DecreaseSummonTribute(card, condition, value)
    local e1 = Effect.CreateEffect(card)
    e1:SetType(EFFECT_TYPE_SINGLE)
    e1:SetCode(EFFECT_DECREASE_TRIBUTE)
    e1:SetProperty(EFFECT_FLAG_CANNOT_DISABLE + EFFECT_FLAG_UNCOPYABLE + EFFECT_FLAG_SINGLE_RANGE)
    if condition then
        e1:SetCondition(condition)
    end
    e1:SetRange(LOCATION_HAND)
    e1:SetValue(RushDuel.DecreaseSummonValue(value or 0x1))
    card:RegisterEffect(e1)
    return e1
end
```

## Used By

Generated from the local `Rush/Scripts/` folder and `rush_cards.cdb`.

- Detected in **2** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=rush&mode=code&q=RushDuel.DecreaseSummonTribute) with `RushDuel.DecreaseSummonTribute`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Ancient Gear Powered Soldier | `120271006` | [Rush/Scripts/c120271006.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120271006.lua) | 1 |
| Ancient Gear Tyranno | `120271005` | [Rush/Scripts/c120271005.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120271005.lua) | 1 |

## Script Examples

### Ancient Gear Powered Soldier (`120271006`)

Source: [Rush/Scripts/c120271006.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120271006.lua)

```lua
	RD.AddCodeList(c,list)
	-- Decrease Tribute
	RD.DecreaseSummonTribute(c,cm.sumcon,0x1)
	--Atk Up
	local e1=Effect.CreateEffect(c)
```

### Ancient Gear Tyranno (`120271005`)

Source: [Rush/Scripts/c120271005.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120271005.lua)

```lua
function cm.initial_effect(c)
	-- Decrease Tribute
	RD.DecreaseSummonTribute(c,cm.sumcon,0x1)
	-- Cannot Activate
	local e1=RD.ContinuousAttackNotChainTrap(c)
```
