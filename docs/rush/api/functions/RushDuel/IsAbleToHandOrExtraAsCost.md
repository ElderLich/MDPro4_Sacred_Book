# RushDuel.IsAbleToHandOrExtraAsCost

Alias: `RD.IsAbleToHandOrExtraAsCost`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.IsAbleToHandOrExtraAsCost(any card) -> any
```

## Description

Rush Duel helper declared in `RDCondition.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
条件: 可以作为Cost回到手卡或者额外卡组
```

## Parameters

- `card` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDCondition.lua:122`

```lua
function RushDuel.IsAbleToHandOrExtraAsCost(card)
    return card:IsAbleToHandAsCost() or card:IsAbleToExtraAsCost()
end
```

## Used By

Generated from the local `Rush/Scripts/` folder and `rush_cards.cdb`.

- Detected in **4** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=rush&mode=code&q=RushDuel.IsAbleToHandOrExtraAsCost) with `RushDuel.IsAbleToHandOrExtraAsCost`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| CAN - Melo:D | `120203010` | [Rush/Scripts/c120203010.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120203010.lua) | 1 |
| Jointech Spike Centipede | `120249007` | [Rush/Scripts/c120249007.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120249007.lua) | 1 |
| Harpie Cielo | `120102003` | [Rush/Scripts/c120102003.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120102003.lua) | 1 |
| Giant Tiger Strike | `120247037` | [Rush/Scripts/c120247037.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120247037.lua) | 1 |

## Script Examples

### CAN - Melo:D (`120203010`)

Source: [Rush/Scripts/c120203010.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120203010.lua)

```lua
--To Deck
function cm.costfilter(c)
	return c:IsFaceup() and c:IsLevelAbove(5) and RD.IsAbleToHandOrExtraAsCost(c)
end
function cm.tdfilter(c)
```

### Jointech Spike Centipede (`120249007`)

Source: [Rush/Scripts/c120249007.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120249007.lua)

```lua
function cm.costfilter(c)
	return c:IsFaceup() and c:IsLevelAbove(5) and c:IsAttribute(ATTRIBUTE_EARTH)
		and c:IsRace(RACE_MACHINE) and RD.IsAbleToHandOrExtraAsCost(c)
end
cm.cost=RD.CostSendMZoneToHand(cm.costfilter,1,1,true)
```

### Harpie Cielo (`120102003`)

Source: [Rush/Scripts/c120102003.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120102003.lua)

```lua
--Discard Deck
function cm.costfilter(c)
	return c:IsFaceup() and c:IsCode(list[1]) and RD.IsAbleToHandOrExtraAsCost(c)
end
function cm.exfilter(c)
```
