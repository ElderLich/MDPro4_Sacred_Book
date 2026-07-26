# Card.GetFlagEffectLabel

## Signature

```lua
Card.GetFlagEffectLabel(Card c, int code) -> int|nil,...?
```

## Description

Returns the first label value from each flag effect with the given code on c.
If c has no matching flag effect, the core returns nil. Matching flag effects with no label return 0 for that slot.
If several matching markers exist, the binding returns several Lua values.

## How To Use It

Use this when a card marker stored an integer payload.

```lua
local label=c:GetFlagEffectLabel(id)
if label then
    e:SetLabel(label)
end
```

If no marker exists, this returns nil. If several matching markers exist, the local binding returns one label value per marker.

## Related Functions

- [Card.RegisterFlagEffect](/api/functions/Card/RegisterFlagEffect)
- [Card.GetFlagEffect](/api/functions/Card/GetFlagEffect)
- [Card.ResetFlagEffect](/api/functions/Card/ResetFlagEffect)

## Parameters

- `c` `Card` - Card whose single-card flag effects are inspected.
- `code` `int` - Flag-effect code; the core masks it with MAX_CARD_ID and adds EFFECT_FLAG_EFFECT.

## Returns

- `int|nil` - First label value, or nil if no matching flag effect exists.
- `...?` - Additional integer label values from additional matching flag effects.

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3559`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **218** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer) with `Card.GetFlagEffectLabel`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Deftero Enneacraft - "alazoneIA"](/examples/cards/92171126) | `92171126` | [Scripts/c92171126.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c92171126.lua) | 68 |
| [Ehther the Heavenly Monarch](/examples/cards/96570609) | `96570609` | [Scripts/c96570609.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c96570609.lua) | 65 |
| [Resurgam Xyz](/examples/cards/49082032) | `49082032` | [Scripts/c49082032.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c49082032.lua) | 64 |
| [Converging Wishes](/examples/cards/20007374) | `20007374` | [Scripts/c20007374.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c20007374.lua) | 64 |
| [PSY-Framelord Omega](/examples/cards/74586817) | `74586817` | [Scripts/c74586817.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c74586817.lua) | 64 |
| [Graydle Split](/examples/cards/75361204) | `75361204` | [Scripts/c75361204.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c75361204.lua) | 64 |
| [Future Fusion Nova](/examples/cards/92058902) | `92058902` | [Scripts/c92058902.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c92058902.lua) | 63 |
| [D/D/D/D Super-Dimensional Sovereign Emperor Zero Paradox](/examples/cards/97417863) | `97417863` | [Scripts/c97417863.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c97417863.lua) | 62 |
| [Shooting Majestic Star Dragon](/examples/cards/40939228) | `40939228` | [Scripts/c40939228.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c40939228.lua) | 62 |
| [PSY-Framelord Zeta](/examples/cards/37192109) | `37192109` | [Scripts/c37192109.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c37192109.lua) | 62 |
| [The Gaze of Timaeus](/examples/cards/22283204) | `22283204` | [Scripts/c22283204.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c22283204.lua) | 62 |
| [Rescue Hamster](/examples/cards/50485594) | `50485594` | [Scripts/c50485594.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c50485594.lua) | 61 |
| Gravity Balance | `37930737` | [Scripts/c37930737.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c37930737.lua) | 60 |
| Trickstar Light Stage | `35371948` | [Scripts/c35371948.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c35371948.lua) | 60 |
| Regenesis Birth | `27781371` | [Scripts/c27781371.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c27781371.lua) | 60 |
| Vernusylph and the Changing Season | `37313338` | [Scripts/c37313338.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c37313338.lua) | 60 |
| Performapal Trump Girl | `42002073` | [Scripts/c42002073.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c42002073.lua) | 60 |
| Angelica, Princess of Noble Arms | `36320744` | [Scripts/c36320744.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c36320744.lua) | 59 |
| Trickstar Light Arena | `63492244` | [Scripts/c63492244.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c63492244.lua) | 59 |
| Ecclesia and the Dark Dragon | `78397661` | [Scripts/c78397661.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c78397661.lua) | 59 |
| Mixeroid | `71340250` | [Scripts/c71340250.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c71340250.lua) | 59 |
| Echelon of the Fire Kings | `38798785` | [Scripts/c38798785.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c38798785.lua) | 59 |
| Magical Hats | `81210420` | [Scripts/c81210420.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c81210420.lua) | 59 |
| Forbidden Dark Contract with the Swamp King | `10833828` | [Scripts/c10833828.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c10833828.lua) | 59 |
| ...and 194 more |  |  |  |

## Script Examples

### Deftero Enneacraft - "alazoneIA" (`92171126`)

Source: [Scripts/c92171126.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c92171126.lua)

```lua
end
function s.retfilter(c,fid)
	return c:GetFlagEffectLabel(id)==fid
end
function s.retcon(e,tp,eg,ep,ev,re,r,rp)
```

### Ehther the Heavenly Monarch (`96570609`)

Source: [Scripts/c96570609.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c96570609.lua)

```lua
function c96570609.thcon(e,tp,eg,ep,ev,re,r,rp)
	local tc=e:GetLabelObject()
	if tc:GetFlagEffectLabel(96570609)~=e:GetLabel() then
		e:Reset()
		return false
```

### Resurgam Xyz (`49082032`)

Source: [Scripts/c49082032.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c49082032.lua)

```lua
function c49082032.retcon(e,tp,eg,ep,ev,re,r,rp)
	local tc=e:GetLabelObject()
	if tc:GetFlagEffectLabel(49082032)~=e:GetLabel() then
		e:Reset()
		return false
```
