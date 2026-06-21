# Card.CheckEquipTarget

## Signature

```lua
Card.CheckEquipTarget(Card c1, Card c2) -> bool
```

## Description

Check whether c2 is the correct equipment object for c1

## Parameters

- `c1` `Card`
- `c2` `Card`

## Returns

- `bool`

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3521`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **48** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer) with `Card.CheckEquipTarget`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Plunder Patroll Shipshape Ships Shipping](/examples/cards/44227727) | `44227727` | [Scripts/c44227727.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c44227727.lua) | 63 |
| Power Tool Braver Dragon | `63265554` | [Scripts/c63265554.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c63265554.lua) | 58 |
| DoomZ XII Zero - Drastea | `92472273` | [Scripts/c92472273.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c92472273.lua) | 57 |
| The Continuing Epic of Charles | `11802691` | [Scripts/c11802691.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c11802691.lua) | 54 |
| Courageous Crimson Chevalier Bradamante | `91479482` | [Scripts/c91479482.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c91479482.lua) | 50 |
| Noble Knights of the Round Table | `55742055` | [Scripts/c55742055.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c55742055.lua) | 49 |
| Ohime the Manifested Mikanko | `81260679` | [Scripts/c81260679.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c81260679.lua) | 48 |
| Sacred Noble Knight of King Artorigus | `10613952` | [Scripts/c10613952.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c10613952.lua) | 48 |
| "Infernoble Arms - Almace" | `98319530` | [Scripts/c98319530.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c98319530.lua) | 48 |
| Jupiter the Power Patron of Destruction | `68231287` | [Scripts/c68231287.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c68231287.lua) | 46 |
| Evil Eyes Unleashed | `8775395` | [Scripts/c8775395.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c8775395.lua) | 46 |
| Arsenal Audit | `49652661` | [Scripts/c49652661.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c49652661.lua) | 46 |
| Mermail King - Neptabyss | `69385019` | [Scripts/c69385019.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c69385019.lua) | 45 |
| Reincarnation Unveiling Mail | `68663427` | [Scripts/c68663427.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c68663427.lua) | 45 |
| Artorigus, King of the Noble Knights | `21223277` | [Scripts/c21223277.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c21223277.lua) | 45 |
| Phantasm Spiral Power | `61397885` | [Scripts/c61397885.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c61397885.lua) | 44 |
| Guardian Dreadscythe | `18175965` | [Scripts/c18175965.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c18175965.lua) | 43 |
| Thunder Discharge | `27623932` | [Scripts/c27623932.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c27623932.lua) | 43 |
| Prinzessin | `78527720` | [Scripts/c78527720.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c78527720.lua) | 42 |
| Infernoble Knight Emperor Charles | `77656797` | [Scripts/c77656797.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c77656797.lua) | 42 |
| Original Bamboo Sword | `33578406` | [Scripts/c33578406.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c33578406.lua) | 41 |
| Mikanko Rivalry | `78199891` | [Scripts/c78199891.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c78199891.lua) | 40 |
| Breath of Resurrection | `64018647` | [Scripts/c64018647.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c64018647.lua) | 40 |
| Arms Regeneration | `32549749` | [Scripts/c32549749.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c32549749.lua) | 40 |
| ...and 24 more |  |  |  |

## Script Examples

### Plunder Patroll Shipshape Ships Shipping (`44227727`)

Source: [Scripts/c44227727.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c44227727.lua)

```lua
end
function c44227727.eqfilter(c,ec,tp)
	return (c:IsType(TYPE_MONSTER) and c:IsSetCard(0x13f) or c:IsCode(80621422) and c:CheckEquipTarget(ec))
		and not c:IsForbidden() and c:CheckUniqueOnField(tp,LOCATION_SZONE)
end
```

### Power Tool Braver Dragon (`63265554`)

Source: [Scripts/c63265554.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c63265554.lua)

```lua
end
function c63265554.eqfilter(c,ec,tp)
	return c:IsType(TYPE_EQUIP) and c:CheckEquipTarget(ec) and c:CheckUniqueOnField(tp,LOCATION_SZONE) and not c:IsForbidden()
end
function c63265554.eqtg(e,tp,eg,ep,ev,re,r,rp,chk)
```

### DoomZ XII Zero - Drastea (`92472273`)

Source: [Scripts/c92472273.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c92472273.lua)

```lua
end
function s.eqfilter(c,ec,tp)
	return c:IsType(TYPE_EQUIP) and c:CheckEquipTarget(ec) and c:CheckUniqueOnField(tp,LOCATION_SZONE) and not c:IsForbidden()
end
function s.spop(e,tp,eg,ep,ev,re,r,rp)
```
