# Auxiliary.AddFusionProcCode2

## Signature

```lua
Auxiliary.AddFusionProcCode2(Card c, int code1, int code2, bool sub, bool insf) -> void
```

## Description

For the c designated card number for the code1 and code2 monster for the fusion material
Sub that can use fusion instead of material, insf that can be summoned with a simple fusion

## Parameters

- `c` `Card`
- `code1` `int`
- `code2` `int`
- `sub` `bool`
- `insf` `bool`

## Source

- `Utilities/procedure.lua:1209`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **114** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer) with `Auxiliary.AddFusionProcCode2`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| A-to-Z-Dragon Buster Cannon | `65172015` | [Scripts/c65172015.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c65172015.lua) | 58 |
| Cyberdark End Dragon | `37542782` | [Scripts/c37542782.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c37542782.lua) | 53 |
| Ultimate Flame Swordsman | `324483` | [Scripts/c324483.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c324483.lua) | 49 |
| Gate Guardian of Water and Thunder | `97783338` | [Scripts/c97783338.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c97783338.lua) | 47 |
| Destiny End Dragoon | `76263644` | [Scripts/c76263644.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c76263644.lua) | 43 |
| Armed Dragon Catapult Cannon | `75906310` | [Scripts/c75906310.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c75906310.lua) | 41 |
| Thousand-Eyes Restrict | `63519819` | [Scripts/c63519819.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c63519819.lua) | 41 |
| Imperion Magnum the Superconductive Battlebot | `4628897` | [Scripts/c4628897.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c4628897.lua) | 40 |
| Gate Guardian of Wind and Water | `61398234` | [Scripts/c61398234.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c61398234.lua) | 40 |
| Gate Guardian of Thunder and Wind | `34904525` | [Scripts/c34904525.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c34904525.lua) | 39 |
| Elemental HERO Glow Neos | `85507811` | [Scripts/c85507811.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c85507811.lua) | 37 |
| Elemental HERO Dark Neos | `28677304` | [Scripts/c28677304.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c28677304.lua) | 35 |
| Elemental HERO Neos Kluger | `90307498` | [Scripts/c90307498.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c90307498.lua) | 34 |
| VWXYZ-Dragon Catapult Cannon | `84243274` | [Scripts/c84243274.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c84243274.lua) | 34 |
| XY-Dragon Cannon | `2111707` | [Scripts/c2111707.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c2111707.lua) | 34 |
| Multiple Piece Golem | `71628381` | [Scripts/c71628381.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c71628381.lua) | 34 |
| Dark Paladin | `98502113` | [Scripts/c98502113.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c98502113.lua) | 33 |
| YZ-Tank Dragon | `25119460` | [Scripts/c25119460.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c25119460.lua) | 33 |
| XZ-Tank Cannon | `99724761` | [Scripts/c99724761.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c99724761.lua) | 33 |
| VW-Tiger Catapult | `58859575` | [Scripts/c58859575.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c58859575.lua) | 33 |
| Reaper on the Nightmare | `85684223` | [Scripts/c85684223.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c85684223.lua) | 32 |
| Ryu Senshi | `49868263` | [Scripts/c49868263.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c49868263.lua) | 32 |
| Elemental HERO Thunder Giant | `61204971` | [Scripts/c61204971.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c61204971.lua) | 32 |
| Elemental HERO Grand Neos | `48996569` | [Scripts/c48996569.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c48996569.lua) | 31 |
| ...and 90 more |  |  |  |

## Script Examples

### A-to-Z-Dragon Buster Cannon (`65172015`)

Source: [Scripts/c65172015.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c65172015.lua)

```lua
function c65172015.initial_effect(c)
	c:EnableReviveLimit()
	aux.AddFusionProcCode2(c,1561110,91998119,true,true)
	--cannot special summon
	local e1=Effect.CreateEffect(c)
```

### Cyberdark End Dragon (`37542782`)

Source: [Scripts/c37542782.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c37542782.lua)

```lua
	--fusion material
	c:EnableReviveLimit()
	aux.AddFusionProcCode2(c,40418351,1546123,true,true)
	--spsummon condition
	local e1=Effect.CreateEffect(c)
```

### Ultimate Flame Swordsman (`324483`)

Source: [Scripts/c324483.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c324483.lua)

```lua
function s.initial_effect(c)
	c:EnableReviveLimit()
	aux.AddFusionProcCode2(c,45231177,36319131,true,true)
	--destroy
	local e1=Effect.CreateEffect(c)
```
