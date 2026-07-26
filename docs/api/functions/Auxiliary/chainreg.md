# Auxiliary.chainreg

## Signature

```lua
Auxiliary.chainreg(Effect e, int tp, Group eg, int ep, any ev, Effect re, any r, int rp) -> void
```

## Description

Registers FLAG_ID_CHAINING on e's handler if that flag is not already present.
The flag resets by the standard event reset, except turn Set reset, and also at the end of the Chain.

## Parameters

- `e` `Effect`
- `tp` `int`
- `eg` `Group`
- `ep` `int`
- `ev` `any`
- `re` `Effect`
- `r` `any`
- `rp` `int`

## Source

- `Utilities/utility.lua:814`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **47** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer) with `Auxiliary.chainreg`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Reflection of Endymion | `39000945` | [Scripts/c39000945.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c39000945.lua) | 1 |
| Magister of Endymion | `66104644` | [Scripts/c66104644.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c66104644.lua) | 1 |
| Servant of Endymion | `92559258` | [Scripts/c92559258.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c92559258.lua) | 1 |
| Machina Fortress | `5556499` | [Scripts/c5556499.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c5556499.lua) | 1 |
| Mythical Beast Master Cerberus | `53842431` | [Scripts/c53842431.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c53842431.lua) | 1 |
| Mythical Beast Medusa | `54965929` | [Scripts/c54965929.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c54965929.lua) | 1 |
| Mythical Beast Garuda | `28570310` | [Scripts/c28570310.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c28570310.lua) | 1 |
| Spell Chronicle | `74402414` | [Scripts/c74402414.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c74402414.lua) | 1 |
| Corrosive Scales | `13235258` | [Scripts/c13235258.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c13235258.lua) | 1 |
| Mythical Beast Jackal | `91182675` | [Scripts/c91182675.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c91182675.lua) | 1 |
| Mythical Beast Bashilisk | `80959027` | [Scripts/c80959027.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c80959027.lua) | 1 |
| Nitro Warrior | `18013090` | [Scripts/c18013090.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c18013090.lua) | 1 |
| Blackwing Full Armor Master | `54082269` | [Scripts/c54082269.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c54082269.lua) | 1 |
| Interdimensional Matter Forwarder | `60238002` | [Scripts/c60238002.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c60238002.lua) | 1 |
| Mythical Beast Jackal King | `27354732` | [Scripts/c27354732.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c27354732.lua) | 1 |
| Skilled Blue Magician | `88901771` | [Scripts/c88901771.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c88901771.lua) | 1 |
| Skilled Red Magician | `65338781` | [Scripts/c65338781.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c65338781.lua) | 1 |
| Thelematech Clatis | `98986900` | [Scripts/c98986900.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c98986900.lua) | 1 |
| Spellbook Star Hall | `56321639` | [Scripts/c56321639.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c56321639.lua) | 1 |
| Megistric Maginician | `83035296` | [Scripts/c83035296.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c83035296.lua) | 1 |
| Endymion's Lab | `65342096` | [Scripts/c65342096.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c65342096.lua) | 1 |
| Skilled Brown Magician | `88232397` | [Scripts/c88232397.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c88232397.lua) | 1 |
| Magical Exemplar | `6061630` | [Scripts/c6061630.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c6061630.lua) | 1 |
| Spellstone Sorcerer Karood | `20630765` | [Scripts/c20630765.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c20630765.lua) | 1 |
| ...and 23 more |  |  |  |

## Script Examples

### Reflection of Endymion (`39000945`)

Source: [Scripts/c39000945.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c39000945.lua)

```lua
	e1:SetProperty(EFFECT_FLAG_CANNOT_DISABLE)
	e1:SetRange(LOCATION_PZONE)
	e1:SetOperation(aux.chainreg)
	c:RegisterEffect(e1)
	local e2=Effect.CreateEffect(c)
```

### Magister of Endymion (`66104644`)

Source: [Scripts/c66104644.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c66104644.lua)

```lua
	e1:SetProperty(EFFECT_FLAG_CANNOT_DISABLE)
	e1:SetRange(LOCATION_PZONE)
	e1:SetOperation(aux.chainreg)
	c:RegisterEffect(e1)
	local e2=Effect.CreateEffect(c)
```

### Servant of Endymion (`92559258`)

Source: [Scripts/c92559258.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c92559258.lua)

```lua
	e1:SetProperty(EFFECT_FLAG_CANNOT_DISABLE)
	e1:SetRange(LOCATION_PZONE)
	e1:SetOperation(aux.chainreg)
	c:RegisterEffect(e1)
	local e2=Effect.CreateEffect(c)
```
