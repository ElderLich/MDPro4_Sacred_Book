# Card.IsAbleToExtraAsCost

## Signature

```lua
Card.IsAbleToExtraAsCost(Card c) -> bool
```

## Description

Checks whether c can be returned to the Extra Deck as a cost.

## Parameters

- `c` `Card`

## Returns

- `bool`

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3594`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **15** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer) with `Card.IsAbleToExtraAsCost`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Vidolium the Unstable Power Patron of Unity](/examples/cards/70488851) | `70488851` | [Scripts/c70488851.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c70488851.lua) | 1 |
| Gladiator Beast Gaiodiaz | `90957527` | [Scripts/c90957527.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c90957527.lua) | 1 |
| Ritual Beast Ulti-Kimunfalcos | `58811192` | [Scripts/c58811192.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c58811192.lua) | 1 |
| Gladiator Beast Gyzarus | `48156348` | [Scripts/c48156348.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c48156348.lua) | 1 |
| Palm Ryzeal | `61116514` | [Scripts/c61116514.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c61116514.lua) | 1 |
| Gladiator Beast Andabata | `3779662` | [Scripts/c3779662.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c3779662.lua) | 1 |
| Gladiator Beast Domitianus | `33652635` | [Scripts/c33652635.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c33652635.lua) | 1 |
| Gladiator Beast Dragases | `62000467` | [Scripts/c62000467.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c62000467.lua) | 1 |
| Supreme King Dragon Dark Rebellion | `42160203` | [Scripts/c42160203.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c42160203.lua) | 1 |
| Gladiator Beast Nerokius | `29357956` | [Scripts/c29357956.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c29357956.lua) | 1 |
| Variety Comes Out | `65196094` | [Scripts/c65196094.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c65196094.lua) | 1 |
| XYZ Combine | `95471006` | [Scripts/c95471006.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c95471006.lua) | 1 |
| Dimension Explosion | `1896112` | [Scripts/c1896112.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c1896112.lua) | 1 |
| Limit Overdrive | `35014241` | [Scripts/c35014241.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c35014241.lua) | 2 |
| Legacy of a HERO | `25614410` | [Scripts/c25614410.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c25614410.lua) | 1 |

## Script Examples

### Vidolium the Unstable Power Patron of Unity (`70488851`)

Source: [Scripts/c70488851.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c70488851.lua)

```lua
end
function s.spfilter2(c)
	return c:IsFaceupEx() and c:IsType(TYPE_FUSION+TYPE_SYNCHRO+TYPE_XYZ) and c:IsAbleToExtraAsCost()
end
function s.gcheck(g,ec,tp)
```

### Gladiator Beast Gaiodiaz (`90957527`)

Source: [Scripts/c90957527.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c90957527.lua)

```lua
function c90957527.spcost(e,tp,eg,ep,ev,re,r,rp,chk)
	local c=e:GetHandler()
	if chk==0 then return c:IsAbleToExtraAsCost() end
	Duel.SendtoDeck(c,nil,SEQ_DECKTOP,REASON_COST)
end
```

### Ritual Beast Ulti-Kimunfalcos (`58811192`)

Source: [Scripts/c58811192.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c58811192.lua)

```lua
function c58811192.spcost(e,tp,eg,ep,ev,re,r,rp,chk)
	local c=e:GetHandler()
	if chk==0 then return c:IsAbleToExtraAsCost() end
	Duel.SendtoDeck(c,nil,SEQ_DECKTOP,REASON_COST)
end
```
