# Card.SetCounterLimit

## Signature

```lua
Card.SetCounterLimit(Card c, int countertype, int limit) -> void
```

## Description

Adds an EFFECT_COUNTER_LIMIT for countertype to c with value limit.

## Parameters

- `c` `Card`
- `countertype` `int`
- `limit` `int`

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3635`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **35** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer) with `Card.SetCounterLimit`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Performapal Turn Trooper | `220414` | [Scripts/c220414.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c220414.lua) | 50 |
| The Deal of Destiny | `32245230` | [Scripts/c32245230.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c32245230.lua) | 47 |
| Forge a New Future | `27104921` | [Scripts/c27104921.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c27104921.lua) | 47 |
| The Kaiju Files | `11163040` | [Scripts/c11163040.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c11163040.lua) | 47 |
| That's 10! | `97223101` | [Scripts/c97223101.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c97223101.lua) | 42 |
| Skilled Blue Magician | `88901771` | [Scripts/c88901771.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c88901771.lua) | 39 |
| Skilled Red Magician | `65338781` | [Scripts/c65338781.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c65338781.lua) | 39 |
| Defect Compiler | `92327802` | [Scripts/c92327802.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c92327802.lua) | 39 |
| Thelematech Clatis | `98986900` | [Scripts/c98986900.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c98986900.lua) | 38 |
| Skilled Brown Magician | `88232397` | [Scripts/c88232397.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c88232397.lua) | 36 |
| Arcane Barrier | `17896384` | [Scripts/c17896384.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c17896384.lua) | 36 |
| Kaiju Capture Mission | `81057455` | [Scripts/c81057455.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c81057455.lua) | 35 |
| Shining Piecephilia | `49776811` | [Scripts/c49776811.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c49776811.lua) | 33 |
| Spellstone Sorcerer Karood | `20630765` | [Scripts/c20630765.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c20630765.lua) | 32 |
| The World Legacy | `92562411` | [Scripts/c92562411.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c92562411.lua) | 32 |
| Silent Magician LV4 | `73665146` | [Scripts/c73665146.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c73665146.lua) | 30 |
| Performage Hat Tricker | `31292357` | [Scripts/c31292357.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c31292357.lua) | 30 |
| Skilled Dark Magician | `73752131` | [Scripts/c73752131.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c73752131.lua) | 30 |
| Skilled White Magician | `46363422` | [Scripts/c46363422.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c46363422.lua) | 29 |
| Karakuri Anatomy | `85541675` | [Scripts/c85541675.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c85541675.lua) | 29 |
| Seed Cannon | `81524977` | [Scripts/c81524977.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c81524977.lua) | 29 |
| Six Samurai United | `72345736` | [Scripts/c72345736.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c72345736.lua) | 29 |
| Summon Over | `48015771` | [Scripts/c48015771.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c48015771.lua) | 28 |
| Shien's Daredevil | `98162021` | [Scripts/c98162021.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c98162021.lua) | 28 |
| ...and 11 more |  |  |  |

## Script Examples

### Performapal Turn Trooper (`220414`)

Source: [Scripts/c220414.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c220414.lua)

```lua
function c220414.initial_effect(c)
	c:EnableCounterPermit(0x50)
	c:SetCounterLimit(0x50,2)
	--add counter
	local e1=Effect.CreateEffect(c)
```

### The Deal of Destiny (`32245230`)

Source: [Scripts/c32245230.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c32245230.lua)

```lua
function c32245230.initial_effect(c)
	c:EnableCounterPermit(0x5e,LOCATION_SZONE)
	c:SetCounterLimit(0x5e,1)
	--Activate
	local e0=Effect.CreateEffect(c)
```

### Forge a New Future (`27104921`)

Source: [Scripts/c27104921.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c27104921.lua)

```lua
function c27104921.initial_effect(c)
	c:EnableCounterPermit(0x61)
	c:SetCounterLimit(0x61,3)
	--activate
	local e1=Effect.CreateEffect(c)
```
