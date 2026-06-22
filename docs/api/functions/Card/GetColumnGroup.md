# Card.GetColumnGroup

## Signature

```lua
Card.GetColumnGroup(Card c) -> Group
```

## Description

Returns a Group containing cards in the same column as c.
This MDPro3/YGOPro binding only takes c. It uses c's current on-field column, including related Monster Zones, Spell & Trap Zones, and Extra Monster Zone column relationships; if c is not on the field, the returned Group is empty.

## Parameters

- `c` `Card`

## Returns

- `Group`

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3427`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **46** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer) with `Card.GetColumnGroup`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Vanquish Soul Trinity Burst | `53330789` | [Scripts/c53330789.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c53330789.lua) | 58 |
| Sprind the Irondash Dragon | `1906812` | [Scripts/c1906812.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c1906812.lua) | 48 |
| Wattkingdom | `41790641` | [Scripts/c41790641.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c41790641.lua) | 46 |
| S-Force Signus | `19951423` | [Scripts/c19951423.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c19951423.lua) | 46 |
| Parallel Panzer | `93394164` | [Scripts/c93394164.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c93394164.lua) | 46 |
| S-Force Nightchaser | `20515672` | [Scripts/c20515672.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c20515672.lua) | 45 |
| Solving for Pendulum | `5208118` | [Scripts/c5208118.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c5208118.lua) | 44 |
| S-Force Rappa Chiyomaru | `22180094` | [Scripts/c22180094.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c22180094.lua) | 44 |
| Shelrokket Dragon | `5087128` | [Scripts/c5087128.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c5087128.lua) | 43 |
| Vanquish Soul Razen | `29302858` | [Scripts/c29302858.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c29302858.lua) | 43 |
| Vanquish Soul Pantera | `66401502` | [Scripts/c66401502.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c66401502.lua) | 42 |
| Junora the Power Patron of Tuning | `5914858` | [Scripts/c5914858.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c5914858.lua) | 41 |
| Thunder Ball | `84813516` | [Scripts/c84813516.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c84813516.lua) | 41 |
| Prey of the Jirai Gumo | `33055499` | [Scripts/c33055499.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c33055499.lua) | 41 |
| S-Force Lapcewell | `27383719` | [Scripts/c27383719.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c27383719.lua) | 41 |
| Mekk-Knight Red Moon | `56809158` | [Scripts/c56809158.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c56809158.lua) | 41 |
| Bomber Place | `71750854` | [Scripts/c71750854.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c71750854.lua) | 40 |
| Mekk-Knight Spectrum Supreme | `38502358` | [Scripts/c38502358.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c38502358.lua) | 40 |
| Girsu, the Orcust Mekk-Knight | `69811710` | [Scripts/c69811710.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c69811710.lua) | 40 |
| S-Force Orrafist | `95974848` | [Scripts/c95974848.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c95974848.lua) | 40 |
| Mekk-Knight Blue Sky | `20537097` | [Scripts/c20537097.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c20537097.lua) | 39 |
| Metalrokket Dragon | `32472237` | [Scripts/c32472237.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c32472237.lua) | 38 |
| Mekk-Knight Green Horizon | `66022706` | [Scripts/c66022706.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c66022706.lua) | 38 |
| Han-Shi Kyudo Spirit | `53270092` | [Scripts/c53270092.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c53270092.lua) | 36 |
| ...and 22 more |  |  |  |

## Script Examples

### Vanquish Soul Trinity Burst (`53330789`)

Source: [Scripts/c53330789.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c53330789.lua)

```lua
		Duel.Hint(HINT_SELECTMSG,tp,HINTMSG_SPSUMMON)
		local tg=g:SelectSubGroup(tp,aux.dncheck,false,1,max)
		local rg=tc:GetColumnGroup():Filter(Card.IsControler,nil,1-tp)
		local fid=c:GetFieldID()
		local sg=Group.CreateGroup()
```

### Sprind the Irondash Dragon (`1906812`)

Source: [Scripts/c1906812.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c1906812.lua)

```lua
	Duel.MoveSequence(c,seq)
	if c:GetSequence()==seq then
		local g=c:GetColumnGroup():Filter(Card.IsFaceup,nil)
		if g:GetCount()>0 and Duel.SelectYesNo(tp,aux.Stringid(1906812,2)) then
			Duel.BreakEffect()
```

### Wattkingdom (`41790641`)

Source: [Scripts/c41790641.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c41790641.lua)

```lua
		and re:GetCode()~=EVENT_SPSUMMON_SUCCESS then return end
	local rc=re:GetHandler()
	local rg=rc:GetColumnGroup()
	local p=e:GetHandlerPlayer()
	return rc:IsControler(1-p) and rg:IsContains(e:GetHandler()) or rg:IsExists(s.lfilter,1,nil,p)
```
