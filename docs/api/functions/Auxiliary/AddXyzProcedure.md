# Auxiliary.AddXyzProcedure

## Signature

```lua
Auxiliary.AddXyzProcedure(Card c, function|nil f, int lv, int ct, [function|nil alterf], [int alterdesc], [int maxct], [function|nil alterop]) -> void
```

## Description

Registers the standard Xyz Summon procedure for c.
f filters materials, lv is the required material Xyz Level, ct is the minimum material count, and maxct optionally caps the maximum.
The helper creates an Extra Deck EFFECT_SPSUMMON_PROC with SUMMON_TYPE_XYZ, checks and selects materials with the core Xyz helpers, records them with Card.SetMaterial, and overlays them with Duel.Overlay.
alterf, alterdesc, and alterop define an optional one-card alternate Xyz Summon route.

## Parameters

- `c` `Card` - Xyz Monster receiving the procedure.
- `f` `function|nil` - Optional per-material filter. nil means no extra material restriction beyond the normal Xyz checks.
- `lv` `int` - Required material Xyz Level.
- `ct` `int` - Minimum material count.
- `alterf` `function|nil` optional - Optional filter for a one-card alternate Xyz Summon route.
- `alterdesc` `int` optional - Prompt text id used when the alternate route can be chosen.
- `maxct` `int` optional - Maximum material count. Defaults to ct when omitted.
- `alterop` `function|nil` optional - Optional check/apply callback for the alternate route. The local helper calls it with chk==0 for legality and chk==1 after selection.

## Source

- `Utilities/procedure.lua:485`

## Guided Examples

Learn how to use this function in context:

- [Xyz Procedure Guide](/learn/xyz-procedure)

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **587** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=standard&mode=code&q=Auxiliary.AddXyzProcedure) with `Auxiliary.AddXyzProcedure`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Cyberse Reminder | `56337500` | [Scripts/c56337500.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c56337500.lua) | 1 |
| Number 101: Silent Honor ARK - Soul Asylum | `2419596` | [Scripts/c2419596.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c2419596.lua) | 1 |
| Number 99: Utopia Dragonar | `95134948` | [Scripts/c95134948.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c95134948.lua) | 1 |
| D/D/D Deviser King Deus Machinex | `46593546` | [Scripts/c46593546.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c46593546.lua) | 1 |
| Performage Trapeze Magician | `17016362` | [Scripts/c17016362.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c17016362.lua) | 1 |
| Number 38: Hope Harbinger Dragon Titanic Galaxy | `63767246` | [Scripts/c63767246.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c63767246.lua) | 1 |
| Toadally Awesome | `90809975` | [Scripts/c90809975.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c90809975.lua) | 1 |
| Odd-Eyes Rebellion Dragon Overlord | `98452268` | [Scripts/c98452268.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c98452268.lua) | 1 |
| Darktellarknight Batlamyus | `64414267` | [Scripts/c64414267.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c64414267.lua) | 1 |
| Number 4: Stealth Kragen | `67557908` | [Scripts/c67557908.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c67557908.lua) | 1 |
| Heroic Champion - Magnum Excalibur | `14301396` | [Scripts/c14301396.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c14301396.lua) | 1 |
| Galaxy-Eyes Cipher X Dragon | `28346136` | [Scripts/c28346136.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c28346136.lua) | 1 |
| Raider's Knight | `28781003` | [Scripts/c28781003.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c28781003.lua) | 1 |
| Number 78: Number Archive | `29085954` | [Scripts/c29085954.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c29085954.lua) | 1 |
| Borreload eXcharge Dragon | `6247535` | [Scripts/c6247535.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c6247535.lua) | 1 |
| Salamangreat Blaze Dragon | `9608555` | [Scripts/c9608555.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c9608555.lua) | 1 |
| Squeeze, the Full Moon of Raise Moon - JACKPOT! | `9484285` | [Scripts/c9484285.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c9484285.lua) | 1 |
| CXyz N.As.Ch. Knight | `61374414` | [Scripts/c61374414.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c61374414.lua) | 1 |
| Fairy Tail - Wiccat | `27632520` | [Scripts/c27632520.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c27632520.lua) | 1 |
| Raidraptor - Rising Rebellion Falcon | `71222868` | [Scripts/c71222868.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c71222868.lua) | 1 |
| Time Thief Redoer | `55285840` | [Scripts/c55285840.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c55285840.lua) | 1 |
| Joyous Melffys | `53054164` | [Scripts/c53054164.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c53054164.lua) | 1 |
| Majespecter Draco - Ryu | `3594985` | [Scripts/c3594985.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c3594985.lua) | 1 |
| Mimighoul Throne | `42940335` | [Scripts/c42940335.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c42940335.lua) | 1 |
| ...and 563 more |  |  |  |

## Script Examples

### Cyberse Reminder (`56337500`)

Source: [Scripts/c56337500.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c56337500.lua)

```lua
function c56337500.initial_effect(c)
	--xyz summon
	aux.AddXyzProcedure(c,nil,3,2)
	c:EnableReviveLimit()
	--to hand
```

### Number 101: Silent Honor ARK - Soul Asylum (`2419596`)

Source: [Scripts/c2419596.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c2419596.lua)

```lua
function s.initial_effect(c)
	--xyz summon
	aux.AddXyzProcedure(c,nil,4,2)
	c:EnableReviveLimit()
	--search & material
```

### Number 99: Utopia Dragonar (`95134948`)

Source: [Scripts/c95134948.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c95134948.lua)

```lua
function c95134948.initial_effect(c)
	--xyz summon
	aux.AddXyzProcedure(c,nil,12,3,nil,nil,99)
	c:EnableReviveLimit()
	--special summon
```
