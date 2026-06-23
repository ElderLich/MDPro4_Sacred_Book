# Duel.SetTargetCard

## Signature

```lua
Duel.SetTargetCard(Card|Group targets) -> void
```

## Description

Stores targets as the target cards for the currently handled Chain.
For non-continuous effects, the core creates Chain relations for those cards and sends the become-target message when the effect has EFFECT_FLAG_CARD_TARGET.
This records broad operation targets; it does not by itself check whether the cards are legal effect targets.

## Parameters

- `targets` `Card|Group` - Card or Group to record as current Chain target cards.

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:5004`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **638** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer) with `Duel.SetTargetCard`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Astrograph Sorcerer, the Star Magician](/examples/cards/48171151) | `48171151` | [Scripts/c48171151.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c48171151.lua) | 80 |
| [Goyo Emperor](/examples/cards/59255742) | `59255742` | [Scripts/c59255742.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c59255742.lua) | 70 |
| [Performage Cup Tricker](/examples/cards/6812770) | `6812770` | [Scripts/c6812770.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c6812770.lua) | 65 |
| [Ghostrick Renovation](/examples/cards/61818176) | `61818176` | [Scripts/c61818176.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c61818176.lua) | 65 |
| [Prank-Kids Weather Washer](/examples/cards/44509529) | `44509529` | [Scripts/c44509529.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c44509529.lua) | 65 |
| [D/D Count Surveyor](/examples/cards/5997110) | `5997110` | [Scripts/c5997110.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c5997110.lua) | 63 |
| [Dracotail Shaulas](/examples/cards/42125140) | `42125140` | [Scripts/c42125140.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c42125140.lua) | 63 |
| [Artmage Masterwork -Succession-](/examples/cards/37517035) | `37517035` | [Scripts/c37517035.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c37517035.lua) | 63 |
| [Enneacraft - Atil.SPIA](/examples/cards/71801447) | `71801447` | [Scripts/c71801447.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c71801447.lua) | 62 |
| [Radiant Typhoon Varuroon, the Marine Eidolon](/examples/cards/39341885) | `39341885` | [Scripts/c39341885.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c39341885.lua) | 61 |
| [Camelot, Realm of Noble Knights and Noble Arms](/examples/cards/15635751) | `15635751` | [Scripts/c15635751.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c15635751.lua) | 61 |
| [Particle Fusion](/examples/cards/39261576) | `39261576` | [Scripts/c39261576.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c39261576.lua) | 61 |
| [Prank-Kids Rocket Ride](/examples/cards/18514525) | `18514525` | [Scripts/c18514525.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c18514525.lua) | 61 |
| Starving Venom Wing Dragon | `5148778` | [Scripts/c5148778.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c5148778.lua) | 60 |
| Red-Eyes Slash Dragon | `21140872` | [Scripts/c21140872.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c21140872.lua) | 60 |
| Gravity Balance | `37930737` | [Scripts/c37930737.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c37930737.lua) | 60 |
| Trickstar Light Arena | `63492244` | [Scripts/c63492244.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c63492244.lua) | 59 |
| Performapal Celestial Magician | `58092907` | [Scripts/c58092907.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c58092907.lua) | 58 |
| Grandpa Demetto | `44190146` | [Scripts/c44190146.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c44190146.lua) | 58 |
| Prank-Kids Bow-Wow-Bark | `43886072` | [Scripts/c43886072.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c43886072.lua) | 58 |
| Triamid Pulse | `96100333` | [Scripts/c96100333.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c96100333.lua) | 58 |
| Divine Serpent Apophis | `97800311` | [Scripts/c97800311.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c97800311.lua) | 58 |
| Super Quantal Mech Ship Magnacarrier | `10424147` | [Scripts/c10424147.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c10424147.lua) | 57 |
| Amazement Administrator Arlekino | `94821366` | [Scripts/c94821366.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c94821366.lua) | 57 |
| ...and 614 more |  |  |  |

## Script Examples

### Astrograph Sorcerer, the Star Magician (`48171151`)

Source: [Scripts/c48171151.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c48171151.lua)

```lua
	end
	local desg=eg:Filter(s.desfilter,nil,tp)
	Duel.SetTargetCard(desg)
	Duel.SetOperationInfo(0,CATEGORY_SPECIAL_SUMMON,c,1,0,0)
end
```

### Goyo Emperor (`59255742`)

Source: [Scripts/c59255742.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c59255742.lua)

```lua
	if chk==0 then return Duel.GetLocationCount(tp,LOCATION_MZONE)>0
		and bc:IsCanBeSpecialSummoned(e,0,tp,false,false) end
	Duel.SetTargetCard(bc)
	Duel.SetOperationInfo(0,CATEGORY_SPECIAL_SUMMON,bc,1,0,0)
end
```

### Performage Cup Tricker (`6812770`)

Source: [Scripts/c6812770.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c6812770.lua)

```lua
	Duel.Hint(HINT_SELECTMSG,tp,HINTMSG_TARGET)
	local sg=g:SelectSubGroup(tp,s.gcheck,false,2,2)
	Duel.SetTargetCard(sg)
end
function s.xyzop(e,tp,eg,ep,ev,re,r,rp)
```
