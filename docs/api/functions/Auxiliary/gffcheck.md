# Auxiliary.gffcheck

## Signature

```lua
Auxiliary.gffcheck(Group g, function f1, any a1, function f2, any a2) -> bool
```

## Description

Checks a 2-card group against two filters in either order: one card must satisfy f1(c,a1) and the other f2(c,a2).

## Parameters

- `g` `Group`
- `f1` `function`
- `a1` `any`
- `f2` `function`
- `a2` `any`

## Returns

- `bool` - true if the two cards satisfy both filters in either order.

## Source

- `Utilities/utility.lua:1160`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **37** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=standard&mode=code&q=Auxiliary.gffcheck) with `Auxiliary.gffcheck`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Lubellion the Searing Dragon](/examples/cards/70534340) | `70534340` | [Scripts/c70534340.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c70534340.lua) | 1 |
| [Albion the Branded Dragon](/examples/cards/87746184) | `87746184` | [Scripts/c87746184.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c87746184.lua) | 1 |
| Red-Eyes Slash Dragon | `21140872` | [Scripts/c21140872.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c21140872.lua) | 1 |
| Dragon Master Magia | `12381100` | [Scripts/c12381100.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c12381100.lua) | 2 |
| Windwitch - Crystal Bell | `25793414` | [Scripts/c25793414.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c25793414.lua) | 1 |
| Red-Eyes Black Dragon Exceed | `17242022` | [Scripts/c17242022.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c17242022.lua) | 1 |
| Black-Winged Assault Dragon | `73218989` | [Scripts/c73218989.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c73218989.lua) | 1 |
| Thunder Dragon Titan | `41685633` | [Scripts/c41685633.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c41685633.lua) | 1 |
| Synchro Fellowship | `43834302` | [Scripts/c43834302.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c43834302.lua) | 3 |
| Blackwing - Aurora the Northern Lights | `4068622` | [Scripts/c4068622.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c4068622.lua) | 1 |
| Phantasmal Lord Ultimitl Bishbaalkin | `90884403` | [Scripts/c90884403.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c90884403.lua) | 1 |
| Ultimaya Tzolkin | `1686814` | [Scripts/c1686814.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c1686814.lua) | 1 |
| Mirrorjade the Iceblade Dragon | `44146295` | [Scripts/c44146295.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c44146295.lua) | 2 |
| Blue-Eyes Tyrant Dragon | `11443677` | [Scripts/c11443677.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c11443677.lua) | 1 |
| Awakening of the Possessed - Nefariouser Archfiend | `65268179` | [Scripts/c65268179.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c65268179.lua) | 1 |
| Sprind the Irondash Dragon | `1906812` | [Scripts/c1906812.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c1906812.lua) | 1 |
| Titaniklad the Ash Dragon | `41373230` | [Scripts/c41373230.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c41373230.lua) | 1 |
| Awakening of the Possessed - Gagigobyte | `74426895` | [Scripts/c74426895.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c74426895.lua) | 1 |
| Dragunity Whirlwind | `89450409` | [Scripts/c89450409.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c89450409.lua) | 2 |
| Albion the Sanctifire Dragon | `38811586` | [Scripts/c38811586.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c38811586.lua) | 1 |
| D/D/D Sky King Zeus Ragnarok | `30998403` | [Scripts/c30998403.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c30998403.lua) | 2 |
| Awakening of the Possessed - Greater Inari Fire | `92652813` | [Scripts/c92652813.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c92652813.lua) | 1 |
| Blackwing - Twin Shadow | `69973414` | [Scripts/c69973414.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c69973414.lua) | 1 |
| Awakening of the Possessed - Rasenryu | `410904` | [Scripts/c410904.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c410904.lua) | 1 |
| ...and 13 more |  |  |  |

## Script Examples

### Lubellion the Searing Dragon (`70534340`)

Source: [Scripts/c70534340.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c70534340.lua)

```lua
end
function c70534340.branded_fusion_check(tp,sg,fc)
	return aux.gffcheck(sg,Card.IsFusionCode,68468459,Card.IsFusionAttribute,ATTRIBUTE_DARK)
end
function c70534340.spcon(e,tp,eg,ep,ev,re,r,rp)
```

### Albion the Branded Dragon (`87746184`)

Source: [Scripts/c87746184.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c87746184.lua)

```lua
end
function c87746184.branded_fusion_check(tp,sg,fc)
	return aux.gffcheck(sg,Card.IsFusionCode,68468459,Card.IsFusionAttribute,ATTRIBUTE_LIGHT)
end
function c87746184.condition(e,tp,eg,ep,ev,re,r,rp)
```

### Red-Eyes Slash Dragon (`21140872`)

Source: [Scripts/c21140872.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c21140872.lua)

```lua
c21140872.material_setcode=0x3b
function c21140872.red_eyes_fusion_check(tp,sg,fc)
	return aux.gffcheck(sg,Card.IsFusionCode,74677422,Card.IsRace,RACE_WARRIOR)
end
function c21140872.eqcon(e)
```
