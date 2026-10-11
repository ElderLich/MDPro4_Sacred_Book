# Card.IsLevel

## Signature

```lua
Card.IsLevel(Card c, int level1, [int level2], [... int]) -> bool
```

## Description

Checks whether c's current Level equals any supplied level value.
nil level arguments are ignored.

## Parameters

- `c` `Card`
- `level1` `int`
- `level2` `int` optional
- `...` `int` optional

## Returns

- `bool`

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3542`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **695** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=standard&mode=code&q=Card.IsLevel) with `Card.IsLevel`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Lady's Dragonmaid](/examples/cards/48658295) | `48658295` | [Scripts/c48658295.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c48658295.lua) | 1 |
| [Magnet Bonding](/examples/cards/65514302) | `65514302` | [Scripts/c65514302.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c65514302.lua) | 1 |
| [Dark End Evaporation Dragon](/examples/cards/62002838) | `62002838` | [Scripts/c62002838.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c62002838.lua) | 1 |
| [Odd-Eyes Arcray Dragon](/examples/cards/6218704) | `6218704` | [Scripts/c6218704.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c6218704.lua) | 1 |
| [Ursarctic Polar Star](/examples/cards/62714453) | `62714453` | [Scripts/c62714453.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c62714453.lua) | 2 |
| [Light End Sublimation Dragon](/examples/cards/35614780) | `35614780` | [Scripts/c35614780.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c35614780.lua) | 1 |
| Flower Cardian Willow with Calligrapher | `89818984` | [Scripts/c89818984.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c89818984.lua) | 1 |
| Supreme King Dragon Lightwurm | `41908872` | [Scripts/c41908872.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c41908872.lua) | 1 |
| Frightfur Meister | `77522571` | [Scripts/c77522571.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c77522571.lua) | 2 |
| Duel Link Dragon, the Duel Dragon | `60025883` | [Scripts/c60025883.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c60025883.lua) | 2 |
| Isolde, Two Tales of the Noble Knights | `59934749` | [Scripts/c59934749.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c59934749.lua) | 1 |
| Super Duper Polymerization | `44886582` | [Scripts/c44886582.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c44886582.lua) | 1 |
| Ecclesia and the Dark Dragon | `78397661` | [Scripts/c78397661.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c78397661.lua) | 1 |
| Mixeroid | `71340250` | [Scripts/c71340250.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c71340250.lua) | 1 |
| Cyberse Reminder | `56337500` | [Scripts/c56337500.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c56337500.lua) | 1 |
| Number 101: Silent Honor ARK - Soul Asylum | `2419596` | [Scripts/c2419596.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c2419596.lua) | 2 |
| XYZ-Hyper Dragon Cannon | `75748977` | [Scripts/c75748977.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c75748977.lua) | 1 |
| Awakening of the Sacred Beasts | `53701259` | [Scripts/c53701259.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c53701259.lua) | 1 |
| Seven Stars Slash - Army Annihilator Hagun | `65114115` | [Scripts/c65114115.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c65114115.lua) | 1 |
| Ursarctic Quint Charge | `15758127` | [Scripts/c15758127.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c15758127.lua) | 1 |
| Emperor Charles the Great | `97864322` | [Scripts/c97864322.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c97864322.lua) | 1 |
| Miscellaneousaurus | `38572779` | [Scripts/c38572779.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c38572779.lua) | 1 |
| World Legacy Monstrosity | `14604710` | [Scripts/c14604710.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c14604710.lua) | 3 |
| Malefic Paradigm Dragon | `16958382` | [Scripts/c16958382.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c16958382.lua) | 1 |
| ...and 671 more |  |  |  |

## Script Examples

### Lady's Dragonmaid (`48658295`)

Source: [Scripts/c48658295.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c48658295.lua)

```lua
	if not c:IsFusionSetCard(0x133) then return false end
	if not sg then return true end
	return not sg:IsExists(Card.IsLevel,1,c,c:GetLevel())
		and sg:IsExists(Card.IsFusionAttribute,1,c,c:GetFusionAttribute())
end
```

### Magnet Bonding (`65514302`)

Source: [Scripts/c65514302.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c65514302.lua)

```lua
end
function s.thfilter2(c)
	return c:IsSetCard(0xe9) and c:IsLevel(8) and c:IsAbleToHand()
end
function s.filter1(c,e)
```

### Dark End Evaporation Dragon (`62002838`)

Source: [Scripts/c62002838.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c62002838.lua)

```lua
s.fusion_effect=true
function s.costfilter(c)
	return c:IsRace(RACE_DRAGON) and c:IsLevel(8) and c:IsAbleToRemoveAsCost()
end
function s.spcost(e,tp,eg,ep,ev,re,r,rp,chk)
```
