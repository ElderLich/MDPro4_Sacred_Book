# Auxiliary.nzdef

## Signature

```lua
Auxiliary.nzdef(Card c) -> bool
```

## Description

Returns true for face-up cards with current DEF greater than 0.

## Parameters

- `c` `Card`

## Returns

- `bool`

## Source

- `Utilities/utility.lua:844`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **6** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer) with `Auxiliary.nzdef`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Apparition | `91392974` | [Scripts/c91392974.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c91392974.lua) | 45 |
| Superheavy Samurai Helper | `44891812` | [Scripts/c44891812.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c44891812.lua) | 43 |
| D/D/D Supersight King Zero Maxwell | `76029419` | [Scripts/c76029419.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c76029419.lua) | 32 |
| Catnipped Kitty | `96501677` | [Scripts/c96501677.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c96501677.lua) | 29 |
| Wild Nature's Release | `61166988` | [Scripts/c61166988.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c61166988.lua) | 23 |
| Gravity Lash | `69319869` | [Scripts/c69319869.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c69319869.lua) | 22 |

## Script Examples

### Apparition (`91392974`)

Source: [Scripts/c91392974.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c91392974.lua)

```lua
end
function c91392974.atkfilter(c)
	return aux.nzatk(c) or aux.nzdef(c)
end
function c91392974.operation(e,tp,eg,ep,ev,re,r,rp)
```

### Superheavy Samurai Helper (`44891812`)

Source: [Scripts/c44891812.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c44891812.lua)

```lua
end
function c44891812.deffilter(c)
	return c:IsFaceup() and c:IsSetCard(0x9a) and aux.nzdef(c)
end
function c44891812.deftg(e,tp,eg,ep,ev,re,r,rp,chk,chkc)
```

### D/D/D Supersight King Zero Maxwell (`76029419`)

Source: [Scripts/c76029419.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c76029419.lua)

```lua
end
function c76029419.deftg(e,tp,eg,ep,ev,re,r,rp,chk,chkc)
	if chkc then return chkc:IsLocation(LOCATION_MZONE) and aux.nzdef(chkc) end
	if chk==0 then return Duel.IsExistingTarget(aux.nzdef,tp,LOCATION_MZONE,LOCATION_MZONE,1,nil) end
	Duel.Hint(HINT_SELECTMSG,tp,HINTMSG_FACEUP)
```
