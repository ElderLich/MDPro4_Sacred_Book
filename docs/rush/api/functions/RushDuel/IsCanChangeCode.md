# RushDuel.IsCanChangeCode

Alias: `RD.IsCanChangeCode`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.IsCanChangeCode(any card, any code) -> any
```

## Description

Rush Duel helper declared in `RDCondition.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
条件: 可以改变卡名
```

## Parameters

- `card` `any`: Type and behavior are not yet reviewed; see the source.
- `code` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDCondition.lua:118`

```lua
function RushDuel.IsCanChangeCode(card, code)
    return not card:IsCode(code)
end
```

## Used By

Generated from the local `Rush/Scripts/` folder and `rush_cards.cdb`.

- Detected in **59** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=rush&mode=code&q=RushDuel.IsCanChangeCode) with `RushDuel.IsCanChangeCode`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Red-Eyes Mars Dragon](/examples/rush-cards/120306034) | `120306034` | [Rush/Scripts/c120306034.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120306034.lua) | 1 |
| [Botonaginata the Music Princess](/examples/rush-cards/120290009) | `120290009` | [Rush/Scripts/c120290009.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120290009.lua) | 1 |
| [Soleil, the Fairy of Skysavior](/examples/rush-cards/120235020) | `120235020` | [Rush/Scripts/c120235020.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120235020.lua) | 1 |
| Harpie Lady Feather Duster | `120279002` | [Rush/Scripts/c120279002.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120279002.lua) | 1 |
| Lua, the Fairy of Skysavior | `120235021` | [Rush/Scripts/c120235021.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120235021.lua) | 1 |
| Imaginary Leading Actor | `120271029` | [Rush/Scripts/c120271029.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120271029.lua) | 1 |
| Battletested Curse of Dragon | `120249031` | [Rush/Scripts/c120249031.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120249031.lua) | 1 |
| Voidvelg Whiterider | `120109060` | [Rush/Scripts/c120109060.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120109060.lua) | 1 |
| Voidalfr Buprestruve | `120300003` | [Rush/Scripts/c120300003.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120300003.lua) | 1 |
| Blue-Eyes Vision Dragon | `120252004` | [Rush/Scripts/c120252004.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120252004.lua) | 1 |
| Vic Viper Beginning | `120294026` | [Rush/Scripts/c120294026.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120294026.lua) | 1 |
| Battletested Gaia The Fierce Knight | `120249032` | [Rush/Scripts/c120249032.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120249032.lua) | 1 |
| Cyber Processor | `120244021` | [Rush/Scripts/c120244021.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120244021.lua) | 1 |
| Skull Archfiend of Confusion | `120277023` | [Rush/Scripts/c120277023.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120277023.lua) | 1 |
| The Swordsman Who Doles Out Victory | `120290023` | [Rush/Scripts/c120290023.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120290023.lua) | 1 |
| Enceladustellime | `120304003` | [Rush/Scripts/c120304003.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120304003.lua) | 1 |
| Vic Viper Spread Bomb | `120294025` | [Rush/Scripts/c120294025.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120294025.lua) | 1 |
| Etraynze the Sprinting Shadow Flower Ninja | `120285012` | [Rush/Scripts/c120285012.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120285012.lua) | 1 |
| The Draco | `120294002` | [Rush/Scripts/c120294002.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120294002.lua) | 1 |
| Resurrection Heliacal Riser | `120304039` | [Rush/Scripts/c120304039.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120304039.lua) | 1 |
| X-Trial Cannon | `120305008` | [Rush/Scripts/c120305008.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120305008.lua) | 1 |
| Cyber Dragon Nachster | `120278009` | [Rush/Scripts/c120278009.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120278009.lua) | 1 |
| Special Operative Flavor Inspector | `120300017` | [Rush/Scripts/c120300017.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120300017.lua) | 1 |
| Super-Dimensional Lord British Space Fighter | `120294065` | [Rush/Scripts/c120294065.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120294065.lua) | 1 |
| ...and 35 more |  |  |  |

## Script Examples

### Red-Eyes Mars Dragon (`120306034`)

Source: [Rush/Scripts/c120306034.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120306034.lua)

```lua
end
function cm.condition(e,tp,eg,ep,ev,re,r,rp)
	return RD.IsCanChangeCode(e:GetHandler(),list[1])
end
cm.cost=RD.CostSendDeckTopToGrave(1)
```

### Botonaginata the Music Princess (`120290009`)

Source: [Rush/Scripts/c120290009.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120290009.lua)

```lua
end
function cm.condition(e,tp,eg,ep,ev,re,r,rp)
	return RD.IsCanChangeCode(e:GetHandler(),list[1])
end
cm.cost=RD.CostSendHandToGrave(Card.IsAbleToGraveAsCost,1,1)
```

### Soleil, the Fairy of Skysavior (`120235020`)

Source: [Rush/Scripts/c120235020.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120235020.lua)

```lua
end
function cm.condition(e,tp,eg,ep,ev,re,r,rp)
	return RD.IsCanChangeCode(e:GetHandler(),list[1])
end
cm.cost=RD.CostShowHand(cm.costfilter,1,1)
```
