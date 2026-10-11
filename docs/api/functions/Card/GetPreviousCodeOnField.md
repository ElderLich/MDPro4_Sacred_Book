# Card.GetPreviousCodeOnField

## Signature

```lua
Card.GetPreviousCodeOnField(Card c) -> int,int|nil
```

## Description

Returns the card code recorded for c's previous on-field state.
If the previous state had a second code, that code is returned as a second value.

## Parameters

- `c` `Card`

## Returns

- `int`
- `int|nil` - Second previous code, when present.

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3497`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **23** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=standard&mode=code&q=Card.GetPreviousCodeOnField) with `Card.GetPreviousCodeOnField`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Numeron Chaos Ritual | `41850466` | [Scripts/c41850466.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c41850466.lua) | 1 |
| Black Rose Garden | `69053263` | [Scripts/c69053263.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c69053263.lua) | 1 |
| D/D/D Zero Doom Queen Machinex | `20715411` | [Scripts/c20715411.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c20715411.lua) | 1 |
| Horus the Black Flame Deity | `99307040` | [Scripts/c99307040.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c99307040.lua) | 2 |
| Dual Avatar Feet - Kokoku | `11759079` | [Scripts/c11759079.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c11759079.lua) | 1 |
| Malefic Truth Dragon | `37115575` | [Scripts/c37115575.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c37115575.lua) | 1 |
| Invincible Demise Lord | `71108540` | [Scripts/c71108540.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c71108540.lua) | 1 |
| Cerulean Skyfire | `54828837` | [Scripts/c54828837.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c54828837.lua) | 3 |
| Manga Ryu-Ran | `38369349` | [Scripts/c38369349.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c38369349.lua) | 1 |
| Blue-Eyes Toon Dragon | `53183600` | [Scripts/c53183600.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c53183600.lua) | 1 |
| Hero of the Ashened City | `30676200` | [Scripts/c30676200.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c30676200.lua) | 1 |
| Toon Summoned Skull | `91842653` | [Scripts/c91842653.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c91842653.lua) | 1 |
| Alluring Mirror Split | `92881099` | [Scripts/c92881099.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c92881099.lua) | 2 |
| Toon Cannon Soldier | `79875176` | [Scripts/c79875176.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c79875176.lua) | 1 |
| Toon Dark Magician Girl | `90960358` | [Scripts/c90960358.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c90960358.lua) | 1 |
| Illusionist Faceless Magician | `15173384` | [Scripts/c15173384.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c15173384.lua) | 1 |
| Toon Gemini Elf | `42386471` | [Scripts/c42386471.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c42386471.lua) | 1 |
| Toon Masked Sorcerer | `16392422` | [Scripts/c16392422.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c16392422.lua) | 1 |
| Toon Mermaid | `65458948` | [Scripts/c65458948.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c65458948.lua) | 1 |
| Generation Shift | `34460239` | [Scripts/c34460239.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c34460239.lua) | 1 |
| Toon Goblin Attack Force | `15270885` | [Scripts/c15270885.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c15270885.lua) | 1 |
| Mitsurugi Mirror | `49721684` | [Scripts/c49721684.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c49721684.lua) | 3 |
| Rebirth of Nephthys | `23459650` | [Scripts/c23459650.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c23459650.lua) | 1 |

## Script Examples

### Numeron Chaos Ritual (`41850466`)

Source: [Scripts/c41850466.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c41850466.lua)

```lua
end
function c41850466.cfilter(c)
	return c:IsPreviousLocation(LOCATION_ONFIELD) and c:IsPreviousPosition(POS_FACEUP) and c:GetPreviousCodeOnField()==79747096
		and c:IsReason(REASON_EFFECT) and c:GetReasonEffect():IsActiveType(TYPE_MONSTER)
end
```

### Black Rose Garden (`69053263`)

Source: [Scripts/c69053263.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c69053263.lua)

```lua
	end
	if c:IsReason(REASON_EFFECT)
		and (eg:IsContains(re:GetHandler()) and rc:GetPreviousCodeOnField()==73580471
		or not eg:IsContains(re:GetHandler()) and rc:IsCode(73580471)) then
		e:SetLabel(1)
```

### D/D/D Zero Doom Queen Machinex (`20715411`)

Source: [Scripts/c20715411.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c20715411.lua)

```lua
end
function s.cfilter(c,tp)
	return c:IsPreviousSetCard(0x10af,0xae) and c:GetPreviousCodeOnField()~=id
		and c:IsPreviousLocation(LOCATION_ONFIELD) and c:IsPreviousPosition(POS_FACEUP) and c:IsPreviousControler(tp)
end
```
