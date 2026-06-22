# Auxiliary.AddFusionProcCode4

## Signature

```lua
Auxiliary.AddFusionProcCode4(Card c, int code1, int code2, int code3, int code4, bool sub, bool insf) -> void
```

## Description

Registers a fixed four-name Fusion procedure requiring code1, code2, code3, and code4 as materials.

## Parameters

- `c` `Card`
- `code1` `int`
- `code2` `int`
- `code3` `int`
- `code4` `int`
- `sub` `bool`
- `insf` `bool`

## Source

- `Utilities/procedure.lua:1230`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **2** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer) with `Auxiliary.AddFusionProcCode4`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Super Vehicroid - Stealth Union | `3897065` | [Scripts/c3897065.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c3897065.lua) | 33 |
| Elemental HERO Electrum | `29343734` | [Scripts/c29343734.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c29343734.lua) | 27 |

## Script Examples

### Super Vehicroid - Stealth Union (`3897065`)

Source: [Scripts/c3897065.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c3897065.lua)

```lua
	--fusion material
	c:EnableReviveLimit()
	aux.AddFusionProcCode4(c,61538782,98049038,71218746,984114,true,true)
	--equip
	local e1=Effect.CreateEffect(c)
```

### Elemental HERO Electrum (`29343734`)

Source: [Scripts/c29343734.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c29343734.lua)

```lua
	--fusion material
	c:EnableReviveLimit()
	aux.AddFusionProcCode4(c,21844576,58932615,84327329,79979666,true,true)
	--spsummon condition
	local e2=Effect.CreateEffect(c)
```
