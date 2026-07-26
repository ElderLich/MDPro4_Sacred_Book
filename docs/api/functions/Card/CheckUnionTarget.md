# Card.CheckUnionTarget

## Signature

```lua
Card.CheckUnionTarget(Card c, Card target) -> bool
```

## Description

Checks whether target is a valid Union equip target for c under EFFECT_UNION_LIMIT.
The core also enforces new/old Union count compatibility between c and target.

## Parameters

- `c` `Card`
- `target` `Card`

## Returns

- `bool`

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3525`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **8** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer) with `Card.CheckUnionTarget`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Union Hangar | `66399653` | [Scripts/c66399653.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c66399653.lua) | 1 |
| Delta Tri | `12079734` | [Scripts/c12079734.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c12079734.lua) | 1 |
| Union Driver | `99249638` | [Scripts/c99249638.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c99249638.lua) | 1 |
| X-Cross Cannon | `70860415` | [Scripts/c70860415.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c70860415.lua) | 1 |
| Union Pilot | `89357740` | [Scripts/c89357740.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c89357740.lua) | 1 |
| Formation Union | `26931058` | [Scripts/c26931058.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c26931058.lua) | 1 |
| Unauthorized Reactivation | `12524259` | [Scripts/c12524259.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c12524259.lua) | 1 |
| Roll Out! | `91597389` | [Scripts/c91597389.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c91597389.lua) | 1 |

## Script Examples

### Union Hangar (`66399653`)

Source: [Scripts/c66399653.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c66399653.lua)

```lua
function c66399653.cfilter(c,ec,tp)
	return c:IsRace(RACE_MACHINE) and c:IsAttribute(ATTRIBUTE_LIGHT) and c:IsType(TYPE_UNION) and not c:IsCode(ec:GetCode())
		and c:CheckUniqueOnField(tp) and not c:IsForbidden() and c:CheckUnionTarget(ec) and aux.CheckUnionEquip(c,ec)
end
function c66399653.eqtg(e,tp,eg,ep,ev,re,r,rp,chk,chkc)
```

### Delta Tri (`12079734`)

Source: [Scripts/c12079734.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c12079734.lua)

```lua
c12079734.has_text_type=TYPE_UNION
function c12079734.filter1(c,ec)
	return c:IsType(TYPE_UNION) and c:CheckUnionTarget(ec) and aux.CheckUnionEquip(c,ec)
end
function c12079734.filter2(c)
```

### Union Driver (`99249638`)

Source: [Scripts/c99249638.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c99249638.lua)

```lua
end
function c99249638.refilter(c,tc,tp,exclude_modern_count)
	return aux.CheckUnionEquip(c,tc,exclude_modern_count) and c:CheckUnionTarget(tc) and c:IsType(TYPE_UNION)
		and c:IsLevelBelow(4) and c:CheckUniqueOnField(tp) and not c:IsForbidden()
end
```
