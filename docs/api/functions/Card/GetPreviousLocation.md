# Card.GetPreviousLocation

## Signature

```lua
Card.GetPreviousLocation(Card c) -> int
```

## Description

Returns the position before the c position changes

## Parameters

- `c` `Card`

## Returns

- `int`

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3467`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **5** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer) with `Card.GetPreviousLocation`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Chevreuil, Hunting Scout of the Deep Forest | `13023431` | [Scripts/c13023431.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c13023431.lua) | 54 |
| Raidraptor - Rising Rebellion Falcon | `71222868` | [Scripts/c71222868.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c71222868.lua) | 52 |
| Evil HERO Inferno Wing - Backfire | `59893882` | [Scripts/c59893882.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c59893882.lua) | 49 |
| Grenosaurus Giga-Cannon | `34481518` | [Scripts/c34481518.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c34481518.lua) | 49 |
| Mirror of the Ice Barrier | `10691144` | [Scripts/c10691144.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c10691144.lua) | 37 |

## Script Examples

### Chevreuil, Hunting Scout of the Deep Forest (`13023431`)

Source: [Scripts/c13023431.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c13023431.lua)

```lua
			and bc:IsType(TYPE_MONSTER) and bc:IsRace(RACE_WARRIOR) and bc:IsAttribute(ATTRIBUTE_EARTH)
	else
		return bc:GetPreviousPosition()&POS_FACEUP>0 and bc:GetPreviousLocation()&LOCATION_MZONE==LOCATION_MZONE and bc:IsPreviousControler(tp)
			and bc:GetPreviousTypeOnField()&TYPE_MONSTER==TYPE_MONSTER and c:GetPreviousRaceOnField()&RACE_WARRIOR==RACE_WARRIOR
			and bc:GetPreviousAttributeOnField()&ATTRIBUTE_EARTH==ATTRIBUTE_EARTH
```

### Raidraptor - Rising Rebellion Falcon (`71222868`)

Source: [Scripts/c71222868.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c71222868.lua)

```lua
end
function s.damval2(c)
	if c:GetPreviousLocation()~=LOCATION_MZONE then return end
	return math.max(0,c:GetTextAttack())
end
```

### Evil HERO Inferno Wing - Backfire (`59893882`)

Source: [Scripts/c59893882.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c59893882.lua)

```lua
		return bc:IsFaceup() and bc:IsLocation(LOCATION_MZONE) and bc:IsControler(tp) and bc:IsType(TYPE_MONSTER) and bc:IsSetCard(0x8)
	else
		return bc:GetPreviousPosition()&POS_FACEUP>0 and bc:GetPreviousLocation()&LOCATION_MZONE==LOCATION_MZONE and bc:IsPreviousControler(tp)
			and bc:GetPreviousTypeOnField()&TYPE_MONSTER==TYPE_MONSTER and bc:IsPreviousSetCard(0x8)
	end
```
