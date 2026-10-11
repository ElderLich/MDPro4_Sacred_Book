# RushDuel.IsAttacking

Alias: `RD.IsAttacking`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.IsAttacking(any effect) -> any
```

## Description

Rush Duel helper declared in `RDCondition.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
条件: 处于攻击中
```

## Parameters

- `effect` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDCondition.lua:56`

```lua
function RushDuel.IsAttacking(effect)
    local player = Duel.GetTurnPlayer()
    return Duel.GetFlagEffect(player, FLAG_ATTACK_ANNOUNCED) ~= 0
end
```

## Used By

Generated from the local `Rush/Scripts/` folder and `rush_cards.cdb`.

- Detected in **7** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=rush&mode=code&q=RushDuel.IsAttacking) with `RushDuel.IsAttacking`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Lostream Polka | `120309040` | [Rush/Scripts/c120309040.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120309040.lua) | 1 |
| Lovely Blessing | `120260051` | [Rush/Scripts/c120260051.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120260051.lua) | 1 |
| Evasive Chaos Ninsect Labyrinth Spider | `120277013` | [Rush/Scripts/c120277013.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120277013.lua) | 1 |
| Fiery Arms - Fretberge | `120228051` | [Rush/Scripts/c120228051.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120228051.lua) | 1 |
| Command Knight | `120109065` | [Rush/Scripts/c120109065.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120109065.lua) | 1 |
| Raging Waves | `120253055` | [Rush/Scripts/c120253055.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120253055.lua) | 1 |
| Magician's Valkyria | `120229002` | [Rush/Scripts/c120229002.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120229002.lua) | 1 |

## Script Examples

### Lostream Polka (`120309040`)

Source: [Rush/Scripts/c120309040.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120309040.lua)

```lua
function cm.atkcon(e)
	local ec=e:GetHandler():GetEquipTarget()
	return aux.IsUnionState(e) and not RD.IsAttacking(e)
		and ec and ec:GetControler()==e:GetHandlerPlayer()
end
```

### Lovely Blessing (`120260051`)

Source: [Rush/Scripts/c120260051.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120260051.lua)

```lua
function cm.atkcon(e)
	local ec=e:GetHandler():GetEquipTarget()
	return not RD.IsAttacking(e) and ec and ec:GetControler()==e:GetHandlerPlayer()
end
function cm.atktg(e,c)
```

### Evasive Chaos Ninsect Labyrinth Spider (`120277013`)

Source: [Rush/Scripts/c120277013.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120277013.lua)

```lua
function cm.condition(e)
	local tp=e:GetHandlerPlayer()
	return not RD.IsAttacking(e)
		and Duel.IsExistingMatchingCard(cm.confilter1,tp,LOCATION_MZONE,0,1,nil)
		and not Duel.IsExistingMatchingCard(cm.confilter2,tp,LOCATION_MZONE,0,1,nil)
```
