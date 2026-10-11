# RushDuel.IsCanChangeDef

Alias: `RD.IsCanChangeDef`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.IsCanChangeDef(any card) -> any
```

## Description

Rush Duel helper declared in `RDCondition.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
条件: 可否改变守备力
```

## Parameters

- `card` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDCondition.lua:107`

```lua
function RushDuel.IsCanChangeDef(card)
    return card:IsDefenseAbove(0) and not RushDuel.IsMaximumMode(card)
end
```

## Used By

Generated from the local `Rush/Scripts/` folder and `rush_cards.cdb`.

- Detected in **6** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=rush&mode=code&q=RushDuel.IsCanChangeDef) with `RushDuel.IsCanChangeDef`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Lightning Braver | `120213018` | [Rush/Scripts/c120213018.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120213018.lua) | 1 |
| Painful Choice | `120109062` | [Rush/Scripts/c120109062.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120109062.lua) | 1 |
| Sword &amp; Shield | `120155052` | [Rush/Scripts/c120155052.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120155052.lua) | 4 |
| Smashing Ground | `120203017` | [Rush/Scripts/c120203017.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120203017.lua) | 1 |
| Fire Golem | `120120019` | [Rush/Scripts/c120120019.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120120019.lua) | 1 |
| Shield &amp; Sword | `120140009` | [Rush/Scripts/c120140009.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120140009.lua) | 1 |

## Script Examples

### Lightning Braver (`120213018`)

Source: [Rush/Scripts/c120213018.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120213018.lua)

```lua
end
function cm.downfilter(c)
	return c:IsFaceup() and RD.IsCanChangeDef(c)
end
cm.cost=RD.CostSendGraveToDeck(cm.costfilter,3,3)
```

### Painful Choice (`120109062`)

Source: [Rush/Scripts/c120109062.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120109062.lua)

```lua
--Activate
function cm.filter(c)
	return c:IsFaceup() and RD.IsCanChangeDef(c)
end
function cm.target(e,tp,eg,ep,ev,re,r,rp,chk)
```

### Sword & Shield (`120155052`)

Source: [Rush/Scripts/c120155052.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120155052.lua)

```lua
	local tc=Duel.GetAttacker()
	local bc=Duel.GetAttackTarget()
	return tc:IsControler(1-tp) and tc:IsLevelBelow(9) and RD.IsCanChangeDef(tc)
		and bc and bc:IsAttackPos() and RD.IsCanChangeDef(bc)
end
```
