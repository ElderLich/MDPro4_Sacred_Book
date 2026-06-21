# Auxiliary.Tuner

## Signature

```lua
Auxiliary.Tuner(function f, ... any) -> void
```

## Description

Filter Tuner monsters satisfying a single filter condition f, returning a function with a bool return type; if only Tuner monsters are required, use aux.Tuner(nil)
Additional parameters start from the second parameter

## Parameters

- `f` `function`
- `...` `any`

## Source

- `Utilities/procedure.lua:42`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **24** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer) with `Auxiliary.Tuner`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Shooting Majestic Star Dragon](/examples/cards/40939228) | `40939228` | [Scripts/c40939228.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c40939228.lua) | 62 |
| Red Nova Dragon - Burning Soul | `65541655` | [Scripts/c65541655.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c65541655.lua) | 57 |
| Kewl Tune Crackle | `39576656` | [Scripts/c39576656.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c39576656.lua) | 56 |
| Kewl Tune Remix | `88170262` | [Scripts/c88170262.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c88170262.lua) | 54 |
| Kewl Tune B2B | `65961304` | [Scripts/c65961304.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c65961304.lua) | 52 |
| X-Saber Gottoms | `8252010` | [Scripts/c8252010.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c8252010.lua) | 52 |
| Commander Souza, Swordmaster | `72867001` | [Scripts/c72867001.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c72867001.lua) | 51 |
| Red Supernova Dragon | `99585850` | [Scripts/c99585850.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c99585850.lua) | 48 |
| Kewl Tune RS | `15665977` | [Scripts/c15665977.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c15665977.lua) | 48 |
| Crystal Clear Wing Over Synchro Dragon | `84343351` | [Scripts/c84343351.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c84343351.lua) | 47 |
| Mannadium Prime-Heart | `90465153` | [Scripts/c90465153.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c90465153.lua) | 47 |
| Blue-Eyes Ultimate Spirit Dragon | `89604813` | [Scripts/c89604813.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c89604813.lua) | 44 |
| Vylon Omega | `93157004` | [Scripts/c93157004.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c93157004.lua) | 44 |
| Ghoti of the Deep Beyond | `72309040` | [Scripts/c72309040.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c72309040.lua) | 44 |
| Hot Red Dragon Archfiend King Calamity | `62242678` | [Scripts/c62242678.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c62242678.lua) | 43 |
| Judgment, the Dragon of Heaven | `41659072` | [Scripts/c41659072.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c41659072.lua) | 43 |
| Visas Amritara | `821049` | [Scripts/c821049.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c821049.lua) | 39 |
| Tyrant Red Dragon Archfiend | `16172067` | [Scripts/c16172067.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c16172067.lua) | 38 |
| Kewl Tune Loudness War | `41069676` | [Scripts/c41069676.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c41069676.lua) | 38 |
| Crystron Quariongandrax | `13455674` | [Scripts/c13455674.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c13455674.lua) | 38 |
| Zalen the Shackled Dragon | `4891376` | [Scripts/c4891376.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c4891376.lua) | 34 |
| Red Nova Dragon | `97489701` | [Scripts/c97489701.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c97489701.lua) | 32 |
| XX-Saber Gottoms | `52352005` | [Scripts/c52352005.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c52352005.lua) | 31 |
| Kewl Tune Track Maker | `42781164` | [Scripts/c42781164.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c42781164.lua) | 29 |

## Script Examples

### Shooting Majestic Star Dragon (`40939228`)

Source: [Scripts/c40939228.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c40939228.lua)

```lua
	aux.AddCodeList(c,44508094)
	--synchro summon
	aux.AddSynchroMixProcedure(c,aux.Tuner(Card.IsCode,21159309),nil,nil,aux.NonTuner(nil),1,99,c40939228.syncheck)
	c:EnableReviveLimit()
	--special summon condition
```

### Red Nova Dragon - Burning Soul (`65541655`)

Source: [Scripts/c65541655.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c65541655.lua)

```lua
	aux.AddCodeList(c,70902743)
	--synchro summon
	aux.AddSynchroMixProcedure(c,aux.Tuner(nil),aux.Tuner(nil),nil,aux.NonTuner(nil),1,1)
	c:EnableReviveLimit()
	--cannot special summon
```

### Kewl Tune Crackle (`39576656`)

Source: [Scripts/c39576656.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c39576656.lua)

```lua
	aux.AddMaterialCodeList(c,43904702)
	--synchro summon
	aux.AddSynchroMixProcedure(c,aux.FilterBoolFunction(Card.IsCode,43904702),nil,nil,aux.Tuner(nil),1,99)
	c:EnableReviveLimit()
	--remove extra
```
