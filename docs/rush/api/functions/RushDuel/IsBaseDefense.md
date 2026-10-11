# RushDuel.IsBaseDefense

Alias: `RD.IsBaseDefense`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.IsBaseDefense(any card, any def) -> any
```

## Description

Rush Duel helper declared in `RDCondition.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
条件: 原本守备力为 def
```

## Parameters

- `card` `any`: Type and behavior are not yet reviewed; see the source.
- `def` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDCondition.lua:103`

```lua
function RushDuel.IsBaseDefense(card, def)
    return card:GetBaseDefense() == def and not RushDuel.IsMaximumMode(card)
end
```

## Used By

Generated from the local `Rush/Scripts/` folder and `rush_cards.cdb`.

- Detected in **20** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=rush&mode=code&q=RushDuel.IsBaseDefense) with `RushDuel.IsBaseDefense`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Handy Girl](/examples/rush-cards/120290012) | `120290012` | [Rush/Scripts/c120290012.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120290012.lua) | 1 |
| Vic Viper Spread Bomb | `120294025` | [Rush/Scripts/c120294025.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120294025.lua) | 1 |
| Lovely Connect | `120300054` | [Rush/Scripts/c120300054.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120300054.lua) | 1 |
| Super-Dimensional Lord British Space Fighter | `120294065` | [Rush/Scripts/c120294065.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120294065.lua) | 1 |
| Lovely Blessing | `120260051` | [Rush/Scripts/c120260051.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120260051.lua) | 1 |
| First Cat Search | `120290046` | [Rush/Scripts/c120290046.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120290046.lua) | 1 |
| Piping Hot Delivery | `120290045` | [Rush/Scripts/c120290045.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120290045.lua) | 1 |
| Gradius' Option | `120294023` | [Rush/Scripts/c120294023.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120294023.lua) | 1 |
| Power Capsule Red | `120294056` | [Rush/Scripts/c120294056.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120294056.lua) | 1 |
| Power Capsule Blue | `120294055` | [Rush/Scripts/c120294055.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120294055.lua) | 1 |
| Plus Skull | `120261040` | [Rush/Scripts/c120261040.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120261040.lua) | 1 |
| Legendary Party | `120309061` | [Rush/Scripts/c120309061.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120309061.lua) | 1 |
| Lovely Return | `120260055` | [Rush/Scripts/c120260055.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120260055.lua) | 1 |
| Home of the Charmers | `120301021` | [Rush/Scripts/c120301021.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120301021.lua) | 2 |
| Healthie Lamilla | `120306021` | [Rush/Scripts/c120306021.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120306021.lua) | 1 |
| The Sounds of a Piano Heard After School | `120306008` | [Rush/Scripts/c120306008.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120306008.lua) | 1 |
| Dark Battle Grounds | `120249053` | [Rush/Scripts/c120249053.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120249053.lua) | 1 |
| The Emperor Realm | `120244056` | [Rush/Scripts/c120244056.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120244056.lua) | 1 |
| Cheerful Waitress | `120290016` | [Rush/Scripts/c120290016.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120290016.lua) | 1 |
| Freshberry Garden | `120264057` | [Rush/Scripts/c120264057.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120264057.lua) | 1 |

## Script Examples

### Handy Girl (`120290012`)

Source: [Rush/Scripts/c120290012.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120290012.lua)

```lua
end
function cm.matfilter(c)
	return RD.IsBaseDefense(c,1200) and c:IsFusionAttribute(ATTRIBUTE_WIND)
end
cm.cost=RD.CostSendHandToDeckBottom(Card.IsAbleToDeckAsCost,1,1,false)
```

### Vic Viper Spread Bomb (`120294025`)

Source: [Rush/Scripts/c120294025.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120294025.lua)

```lua
end
function cm.atktg(e,c)
	return not (RD.IsBaseDefense(c,800) and c:IsRace(RACE_MACHINE))
end
```

### Lovely Connect (`120300054`)

Source: [Rush/Scripts/c120300054.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120300054.lua)

```lua
function cm.exfilter(c)
	return c:IsFaceup() and c:IsAttribute(ATTRIBUTE_LIGHT) and c:IsRace(RACE_FAIRY)
		and c:GetBaseAttack()==0 and RD.IsBaseDefense(c,0)
end
function cm.tdfilter(c)
```
