# RushDuel.IsLegendCard

Alias: `RD.IsLegendCard`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.IsLegendCard(Card card) -> bool
```

## Description

Checks TYPE_LEGEND or an EFFECT_LEGEND_CARD marker. This supports both the printed Rush Legend bit and effect-based Legend treatment.

## Parameters

- `card` `Card`: Card to inspect.

## Returns

- `bool`: Whether the card is treated as Legend.

## Source

`Rush/Utilities/RDLegend.lua:26`

```lua
function RushDuel.IsLegendCard(card)
    return card:IsType(TYPE_LEGEND) or card:IsHasEffect(EFFECT_LEGEND_CARD) ~= nil
end
```

## Used By

Generated from the local `Rush/Scripts/` folder and `rush_cards.cdb`.

- Detected in **34** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=rush&mode=code&q=RushDuel.IsLegendCard) with `RushDuel.IsLegendCard`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Red-Eyes Mars Dragon](/examples/rush-cards/120306034) | `120306034` | [Rush/Scripts/c120306034.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120306034.lua) | 1 |
| Udzue the Frost-Purifying Purebreed | `120296001` | [Rush/Scripts/c120296001.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120296001.lua) | 1 |
| Fate of the World | `120271054` | [Rush/Scripts/c120271054.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120271054.lua) | 1 |
| Legendary Saber | `120238010` | [Rush/Scripts/c120238010.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120238010.lua) | 1 |
| Legendary Hunter | `120271046` | [Rush/Scripts/c120271046.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120271046.lua) | 1 |
| Legendary Scout | `120271047` | [Rush/Scripts/c120271047.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120271047.lua) | 2 |
| Legendary Shooter | `120271045` | [Rush/Scripts/c120271045.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120271045.lua) | 1 |
| Skysavior Aspiration | `120301051` | [Rush/Scripts/c120301051.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120301051.lua) | 1 |
| Master Craftsman Kotetsu | `120238036` | [Rush/Scripts/c120238036.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120238036.lua) | 1 |
| Blue-Eyes Bright Dragon | `120252003` | [Rush/Scripts/c120252003.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120252003.lua) | 1 |
| Dark Magician of Chaos | `120307001` | [Rush/Scripts/c120307001.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120307001.lua) | 1 |
| Reminiscence of the Epic Tale | `120272054` | [Rush/Scripts/c120272054.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120272054.lua) | 1 |
| Legendary Strike | `120249057` | [Rush/Scripts/c120249057.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120249057.lua) | 2 |
| Malevolent Seller | `120238040` | [Rush/Scripts/c120238040.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120238040.lua) | 1 |
| Dark Paladin | `120283002` | [Rush/Scripts/c120283002.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120283002.lua) | 1 |
| Grand Legendar Saber Spirit | `120293067` | [Rush/Scripts/c120293067.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120293067.lua) | 1 |
| Yabume the Frost-Purifying Purebreed | `120298045` | [Rush/Scripts/c120298045.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120298045.lua) | 1 |
| Commanding Ritzy King Rex | `120290010` | [Rush/Scripts/c120290010.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120290010.lua) | 1 |
| Grand Legendary Party | `120309060` | [Rush/Scripts/c120309060.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120309060.lua) | 2 |
| Legendary Sparkseed | `120271061` | [Rush/Scripts/c120271061.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120271061.lua) | 1 |
| Legendary Magician | `120238005` | [Rush/Scripts/c120238005.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120238005.lua) | 1 |
| Grand Legendary Saber | `120271041` | [Rush/Scripts/c120271041.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120271041.lua) | 2 |
| Grand Legendary Magician | `120271042` | [Rush/Scripts/c120271042.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120271042.lua) | 1 |
| Legendary Priest | `120271044` | [Rush/Scripts/c120271044.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120271044.lua) | 1 |
| ...and 10 more |  |  |  |

## Script Examples

### Red-Eyes Mars Dragon (`120306034`)

Source: [Rush/Scripts/c120306034.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120306034.lua)

```lua
--Change Code
function cm.exfilter(c)
	return RD.IsLegendCard(c) and c:IsType(TYPE_NORMAL)
end
function cm.condition(e,tp,eg,ep,ev,re,r,rp)
```

### Udzue the Frost-Purifying Purebreed (`120296001`)

Source: [Rush/Scripts/c120296001.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120296001.lua)

```lua
--To Hand
function cm.thfilter(c)
	return not RD.IsLegendCard(c) and c:GetType()==TYPE_TRAP and c:IsAbleToHand()
end
function cm.target(e,tp,eg,ep,ev,re,r,rp,chk)
```

### Fate of the World (`120271054`)

Source: [Rush/Scripts/c120271054.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120271054.lua)

```lua
end
function cm.costfilter(c)
	return RD.IsLegendCard(c) and c:IsType(TYPE_MONSTER) and c:IsAbleToDeckAsCost()
end
function cm.filter(c)
```
