# RushDuel.ConditionSummonOrSpecialSummonMainPhase

Alias: `RD.ConditionSummonOrSpecialSummonMainPhase`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.ConditionSummonOrSpecialSummonMainPhase(any e) -> any
```

## Description

Rush Duel helper declared in `RDCondition.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
通用条件: 这张卡召唤·特殊召唤的自己主要阶段
```

## Parameters

- `e` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDCondition.lua:436`

```lua
function RushDuel.ConditionSummonOrSpecialSummonMainPhase(e)
	return RushDuel.IsSummonOrSpecialSummonMainPhase(e:GetHandler())
end
```

## Used By

Generated from the local `Rush/Scripts/` folder and `rush_cards.cdb`.

- Detected in **102** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=rush&mode=code&q=RushDuel.ConditionSummonOrSpecialSummonMainPhase) with `RushDuel.ConditionSummonOrSpecialSummonMainPhase`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [The Black Witch Facing the Temple](/examples/rush-cards/120309048) | `120309048` | [Rush/Scripts/c120309048.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120309048.lua) | 1 |
| [Handy Girl](/examples/rush-cards/120290012) | `120290012` | [Rush/Scripts/c120290012.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120290012.lua) | 1 |
| [Necromaid Timer](/examples/rush-cards/120294014) | `120294014` | [Rush/Scripts/c120294014.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120294014.lua) | 1 |
| [Ecliceras Drakon](/examples/rush-cards/120109033) | `120109033` | [Rush/Scripts/c120109033.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120109033.lua) | 1 |
| Qadi of the Monumenthes | `120300009` | [Rush/Scripts/c120300009.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120300009.lua) | 1 |
| Blaze Fiend Overlord Zebulth | `120287033` | [Rush/Scripts/c120287033.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120287033.lua) | 1 |
| Speed Carrier | `120301059` | [Rush/Scripts/c120301059.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120301059.lua) | 1 |
| Soul Drake | `120252007` | [Rush/Scripts/c120252007.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120252007.lua) | 1 |
| Sparkhearts Anesh | `120298022` | [Rush/Scripts/c120298022.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120298022.lua) | 1 |
| Lana the Holy Wind of Healing | `120298044` | [Rush/Scripts/c120298044.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120298044.lua) | 1 |
| Salvage Wolfish | `120228036` | [Rush/Scripts/c120228036.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120228036.lua) | 1 |
| Speed Commander | `120301058` | [Rush/Scripts/c120301058.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120301058.lua) | 1 |
| Grand Legendary Priest | `120271043` | [Rush/Scripts/c120271043.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120271043.lua) | 1 |
| Animagica Shooter | `120277032` | [Rush/Scripts/c120277032.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120277032.lua) | 1 |
| Draco the Wounded | `120294004` | [Rush/Scripts/c120294004.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120294004.lua) | 1 |
| Beast Gear Sage Roller Stag | `120222033` | [Rush/Scripts/c120222033.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120222033.lua) | 1 |
| Freewind | `120290017` | [Rush/Scripts/c120290017.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120290017.lua) | 1 |
| Princess Cosmos the Trickster | `120293046` | [Rush/Scripts/c120293046.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120293046.lua) | 1 |
| Reifu the Dimensional Sworn Ally | `120309028` | [Rush/Scripts/c120309028.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120309028.lua) | 1 |
| Scissor Hercules | `120298038` | [Rush/Scripts/c120298038.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120298038.lua) | 1 |
| Healthie Olivia | `120306023` | [Rush/Scripts/c120306023.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120306023.lua) | 1 |
| Rising Unit | `120304026` | [Rush/Scripts/c120304026.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120304026.lua) | 1 |
| Animagica Gardna | `120277027` | [Rush/Scripts/c120277027.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120277027.lua) | 1 |
| Dedicated Gaia The Fierce Knight | `120293032` | [Rush/Scripts/c120293032.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120293032.lua) | 1 |
| ...and 78 more |  |  |  |

## Script Examples

### The Black Witch Facing the Temple (`120309048`)

Source: [Rush/Scripts/c120309048.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120309048.lua)

```lua
	e1:SetType(EFFECT_TYPE_IGNITION)
	e1:SetRange(LOCATION_MZONE)
	e1:SetCondition(RD.ConditionSummonOrSpecialSummonMainPhase)
	e1:SetCost(cm.cost)
	e1:SetTarget(cm.target)
```

### Handy Girl (`120290012`)

Source: [Rush/Scripts/c120290012.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120290012.lua)

```lua
	e1:SetType(EFFECT_TYPE_IGNITION)
	e1:SetRange(LOCATION_MZONE)
	e1:SetCondition(RD.ConditionSummonOrSpecialSummonMainPhase)
	e1:SetCost(cm.cost)
	e1:SetTarget(cm.target)
```

### Necromaid Timer (`120294014`)

Source: [Rush/Scripts/c120294014.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120294014.lua)

```lua
	e1:SetType(EFFECT_TYPE_IGNITION)
	e1:SetRange(LOCATION_MZONE)
	e1:SetCondition(RD.ConditionSummonOrSpecialSummonMainPhase)
	e1:SetCost(cm.cost)
	e1:SetTarget(cm.target)
```
