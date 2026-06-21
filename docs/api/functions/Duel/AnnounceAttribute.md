# Duel.AnnounceAttribute

## Signature

```lua
Duel.AnnounceAttribute(int player, int count, int available) -> int
```

## Description

Let the player player declare count attributes from the optional attribute
Available is the combined value of all optional attributes

## Parameters

- `player` `int`
- `count` `int`
- `available` `int`

## Returns

- `int`

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:5030`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **53** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer) with `Duel.AnnounceAttribute`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Surprise Fusion](/examples/cards/35167375) | `35167375` | [Scripts/c35167375.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c35167375.lua) | 73 |
| Plunder Patrollship Jord | `85969517` | [Scripts/c85969517.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c85969517.lua) | 58 |
| Invoked Transcendence Aeon | `33166263` | [Scripts/c33166263.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c33166263.lua) | 55 |
| Nephe Shaddoll Fusion | `60226558` | [Scripts/c60226558.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c60226558.lua) | 55 |
| Eidos the Underworld Monarch | `31596518` | [Scripts/c31596518.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c31596518.lua) | 49 |
| Plunder Patroll Booty | `20426176` | [Scripts/c20426176.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c20426176.lua) | 47 |
| Theorealize | `48739627` | [Scripts/c48739627.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c48739627.lua) | 47 |
| Spiritual Art Familiars | `45538320` | [Scripts/c45538320.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c45538320.lua) | 46 |
| Archnemeses Protos | `6728559` | [Scripts/c6728559.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c6728559.lua) | 46 |
| Strike of the Monarchs | `5795980` | [Scripts/c5795980.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c5795980.lua) | 46 |
| Ancient Warriors Saga - Deception and Betrayal | `45115956` | [Scripts/c45115956.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c45115956.lua) | 45 |
| Crowley, the Magistus of Grimoires | `9505425` | [Scripts/c9505425.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c9505425.lua) | 45 |
| Shipping Archfiend | `57256127` | [Scripts/c57256127.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c57256127.lua) | 45 |
| Dark Infant @Ignister | `74567889` | [Scripts/c74567889.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c74567889.lua) | 45 |
| Dipsea Fiend | `66472129` | [Scripts/c66472129.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c66472129.lua) | 44 |
| Xyz Poseidon Splash | `16938770` | [Scripts/c16938770.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c16938770.lua) | 41 |
| Elementsaber Aina | `83032858` | [Scripts/c83032858.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c83032858.lua) | 39 |
| Elementsaber Nalu | `46425662` | [Scripts/c46425662.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c46425662.lua) | 38 |
| Elementsaber Molehu | `45702014` | [Scripts/c45702014.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c45702014.lua) | 38 |
| Ancient Warriors Saga - Sun-Liu Alliance | `58116537` | [Scripts/c58116537.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c58116537.lua) | 37 |
| You and A.I. | `32056070` | [Scripts/c32056070.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c32056070.lua) | 37 |
| Tualatin | `27769400` | [Scripts/c27769400.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c27769400.lua) | 37 |
| Maple Maiden | `73104892` | [Scripts/c73104892.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c73104892.lua) | 36 |
| Herald of the Abyss | `94016752` | [Scripts/c94016752.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c94016752.lua) | 36 |
| ...and 29 more |  |  |  |

## Script Examples

### Surprise Fusion (`35167375`)

Source: [Scripts/c35167375.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c35167375.lua)

```lua
	Duel.Hint(HINT_SELECTMSG,tp,HINTMSG_ATTRIBUTE)
	if RACE_ALL&~tc:GetRace()==0 or race==tc:GetRace() then
		att=Duel.AnnounceAttribute(tp,1,ATTRIBUTE_ALL&~tc:GetAttribute())
	else
		att=Duel.AnnounceAttribute(tp,1,ATTRIBUTE_ALL)
```

### Plunder Patrollship Jord (`85969517`)

Source: [Scripts/c85969517.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c85969517.lua)

```lua
	end
	Duel.Hint(HINT_SELECTMSG,tp,HINTMSG_ATTRIBUTE)
	local attr=Duel.AnnounceAttribute(tp,1,s.GetLegalAttributesOnly(tp))
	Duel.SetTargetParam(attr)
	Duel.SetOperationInfo(0,CATEGORY_TODECK,c,1,0,0)
```

### Invoked Transcendence Aeon (`33166263`)

Source: [Scripts/c33166263.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c33166263.lua)

```lua
	end
	Duel.Hint(HINT_SELECTMSG,tp,HINTMSG_ATTRIBUTE)
	local ratt=Duel.AnnounceAttribute(tp,1,att)
	e:SetLabel(ratt)
end
```
