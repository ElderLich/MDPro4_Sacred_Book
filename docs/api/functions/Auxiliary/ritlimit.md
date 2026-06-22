# Auxiliary.ritlimit

## Signature

```lua
Auxiliary.ritlimit(Effect e, Effect se, int sp, int st) -> bool
```

## Description

Special Summon condition helper that returns true only when the Summon Type contains SUMMON_TYPE_RITUAL.

## Parameters

- `e` `Effect`
- `se` `Effect`
- `sp` `int`
- `st` `int`

## Returns

- `bool`

## Source

- `Utilities/procedure.lua:2293`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **23** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer) with `Auxiliary.ritlimit`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Shinobaroness Peacock | `25415052` | [Scripts/c25415052.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c25415052.lua) | 52 |
| Odd-Eyes Pendulumgraph Dragon | `66425726` | [Scripts/c66425726.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c66425726.lua) | 49 |
| Shinobaron Peacock | `52900000` | [Scripts/c52900000.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c52900000.lua) | 49 |
| Archfiend Emperor | `48469380` | [Scripts/c48469380.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c48469380.lua) | 47 |
| Miracle Raven | `18988396` | [Scripts/c18988396.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c18988396.lua) | 47 |
| Black Luster Soldier - Legendary Swordsman | `70551291` | [Scripts/c70551291.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c70551291.lua) | 47 |
| Nekroz of Metaltron | `13408726` | [Scripts/c13408726.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c13408726.lua) | 44 |
| Archfiend Matriarch | `78744660` | [Scripts/c78744660.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c78744660.lua) | 44 |
| Malacoda, Netherlord of the Burning Abyss | `35330871` | [Scripts/c35330871.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c35330871.lua) | 44 |
| Megalith Notrah Plura | `44293356` | [Scripts/c44293356.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c44293356.lua) | 43 |
| Nekroz of Clausolas | `99185129` | [Scripts/c99185129.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c99185129.lua) | 42 |
| Nekroz of Trishula | `52068432` | [Scripts/c52068432.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c52068432.lua) | 40 |
| Nekroz of Catastor | `52846880` | [Scripts/c52846880.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c52846880.lua) | 39 |
| Nekroz of Valkyrus | `25857246` | [Scripts/c25857246.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c25857246.lua) | 39 |
| Nekroz of Decisive Armor | `88240999` | [Scripts/c88240999.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c88240999.lua) | 39 |
| Nekroz of Areadbhair | `39468724` | [Scripts/c39468724.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c39468724.lua) | 38 |
| Prediction Princess Tarotreith | `42932862` | [Scripts/c42932862.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c42932862.lua) | 38 |
| Nekroz of Brionac | `26674724` | [Scripts/c26674724.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c26674724.lua) | 37 |
| Nekroz of Gungnir | `74122412` | [Scripts/c74122412.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c74122412.lua) | 36 |
| Blue-Eyes Chaos Dragon | `20654247` | [Scripts/c20654247.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c20654247.lua) | 35 |
| Herald of Ultimateness | `48546368` | [Scripts/c48546368.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c48546368.lua) | 35 |
| Nekroz of Unicore | `89463537` | [Scripts/c89463537.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c89463537.lua) | 32 |
| Blue-Eyes Chaos MAX Dragon | `55410871` | [Scripts/c55410871.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c55410871.lua) | 12 |

## Script Examples

### Shinobaroness Peacock (`25415052`)

Source: [Scripts/c25415052.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c25415052.lua)

```lua
	e1:SetCode(EFFECT_SPSUMMON_CONDITION)
	e1:SetProperty(EFFECT_FLAG_CANNOT_DISABLE+EFFECT_FLAG_UNCOPYABLE)
	e1:SetValue(aux.ritlimit)
	c:RegisterEffect(e1)
	--to deck
```

### Odd-Eyes Pendulumgraph Dragon (`66425726`)

Source: [Scripts/c66425726.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c66425726.lua)

```lua
	e0:SetProperty(EFFECT_FLAG_CANNOT_DISABLE+EFFECT_FLAG_UNCOPYABLE)
	e0:SetCode(EFFECT_SPSUMMON_CONDITION)
	e0:SetValue(aux.ritlimit)
	c:RegisterEffect(e0)
	--to hand
```

### Shinobaron Peacock (`52900000`)

Source: [Scripts/c52900000.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c52900000.lua)

```lua
	e1:SetCode(EFFECT_SPSUMMON_CONDITION)
	e1:SetProperty(EFFECT_FLAG_CANNOT_DISABLE+EFFECT_FLAG_UNCOPYABLE)
	e1:SetValue(aux.ritlimit)
	c:RegisterEffect(e1)
	--tohand
```
