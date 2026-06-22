# Auxiliary.IsSelfEquip

## Signature

```lua
Auxiliary.IsSelfEquip(Card c, int id) -> bool
```

## Description

Checks whether c has an equipped card carrying flag effect id, which marks equipment created by that card's own effect.

## Parameters

- `c` `Card`
- `id` `int`

## Returns

- `bool`

## Source

- `Utilities/utility.lua:1953`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **4** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer) with `Auxiliary.IsSelfEquip`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Allure Queen LV5 | `23756165` | [Scripts/c23756165.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c23756165.lua) | 51 |
| Allure Queen LV3 | `87257460` | [Scripts/c87257460.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c87257460.lua) | 47 |
| Allure Palace | `31322640` | [Scripts/c31322640.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c31322640.lua) | 42 |
| Allure Queen LV7 | `50140163` | [Scripts/c50140163.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c50140163.lua) | 38 |

## Script Examples

### Allure Queen LV5 (`23756165`)

Source: [Scripts/c23756165.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c23756165.lua)

```lua
function c23756165.eqcon1(e,tp,eg,ep,ev,re,r,rp)
	local c=e:GetHandler()
	return c:GetFlagEffect(id+1)>0 and not aux.IsSelfEquip(c,FLAG_ID_ALLURE_QUEEN) and not aux.IsCanBeQuickEffect(c,tp,95937545)
end
function c23756165.eqcon2(e,tp,eg,ep,ev,re,r,rp)
```

### Allure Queen LV3 (`87257460`)

Source: [Scripts/c87257460.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c87257460.lua)

```lua
function c87257460.eqcon1(e,tp,eg,ep,ev,re,r,rp)
	local c=e:GetHandler()
	return not aux.IsSelfEquip(c,FLAG_ID_ALLURE_QUEEN) and not aux.IsCanBeQuickEffect(c,tp,95937545)
end
function c87257460.eqcon2(e,tp,eg,ep,ev,re,r,rp)
```

### Allure Palace (`31322640`)

Source: [Scripts/c31322640.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c31322640.lua)

```lua
function s.spcost(e,tp,eg,ep,ev,re,r,rp,chk)
	local c=e:GetHandler()
	if chk==0 then return c:IsAbleToGraveAsCost() and aux.IsSelfEquip(c,FLAG_ID_ALLURE_QUEEN) end
	Duel.SendtoGrave(c,REASON_COST)
end
```
