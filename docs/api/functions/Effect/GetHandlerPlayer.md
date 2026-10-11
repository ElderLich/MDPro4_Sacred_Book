# Effect.GetHandlerPlayer

## Signature

```lua
Effect.GetHandlerPlayer(Effect e) -> int
```

## Description

Returns the current controller of e's handler.

## Parameters

- `e` `Effect`

## Returns

- `int`

## Source

- `D:\Programs\GitHub\ygopro-core\libeffect.cpp:649`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **974** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=standard&mode=code&q=Effect.GetHandlerPlayer) with `Effect.GetHandlerPlayer`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Melffy Playtime Surprise](/examples/cards/58036097) | `58036097` | [Scripts/c58036097.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c58036097.lua) | 1 |
| [El Shaddoll Apkallone](/examples/cards/50907446) | `50907446` | [Scripts/c50907446.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c50907446.lua) | 2 |
| [Am Duazenet](/examples/cards/45151304) | `45151304` | [Scripts/c45151304.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c45151304.lua) | 1 |
| [Hecahands Tartaros](/examples/cards/57809669) | `57809669` | [Scripts/c57809669.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c57809669.lua) | 1 |
| [Prank-Kids Weather Washer](/examples/cards/44509529) | `44509529` | [Scripts/c44509529.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c44509529.lua) | 1 |
| [Odd-Eyes Revolution Dragon](/examples/cards/16306932) | `16306932` | [Scripts/c16306932.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c16306932.lua) | 1 |
| [Converging Wishes](/examples/cards/20007374) | `20007374` | [Scripts/c20007374.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c20007374.lua) | 1 |
| [Graydle Split](/examples/cards/75361204) | `75361204` | [Scripts/c75361204.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c75361204.lua) | 1 |
| [Enneacraft - Aiza.LEON](/examples/cards/82359538) | `82359538` | [Scripts/c82359538.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c82359538.lua) | 1 |
| [Ultimate Crystal Rainbow Dragon Overdrive](/examples/cards/84544192) | `84544192` | [Scripts/c84544192.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c84544192.lua) | 1 |
| [Shooting Majestic Star Dragon](/examples/cards/40939228) | `40939228` | [Scripts/c40939228.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c40939228.lua) | 1 |
| [Camelot, Realm of Noble Knights and Noble Arms](/examples/cards/15635751) | `15635751` | [Scripts/c15635751.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c15635751.lua) | 1 |
| [Cerynemesia, Mystical Beast of the Forest](/examples/cards/43632709) | `43632709` | [Scripts/c43632709.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c43632709.lua) | 2 |
| El Shaddoll Meshachrer | `32467459` | [Scripts/c32467459.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c32467459.lua) | 4 |
| Fiendsmith Kyrie | `26434972` | [Scripts/c26434972.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c26434972.lua) | 1 |
| Artmage Pact -Awakening- | `23599634` | [Scripts/c23599634.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c23599634.lua) | 1 |
| Gravity Balance | `37930737` | [Scripts/c37930737.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c37930737.lua) | 1 |
| Trirealm Rift Judgment | `65195679` | [Scripts/c65195679.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c65195679.lua) | 1 |
| Chaos Magical Hats | `2372506` | [Scripts/c2372506.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c2372506.lua) | 1 |
| Duel Link Dragon, the Duel Dragon | `60025883` | [Scripts/c60025883.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c60025883.lua) | 1 |
| Ancient Gear Duel | `53541822` | [Scripts/c53541822.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c53541822.lua) | 1 |
| Alba System Dogmatikalamity | `93053159` | [Scripts/c93053159.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c93053159.lua) | 3 |
| Dragon Master Magia | `12381100` | [Scripts/c12381100.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c12381100.lua) | 1 |
| Awakening of the Sacred Beasts | `53701259` | [Scripts/c53701259.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c53701259.lua) | 2 |
| ...and 950 more |  |  |  |

## Script Examples

### Melffy Playtime Surprise (`58036097`)

Source: [Scripts/c58036097.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c58036097.lua)

```lua
end
function s.efilter(e,re)
	return e:GetHandlerPlayer()~=re:GetOwnerPlayer() and re:IsActivated()
end
```

### El Shaddoll Apkallone (`50907446`)

Source: [Scripts/c50907446.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c50907446.lua)

```lua
end
function c50907446.FShaddollCondition(e,g,gc,chkf)
	if g==nil then return aux.MustMaterialCheck(nil,e:GetHandlerPlayer(),EFFECT_MUST_BE_FMATERIAL) end
	local c=e:GetHandler()
	local mg=g:Filter(c50907446.FShaddollFilter,nil,c)
```

### Am Duazenet (`45151304`)

Source: [Scripts/c45151304.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c45151304.lua)

```lua
end
function s.repval(e,c)
	return s.repfilter(c,e:GetHandlerPlayer())
end
function s.repop(e,tp,eg,ep,ev,re,r,rp)
```
