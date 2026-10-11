# Card.IsFusionType

## Signature

```lua
Card.IsFusionType(Card c, int type) -> bool
```

## Description

Checks whether c's type while used as Fusion Material contains type.
For an original Monster Card in the Spell & Trap Zone, the core uses the card-data type while material checks are active; otherwise it uses c's current type.

## Parameters

- `c` `Card`
- `type` `int`

## Returns

- `bool`

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3538`

## Guided Examples

Learn how to use this function in context:

- [Fusion Procedure Guide](/learn/fusion-procedure)

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **87** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=standard&mode=code&q=Card.IsFusionType) with `Card.IsFusionType`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Goyo Emperor](/examples/cards/59255742) | `59255742` | [Scripts/c59255742.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c59255742.lua) | 1 |
| [D/D/D/D Dimensional King Arc Crisis](/examples/cards/71398055) | `71398055` | [Scripts/c71398055.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c71398055.lua) | 4 |
| [Odd-Eyes Arcray Dragon](/examples/cards/6218704) | `6218704` | [Scripts/c6218704.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c6218704.lua) | 4 |
| [Starving Venemy Dragon](/examples/cards/93729065) | `93729065` | [Scripts/c93729065.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c93729065.lua) | 1 |
| Vaylantz Genesis Grand Duke | `76075139` | [Scripts/c76075139.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c76075139.lua) | 1 |
| Starving Venom Wing Dragon | `5148778` | [Scripts/c5148778.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c5148778.lua) | 1 |
| Magikey Dragon - Andrabime | `71159974` | [Scripts/c71159974.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c71159974.lua) | 2 |
| Windwitch - Crystal Bell | `25793414` | [Scripts/c25793414.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c25793414.lua) | 1 |
| Zoroa, the Magistus Verethragna | `37260677` | [Scripts/c37260677.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c37260677.lua) | 1 |
| Destiny HERO - Dusktopia | `93657021` | [Scripts/c93657021.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c93657021.lua) | 1 |
| Miracle Synchro Fusion | `36484016` | [Scripts/c36484016.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c36484016.lua) | 1 |
| Cyberdark End Dragon | `37542782` | [Scripts/c37542782.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c37542782.lua) | 1 |
| Millennium-Eyes Restrict | `41578483` | [Scripts/c41578483.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c41578483.lua) | 1 |
| Thunder Dragon Titan | `41685633` | [Scripts/c41685633.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c41685633.lua) | 1 |
| Supreme King Z-ARC | `13331639` | [Scripts/c13331639.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c13331639.lua) | 4 |
| Pendulum Dimension | `84274024` | [Scripts/c84274024.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c84274024.lua) | 1 |
| Red-Eyes Dark Dragoon | `37818794` | [Scripts/c37818794.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c37818794.lua) | 2 |
| Borreload Fatalflare Dragon | `84464389` | [Scripts/c84464389.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c84464389.lua) | 1 |
| Oracle of Zefra | `32354768` | [Scripts/c32354768.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c32354768.lua) | 1 |
| Mirrorjade the Iceblade Dragon | `44146295` | [Scripts/c44146295.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c44146295.lua) | 3 |
| Cyberse Clock Dragon | `42717221` | [Scripts/c42717221.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c42717221.lua) | 1 |
| Dinomorphia Rexterm | `92798873` | [Scripts/c92798873.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c92798873.lua) | 1 |
| Sprind the Irondash Dragon | `1906812` | [Scripts/c1906812.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c1906812.lua) | 1 |
| Invoked Magistus Omega | `38423248` | [Scripts/c38423248.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c38423248.lua) | 1 |
| ...and 63 more |  |  |  |

## Script Examples

### Goyo Emperor (`59255742`)

Source: [Scripts/c59255742.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c59255742.lua)

```lua
c59255742.material_type=TYPE_SYNCHRO
function c59255742.ffilter(c)
	return c:IsFusionAttribute(ATTRIBUTE_EARTH) and c:IsRace(RACE_WARRIOR) and c:IsFusionType(TYPE_SYNCHRO)
end
function c59255742.spcon(e,tp,eg,ep,ev,re,r,rp)
```

### D/D/D/D Dimensional King Arc Crisis (`71398055`)

Source: [Scripts/c71398055.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c71398055.lua)

```lua
end
function s.fusfilter1(c)
	return c:IsRace(RACE_FIEND) and c:IsFusionType(TYPE_FUSION)
end
function s.fusfilter2(c)
```

### Odd-Eyes Arcray Dragon (`6218704`)

Source: [Scripts/c6218704.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c6218704.lua)

```lua
c6218704.material_type=TYPE_SYNCHRO
function c6218704.fusfilter1(c)
	return c:IsRace(RACE_DRAGON) and c:IsFusionType(TYPE_FUSION)
end
function c6218704.fusfilter2(c)
```
