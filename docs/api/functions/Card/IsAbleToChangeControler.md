# Card.IsAbleToChangeControler

## Signature

```lua
Card.IsAbleToChangeControler(Card c) -> bool
```

## Description

Check whether c can change the control
Note: This function returns false only if the card receives the effect of "Can not change control"

## Parameters

- `c` `Card`

## Returns

- `bool`

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3626`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **88** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer) with `Card.IsAbleToChangeControler`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [D/D/D/D Super-Dimensional Sovereign Emperor Zero Paradox](/examples/cards/97417863) | `97417863` | [Scripts/c97417863.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c97417863.lua) | 62 |
| [Radiant Typhoon Varuroon, the Marine Eidolon](/examples/cards/39341885) | `39341885` | [Scripts/c39341885.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c39341885.lua) | 61 |
| Relinquished Fusion | `78063197` | [Scripts/c78063197.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c78063197.lua) | 59 |
| Meklord Astro Mekanikle | `63468625` | [Scripts/c63468625.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c63468625.lua) | 57 |
| Zoroa, the Magistus Verethragna | `37260677` | [Scripts/c37260677.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c37260677.lua) | 57 |
| Yummy★Redemption | `65853758` | [Scripts/c65853758.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c65853758.lua) | 53 |
| Cyberdark End Dragon | `37542782` | [Scripts/c37542782.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c37542782.lua) | 53 |
| Millennium-Eyes Restrict | `41578483` | [Scripts/c41578483.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c41578483.lua) | 53 |
| Snake-Eyes Vengeance Dragon | `79415624` | [Scripts/c79415624.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c79415624.lua) | 52 |
| Immortal Phoenix Gearfried | `22091647` | [Scripts/c22091647.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c22091647.lua) | 51 |
| Allure Queen LV5 | `23756165` | [Scripts/c23756165.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c23756165.lua) | 51 |
| Meklord Emperor Granel | `4545683` | [Scripts/c4545683.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c4545683.lua) | 50 |
| Courageous Crimson Chevalier Bradamante | `91479482` | [Scripts/c91479482.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c91479482.lua) | 50 |
| Meklord Emperor Skiel | `31930787` | [Scripts/c31930787.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c31930787.lua) | 48 |
| Nightmare-Eyes Restrict | `30138615` | [Scripts/c30138615.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c30138615.lua) | 48 |
| Underground Arachnid | `63465535` | [Scripts/c63465535.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c63465535.lua) | 48 |
| Majestic Absorption | `63144961` | [Scripts/c63144961.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c63144961.lua) | 48 |
| Snake-Eyes Doomed Dragon | `58071334` | [Scripts/c58071334.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c58071334.lua) | 48 |
| Meklord Emperor Wisel | `68140974` | [Scripts/c68140974.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c68140974.lua) | 47 |
| Draco Awakening | `66092596` | [Scripts/c66092596.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c66092596.lua) | 47 |
| Sky Striker Ace - Azalea Temperance | `56741506` | [Scripts/c56741506.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c56741506.lua) | 47 |
| Mikanko Spiritwalk | `53174748` | [Scripts/c53174748.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c53174748.lua) | 47 |
| Allure Queen LV3 | `87257460` | [Scripts/c87257460.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c87257460.lua) | 47 |
| Vylon Disigma | `39987164` | [Scripts/c39987164.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c39987164.lua) | 47 |
| ...and 64 more |  |  |  |

## Script Examples

### D/D/D/D Super-Dimensional Sovereign Emperor Zero Paradox (`97417863`)

Source: [Scripts/c97417863.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c97417863.lua)

```lua
end
function c97417863.pltg(e,tp,eg,ep,ev,re,r,rp,chk,chkc)
	if chkc then return chkc:IsLocation(LOCATION_PZONE) and chkc:IsControler(1-tp) and chkc:IsAbleToChangeControler() end
	local c=e:GetHandler()
	if chk==0 then return Duel.IsExistingTarget(Card.IsAbleToChangeControler,tp,0,LOCATION_PZONE,1,nil)
```

### Radiant Typhoon Varuroon, the Marine Eidolon (`39341885`)

Source: [Scripts/c39341885.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c39341885.lua)

```lua
end
function s.mvfilter(c)
	return c:IsFaceup() and (c:IsControler(c:GetOwner()) or c:IsAbleToChangeControler())
		and not c:IsForbidden() and c:CheckUniqueOnField(c:GetOwner())
end
```

### Relinquished Fusion (`78063197`)

Source: [Scripts/c78063197.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c78063197.lua)

```lua
end
function c78063197.filter(c)
	return c:IsFaceup() and c:IsType(TYPE_EFFECT) and c:IsAbleToChangeControler()
end
function c78063197.eqfilter(c)
```
