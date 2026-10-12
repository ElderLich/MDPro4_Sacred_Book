# Group.RemoveCard

## Signature

```lua
Group.RemoveCard(Group g, Card c) -> void
```

## Description

Removes c from g. The function mutates g unless g is read-only and returns no Lua value.

## Parameters

- `g` `Group`
- `c` `Card`

## Source

- `D:\Programs\GitHub\ygopro-core\libgroup.cpp:907`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **116** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=standard&mode=code&q=Group.RemoveCard) with `Group.RemoveCard`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Ashtraja Susanoo](/examples/cards/17020474) | `17020474` | [Scripts/c17020474.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c17020474.lua) | 1 |
| [Deftero Enneacraft - "alazoneIA"](/examples/cards/92171126) | `92171126` | [Scripts/c92171126.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c92171126.lua) | 1 |
| [El Shaddoll Apkallone](/examples/cards/50907446) | `50907446` | [Scripts/c50907446.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c50907446.lua) | 1 |
| [Meteoroa Drytron](/examples/cards/24166324) | `24166324` | [Scripts/c24166324.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c24166324.lua) | 2 |
| [Gem-Knight Dispersion](/examples/cards/24220368) | `24220368` | [Scripts/c24220368.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c24220368.lua) | 1 |
| [Prank-Kids Weather Washer](/examples/cards/44509529) | `44509529` | [Scripts/c44509529.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c44509529.lua) | 1 |
| [GMX 55th Experiment Report](/examples/cards/38984832) | `38984832` | [Scripts/c38984832.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c38984832.lua) | 1 |
| [PSY-Framelord Omega](/examples/cards/74586817) | `74586817` | [Scripts/c74586817.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c74586817.lua) | 1 |
| [Flower Cardian Peony with Butterfly](/examples/cards/57261568) | `57261568` | [Scripts/c57261568.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c57261568.lua) | 1 |
| [PSY-Framelord Zeta](/examples/cards/37192109) | `37192109` | [Scripts/c37192109.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c37192109.lua) | 1 |
| [Sonic Tracker](/examples/cards/17888577) | `17888577` | [Scripts/c17888577.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c17888577.lua) | 1 |
| Flower Cardian Willow with Calligrapher | `89818984` | [Scripts/c89818984.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c89818984.lua) | 1 |
| Aroma Blend | `25861589` | [Scripts/c25861589.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c25861589.lua) | 1 |
| Prank-Kids Rocket Ride | `18514525` | [Scripts/c18514525.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c18514525.lua) | 1 |
| Gishki Nekromirror | `36982581` | [Scripts/c36982581.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c36982581.lua) | 1 |
| Magical Hats | `81210420` | [Scripts/c81210420.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c81210420.lua) | 1 |
| Secrets of Dark Magic | `59514116` | [Scripts/c59514116.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c59514116.lua) | 1 |
| Meteonis Drytron | `22398665` | [Scripts/c22398665.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c22398665.lua) | 2 |
| Alba System Dogmatikalamity | `93053159` | [Scripts/c93053159.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c93053159.lua) | 1 |
| Prank-Kids Bow-Wow-Bark | `43886072` | [Scripts/c43886072.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c43886072.lua) | 1 |
| Triamid Pulse | `96100333` | [Scripts/c96100333.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c96100333.lua) | 6 |
| Magikey Duo | `51510279` | [Scripts/c51510279.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c51510279.lua) | 2 |
| Blessing of the Voiceless Voice | `39114494` | [Scripts/c39114494.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c39114494.lua) | 1 |
| Flower Cardian Moonflowerviewing | `33541430` | [Scripts/c33541430.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c33541430.lua) | 1 |
| ...and 92 more |  |  |  |

## Script Examples

### Ashtraja Susanoo (`17020474`)

Source: [Scripts/c17020474.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c17020474.lua)

```lua
				end
				if selg:IsContains(tc) then
					selg:RemoveCard(tc)
				else
					selg:AddCard(tc)
```

### Deftero Enneacraft - "alazoneIA" (`92171126`)

Source: [Scripts/c92171126.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c92171126.lua)

```lua
		local og=Duel.GetOperatedGroup()
		if c:GetOriginalCode()~=id then
			og:RemoveCard(c)
		end
		local oc=og:GetFirst()
```

### El Shaddoll Apkallone (`50907446`)

Source: [Scripts/c50907446.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c50907446.lua)

```lua
	if gc then
		g=Group.FromCards(gc)
		mg:RemoveCard(gc)
	else
		Duel.Hint(HINT_SELECTMSG,tp,HINTMSG_FMATERIAL)
```
