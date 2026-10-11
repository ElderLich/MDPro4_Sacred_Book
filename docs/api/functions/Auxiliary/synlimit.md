# Auxiliary.synlimit

## Signature

```lua
Auxiliary.synlimit(Effect e, Effect se, int sp, int st) -> bool
```

## Description

Special Summon condition helper that returns true only when st contains SUMMON_TYPE_SYNCHRO.

## Parameters

- `e` `Effect`
- `se` `Effect`
- `sp` `int`
- `st` `int`

## Returns

- `bool`

## Source

- `Utilities/procedure.lua:2297`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **15** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=standard&mode=code&q=Auxiliary.synlimit) with `Auxiliary.synlimit`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Shooting Majestic Star Dragon](/examples/cards/40939228) | `40939228` | [Scripts/c40939228.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c40939228.lua) | 1 |
| Red Nova Dragon - Burning Soul | `65541655` | [Scripts/c65541655.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c65541655.lua) | 1 |
| Black-Winged Assault Dragon | `73218989` | [Scripts/c73218989.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c73218989.lua) | 1 |
| Red Supernova Dragon | `99585850` | [Scripts/c99585850.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c99585850.lua) | 1 |
| Crystal Clear Wing Over Synchro Dragon | `84343351` | [Scripts/c84343351.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c84343351.lua) | 1 |
| Stardust Sifr Divine Dragon | `26268488` | [Scripts/c26268488.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c26268488.lua) | 1 |
| T.G. Glaive Blaster | `95973569` | [Scripts/c95973569.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c95973569.lua) | 1 |
| Cosmic Blazar Dragon | `21123811` | [Scripts/c21123811.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c21123811.lua) | 1 |
| Stardust Chronicle Spark Dragon | `89474727` | [Scripts/c89474727.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c89474727.lua) | 1 |
| T.G. Halberd Cannon | `97836203` | [Scripts/c97836203.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c97836203.lua) | 1 |
| Tyrant Red Dragon Archfiend | `16172067` | [Scripts/c16172067.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c16172067.lua) | 1 |
| Shooting Quasar Dragon | `35952884` | [Scripts/c35952884.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c35952884.lua) | 1 |
| Trident Dragion | `39402797` | [Scripts/c39402797.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c39402797.lua) | 1 |
| Blackwing - Gram the Shining Star | `17377751` | [Scripts/c17377751.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c17377751.lua) | 1 |
| Star Eater | `41517789` | [Scripts/c41517789.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c41517789.lua) | 1 |

## Script Examples

### Shooting Majestic Star Dragon (`40939228`)

Source: [Scripts/c40939228.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c40939228.lua)

```lua
	e1:SetCode(EFFECT_SPSUMMON_CONDITION)
	e1:SetRange(LOCATION_EXTRA)
	e1:SetValue(aux.synlimit)
	c:RegisterEffect(e1)
	--disable
```

### Red Nova Dragon - Burning Soul (`65541655`)

Source: [Scripts/c65541655.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c65541655.lua)

```lua
	e1:SetProperty(EFFECT_FLAG_CANNOT_DISABLE+EFFECT_FLAG_UNCOPYABLE)
	e1:SetCode(EFFECT_SPSUMMON_CONDITION)
	e1:SetValue(aux.synlimit)
	c:RegisterEffect(e1)
	--special summon
```

### Black-Winged Assault Dragon (`73218989`)

Source: [Scripts/c73218989.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c73218989.lua)

```lua
	e1:SetProperty(EFFECT_FLAG_CANNOT_DISABLE+EFFECT_FLAG_UNCOPYABLE)
	e1:SetCode(EFFECT_SPSUMMON_CONDITION)
	e1:SetValue(aux.synlimit)
	c:RegisterEffect(e1)
	--spsummon
```
