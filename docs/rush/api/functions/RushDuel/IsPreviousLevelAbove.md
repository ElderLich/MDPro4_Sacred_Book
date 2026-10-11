# RushDuel.IsPreviousLevelAbove

Alias: `RD.IsPreviousLevelAbove`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.IsPreviousLevelAbove(any card, any level) -> any
```

## Description

Rush Duel helper declared in `RDCondition.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
条件: 位置变化前的等级大于
```

## Parameters

- `card` `any`: Type and behavior are not yet reviewed; see the source.
- `level` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDCondition.lua:214`

```lua
function RushDuel.IsPreviousLevelAbove(card, level)
    return card:GetPreviousLevelOnField() >= level
end
```

## Used By

Generated from the local `Rush/Scripts/` folder and `rush_cards.cdb`.

- Detected in **3** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=rush&mode=code&q=RushDuel.IsPreviousLevelAbove) with `RushDuel.IsPreviousLevelAbove`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Dark Ruler Sword Swipe | `120188030` | [Rush/Scripts/c120188030.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120188030.lua) | 1 |
| Archfiend's Revival | `120170062` | [Rush/Scripts/c120170062.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120170062.lua) | 1 |
| Constructor Resurrection | `120151033` | [Rush/Scripts/c120151033.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120151033.lua) | 1 |

## Script Examples

### Dark Ruler Sword Swipe (`120188030`)

Source: [Rush/Scripts/c120188030.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120188030.lua)

```lua
--Activate
function cm.confilter(c,tp,re,rp)
	return c:IsPreviousPosition(POS_ATTACK) and RD.IsPreviousLevelAbove(c,7)
		and RD.IsPreviousRace(c,RACE_WARRIOR)
		and RD.IsPreviousControler(c,tp) and c:IsPreviousLocation(LOCATION_MZONE)
```

### Archfiend's Revival (`120170062`)

Source: [Rush/Scripts/c120170062.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120170062.lua)

```lua
function cm.confilter(c,tp)
	return (RD.IsLegendCode(c,list[1]) or RD.IsPreviousCode(c,list[1]) or (
			RD.IsPreviousType(c,TYPE_NORMAL) and RD.IsPreviousLevelAbove(c,7) and RD.IsPreviousRace(c,RACE_FIEND)
		)) and RD.IsPreviousControler(c,tp) and c==Duel.GetAttackTarget()
end
```

### Constructor Resurrection (`120151033`)

Source: [Rush/Scripts/c120151033.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120151033.lua)

```lua
	return RD.IsPreviousControler(c,tp) and c==Duel.GetAttackTarget()
		and RD.IsPreviousRace(c,RACE_WYRM)
		and RD.IsPreviousLevelAbove(c,7)
end
function cm.spfilter(c,e,tp)
```
