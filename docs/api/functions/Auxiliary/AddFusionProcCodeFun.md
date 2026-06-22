# Auxiliary.AddFusionProcCodeFun

## Signature

```lua
Auxiliary.AddFusionProcCodeFun(Card c, int|table code1, function|table f, int cc, bool sub, bool insf) -> void
```

## Description

Registers a Fusion Summon procedure on c requiring code1 and cc additional Fusion Materials matching f.
The helper builds cc copies of f and forwards them to Auxiliary.AddFusionProcMix together with sub and insf.

## Parameters

- `c` `Card`
- `code1` `int|table`
- `f` `function|table`
- `cc` `int`
- `sub` `bool`
- `insf` `bool`

## Source

- `Utilities/procedure.lua:1263`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **80** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer) with `Auxiliary.AddFusionProcCodeFun`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Lubellion the Searing Dragon](/examples/cards/70534340) | `70534340` | [Scripts/c70534340.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c70534340.lua) | 65 |
| [Albion the Branded Dragon](/examples/cards/87746184) | `87746184` | [Scripts/c87746184.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c87746184.lua) | 62 |
| Red-Eyes Slash Dragon | `21140872` | [Scripts/c21140872.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c21140872.lua) | 60 |
| Alba System Dogmatikalamity | `93053159` | [Scripts/c93053159.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c93053159.lua) | 58 |
| Windwitch - Crystal Bell | `25793414` | [Scripts/c25793414.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c25793414.lua) | 57 |
| Gladiator Beast Gaiodiaz | `90957527` | [Scripts/c90957527.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c90957527.lua) | 54 |
| Millennium-Eyes Restrict | `41578483` | [Scripts/c41578483.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c41578483.lua) | 53 |
| Shura the Combat Star | `32615065` | [Scripts/c32615065.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c32615065.lua) | 52 |
| Gladiator Beast Gyzarus | `48156348` | [Scripts/c48156348.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c48156348.lua) | 51 |
| Red-Eyes Dark Dragoon | `37818794` | [Scripts/c37818794.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c37818794.lua) | 50 |
| Mirrorjade the Iceblade Dragon | `44146295` | [Scripts/c44146295.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c44146295.lua) | 49 |
| Invoked Magistus Omega | `38423248` | [Scripts/c38423248.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c38423248.lua) | 49 |
| Evil HERO Inferno Wing - Backfire | `59893882` | [Scripts/c59893882.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c59893882.lua) | 49 |
| Blue-Eyes Tyrant Dragon | `11443677` | [Scripts/c11443677.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c11443677.lua) | 49 |
| Dark Magician of Destruction | `59400890` | [Scripts/c59400890.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c59400890.lua) | 48 |
| Sprind the Irondash Dragon | `1906812` | [Scripts/c1906812.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c1906812.lua) | 48 |
| Master of Chaos | `85059922` | [Scripts/c85059922.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c85059922.lua) | 48 |
| Titaniklad the Ash Dragon | `41373230` | [Scripts/c41373230.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c41373230.lua) | 47 |
| Fallen Angel of the Golden Land | `43143567` | [Scripts/c43143567.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c43143567.lua) | 47 |
| Rindbrumm the Striking Dragon | `51409648` | [Scripts/c51409648.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c51409648.lua) | 47 |
| Armed Neos | `31817415` | [Scripts/c31817415.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c31817415.lua) | 47 |
| Fiendsmith's Desirae | `82135803` | [Scripts/c82135803.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c82135803.lua) | 47 |
| Albion the Sanctifire Dragon | `38811586` | [Scripts/c38811586.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c38811586.lua) | 46 |
| Artmage Diactorus | `27184601` | [Scripts/c27184601.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c27184601.lua) | 46 |
| ...and 56 more |  |  |  |

## Script Examples

### Lubellion the Searing Dragon (`70534340`)

Source: [Scripts/c70534340.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c70534340.lua)

```lua
	--fusion material
	c:EnableReviveLimit()
	aux.AddFusionProcCodeFun(c,68468459,aux.FilterBoolFunction(Card.IsFusionAttribute,ATTRIBUTE_DARK),1,true,true)
	--spsummon
	local e1=Effect.CreateEffect(c)
```

### Albion the Branded Dragon (`87746184`)

Source: [Scripts/c87746184.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c87746184.lua)

```lua
	--fusion material
	c:EnableReviveLimit()
	aux.AddFusionProcCodeFun(c,68468459,aux.FilterBoolFunction(Card.IsFusionAttribute,ATTRIBUTE_LIGHT),1,true,true)
	--fusion summon
	local e1=Effect.CreateEffect(c)
```

### Red-Eyes Slash Dragon (`21140872`)

Source: [Scripts/c21140872.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c21140872.lua)

```lua
	--fusion material
	c:EnableReviveLimit()
	aux.AddFusionProcCodeFun(c,74677422,aux.FilterBoolFunction(Card.IsRace,RACE_WARRIOR),1,true,true)
	--equip
	local e1=Effect.CreateEffect(c)
```
