# Card.IsFusionCode

## Signature

```lua
Card.IsFusionCode(Card c, int code1, [int code2], [... int]) -> bool
```

## Description

Checks whether c can be treated as any supplied code while used as Fusion Material.
The core includes c's current code, second code, and EFFECT_ADD_FUSION_CODE values. If no Fusion-only code additions apply, or material-code checks are disabled, it falls back to Card.IsCode.

## Parameters

- `c` `Card`
- `code1` `int`
- `code2` `int` optional
- `...` `int` optional

## Returns

- `bool`

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3441`

## Guided Examples

Learn how to use this function in context:

- [Fusion Procedure Guide](/learn/fusion-procedure)

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **49** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=standard&mode=code&q=Card.IsFusionCode) with `Card.IsFusionCode`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Lubellion the Searing Dragon](/examples/cards/70534340) | `70534340` | [Scripts/c70534340.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c70534340.lua) | 1 |
| [Future Fusion Nova](/examples/cards/92058902) | `92058902` | [Scripts/c92058902.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c92058902.lua) | 1 |
| [Albion the Branded Dragon](/examples/cards/87746184) | `87746184` | [Scripts/c87746184.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c87746184.lua) | 1 |
| [Ashened to Endlessness](/examples/cards/34813443) | `34813443` | [Scripts/c34813443.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c34813443.lua) | 1 |
| Red-Eyes Slash Dragon | `21140872` | [Scripts/c21140872.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c21140872.lua) | 1 |
| Secrets of Dark Magic | `59514116` | [Scripts/c59514116.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c59514116.lua) | 1 |
| Alba System Dogmatikalamity | `93053159` | [Scripts/c93053159.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c93053159.lua) | 1 |
| Dragon Master Magia | `12381100` | [Scripts/c12381100.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c12381100.lua) | 2 |
| Windwitch - Crystal Bell | `25793414` | [Scripts/c25793414.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c25793414.lua) | 1 |
| Ultimate Fusion | `71143015` | [Scripts/c71143015.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c71143015.lua) | 3 |
| Gladiator Beast Gaiodiaz | `90957527` | [Scripts/c90957527.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c90957527.lua) | 1 |
| Red-Eyes Black Dragon Exceed | `17242022` | [Scripts/c17242022.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c17242022.lua) | 1 |
| Thunder Dragon Titan | `41685633` | [Scripts/c41685633.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c41685633.lua) | 1 |
| Branded Fusion | `44362883` | [Scripts/c44362883.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c44362883.lua) | 1 |
| Gladiator Beast Gyzarus | `48156348` | [Scripts/c48156348.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c48156348.lua) | 1 |
| Red-Eyes Dark Dragoon | `37818794` | [Scripts/c37818794.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c37818794.lua) | 1 |
| Destiny HERO - Dreadnought Master | `54641720` | [Scripts/c54641720.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c54641720.lua) | 1 |
| Blue-Eyes Toon Ultimate Dragon | `71808988` | [Scripts/c71808988.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c71808988.lua) | 2 |
| Guardian Chimera | `11321089` | [Scripts/c11321089.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c11321089.lua) | 1 |
| Mirrorjade the Iceblade Dragon | `44146295` | [Scripts/c44146295.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c44146295.lua) | 2 |
| Arcana Force EX - The Chaos Ruler | `12686296` | [Scripts/c12686296.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c12686296.lua) | 1 |
| Dinomorphia Kentregina | `48832775` | [Scripts/c48832775.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c48832775.lua) | 1 |
| Blue-Eyes Tyrant Dragon | `11443677` | [Scripts/c11443677.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c11443677.lua) | 2 |
| Destruction Swordsman Fusion | `41940225` | [Scripts/c41940225.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c41940225.lua) | 1 |
| ...and 25 more |  |  |  |

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

### Future Fusion Nova (`92058902`)

Source: [Scripts/c92058902.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c92058902.lua)

```lua
end
function s.fcheck(tp,sg,fc)
	return sg:IsExists(Card.IsFusionCode,1,nil,70095154)
end
function s.target(e,tp,eg,ep,ev,re,r,rp,chk)
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
