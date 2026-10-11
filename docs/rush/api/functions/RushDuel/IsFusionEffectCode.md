# RushDuel.IsFusionEffectCode

Alias: `RD.IsFusionEffectCode`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.IsFusionEffectCode(any code) -> any
```

## Description

Rush Duel helper declared in `RDCondition.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
条件: 当前的融合效果的卡片编号
```

## Parameters

- `code` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDCondition.lua:144`

```lua
function RushDuel.IsFusionEffectCode(code)
    if RD.CurrentFusionEffect then
        return RD.CurrentFusionEffect:GetHandler():IsCode(code)
    end
    return false
end
```

## Used By

Generated from the local `Rush/Scripts/` folder and `rush_cards.cdb`.

- Detected in **2** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=rush&mode=code&q=RushDuel.IsFusionEffectCode) with `RushDuel.IsFusionEffectCode`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Variable Stellariser | `120277007` | [Rush/Scripts/c120277007.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120277007.lua) | 1 |
| Tama Bond | `120285053` | [Rush/Scripts/c120285053.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120285053.lua) | 1 |

## Script Examples

### Variable Stellariser (`120277007`)

Source: [Rush/Scripts/c120277007.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120277007.lua)

```lua
end
function cm.fucon(e)
	return RD.IsFusionEffectCode(list[1])
end
```

### Tama Bond (`120285053`)

Source: [Rush/Scripts/c120285053.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120285053.lua)

```lua
function cm.codetg(e,c)
	-- 临时解决办法: 使用"蛋球结合"时，赋予额外的融合卡号
	return RD.IsFusionEffectCode(120285053)
		and c:IsLevel(7) and c:IsAttribute(ATTRIBUTE_EARTH) and c:IsRace(RACE_MACHINE)
end
```
