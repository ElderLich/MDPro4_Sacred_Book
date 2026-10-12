# Card.IsCanBeEffectTarget

## Signature

```lua
Card.IsCanBeEffectTarget(Card c, [Effect e]) -> bool
```

## Description

Checks whether c can be targeted by e, or by the current reason effect when e is omitted.

## Parameters

- `c` `Card`
- `e` `Effect` optional

## Returns

- `bool`

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3703`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **328** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=standard&mode=code&q=Card.IsCanBeEffectTarget) with `Card.IsCanBeEffectTarget`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Performage Cup Tricker](/examples/cards/6812770) | `6812770` | [Scripts/c6812770.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c6812770.lua) | 1 |
| [Ghostrick Renovation](/examples/cards/61818176) | `61818176` | [Scripts/c61818176.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c61818176.lua) | 1 |
| [Prank-Kids Weather Washer](/examples/cards/44509529) | `44509529` | [Scripts/c44509529.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c44509529.lua) | 1 |
| [D/D Count Surveyor](/examples/cards/5997110) | `5997110` | [Scripts/c5997110.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c5997110.lua) | 1 |
| [Artmage Masterwork -Succession-](/examples/cards/37517035) | `37517035` | [Scripts/c37517035.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c37517035.lua) | 1 |
| [Dracotail Shaulas](/examples/cards/42125140) | `42125140` | [Scripts/c42125140.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c42125140.lua) | 1 |
| [Radiant Typhoon Varuroon, the Marine Eidolon](/examples/cards/39341885) | `39341885` | [Scripts/c39341885.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c39341885.lua) | 1 |
| Prank-Kids Rocket Ride | `18514525` | [Scripts/c18514525.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c18514525.lua) | 1 |
| Starving Venom Wing Dragon | `5148778` | [Scripts/c5148778.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c5148778.lua) | 1 |
| Gravity Balance | `37930737` | [Scripts/c37930737.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c37930737.lua) | 1 |
| Trirealm Rift Judgment | `65195679` | [Scripts/c65195679.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c65195679.lua) | 1 |
| Trickstar Light Arena | `63492244` | [Scripts/c63492244.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c63492244.lua) | 1 |
| Grandpa Demetto | `44190146` | [Scripts/c44190146.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c44190146.lua) | 1 |
| Prank-Kids Bow-Wow-Bark | `43886072` | [Scripts/c43886072.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c43886072.lua) | 1 |
| Phantom Knights' Rank-Up-Magic Force | `88504133` | [Scripts/c88504133.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c88504133.lua) | 1 |
| Super Quantal Mech Ship Magnacarrier | `10424147` | [Scripts/c10424147.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c10424147.lua) | 1 |
| Amazement Administrator Arlekino | `94821366` | [Scripts/c94821366.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c94821366.lua) | 1 |
| Divine Serpent Apophis | `97800311` | [Scripts/c97800311.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c97800311.lua) | 1 |
| Berserkion the Electromagna Warrior | `42901635` | [Scripts/c42901635.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c42901635.lua) | 1 |
| Nebulus, Dragon Ruler of Mishaps | `94655777` | [Scripts/c94655777.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c94655777.lua) | 1 |
| Galaxy-Eyes Photon Dragon | `93717133` | [Scripts/c93717133.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c93717133.lua) | 1 |
| Darkuriboh | `1035143` | [Scripts/c1035143.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c1035143.lua) | 1 |
| ABC-Dragon Buster | `1561110` | [Scripts/c1561110.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c1561110.lua) | 1 |
| Triamid Dancer | `69529337` | [Scripts/c69529337.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c69529337.lua) | 1 |
| ...and 304 more |  |  |  |

## Script Examples

### Performage Cup Tricker (`6812770`)

Source: [Scripts/c6812770.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c6812770.lua)

```lua
end
function s.xyzfilter(c,e)
	return c:IsFaceup() and c:IsType(TYPE_XYZ) and c:IsCanBeEffectTarget(e)
end
function s.gcheck(g)
```

### Ghostrick Renovation (`61818176`)

Source: [Scripts/c61818176.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c61818176.lua)

```lua
	local tc=Duel.GetFieldCard(tp,LOCATION_FZONE,0)
	if chkc then return false end
	if chk==0 then return tc and tc:IsFaceup() and tc:IsSetCard(0x8d) and tc:IsAbleToHand() and tc:IsCanBeEffectTarget(e) end
	if not Duel.CheckPhaseActivity() then e:SetLabel(1) else e:SetLabel(0) end
	Duel.SetTargetCard(tc)
```

### Prank-Kids Weather Washer (`44509529`)

Source: [Scripts/c44509529.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c44509529.lua)

```lua
function c44509529.spfilter(c,e,tp)
	return c:IsSetCard(0x120) and not c:IsType(TYPE_FUSION)
		and c:IsCanBeEffectTarget(e) and c:IsCanBeSpecialSummoned(e,0,tp,false,false)
end
function c44509529.sptg(e,tp,eg,ep,ev,re,r,rp,chk,chkc)
```
