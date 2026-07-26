# Card.IsSynchroType

## Signature

```lua
Card.IsSynchroType(Card c, int type) -> bool
```

## Description

Checks whether c's type while used as Synchro Material contains type.

## Parameters

- `c` `Card`
- `type` `int`

## Returns

- `bool`

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3487`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **37** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer) with `Card.IsSynchroType`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Shooting Majestic Star Dragon](/examples/cards/40939228) | `40939228` | [Scripts/c40939228.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c40939228.lua) | 62 |
| Red Hypernova Dragon | `30698243` | [Scripts/c30698243.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c30698243.lua) | 53 |
| Kewl Tune B2B | `65961304` | [Scripts/c65961304.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c65961304.lua) | 52 |
| Pendulum Dimension | `84274024` | [Scripts/c84274024.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c84274024.lua) | 50 |
| Stardust Warrior | `74892653` | [Scripts/c74892653.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c74892653.lua) | 50 |
| Ruddy Rose Dragon | `40139997` | [Scripts/c40139997.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c40139997.lua) | 50 |
| Oracle of Zefra | `32354768` | [Scripts/c32354768.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c32354768.lua) | 49 |
| Shooting Star Dragon T.G. EX | `63180841` | [Scripts/c63180841.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c63180841.lua) | 49 |
| Dragunity Knight - Areus | `34528176` | [Scripts/c34528176.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c34528176.lua) | 49 |
| Red Supernova Dragon | `99585850` | [Scripts/c99585850.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c99585850.lua) | 48 |
| Crystal Clear Wing Synchro Dragon | `59765225` | [Scripts/c59765225.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c59765225.lua) | 47 |
| Stardust Sifr Divine Dragon | `26268488` | [Scripts/c26268488.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c26268488.lua) | 47 |
| Kewl Tune Rotary | `17209452` | [Scripts/c17209452.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c17209452.lua) | 46 |
| Battlewasp - Hama the Conquering Bow | `80949182` | [Scripts/c80949182.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c80949182.lua) | 46 |
| Shooting Star Dragon | `24696097` | [Scripts/c24696097.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c24696097.lua) | 45 |
| Cosmic Quasar Dragon | `37442336` | [Scripts/c37442336.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c37442336.lua) | 45 |
| Satellite Warrior | `84664085` | [Scripts/c84664085.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c84664085.lua) | 45 |
| Metaphys Horus | `36898537` | [Scripts/c36898537.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c36898537.lua) | 44 |
| Kewl Tune Cue | `16387555` | [Scripts/c16387555.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c16387555.lua) | 43 |
| Hot Red Dragon Archfiend King Calamity | `62242678` | [Scripts/c62242678.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c62242678.lua) | 43 |
| Cosmic Blazar Dragon | `21123811` | [Scripts/c21123811.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c21123811.lua) | 43 |
| Stardust Chronicle Spark Dragon | `89474727` | [Scripts/c89474727.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c89474727.lua) | 43 |
| T.G. Blade Blaster | `51447164` | [Scripts/c51447164.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c51447164.lua) | 41 |
| Ignister Prominence, the Blasting Dracoslayer | `18239909` | [Scripts/c18239909.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c18239909.lua) | 41 |
| ...and 13 more |  |  |  |

## Script Examples

### Shooting Majestic Star Dragon (`40939228`)

Source: [Scripts/c40939228.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c40939228.lua)

```lua
c40939228.material_type=TYPE_SYNCHRO
function c40939228.cfilter(c,syncard)
	return c:IsRace(RACE_DRAGON) and c:IsSynchroType(TYPE_SYNCHRO) and c:IsNotTuner(syncard)
end
function c40939228.syncheck(g,syncard)
```

### Red Hypernova Dragon (`30698243`)

Source: [Scripts/c30698243.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c30698243.lua)

```lua
	aux.AddCodeList(c,97489701)
	--material
	aux.AddSynchroMixProcedure(c,aux.NonTuner(Card.IsSynchroType,TYPE_SYNCHRO),nil,nil,s.mfilter,4,99,s.syncheck)
	c:EnableReviveLimit()
	--cannot special summon
```

### Kewl Tune B2B (`65961304`)

Source: [Scripts/c65961304.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c65961304.lua)

```lua
	--Synchro Summon
	c:EnableReviveLimit()
	aux.AddSynchroMixProcedure(c,aux.Tuner(nil),nil,nil,aux.FilterBoolFunction(Card.IsSynchroType,TYPE_SYNCHRO),1,99)
	local e0=Effect.CreateEffect(c)
	e0:SetType(EFFECT_TYPE_SINGLE)
```
