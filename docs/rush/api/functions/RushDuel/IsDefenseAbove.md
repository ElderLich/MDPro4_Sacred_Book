# RushDuel.IsDefenseAbove

Alias: `RD.IsDefenseAbove`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.IsDefenseAbove(any card, any def) -> any
```

## Description

Rush Duel helper declared in `RDCondition.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
条件: 守备力在 def 以上
```

## Parameters

- `card` `any`: Type and behavior are not yet reviewed; see the source.
- `def` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDCondition.lua:95`

```lua
function RushDuel.IsDefenseAbove(card, def)
    return card:IsDefenseAbove(def) and not RushDuel.IsMaximumMode(card)
end
```

## Used By

Generated from the local `Rush/Scripts/` folder and `rush_cards.cdb`.

- Detected in **10** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=rush&mode=code&q=RushDuel.IsDefenseAbove) with `RushDuel.IsDefenseAbove`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Sword Skill - Ruler's Slash | `120208046` | [Rush/Scripts/c120208046.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120208046.lua) | 1 |
| Animagica Coin | `120277056` | [Rush/Scripts/c120277056.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120277056.lua) | 1 |
| Animagica Gardna | `120277027` | [Rush/Scripts/c120277027.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120277027.lua) | 1 |
| Light-Calling Griffore | `120280008` | [Rush/Scripts/c120280008.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120280008.lua) | 1 |
| Void Dust Fusion | `120277052` | [Rush/Scripts/c120277052.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120277052.lua) | 1 |
| Defense Destroying Sword | `120208047` | [Rush/Scripts/c120208047.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120208047.lua) | 1 |
| Scarechair Code | `120260072` | [Rush/Scripts/c120260072.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120260072.lua) | 1 |
| Long Shield Gardna | `120145037` | [Rush/Scripts/c120145037.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120145037.lua) | 1 |
| All-Seeing Harvey | `120249040` | [Rush/Scripts/c120249040.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120249040.lua) | 1 |
| Dark Ruler Tempest | `120183042` | [Rush/Scripts/c120183042.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120183042.lua) | 1 |

## Script Examples

### Sword Skill - Ruler's Slash (`120208046`)

Source: [Rush/Scripts/c120208046.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120208046.lua)

```lua
end
function cm.filter(c)
	return c:IsFaceup() and c:IsAttackAbove(2500) and RD.IsDefenseAbove(c,2500)
end
function cm.desfilter(c)
```

### Animagica Coin (`120277056`)

Source: [Rush/Scripts/c120277056.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120277056.lua)

```lua
function cm.thfilter(c)
	return c:IsLevel(7,8) and c:IsAttribute(ATTRIBUTE_LIGHT) and c:IsRace(RACE_BEAST)
		and RD.IsDefenseAbove(c,1500) and c:IsAbleToHand()
end
function cm.target(e,tp,eg,ep,ev,re,r,rp,chk)
```

### Animagica Gardna (`120277027`)

Source: [Rush/Scripts/c120277027.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120277027.lua)

```lua
function cm.thfilter(c)
	return c:IsLevel(7,8) and c:IsAttribute(ATTRIBUTE_LIGHT) and c:IsRace(RACE_BEAST)
		and RD.IsDefenseAbove(c,1500) and c:IsAbleToHand()
end
cm.cost=RD.CostSendHandToGrave(Card.IsAbleToGraveAsCost,1,1)
```
