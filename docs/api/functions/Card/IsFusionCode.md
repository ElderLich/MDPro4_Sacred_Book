# Card.IsFusionCode

## Signature

```lua
Card.IsFusionCode(Card c, int code, [... int]) -> bool
```

## Description

Check the c as a fusion material can be used as the card number for the code card

## Parameters

- `c` `Card`
- `code` `int`
- `...` `int` optional

## Returns

- `bool`

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3391`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **46** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer) with `Card.IsFusionCode`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Lubellion the Searing Dragon](/examples/cards/70534340) | `70534340` | [Scripts/c70534340.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c70534340.lua) | 65 |
| [Future Fusion Nova](/examples/cards/92058902) | `92058902` | [Scripts/c92058902.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c92058902.lua) | 63 |
| [Albion the Branded Dragon](/examples/cards/87746184) | `87746184` | [Scripts/c87746184.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c87746184.lua) | 62 |
| [Ashened to Endlessness](/examples/cards/34813443) | `34813443` | [Scripts/c34813443.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c34813443.lua) | 62 |
| Red-Eyes Slash Dragon | `21140872` | [Scripts/c21140872.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c21140872.lua) | 60 |
| Secrets of Dark Magic | `59514116` | [Scripts/c59514116.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c59514116.lua) | 59 |
| Alba System Dogmatikalamity | `93053159` | [Scripts/c93053159.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c93053159.lua) | 58 |
| Dragon Master Magia | `12381100` | [Scripts/c12381100.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c12381100.lua) | 57 |
| Windwitch - Crystal Bell | `25793414` | [Scripts/c25793414.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c25793414.lua) | 57 |
| Ultimate Fusion | `71143015` | [Scripts/c71143015.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c71143015.lua) | 56 |
| Gladiator Beast Gaiodiaz | `90957527` | [Scripts/c90957527.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c90957527.lua) | 54 |
| Thunder Dragon Titan | `41685633` | [Scripts/c41685633.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c41685633.lua) | 52 |
| Branded Fusion | `44362883` | [Scripts/c44362883.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c44362883.lua) | 52 |
| Gladiator Beast Gyzarus | `48156348` | [Scripts/c48156348.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c48156348.lua) | 51 |
| Red-Eyes Dark Dragoon | `37818794` | [Scripts/c37818794.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c37818794.lua) | 50 |
| Guardian Chimera | `11321089` | [Scripts/c11321089.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c11321089.lua) | 49 |
| Mirrorjade the Iceblade Dragon | `44146295` | [Scripts/c44146295.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c44146295.lua) | 49 |
| Arcana Force EX - The Chaos Ruler | `12686296` | [Scripts/c12686296.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c12686296.lua) | 49 |
| Dinomorphia Kentregina | `48832775` | [Scripts/c48832775.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c48832775.lua) | 49 |
| Blue-Eyes Tyrant Dragon | `11443677` | [Scripts/c11443677.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c11443677.lua) | 49 |
| Destruction Swordsman Fusion | `41940225` | [Scripts/c41940225.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c41940225.lua) | 49 |
| Sprind the Irondash Dragon | `1906812` | [Scripts/c1906812.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c1906812.lua) | 48 |
| Titaniklad the Ash Dragon | `41373230` | [Scripts/c41373230.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c41373230.lua) | 47 |
| Albion the Sanctifire Dragon | `38811586` | [Scripts/c38811586.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c38811586.lua) | 46 |
| ...and 22 more |  |  |  |

## Script Examples

### Lubellion the Searing Dragon (`70534340`)

Source: [Scripts/c70534340.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c70534340.lua)

```lua
end
function c70534340.branded_fusion_check(tp,sg,fc)
	return aux.gffcheck(sg,Card.IsFusionCode,68468459,Card.IsFusionAttribute,ATTRIBUTE_DARK)
end
function c70534340.spcon(e,tp,eg,ep,ev,re,r,rp)
```

### Future Fusion Nova (`92058902`)

Source: [Scripts/c92058902.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c92058902.lua)

```lua
end
function s.fcheck(tp,sg,fc)
	return sg:IsExists(Card.IsFusionCode,1,nil,70095154)
end
function s.target(e,tp,eg,ep,ev,re,r,rp,chk)
```

### Albion the Branded Dragon (`87746184`)

Source: [Scripts/c87746184.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c87746184.lua)

```lua
end
function c87746184.branded_fusion_check(tp,sg,fc)
	return aux.gffcheck(sg,Card.IsFusionCode,68468459,Card.IsFusionAttribute,ATTRIBUTE_LIGHT)
end
function c87746184.condition(e,tp,eg,ep,ev,re,r,rp)
```
