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

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3646`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **20** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=standard&mode=code&q=Card.IsAbleToExtraAsCost) with `Card.IsAbleToExtraAsCost`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Yomagna the Fire Phantom](/examples/cards/17350692) | `17350692` | [Scripts/c17350692.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c17350692.lua) | 1 |
| [Vidolium the Unstable Power Patron of Unity](/examples/cards/70488851) | `70488851` | [Scripts/c70488851.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c70488851.lua) | 1 |
| Gladiator Beast Gaiodiaz | `90957527` | [Scripts/c90957527.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c90957527.lua) | 1 |
| Ritual Beast Ulti-Kimunfalcos | `58811192` | [Scripts/c58811192.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c58811192.lua) | 1 |
| Gladiator Beast Gyzarus | `48156348` | [Scripts/c48156348.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c48156348.lua) | 1 |
| Yoa the Plague Deity Ashtra | `1710647` | [Scripts/c1710647.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c1710647.lua) | 1 |
| Palm Ryzeal | `61116514` | [Scripts/c61116514.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c61116514.lua) | 1 |
| Gladiator Beast Andabata | `3779662` | [Scripts/c3779662.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c3779662.lua) | 1 |
| Kuzuha the Bewitching Deity Ashtra | `65325949` | [Scripts/c65325949.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c65325949.lua) | 1 |
| Akasuna the Battle Ashtra | `38331244` | [Scripts/c38331244.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c38331244.lua) | 1 |
| Gladiator Beast Domitianus | `33652635` | [Scripts/c33652635.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c33652635.lua) | 1 |
| Mikumari the Sealing Deity Ashtra | `38114652` | [Scripts/c38114652.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c38114652.lua) | 1 |
| Gladiator Beast Dragases | `62000467` | [Scripts/c62000467.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c62000467.lua) | 1 |
| Supreme King Dragon Dark Rebellion | `42160203` | [Scripts/c42160203.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c42160203.lua) | 1 |
| Gladiator Beast Nerokius | `29357956` | [Scripts/c29357956.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c29357956.lua) | 1 |
| Variety Comes Out | `65196094` | [Scripts/c65196094.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c65196094.lua) | 1 |
| XYZ Combine | `95471006` | [Scripts/c95471006.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c95471006.lua) | 1 |
| Dimension Explosion | `1896112` | [Scripts/c1896112.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c1896112.lua) | 1 |
| Limit Overdrive | `35014241` | [Scripts/c35014241.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c35014241.lua) | 2 |
| Legacy of a HERO | `25614410` | [Scripts/c25614410.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c25614410.lua) | 1 |

## Script Examples

### Yomagna the Fire Phantom (`17350692`)

Source: [Scripts/c17350692.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c17350692.lua)

```lua
end
function s.sprfilter(c)
	return c:IsAbleToDeckAsCost() or c:IsAbleToExtraAsCost()
end
function s.gcheck(g)
```

### Vidolium the Unstable Power Patron of Unity (`70488851`)

Source: [Scripts/c70488851.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c70488851.lua)

```lua
end
function s.spfilter2(c)
	return c:IsFaceupEx() and c:IsType(TYPE_FUSION+TYPE_SYNCHRO+TYPE_XYZ) and c:IsAbleToExtraAsCost()
end
function s.gcheck(g,ec,tp)
```

### Gladiator Beast Gaiodiaz (`90957527`)

Source: [Scripts/c90957527.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c90957527.lua)

```lua
function c90957527.spcost(e,tp,eg,ep,ev,re,r,rp,chk)
	local c=e:GetHandler()
	if chk==0 then return c:IsAbleToExtraAsCost() end
	Duel.SendtoDeck(c,nil,SEQ_DECKTOP,REASON_COST)
end
```
