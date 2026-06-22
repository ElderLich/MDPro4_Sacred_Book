# Group.FromCards

## Signature

```lua
Group.FromCards(... Card) -> Group
```

## Description

Creates and returns a new Group containing the non-nil Card arguments.

## Parameters

- `...` `Card`

## Returns

- `Group`

## Source

- `D:\Programs\GitHub\ygopro-core\libgroup.cpp:904`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **420** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer) with `Group.FromCards`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Artmage Non-Finito](/examples/cards/74631897) | `74631897` | [Scripts/c74631897.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c74631897.lua) | 78 |
| [Pendulum Evolution](/examples/cards/55795155) | `55795155` | [Scripts/c55795155.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c55795155.lua) | 77 |
| [Astrograph Sorcerer](/examples/cards/76794549) | `76794549` | [Scripts/c76794549.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c76794549.lua) | 71 |
| [El Shaddoll Apkallone](/examples/cards/50907446) | `50907446` | [Scripts/c50907446.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c50907446.lua) | 68 |
| [Performage Cup Tricker](/examples/cards/6812770) | `6812770` | [Scripts/c6812770.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c6812770.lua) | 65 |
| [Ghostrick Renovation](/examples/cards/61818176) | `61818176` | [Scripts/c61818176.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c61818176.lua) | 65 |
| [Resurgam Xyz](/examples/cards/49082032) | `49082032` | [Scripts/c49082032.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c49082032.lua) | 64 |
| [GMX 55th Experiment Report](/examples/cards/38984832) | `38984832` | [Scripts/c38984832.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c38984832.lua) | 64 |
| [PSY-Framelord Omega](/examples/cards/74586817) | `74586817` | [Scripts/c74586817.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c74586817.lua) | 64 |
| [D/D Count Surveyor](/examples/cards/5997110) | `5997110` | [Scripts/c5997110.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c5997110.lua) | 63 |
| [Shining Draw](/examples/cards/35906693) | `35906693` | [Scripts/c35906693.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c35906693.lua) | 63 |
| [Nekroz Kaleidoscope](/examples/cards/51124303) | `51124303` | [Scripts/c51124303.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c51124303.lua) | 63 |
| [Odd-Eyes Arcray Dragon](/examples/cards/6218704) | `6218704` | [Scripts/c6218704.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c6218704.lua) | 62 |
| [Flower Cardian Peony with Butterfly](/examples/cards/57261568) | `57261568` | [Scripts/c57261568.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c57261568.lua) | 62 |
| [Ursarctic Polar Star](/examples/cards/62714453) | `62714453` | [Scripts/c62714453.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c62714453.lua) | 62 |
| [PSY-Framelord Zeta](/examples/cards/37192109) | `37192109` | [Scripts/c37192109.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c37192109.lua) | 62 |
| [The Gaze of Timaeus](/examples/cards/22283204) | `22283204` | [Scripts/c22283204.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c22283204.lua) | 62 |
| [Starving Venemy Dragon](/examples/cards/93729065) | `93729065` | [Scripts/c93729065.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c93729065.lua) | 61 |
| [Chronograph Sorcerer](/examples/cards/12289247) | `12289247` | [Scripts/c12289247.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c12289247.lua) | 61 |
| [Flower Cardian Willow with Calligrapher](/examples/cards/89818984) | `89818984` | [Scripts/c89818984.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c89818984.lua) | 61 |
| [El Shaddoll Meshachrer](/examples/cards/32467459) | `32467459` | [Scripts/c32467459.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c32467459.lua) | 61 |
| Vaylantz Genesis Grand Duke | `76075139` | [Scripts/c76075139.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c76075139.lua) | 60 |
| Trickstar Light Stage | `35371948` | [Scripts/c35371948.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c35371948.lua) | 60 |
| Ostinato | `9113513` | [Scripts/c9113513.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c9113513.lua) | 60 |
| ...and 396 more |  |  |  |

## Script Examples

### Artmage Non-Finito (`74631897`)

Source: [Scripts/c74631897.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c74631897.lua)

```lua
		if tc2 then
			tc2:RegisterFlagEffect(id+o,RESET_EVENT+RESETS_STANDARD,0,1)
			local sg=Group.FromCards(tc,tc2)
			sg:KeepAlive()
			e:SetLabelObject(sg)
```

### Pendulum Evolution (`55795155`)

Source: [Scripts/c55795155.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c55795155.lua)

```lua
	local sg=Group.CreateGroup()
	sg:Merge(g)
	Duel.HintSelection(Group.FromCards(lpz))
	Duel.HintSelection(Group.FromCards(rpz))
	Duel.RaiseEvent(sg,EVENT_SPSUMMON_SUCCESS_G_P,e,REASON_EFFECT,tp,tp,0)
```

### Astrograph Sorcerer (`76794549`)

Source: [Scripts/c76794549.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c76794549.lua)

```lua
end
function c76794549.hngoal(g,e,tp,c)
	local sg=Group.FromCards(c)
	sg:Merge(g)
	return Duel.IsExistingMatchingCard(c76794549.hnfilter,tp,LOCATION_EXTRA,0,1,nil,e,tp,sg)
```
