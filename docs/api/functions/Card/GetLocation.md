# Card.GetLocation

## Signature

```lua
Card.GetLocation(Card c) -> int
```

## Description

Returns the current position of c

## Parameters

- `c` `Card`

## Returns

- `int`

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3466`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **23** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer) with `Card.GetLocation`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Bujinki Ahashima](/examples/cards/71095768) | `71095768` | [Scripts/c71095768.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c71095768.lua) | 62 |
| Daigusto Laplampilica | `76937326` | [Scripts/c76937326.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c76937326.lua) | 52 |
| Raidraptor - Rising Rebellion Falcon | `71222868` | [Scripts/c71222868.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c71222868.lua) | 52 |
| Goblin Biker Grand Crisis | `15094540` | [Scripts/c15094540.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c15094540.lua) | 51 |
| Amazement Abomination Arlekino | `31600845` | [Scripts/c31600845.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c31600845.lua) | 49 |
| EN - Engage Neo Space | `80170678` | [Scripts/c80170678.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c80170678.lua) | 46 |
| Ninjitsu Art Notebook of Mystery | `95545183` | [Scripts/c95545183.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c95545183.lua) | 45 |
| Gold Pride - Nytro Head | `59900655` | [Scripts/c59900655.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c59900655.lua) | 44 |
| Rage Rose Witch | `33955120` | [Scripts/c33955120.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c33955120.lua) | 43 |
| Infinite Light | `72883039` | [Scripts/c72883039.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c72883039.lua) | 43 |
| Cybernetic Horizon | `63031396` | [Scripts/c63031396.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c63031396.lua) | 43 |
| Mathmech Division | `89743495` | [Scripts/c89743495.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c89743495.lua) | 43 |
| T.G. Trident Launcher | `50750868` | [Scripts/c50750868.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c50750868.lua) | 42 |
| Springans Ship - Exblowrer | `62941499` | [Scripts/c62941499.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c62941499.lua) | 42 |
| Parametalfoes Fusion | `58549532` | [Scripts/c58549532.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c58549532.lua) | 42 |
| Spell Gear | `313513` | [Scripts/c313513.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c313513.lua) | 40 |
| The Bystial Aluber | `45005708` | [Scripts/c45005708.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c45005708.lua) | 39 |
| Super Soldier Synthesis | `45948430` | [Scripts/c45948430.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c45948430.lua) | 38 |
| Traptrix Genlisea | `88078306` | [Scripts/c88078306.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c88078306.lua) | 35 |
| Theinen the Great Sphinx | `87997872` | [Scripts/c87997872.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c87997872.lua) | 33 |
| Mikazukinoyaiba, the Moon Fang Dragon | `85753549` | [Scripts/c85753549.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c85753549.lua) | 33 |
| Dances with Beasts | `33298291` | [Scripts/c33298291.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c33298291.lua) | 30 |
| Oh my Trap Hole! | `10529441` | [Scripts/c10529441.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c10529441.lua) | 30 |

## Script Examples

### Bujinki Ahashima (`71095768`)

Source: [Scripts/c71095768.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c71095768.lua)

```lua
end
function c71095768.fselect(g,tp)
	return g:GetClassCount(Card.GetLocation)==g:GetCount() and g:GetClassCount(Card.GetLevel)==1
		and Duel.IsExistingMatchingCard(Card.IsXyzSummonable,tp,LOCATION_EXTRA,0,1,nil,g,2,2)
end
```

### Daigusto Laplampilica (`76937326`)

Source: [Scripts/c76937326.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c76937326.lua)

```lua
end
function c76937326.fselect(g,tp)
	return g:GetClassCount(Card.GetLocation)==#g and Duel.IsExistingMatchingCard(c76937326.synfilter,tp,LOCATION_EXTRA,0,1,nil,g)
end
function c76937326.synfilter(c,g)
```

### Raidraptor - Rising Rebellion Falcon (`71222868`)

Source: [Scripts/c71222868.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c71222868.lua)

```lua
end
function s.damval1(c)
	if c:GetLocation()~=LOCATION_MZONE then return end
	return math.max(0,c:GetTextAttack())
end
```
