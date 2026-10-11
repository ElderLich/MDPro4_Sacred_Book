# Card.IsFusionAttribute

## Signature

```lua
Card.IsFusionAttribute(Card c, int attribute, [int player]) -> bool
```

## Description

Checks whether c's Attribute while used as Fusion Material contains attribute.
player defaults to the current reason player. The core uses c:GetFusionAttribute(player), so Fusion Material Attribute-changing effects are included.

## Parameters

- `c` `Card`
- `attribute` `int`
- `player` `int` optional - default: current reason player

## Returns

- `bool`

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3550`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **84** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=standard&mode=code&q=Card.IsFusionAttribute) with `Card.IsFusionAttribute`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Lady's Dragonmaid](/examples/cards/48658295) | `48658295` | [Scripts/c48658295.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c48658295.lua) | 1 |
| [Goyo Emperor](/examples/cards/59255742) | `59255742` | [Scripts/c59255742.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c59255742.lua) | 1 |
| [El Shaddoll Apkallone](/examples/cards/50907446) | `50907446` | [Scripts/c50907446.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c50907446.lua) | 1 |
| [Favorite HERO Flame Wingman](/examples/cards/13243124) | `13243124` | [Scripts/c13243124.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c13243124.lua) | 1 |
| [Invoked Sorath](/examples/cards/43989315) | `43989315` | [Scripts/c43989315.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c43989315.lua) | 1 |
| [Lubellion the Searing Dragon](/examples/cards/70534340) | `70534340` | [Scripts/c70534340.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c70534340.lua) | 2 |
| [Albion the Branded Dragon](/examples/cards/87746184) | `87746184` | [Scripts/c87746184.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c87746184.lua) | 2 |
| [Starving Venemy Dragon](/examples/cards/93729065) | `93729065` | [Scripts/c93729065.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c93729065.lua) | 1 |
| El Shaddoll Meshachrer | `32467459` | [Scripts/c32467459.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c32467459.lua) | 3 |
| Starving Venom Fusion Dragon, Four Heavenly Dragons | `27118421` | [Scripts/c27118421.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c27118421.lua) | 3 |
| Chevreuil, Hunting Scout of the Deep Forest | `13023431` | [Scripts/c13023431.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c13023431.lua) | 2 |
| Possessed Destiny - Wynn | `60516416` | [Scripts/c60516416.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c60516416.lua) | 1 |
| Earthbound Servant Geo Gremlina | `33202303` | [Scripts/c33202303.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c33202303.lua) | 1 |
| Starving Venom Fusion Dragon | `41209827` | [Scripts/c41209827.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c41209827.lua) | 1 |
| Egyptian God Slime | `42166000` | [Scripts/c42166000.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c42166000.lua) | 1 |
| Gilti-Gearfried the Magical Steel Knight | `49161188` | [Scripts/c49161188.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c49161188.lua) | 1 |
| Fata Dragna | `41763141` | [Scripts/c41763141.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c41763141.lua) | 1 |
| Invoked Baybarron | `70383419` | [Scripts/c70383419.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c70383419.lua) | 1 |
| Borreload Fatalflare Dragon | `84464389` | [Scripts/c84464389.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c84464389.lua) | 2 |
| Predaplant Chimerafflesia | `25586143` | [Scripts/c25586143.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c25586143.lua) | 1 |
| Fiendsmith's Lacrima | `46640168` | [Scripts/c46640168.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c46640168.lua) | 1 |
| Darklord Eveningstar | `10136446` | [Scripts/c10136446.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c10136446.lua) | 1 |
| Dark Magician of Destruction | `59400890` | [Scripts/c59400890.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c59400890.lua) | 1 |
| Elemental HERO Sunrise | `22908820` | [Scripts/c22908820.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c22908820.lua) | 1 |
| ...and 60 more |  |  |  |

## Script Examples

### Lady's Dragonmaid (`48658295`)

Source: [Scripts/c48658295.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c48658295.lua)

```lua
	if not sg then return true end
	return not sg:IsExists(Card.IsLevel,1,c,c:GetLevel())
		and sg:IsExists(Card.IsFusionAttribute,1,c,c:GetFusionAttribute())
end
function s.splimit(e,se,sp,st)
```

### Goyo Emperor (`59255742`)

Source: [Scripts/c59255742.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c59255742.lua)

```lua
c59255742.material_type=TYPE_SYNCHRO
function c59255742.ffilter(c)
	return c:IsFusionAttribute(ATTRIBUTE_EARTH) and c:IsRace(RACE_WARRIOR) and c:IsFusionType(TYPE_SYNCHRO)
end
function c59255742.spcon(e,tp,eg,ep,ev,re,r,rp)
```

### El Shaddoll Apkallone (`50907446`)

Source: [Scripts/c50907446.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c50907446.lua)

```lua
end
function c50907446.FShaddollFilter1(c,g)
	return c:IsFusionSetCard(0x9d) and g:IsExists(c50907446.FShaddollFilter2,1,c) and not g:IsExists(Card.IsFusionAttribute,1,c,c:GetFusionAttribute())
end
function c50907446.FShaddollFilter2(c)
```
