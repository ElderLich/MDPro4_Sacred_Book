# RushDuel.ContinuousAttackNotChainTrap

Alias: `RD.ContinuousAttackNotChainTrap`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.ContinuousAttackNotChainTrap(any card) -> any
```

## Description

Rush Duel helper declared in `RDContinuous.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
永续效果: 攻击宣言时, 对方不能把陷阱卡发动
```

## Parameters

- `card` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDContinuous.lua:67`

```lua
function RushDuel.ContinuousAttackNotChainTrap(card)
    local e1 = Effect.CreateEffect(card)
    e1:SetType(EFFECT_TYPE_SINGLE + EFFECT_TYPE_CONTINUOUS)
    e1:SetCode(EVENT_ATTACK_ANNOUNCE)
    e1:SetLabel(card:GetOriginalCode())
    e1:SetOperation(RushDuel.AttackNotChainTrapOperation)
    card:RegisterEffect(e1)
    return e1
end
```

## Used By

Generated from the local `Rush/Scripts/` folder and `rush_cards.cdb`.

- Detected in **8** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=rush&mode=code&q=RushDuel.ContinuousAttackNotChainTrap) with `RushDuel.ContinuousAttackNotChainTrap`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Ancient Gear Megaton Golem | `120283030` | [Rush/Scripts/c120283030.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120283030.lua) | 1 |
| Ancient Gear Powered Soldier | `120271006` | [Rush/Scripts/c120271006.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120271006.lua) | 1 |
| Abyssal Dragon Lord Abyss Poseidra | `120239014` | [Rush/Scripts/c120239014.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120239014.lua) | 1 |
| Ancient Gear Gadjiltron Baena | `120272019` | [Rush/Scripts/c120272019.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120272019.lua) | 1 |
| Ancient Gear Tyranno | `120271005` | [Rush/Scripts/c120271005.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120271005.lua) | 1 |
| Ancient Gear Golem | `120271004` | [Rush/Scripts/c120271004.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120271004.lua) | 1 |
| Ancient Gear Beast | `120271007` | [Rush/Scripts/c120271007.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120271007.lua) | 1 |
| Ancient Gear Soldier | `120271008` | [Rush/Scripts/c120271008.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120271008.lua) | 1 |

## Script Examples

### Ancient Gear Megaton Golem (`120283030`)

Source: [Rush/Scripts/c120283030.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120283030.lua)

```lua
	RD.CreateFusionSummonFlag(c,20283030)
	-- Cannot Activate
	local e1=RD.ContinuousAttackNotChainTrap(c)
	--Attack Twice
	local e2=Effect.CreateEffect(c)
```

### Ancient Gear Powered Soldier (`120271006`)

Source: [Rush/Scripts/c120271006.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120271006.lua)

```lua
	c:RegisterEffect(e1)
	-- Cannot Activate
	local e2=RD.ContinuousAttackNotChainTrap(c)
	--Continuous Effect
	RD.AddContinuousEffect(c,e1,e2)
```

### Abyssal Dragon Lord Abyss Poseidra (`120239014`)

Source: [Rush/Scripts/c120239014.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120239014.lua)

```lua
	RD.AddMaximumProcedure(c,4000,list[1],list[2])
	--Cannot Activate
	local e1=RD.ContinuousAttackNotChainTrap(c)
	e1:SetCondition(cm.actcon)
	--Indes
```
