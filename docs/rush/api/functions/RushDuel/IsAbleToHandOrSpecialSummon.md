# RushDuel.IsAbleToHandOrSpecialSummon

Alias: `RD.IsAbleToHandOrSpecialSummon`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.IsAbleToHandOrSpecialSummon(any card, any effect, any player, any position) -> any
```

## Description

Rush Duel helper declared in `RDCondition.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
条件: 可否加入手卡或特殊召唤
```

## Parameters

- `card` `any`: Type and behavior are not yet reviewed; see the source.
- `effect` `any`: Type and behavior are not yet reviewed; see the source.
- `player` `any`: Type and behavior are not yet reviewed; see the source.
- `position` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDCondition.lua:130`

```lua
function RushDuel.IsAbleToHandOrSpecialSummon(card, effect, player, position)
    return card:IsAbleToHand() or (Duel.GetLocationCount(player, LOCATION_MZONE) > 0 and RushDuel.IsCanBeSpecialSummoned(card, effect, player, position))
end
```

## Used By

Generated from the local `Rush/Scripts/` folder and `rush_cards.cdb`.

- Detected in **6** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=rush&mode=code&q=RushDuel.IsAbleToHandOrSpecialSummon) with `RushDuel.IsAbleToHandOrSpecialSummon`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Bone Spine Whip | `120277064` | [Rush/Scripts/c120277064.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120277064.lua) | 1 |
| Hydro Blaster Mini Bluefin | `120253017` | [Rush/Scripts/c120253017.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120253017.lua) | 1 |
| Geefor the Defiant Soul | `120298006` | [Rush/Scripts/c120298006.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120298006.lua) | 1 |
| Hack for the Intel | `120290059` | [Rush/Scripts/c120290059.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120290059.lua) | 1 |
| Blaze Fiend Overlord Luciless | `120254036` | [Rush/Scripts/c120254036.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120254036.lua) | 1 |
| Wooly Wonderland Fluffy | `120293018` | [Rush/Scripts/c120293018.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120293018.lua) | 1 |

## Script Examples

### Bone Spine Whip (`120277064`)

Source: [Rush/Scripts/c120277064.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120277064.lua)

```lua
function cm.filter(c,e,tp)
	return c:IsLevelBelow(5) and c:IsRace(RACE_ZOMBIE)
		and RD.IsAbleToHandOrSpecialSummon(c,e,tp,POS_FACEUP)
end
function cm.exfilter(c)
```

### Hydro Blaster Mini Bluefin (`120253017`)

Source: [Rush/Scripts/c120253017.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120253017.lua)

```lua
end
function cm.exfilter(c,e,tp)
	return c:IsCode(list[1]) and RD.IsAbleToHandOrSpecialSummon(c,e,tp,POS_FACEUP)
end
cm.cost=RD.CostSendDeckTopToGrave(1)
```

### Geefor the Defiant Soul (`120298006`)

Source: [Rush/Scripts/c120298006.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120298006.lua)

```lua
function cm.exfilter(c,e,tp)
	return c:IsLevel(5) and c:IsCode(list[1])
		and RD.IsAbleToHandOrSpecialSummon(c,e,tp,POS_FACEUP)
end
cm.cost=RD.CostSendDeckTopToGrave(1)
```
