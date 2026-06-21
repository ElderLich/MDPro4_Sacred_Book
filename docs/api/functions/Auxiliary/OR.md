# Auxiliary.OR

## Signature

```lua
Auxiliary.OR(... function) -> function
```

## Description

Returns a composed predicate that calls each function with the same arguments and stops at the first truthy result.

## Parameters

- `...` `function`

## Returns

- `function` - A composed predicate.

## Source

- `Utilities/utility.lua:108`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **1** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer) with `Auxiliary.OR`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Dominus Spiral | `42091632` | [Scripts/c42091632.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c42091632.lua) | 46 |

## Script Examples

### Dominus Spiral (`42091632`)

Source: [Scripts/c42091632.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c42091632.lua)

```lua
	if chkc then return chkc:IsLocation(LOCATION_MZONE) and chkc:IsControler(1-tp) and (chkc:IsAbleToHand() or chkc:IsAbleToExtra()) end
	e:SetLabel(0)
	if chk==0 then return Duel.IsExistingTarget(aux.OR(Card.IsAbleToHand,Card.IsAbleToExtra),tp,0,LOCATION_MZONE,1,nil) end
	Duel.Hint(HINT_SELECTMSG,tp,HINTMSG_RTOHAND)
	local g=Duel.SelectTarget(tp,aux.OR(Card.IsAbleToHand,Card.IsAbleToExtra),tp,0,LOCATION_MZONE,1,1,nil)
```
