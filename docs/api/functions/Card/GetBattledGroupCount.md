# Card.GetBattledGroupCount

## Signature

```lua
Card.GetBattledGroupCount(Card c) -> int
```

## Description

Returns the number of cards currently recorded in c's battled-cards set.

## Parameters

- `c` `Card`

## Returns

- `int`

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3533`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **10** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer) with `Card.GetBattledGroupCount`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Ultimate Crystal Rainbow Dragon Overdrive](/examples/cards/84544192) | `84544192` | [Scripts/c84544192.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c84544192.lua) | 62 |
| Arrow of Regulus | `60439482` | [Scripts/c60439482.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c60439482.lua) | 49 |
| Timelord Progenitor Vorpgate | `67508932` | [Scripts/c67508932.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c67508932.lua) | 47 |
| Gladiator Beast Tamer Editor | `30864377` | [Scripts/c30864377.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c30864377.lua) | 44 |
| Heretical Phobos Covos | `76078185` | [Scripts/c76078185.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c76078185.lua) | 41 |
| Archfiend Black Skull Dragon | `45349196` | [Scripts/c45349196.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c45349196.lua) | 40 |
| Phantasm Spiral Wave | `1197847` | [Scripts/c1197847.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c1197847.lua) | 40 |
| Frightfur Kraken | `40636712` | [Scripts/c40636712.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c40636712.lua) | 33 |
| Hi-Five the Sky | `91677585` | [Scripts/c91677585.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c91677585.lua) | 30 |
| Turbo Booster | `60187739` | [Scripts/c60187739.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c60187739.lua) | 29 |

## Script Examples

### Ultimate Crystal Rainbow Dragon Overdrive (`84544192`)

Source: [Scripts/c84544192.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c84544192.lua)

```lua
function s.tdcost(e,tp,eg,ep,ev,re,r,rp,chk)
	local c=e:GetHandler()
	if chk==0 then return c:GetBattledGroupCount()==0 and c:IsReleasable() end
	Duel.Release(c,REASON_COST)
end
```

### Arrow of Regulus (`60439482`)

Source: [Scripts/c60439482.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c60439482.lua)

```lua
end
function s.desfilter(c)
	return c:GetBattledGroupCount()>0
end
function s.target(e,tp,eg,ep,ev,re,r,rp,chk)
```

### Timelord Progenitor Vorpgate (`67508932`)

Source: [Scripts/c67508932.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c67508932.lua)

```lua
function c67508932.rmcond(e,tp,eg,ep,ev,re,r,rp)
	local c=e:GetHandler()
	return aux.dsercon(e,tp,eg,ep,ev,re,r,rp) and c:IsSummonLocation(LOCATION_EXTRA) and c:GetBattledGroupCount()>0
end
function c67508932.rmtg(e,tp,eg,ep,ev,re,r,rp,chk)
```
