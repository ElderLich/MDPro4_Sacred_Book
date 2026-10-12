# RushDuel.IsCanAttachCannotTrigger

Alias: `RD.IsCanAttachCannotTrigger`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.IsCanAttachCannotTrigger(any card) -> any
```

## Description

Rush Duel helper declared in `RDCondition.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
条件: 可否赋予效果 - 不能发动效果
```

## Parameters

- `card` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDCondition.lua:350`

```lua
function RushDuel.IsCanAttachCannotTrigger(card)
    return not card:IsHasEffect(EFFECT_CANNOT_TRIGGER)
end
```

## Used By

Generated from the local `Rush/Scripts/` folder and `rush_cards.cdb`.

- Detected in **6** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=rush&mode=code&q=RushDuel.IsCanAttachCannotTrigger) with `RushDuel.IsCanAttachCannotTrigger`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Raging Rock | `120246072` | [Rush/Scripts/c120246072.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120246072.lua) | 1 |
| Spirit of Isyria | `120300061` | [Rush/Scripts/c120300061.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120300061.lua) | 1 |
| Metarion Medustar | `120271018` | [Rush/Scripts/c120271018.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120271018.lua) | 1 |
| Thunderbeetle Crash | `120306007` | [Rush/Scripts/c120306007.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120306007.lua) | 1 |
| Criatura Brazo | `120291005` | [Rush/Scripts/c120291005.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120291005.lua) | 1 |
| Ultimate Flag Beast Boltricorn | `120246013` | [Rush/Scripts/c120246013.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120246013.lua) | 1 |

## Script Examples

### Raging Rock (`120246072`)

Source: [Rush/Scripts/c120246072.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120246072.lua)

```lua
end
function cm.filter(c)
	return c:IsFaceup() and c:IsType(TYPE_EFFECT) and RD.IsCanAttachCannotTrigger(c)
end
function cm.condition(e,tp,eg,ep,ev,re,r,rp)
```

### Spirit of Isyria (`120300061`)

Source: [Rush/Scripts/c120300061.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120300061.lua)

```lua
function cm.filter(c)
	return c:IsFaceup() and c:IsType(TYPE_EFFECT) and c:IsLevelBelow(8)
		and RD.IsCanAttachCannotTrigger(c)
end
function cm.condition(e,tp,eg,ep,ev,re,r,rp)
```

### Metarion Medustar (`120271018`)

Source: [Rush/Scripts/c120271018.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120271018.lua)

```lua
--Cannot Trigger
function cm.setfilter(c)
	return c:IsFacedown() and c:IsType(TYPE_SPELL+TYPE_TRAP) and RD.IsCanAttachCannotTrigger(c)
end
function cm.target1(e,tp,eg,ep,ev,re,r,rp,chk)
```
