# Auxiliary.AddSynchroProcedure

## Signature

```lua
Auxiliary.AddSynchroProcedure(Card c, [function|nil f1], [function|nil f2], int minc, [int maxc]) -> void
```

## Description

Registers the standard Synchro Summon procedure for c.
f1 filters the Tuner material, f2 filters non-Tuner materials, and minc/maxc set the number of non-Tuner materials required.

## Parameters

- `c` `Card`
- `f1` `function|nil` optional
- `f2` `function|nil` optional
- `minc` `int`
- `maxc` `int` optional

## Source

- `Utilities/procedure.lua:60`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **488** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer) with `Auxiliary.AddSynchroProcedure`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Accel Synchro Stardust Dragon](/examples/cards/30983281) | `30983281` | [Scripts/c30983281.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c30983281.lua) | 69 |
| [Predaplant Bal Teah](/examples/cards/66787942) | `66787942` | [Scripts/c66787942.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c66787942.lua) | 64 |
| [PSY-Framelord Omega](/examples/cards/74586817) | `74586817` | [Scripts/c74586817.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c74586817.lua) | 64 |
| [Ecclesia and the Dark Dragon](/examples/cards/78397661) | `78397661` | [Scripts/c78397661.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c78397661.lua) | 62 |
| [PSY-Framelord Zeta](/examples/cards/37192109) | `37192109` | [Scripts/c37192109.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c37192109.lua) | 62 |
| [Earthbound Servant Geo Gremlin](/examples/cards/8690387) | `8690387` | [Scripts/c8690387.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c8690387.lua) | 61 |
| Angelica, Princess of Noble Arms | `36320744` | [Scripts/c36320744.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c36320744.lua) | 59 |
| Plunder Patrollship Jord | `85969517` | [Scripts/c85969517.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c85969517.lua) | 58 |
| Power Tool Braver Dragon | `63265554` | [Scripts/c63265554.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c63265554.lua) | 58 |
| Saiba the Soldier Swordsmith | `36608728` | [Scripts/c36608728.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c36608728.lua) | 57 |
| Arms of Genex Return Zero | `61775475` | [Scripts/c61775475.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c61775475.lua) | 56 |
| Hi-Speedroid Cork Shooter | `23361526` | [Scripts/c23361526.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c23361526.lua) | 56 |
| Flower Cardian Moonflowerviewing | `33541430` | [Scripts/c33541430.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c33541430.lua) | 56 |
| Genex Ally Triforce | `52709508` | [Scripts/c52709508.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c52709508.lua) | 55 |
| Genex Ally Triarm | `17760003` | [Scripts/c17760003.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c17760003.lua) | 55 |
| Supreme King Z-ARC - Synchro Universe | `48654267` | [Scripts/c48654267.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c48654267.lua) | 54 |
| Clear Wing Fast Dragon | `90036274` | [Scripts/c90036274.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c90036274.lua) | 54 |
| Cupid Pitch | `21915012` | [Scripts/c21915012.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c21915012.lua) | 54 |
| Masterflare Hyperion | `63101468` | [Scripts/c63101468.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c63101468.lua) | 53 |
| D/D/D Super Doom King Bright Armageddon | `72402069` | [Scripts/c72402069.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c72402069.lua) | 52 |
| Psychic Omnibuster | `70659412` | [Scripts/c70659412.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c70659412.lua) | 52 |
| Daigusto Laplampilica | `76937326` | [Scripts/c76937326.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c76937326.lua) | 52 |
| Black-Winged Assault Dragon | `73218989` | [Scripts/c73218989.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c73218989.lua) | 52 |
| Junk Warrior Extreme | `16327715` | [Scripts/c16327715.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c16327715.lua) | 52 |
| ...and 464 more |  |  |  |

## Script Examples

### Accel Synchro Stardust Dragon (`30983281`)

Source: [Scripts/c30983281.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c30983281.lua)

```lua
	aux.AddCodeList(c,44508094)
	--synchro summon
	aux.AddSynchroProcedure(c,nil,aux.NonTuner(nil),1)
	c:EnableReviveLimit()
	--special summon
```

### Predaplant Bal Teah (`66787942`)

Source: [Scripts/c66787942.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c66787942.lua)

```lua
	local e0=aux.AddThisCardInGraveAlreadyCheck(c)
	--Synchro summon
	aux.AddSynchroProcedure(c,nil,aux.NonTuner(nil),1)
	c:EnableReviveLimit()
	--special summon
```

### PSY-Framelord Omega (`74586817`)

Source: [Scripts/c74586817.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c74586817.lua)

```lua
function c74586817.initial_effect(c)
	--synchro summon
	aux.AddSynchroProcedure(c,nil,aux.NonTuner(nil),1)
	c:EnableReviveLimit()
	--remove
```
