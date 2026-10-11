# Duel.Release

## Signature

```lua
Duel.Release(Card|Group targets, int reason, [int reason_player]) -> int
```

## Description

Tributes/Releases targets for reason and returns the number of cards actually released.
Use REASON_COST when paying a cost and REASON_EFFECT or REASON_SPSUMMON when the release is part of an effect or Summon procedure.
Match the reason to the filter that selected the cards, such as cost-specific releasable checks for costs.

## How To Use It

Use this to Tribute/Release cards as a cost, effect, or Summon procedure.

When selecting a release cost, select cards that are legal to release, then release them with the same reason used for the cost:

```lua
local g=Duel.SelectReleaseGroupEx(tp,nil,1,1,REASON_COST,false,nil)
if #g>0 then
    Duel.Release(g,REASON_COST)
end
```

The return value is the number of cards actually released.

## Related Functions

- [Card.IsReleasable](/api/functions/Card/IsReleasable)
- [Duel.GetReleaseGroup](/api/functions/Duel/GetReleaseGroup)
- [Duel.SelectReleaseGroupEx](/api/functions/Duel/SelectReleaseGroupEx)

## Parameters

- `targets` `Card|Group`
- `reason` `int`
- `reason_player` `int` optional

## Returns

- `int`

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:4881`

## Guided Examples

Learn how to use this function in context:

- [Functions That Move Cards Across Locations](/learn/moving-cards)
- [Special Summon-Only Monster Guide](/learn/special-summon-only-monsters)
- [Tribute Summon Materials](/learn/tribute-summon-materials)

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **1075** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=standard&mode=code&q=Duel.Release) with `Duel.Release`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Astrograph Sorcerer, the Starfrost Magician](/examples/cards/48171151) | `48171151` | [Scripts/c48171151.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c48171151.lua) | 1 |
| [Artmage Non-Finito](/examples/cards/74631897) | `74631897` | [Scripts/c74631897.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c74631897.lua) | 1 |
| [Surprise Fusion](/examples/cards/35167375) | `35167375` | [Scripts/c35167375.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c35167375.lua) | 1 |
| [Goyo Emperor](/examples/cards/59255742) | `59255742` | [Scripts/c59255742.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c59255742.lua) | 1 |
| [Accel Synchro Stardust Dragon](/examples/cards/30983281) | `30983281` | [Scripts/c30983281.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c30983281.lua) | 1 |
| [Meteoroa Drytron](/examples/cards/24166324) | `24166324` | [Scripts/c24166324.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c24166324.lua) | 1 |
| [Ehther the Heavenly Monarch](/examples/cards/96570609) | `96570609` | [Scripts/c96570609.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c96570609.lua) | 1 |
| [Ursarctic Polari](/examples/cards/27693363) | `27693363` | [Scripts/c27693363.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c27693363.lua) | 1 |
| [Prank-Kids Weather Washer](/examples/cards/44509529) | `44509529` | [Scripts/c44509529.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c44509529.lua) | 1 |
| [Odd-Eyes Revolution Dragon](/examples/cards/16306932) | `16306932` | [Scripts/c16306932.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c16306932.lua) | 1 |
| [D/D Count Surveyor](/examples/cards/5997110) | `5997110` | [Scripts/c5997110.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c5997110.lua) | 1 |
| [Odd-Eyes Arcray Dragon](/examples/cards/6218704) | `6218704` | [Scripts/c6218704.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c6218704.lua) | 1 |
| [Flower Cardian Peony with Butterfly](/examples/cards/57261568) | `57261568` | [Scripts/c57261568.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c57261568.lua) | 1 |
| [Ultimate Crystal Rainbow Dragon Overdrive](/examples/cards/84544192) | `84544192` | [Scripts/c84544192.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c84544192.lua) | 1 |
| [Tellusion the Magna Warrior](/examples/cards/24431911) | `24431911` | [Scripts/c24431911.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c24431911.lua) | 1 |
| [Ursarctic Polar Star](/examples/cards/62714453) | `62714453` | [Scripts/c62714453.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c62714453.lua) | 1 |
| [Penetration Fusion](/examples/cards/8778267) | `8778267` | [Scripts/c8778267.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c8778267.lua) | 1 |
| [DoSolfachord Coolia](/examples/cards/80776622) | `80776622` | [Scripts/c80776622.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c80776622.lua) | 1 |
| [Rescue Hamster](/examples/cards/50485594) | `50485594` | [Scripts/c50485594.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c50485594.lua) | 1 |
| [Mitsurugi Magatama](/examples/cards/76725398) | `76725398` | [Scripts/c76725398.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c76725398.lua) | 1 |
| Flower Cardian Willow with Calligrapher | `89818984` | [Scripts/c89818984.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c89818984.lua) | 1 |
| Cyber Pharos | `29719112` | [Scripts/c29719112.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c29719112.lua) | 1 |
| Prank-Kids Rocket Ride | `18514525` | [Scripts/c18514525.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c18514525.lua) | 1 |
| Vaylantz Genesis Grand Duke | `76075139` | [Scripts/c76075139.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c76075139.lua) | 1 |
| ...and 1051 more |  |  |  |

## Script Examples

### Astrograph Sorcerer, the Starfrost Magician (`48171151`)

Source: [Scripts/c48171151.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c48171151.lua)

```lua
	local c=e:GetHandler()
	if not c:IsRelateToChain() or not c:IsReleasable(REASON_EFFECT) then return end
	Duel.Release(c,REASON_EFFECT)
	local chkf=tp
	local mg1=Duel.GetFusionMaterial(tp):Filter(s.filter0,nil,e)
```

### Artmage Non-Finito (`74631897`)

Source: [Scripts/c74631897.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c74631897.lua)

```lua
	g:Sub(dg)
	Duel.SendtoGrave(dg,REASON_SPSUMMON+REASON_DISCARD)
	Duel.Release(g,REASON_SPSUMMON)
	g:DeleteGroup()
end
```

### Surprise Fusion (`35167375`)

Source: [Scripts/c35167375.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c35167375.lua)

```lua
		local rc=srg:GetFirst()
		local level=rc:GetLevel()
		if Duel.Release(rc,REASON_EFFECT)>0
			and Duel.GetLocationCount(tp,LOCATION_MZONE)>1
			and not Duel.IsPlayerAffectedByEffect(tp,59822133)
```
