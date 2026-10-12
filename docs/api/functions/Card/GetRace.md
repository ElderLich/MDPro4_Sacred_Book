# Card.GetRace

## Signature

```lua
Card.GetRace(Card c) -> int
```

## Description

Returns c's current Race value. Cards with multiple Races can return a bitmask containing more than one Race.

## Parameters

- `c` `Card`

## Returns

- `int`

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3487`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **153** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=standard&mode=code&q=Card.GetRace) with `Card.GetRace`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Surprise Fusion](/examples/cards/35167375) | `35167375` | [Scripts/c35167375.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c35167375.lua) | 5 |
| [Yomagna the Fire Phantom](/examples/cards/17350692) | `17350692` | [Scripts/c17350692.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c17350692.lua) | 2 |
| [Favorite HERO Flame Wingman](/examples/cards/13243124) | `13243124` | [Scripts/c13243124.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c13243124.lua) | 1 |
| [Spirit Illusion](/examples/cards/71939275) | `71939275` | [Scripts/c71939275.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c71939275.lua) | 3 |
| [Resurgam Xyz](/examples/cards/49082032) | `49082032` | [Scripts/c49082032.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c49082032.lua) | 2 |
| [D/D Count Surveyor](/examples/cards/5997110) | `5997110` | [Scripts/c5997110.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c5997110.lua) | 1 |
| [A Bao A Qu, the Lightless Shadow](/examples/cards/4731783) | `4731783` | [Scripts/c4731783.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c4731783.lua) | 2 |
| [Sonic Tracker](/examples/cards/17888577) | `17888577` | [Scripts/c17888577.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c17888577.lua) | 2 |
| Duel Link Dragon, the Duel Dragon | `60025883` | [Scripts/c60025883.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c60025883.lua) | 1 |
| Super Duper Polymerization | `44886582` | [Scripts/c44886582.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c44886582.lua) | 1 |
| Echelon of the Fire Kings | `38798785` | [Scripts/c38798785.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c38798785.lua) | 5 |
| Rank-Up-Magic Astral Force | `45950291` | [Scripts/c45950291.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c45950291.lua) | 2 |
| Number 101: Silent Honor ARK - Soul Asylum | `2419596` | [Scripts/c2419596.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c2419596.lua) | 1 |
| Seven Stars Slash - Army Annihilator Hagun | `65114115` | [Scripts/c65114115.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c65114115.lua) | 2 |
| Abyss-steam | `63941169` | [Scripts/c63941169.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c63941169.lua) | 1 |
| Cyberse Contract Witch | `37458564` | [Scripts/c37458564.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c37458564.lua) | 2 |
| Rescue Hedgehog | `99742859` | [Scripts/c99742859.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c99742859.lua) | 1 |
| Rank-Up-Magic Numeron Force | `48333324` | [Scripts/c48333324.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c48333324.lua) | 2 |
| Max Metalmorph | `89812483` | [Scripts/c89812483.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c89812483.lua) | 2 |
| Tri-Brigade Rugal the Silver Sheller | `52331012` | [Scripts/c52331012.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c52331012.lua) | 2 |
| Fata Dragna | `41763141` | [Scripts/c41763141.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c41763141.lua) | 1 |
| Primite Imperial Dragon | `81418467` | [Scripts/c81418467.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c81418467.lua) | 1 |
| First Penguin | `12975671` | [Scripts/c12975671.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c12975671.lua) | 2 |
| Stellarnova Binding | `69678646` | [Scripts/c69678646.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c69678646.lua) | 1 |
| ...and 129 more |  |  |  |

## Script Examples

### Surprise Fusion (`35167375`)

Source: [Scripts/c35167375.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c35167375.lua)

```lua
end
function s.rafilter(c)
	return c:IsFaceup() and ((RACE_ALL&~c:GetRace())~=0 or (ATTRIBUTE_ALL&~c:GetAttribute())~=0)
end
function s.target(e,tp,eg,ep,ev,re,r,rp,chk,chkc)
```

### Yomagna the Fire Phantom (`17350692`)

Source: [Scripts/c17350692.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c17350692.lua)

```lua
	if chk==0 then return true end
	Duel.Hint(HINT_SELECTMSG,tp,HINTMSG_RACE)
	local race=Duel.AnnounceRace(tp,1,RACE_ALL&~e:GetHandler():GetRace())
	e:SetLabel(race)
end
```

### Favorite HERO Flame Wingman (`13243124`)

Source: [Scripts/c13243124.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c13243124.lua)

```lua
function s.ffilter(c,fc,sub,mg,sg)
	return not sg or sg:FilterCount(aux.TRUE,c)==0
		or (sg:IsExists(Card.IsRace,1,c,c:GetRace())
			and not sg:IsExists(Card.IsFusionAttribute,1,c,c:GetFusionAttribute()))
end
```
