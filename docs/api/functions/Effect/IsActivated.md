# Effect.IsActivated

## Signature

```lua
Effect.IsActivated(Effect e) -> bool
```

## Description

Checks whether e has one of the EFFECT_TYPES_CHAIN_LINK type bits.

## Parameters

- `e` `Effect`

## Returns

- `bool`

## Source

- `D:\Programs\GitHub\ygopro-core\libeffect.cpp:655`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **147** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer) with `Effect.IsActivated`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Accel Synchro Stardust Dragon](/examples/cards/30983281) | `30983281` | [Scripts/c30983281.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c30983281.lua) | 69 |
| [Exciting Melffy Time](/examples/cards/58036097) | `58036097` | [Scripts/c58036097.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c58036097.lua) | 69 |
| [Performage Cup Tricker](/examples/cards/6812770) | `6812770` | [Scripts/c6812770.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c6812770.lua) | 65 |
| [El Shaddoll Meshachrer](/examples/cards/32467459) | `32467459` | [Scripts/c32467459.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c32467459.lua) | 61 |
| Ancient Gear Duel | `53541822` | [Scripts/c53541822.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c53541822.lua) | 58 |
| Branded in White | `34995106` | [Scripts/c34995106.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c34995106.lua) | 58 |
| Miscellaneousaurus | `38572779` | [Scripts/c38572779.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c38572779.lua) | 56 |
| Fallen Paradise of the Sacred Beasts | `65861210` | [Scripts/c65861210.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c65861210.lua) | 56 |
| Heavy Interlock | `20071842` | [Scripts/c20071842.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c20071842.lua) | 56 |
| Sinful Spoils of the White Forest | `3496543` | [Scripts/c3496543.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c3496543.lua) | 56 |
| Vanquish Soul Caesar Valius | `91073013` | [Scripts/c91073013.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c91073013.lua) | 54 |
| Chevreuil, Hunting Scout of the Deep Forest | `13023431` | [Scripts/c13023431.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c13023431.lua) | 54 |
| Gagaga Girl - Cell Phone Subtraction | `48393693` | [Scripts/c48393693.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c48393693.lua) | 53 |
| Cyberdark End Dragon | `37542782` | [Scripts/c37542782.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c37542782.lua) | 53 |
| Fairy Tail - Wiccat | `27632520` | [Scripts/c27632520.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c27632520.lua) | 52 |
| Shadow Severing Strike | `57232301` | [Scripts/c57232301.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c57232301.lua) | 52 |
| Emblema Salvation | `61950680` | [Scripts/c61950680.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c61950680.lua) | 52 |
| Rapid Trigger | `67526112` | [Scripts/c67526112.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c67526112.lua) | 52 |
| Black Chaos the Ultimate Magical Swordsman | `98684220` | [Scripts/c98684220.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c98684220.lua) | 51 |
| Shichi-Go-San | `11035075` | [Scripts/c11035075.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c11035075.lua) | 51 |
| Scourge of the White Forest | `93723936` | [Scripts/c93723936.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c93723936.lua) | 51 |
| Exstellarknight Constellar Ptolemy Ω7 | `6195332` | [Scripts/c6195332.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c6195332.lua) | 50 |
| Artmage Peripeteia -Turmoil- | `17719582` | [Scripts/c17719582.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c17719582.lua) | 50 |
| Qliphort Genius | `22423493` | [Scripts/c22423493.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c22423493.lua) | 49 |
| ...and 123 more |  |  |  |

## Script Examples

### Accel Synchro Stardust Dragon (`30983281`)

Source: [Scripts/c30983281.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c30983281.lua)

```lua
end
function c30983281.immval(e,te)
	return te:GetOwnerPlayer()~=e:GetOwnerPlayer() and te:IsActivated()
end
```

### Exciting Melffy Time (`58036097`)

Source: [Scripts/c58036097.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c58036097.lua)

```lua
end
function s.efilter(e,re)
	return e:GetHandlerPlayer()~=re:GetOwnerPlayer() and re:IsActivated()
end
```

### Performage Cup Tricker (`6812770`)

Source: [Scripts/c6812770.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c6812770.lua)

```lua
function s.xyzcon(e,tp,eg,ep,ev,re,r,rp)
	local c=e:GetHandler()
	return c:IsReason(REASON_COST) and re:IsActivated() and re:IsActiveType(TYPE_XYZ)
		and c:IsPreviousLocation(LOCATION_OVERLAY)
end
```
