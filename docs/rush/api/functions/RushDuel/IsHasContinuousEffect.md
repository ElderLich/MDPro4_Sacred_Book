# RushDuel.IsHasContinuousEffect

Alias: `RD.IsHasContinuousEffect`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.IsHasContinuousEffect(any card) -> any
```

## Description

Rush Duel helper declared in `RDCondition.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
条件: 是否拥有永续效果
```

## Parameters

- `card` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDCondition.lua:134`

```lua
function RushDuel.IsHasContinuousEffect(card)
    local has_effect = card.continuous_effect
    if RushDuel.IsMaximumMode(card) then
        card:GetOverlayGroup():ForEach(function(tc)
            has_effect = has_effect or tc.continuous_effect
        end)
    end
    return has_effect
end
```

## Used By

Generated from the local `Rush/Scripts/` folder and `rush_cards.cdb`.

- Detected in **5** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=rush&mode=code&q=RushDuel.IsHasContinuousEffect) with `RushDuel.IsHasContinuousEffect`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Ancient Gear Medic | `120271009` | [Rush/Scripts/c120271009.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120271009.lua) | 1 |
| Evasive Chaos Ninjutsu Art of I Want You | `120277053` | [Rush/Scripts/c120277053.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120277053.lua) | 1 |
| Mulliness Power Beetle | `120277038` | [Rush/Scripts/c120277038.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120277038.lua) | 1 |
| Evasive Chaos Ninsect Rosary Cicada | `120277012` | [Rush/Scripts/c120277012.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120277012.lua) | 1 |
| Ancient Gear Tyranno | `120271005` | [Rush/Scripts/c120271005.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120271005.lua) | 1 |

## Script Examples

### Ancient Gear Medic (`120271009`)

Source: [Rush/Scripts/c120271009.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120271009.lua)

```lua
end
function cm.thfilter(c)
	return RD.IsHasContinuousEffect(c) and c:IsAttribute(ATTRIBUTE_EARTH) and c:IsRace(RACE_MACHINE)
		and c:IsAbleToHand()
end
```

### Evasive Chaos Ninjutsu Art of I Want You (`120277053`)

Source: [Rush/Scripts/c120277053.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120277053.lua)

```lua
end
function cm.spfilter(c,e,tp)
	return RD.IsHasContinuousEffect(c) and c:IsLevelAbove(5) and c:IsLevelBelow(8)
		and c:IsAttribute(ATTRIBUTE_DARK) and c:IsRace(RACE_INSECT) and RD.IsDefense(c,400)
		and RD.IsCanBeSpecialSummoned(c,e,tp,POS_FACEUP)
```

### Mulliness Power Beetle (`120277038`)

Source: [Rush/Scripts/c120277038.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120277038.lua)

```lua
end
function cm.spfilter(c,e,tp)
	return RD.IsHasContinuousEffect(c) and c:IsRace(RACE_INSECT) and RD.IsDefense(c,400)
		and RD.IsCanBeSpecialSummoned(c,e,tp,POS_FACEUP_DEFENSE)
end
```
