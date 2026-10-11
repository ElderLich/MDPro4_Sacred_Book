# RushDuel.ContinuousBattleDestroyToGrave

Alias: `RD.ContinuousBattleDestroyToGrave`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.ContinuousBattleDestroyToGrave(any card, any condition, any operation, any register) -> any
```

## Description

Rush Duel helper declared in `RDContinuous.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
永续效果: 战斗破坏怪兽送去墓地时的处理
```

## Parameters

- `card` `any`: Type and behavior are not yet reviewed; see the source.
- `condition` `any`: Type and behavior are not yet reviewed; see the source.
- `operation` `any`: Type and behavior are not yet reviewed; see the source.
- `register` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDContinuous.lua:85`

```lua
function RushDuel.ContinuousBattleDestroyToGrave(card, condition, operation, register)
    local e1 = Effect.CreateEffect(card)
    e1:SetType(EFFECT_TYPE_SINGLE + EFFECT_TYPE_CONTINUOUS)
    e1:SetCode(EVENT_BATTLE_DESTROYING)
    e1:SetCondition(RushDuel.BattleDestroyToGraveCondition(condition))
    e1:SetOperation(RushDuel.BattleDestroyToGraveOperation(operation))
    if register ~= false then
        card:RegisterEffect(e1)
    end
    return e1
end
```

## Used By

Generated from the local `Rush/Scripts/` folder and `rush_cards.cdb`.

- Detected in **6** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=rush&mode=code&q=RushDuel.ContinuousBattleDestroyToGrave) with `RushDuel.ContinuousBattleDestroyToGrave`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Executie Prouty Frontiere | `120283033` | [Rush/Scripts/c120283033.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120283033.lua) | 1 |
| Elemental HERO Shining Flare Wingman | `120264000` | [Rush/Scripts/c120264000.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120264000.lua) | 1 |
| Red-Eyes Maxi-Flare Dragon \[L\] | `120274001` | [Rush/Scripts/c120274001.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120274001.lua) | 1 |
| Elemental HERO Flame Wingman | `120263001` | [Rush/Scripts/c120263001.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120263001.lua) | 1 |
| Goblin Attack Force | `120307025` | [Rush/Scripts/c120307025.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120307025.lua) | 1 |
| Chainsaw Insect | `120300029` | [Rush/Scripts/c120300029.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120300029.lua) | 1 |

## Script Examples

### Executie Prouty Frontiere (`120283033`)

Source: [Rush/Scripts/c120283033.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120283033.lua)

```lua
	c:RegisterEffect(e2)
	--Recover
	local e3=RD.ContinuousBattleDestroyToGrave(c,nil,cm.recop)
	--Continuous Effect
	RD.AddContinuousEffect(c,e1,e2,e3)
```

### Elemental HERO Shining Flare Wingman (`120264000`)

Source: [Rush/Scripts/c120264000.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120264000.lua)

```lua
	c:RegisterEffect(e1)
	--Damage
	local e2=RD.ContinuousBattleDestroyToGrave(c,nil,cm.damop)
	--Continuous Effect
	RD.AddContinuousEffect(c,e1,e2)
```

### Red-Eyes Maxi-Flare Dragon [L] (`120274001`)

Source: [Rush/Scripts/c120274001.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120274001.lua)

```lua
	c:RegisterEffect(e2)
	--Damage
	local e3=RD.ContinuousBattleDestroyToGrave(c,cm.damcon,cm.damop,false)
	e3:SetType(EFFECT_TYPE_XMATERIAL+EFFECT_TYPE_CONTINUOUS)
	c:RegisterEffect(e3)
```
