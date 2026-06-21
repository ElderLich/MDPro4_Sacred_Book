# Auxiliary.AddMaterialCodeList

## Signature

```lua
Auxiliary.AddMaterialCodeList(Card c, ... any) -> void
```

## Description

Registers one or more material card codes for c and also adds each code to c's listed-code table.
Fusion Monsters normally do not need this helper.

## Parameters

- `c` `Card`
- `...` `any`

## Source

- `Utilities/utility.lua:498`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **47** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer) with `Auxiliary.AddMaterialCodeList`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Enlightenment Dragon](/examples/cards/46186135) | `46186135` | [Scripts/c46186135.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c46186135.lua) | 62 |
| [Shooting Majestic Star Dragon](/examples/cards/40939228) | `40939228` | [Scripts/c40939228.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c40939228.lua) | 62 |
| Alba System Dogmatikalamity | `93053159` | [Scripts/c93053159.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c93053159.lua) | 58 |
| Dragon Master Magia | `12381100` | [Scripts/c12381100.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c12381100.lua) | 57 |
| Kewl Tune Crackle | `39576656` | [Scripts/c39576656.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c39576656.lua) | 56 |
| Genex Ally Triarm | `17760003` | [Scripts/c17760003.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c17760003.lua) | 55 |
| Kewl Tune Remix | `88170262` | [Scripts/c88170262.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c88170262.lua) | 54 |
| Junk Warrior Extreme | `16327715` | [Scripts/c16327715.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c16327715.lua) | 52 |
| Majestic Star Dragon | `7841112` | [Scripts/c7841112.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c7841112.lua) | 49 |
| Evil HERO Inferno Wing - Backfire | `59893882` | [Scripts/c59893882.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c59893882.lua) | 49 |
| Kewl Tune RS | `15665977` | [Scripts/c15665977.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c15665977.lua) | 48 |
| Crystal Clear Wing Over Synchro Dragon | `84343351` | [Scripts/c84343351.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c84343351.lua) | 47 |
| Deep Sea Repetiteur | `33467872` | [Scripts/c33467872.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c33467872.lua) | 47 |
| Shooting Star Dragon | `24696097` | [Scripts/c24696097.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c24696097.lua) | 45 |
| Cosmic Fortress Gol'gar | `68319538` | [Scripts/c68319538.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c68319538.lua) | 45 |
| Drill Warrior | `3429238` | [Scripts/c3429238.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c3429238.lua) | 45 |
| Junk Berserker | `59771339` | [Scripts/c59771339.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c59771339.lua) | 45 |
| Nitro Warrior | `18013090` | [Scripts/c18013090.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c18013090.lua) | 44 |
| Majestic Red Dragon | `67030233` | [Scripts/c67030233.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c67030233.lua) | 43 |
| Night's End Administrator | `3779493` | [Scripts/c3779493.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c3779493.lua) | 42 |
| The Dragon that Devours the Dogma | `76666602` | [Scripts/c76666602.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c76666602.lua) | 40 |
| Union Controller | `2133971` | [Scripts/c2133971.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c2133971.lua) | 39 |
| Cyber Dragon Sieger | `46724542` | [Scripts/c46724542.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c46724542.lua) | 39 |
| Sun Dragon Inti | `39823987` | [Scripts/c39823987.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c39823987.lua) | 39 |
| ...and 23 more |  |  |  |

## Script Examples

### Enlightenment Dragon (`46186135`)

Source: [Scripts/c46186135.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c46186135.lua)

```lua
	--fusion material
	c:EnableReviveLimit()
	aux.AddMaterialCodeList(c,19959563,57774843)
	--cannot special summon
	local e1=Effect.CreateEffect(c)
```

### Shooting Majestic Star Dragon (`40939228`)

Source: [Scripts/c40939228.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c40939228.lua)

```lua
local s,id,o=GetID()
function c40939228.initial_effect(c)
	aux.AddMaterialCodeList(c,21159309)
	aux.AddCodeList(c,44508094)
	--synchro summon
```

### Alba System Dogmatikalamity (`93053159`)

Source: [Scripts/c93053159.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c93053159.lua)

```lua
function s.initial_effect(c)
	aux.AddCodeList(c,68468459)
	aux.AddMaterialCodeList(c,68468459)
	--aux.AddFusionProcCodeFun(c,68468459,s.mfilter,6,true,true)
	c:EnableReviveLimit()
```
