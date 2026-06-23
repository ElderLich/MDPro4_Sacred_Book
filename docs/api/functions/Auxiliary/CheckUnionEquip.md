# Auxiliary.CheckUnionEquip

## Signature

```lua
Auxiliary.CheckUnionEquip(Card uc, Card tc, [int exclude_modern_count]) -> bool
```

## Description

Checks whether Union Monster uc can be equipped to target tc under the local modern/old Union count rules.
Use exclude_modern_count when a replacement-style effect will remove an already equipped modern Union before equipping another one.

## Parameters

- `uc` `Card` - Union Monster that would become equipped.
- `tc` `Card` - Monster that would receive the Union card.
- `exclude_modern_count` `int` optional - Modern Union count to ignore while checking the target, commonly 1 when replacing the currently equipped Union.

## Returns

- `bool` - true if the target can receive this Union card under the count compatibility rule.

## Source

- `Utilities/utility.lua:335`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **8** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer) with `Auxiliary.CheckUnionEquip`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Union Hangar | `66399653` | [Scripts/c66399653.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c66399653.lua) | 48 |
| Delta Tri | `12079734` | [Scripts/c12079734.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c12079734.lua) | 39 |
| Union Driver | `99249638` | [Scripts/c99249638.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c99249638.lua) | 37 |
| X-Cross Cannon | `70860415` | [Scripts/c70860415.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c70860415.lua) | 36 |
| Union Pilot | `89357740` | [Scripts/c89357740.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c89357740.lua) | 34 |
| Formation Union | `26931058` | [Scripts/c26931058.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c26931058.lua) | 34 |
| Unauthorized Reactivation | `12524259` | [Scripts/c12524259.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c12524259.lua) | 33 |
| Roll Out! | `91597389` | [Scripts/c91597389.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c91597389.lua) | 26 |

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
