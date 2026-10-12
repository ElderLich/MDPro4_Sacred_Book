# RushDuel.ConditionFlipMainPhase

Alias: `RD.ConditionFlipMainPhase`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.ConditionFlipMainPhase(any e) -> any
```

## Description

Rush Duel helper declared in `RDCondition.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
通用条件: 这张卡反转的自己主要阶段
```

## Parameters

- `e` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDCondition.lua:440`

```lua
function RushDuel.ConditionFlipMainPhase(e)
	return RushDuel.IsFlipMainPhase(e:GetHandler())
end
```

## Used By

Generated from the local `Rush/Scripts/` folder and `rush_cards.cdb`.

- Detected in **3** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=rush&mode=code&q=RushDuel.ConditionFlipMainPhase) with `RushDuel.ConditionFlipMainPhase`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Magician of Faith | `120307006` | [Rush/Scripts/c120307006.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120307006.lua) | 1 |
| Mask of Darkness | `120307007` | [Rush/Scripts/c120307007.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120307007.lua) | 1 |
| Penguin Soldier | `120307022` | [Rush/Scripts/c120307022.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120307022.lua) | 1 |

## Script Examples

### Magician of Faith (`120307006`)

Source: [Rush/Scripts/c120307006.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120307006.lua)

```lua
	e1:SetType(EFFECT_TYPE_IGNITION)
	e1:SetRange(LOCATION_MZONE)
	e1:SetCondition(RD.ConditionFlipMainPhase)
	e1:SetTarget(cm.target)
	e1:SetOperation(cm.operation)
```

### Mask of Darkness (`120307007`)

Source: [Rush/Scripts/c120307007.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120307007.lua)

```lua
	e1:SetType(EFFECT_TYPE_IGNITION)
	e1:SetRange(LOCATION_MZONE)
	e1:SetCondition(RD.ConditionFlipMainPhase)
	e1:SetTarget(cm.target)
	e1:SetOperation(cm.operation)
```

### Penguin Soldier (`120307022`)

Source: [Rush/Scripts/c120307022.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120307022.lua)

```lua
	e1:SetType(EFFECT_TYPE_IGNITION)
	e1:SetRange(LOCATION_MZONE)
	e1:SetCondition(RD.ConditionFlipMainPhase)
	e1:SetTarget(cm.target)
	e1:SetOperation(cm.operation)
```
