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

- Detected in **48** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=standard&mode=code&q=Auxiliary.AddMaterialCodeList) with `Auxiliary.AddMaterialCodeList`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Enlightenment Dragon](/examples/cards/46186135) | `46186135` | [Scripts/c46186135.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c46186135.lua) | 1 |
| [Shooting Majestic Star Dragon](/examples/cards/40939228) | `40939228` | [Scripts/c40939228.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c40939228.lua) | 1 |
| [Kewl Tune Crackle](/examples/cards/39576656) | `39576656` | [Scripts/c39576656.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c39576656.lua) | 1 |
| Alba System Dogmatikalamity | `93053159` | [Scripts/c93053159.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c93053159.lua) | 1 |
| Dragon Master Magia | `12381100` | [Scripts/c12381100.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c12381100.lua) | 1 |
| Genex Ally Triarm | `17760003` | [Scripts/c17760003.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c17760003.lua) | 1 |
| Kewl Tune Remix | `88170262` | [Scripts/c88170262.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c88170262.lua) | 1 |
| Junk Warrior Extreme | `16327715` | [Scripts/c16327715.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c16327715.lua) | 1 |
| Blue-Eyes Toon Ultimate Dragon | `71808988` | [Scripts/c71808988.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c71808988.lua) | 1 |
| Majestic Star Dragon | `7841112` | [Scripts/c7841112.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c7841112.lua) | 1 |
| Evil HERO Inferno Wing - Backfire | `59893882` | [Scripts/c59893882.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c59893882.lua) | 1 |
| Kewl Tune RS | `15665977` | [Scripts/c15665977.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c15665977.lua) | 1 |
| Crystal Clear Wing Over Synchro Dragon | `84343351` | [Scripts/c84343351.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c84343351.lua) | 1 |
| Deep Sea Repetiteur | `33467872` | [Scripts/c33467872.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c33467872.lua) | 1 |
| Shooting Star Dragon | `24696097` | [Scripts/c24696097.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c24696097.lua) | 1 |
| Cosmic Fortress Gol'gar | `68319538` | [Scripts/c68319538.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c68319538.lua) | 1 |
| Drill Warrior | `3429238` | [Scripts/c3429238.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c3429238.lua) | 1 |
| Junk Berserker | `59771339` | [Scripts/c59771339.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c59771339.lua) | 1 |
| Nitro Warrior | `18013090` | [Scripts/c18013090.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c18013090.lua) | 1 |
| Majestic Red Dragon | `67030233` | [Scripts/c67030233.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c67030233.lua) | 1 |
| Night's End Administrator | `3779493` | [Scripts/c3779493.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c3779493.lua) | 1 |
| The Dragon that Devours the Dogma | `76666602` | [Scripts/c76666602.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c76666602.lua) | 1 |
| Union Controller | `2133971` | [Scripts/c2133971.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c2133971.lua) | 1 |
| Cyber Dragon Sieger | `46724542` | [Scripts/c46724542.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c46724542.lua) | 1 |
| ...and 24 more |  |  |  |

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

### Kewl Tune Crackle (`39576656`)

Source: [Scripts/c39576656.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c39576656.lua)

```lua
local s,id,o=GetID()
function s.initial_effect(c)
	aux.AddMaterialCodeList(c,43904702)
	--synchro summon
	aux.AddSynchroMixProcedure(c,aux.FilterBoolFunction(Card.IsCode,43904702),nil,nil,aux.Tuner(nil),1,99)
```
