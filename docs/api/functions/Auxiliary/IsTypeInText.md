# Auxiliary.IsTypeInText

## Signature

```lua
Auxiliary.IsTypeInText(Card c, int type) -> bool
```

## Description

Returns true if c's text-registered type mask contains type.

## Parameters

- `c` `Card`
- `type` `int`

## Returns

- `bool` - true if c's text type mask contains type.

## Source

- `Utilities/utility.lua:584`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **3** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=standard&mode=code&q=Auxiliary.IsTypeInText) with `Auxiliary.IsTypeInText`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Union Controller | `2133971` | [Scripts/c2133971.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c2133971.lua) | 1 |
| Shinobaroness Shade Peacock | `33325951` | [Scripts/c33325951.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c33325951.lua) | 1 |
| Geminize Lord Golknight | `72305034` | [Scripts/c72305034.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c72305034.lua) | 1 |

## Script Examples

### Union Controller (`2133971`)

Source: [Scripts/c2133971.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c2133971.lua)

```lua
end
function s.filter(c)
	return c:IsType(TYPE_SPELL+TYPE_TRAP) and aux.IsTypeInText(c,TYPE_UNION) and c:IsAbleToHand()
end
function s.thtg(e,tp,eg,ep,ev,re,r,rp,chk)
```

### Shinobaroness Shade Peacock (`33325951`)

Source: [Scripts/c33325951.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c33325951.lua)

```lua
end
function s.filter(c)
	return c:IsType(TYPE_SPELL+TYPE_TRAP) and aux.IsTypeInText(c,TYPE_SPIRIT) and c:IsAbleToHand()
end
function s.thtg(e,tp,eg,ep,ev,re,r,rp,chk)
```

### Geminize Lord Golknight (`72305034`)

Source: [Scripts/c72305034.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c72305034.lua)

```lua
end
function c72305034.thfilter(c)
	return aux.IsTypeInText(c,TYPE_DUAL) and c:IsType(TYPE_SPELL+TYPE_TRAP) and c:IsAbleToHand()
end
function c72305034.thtg(e,tp,eg,ep,ev,re,r,rp,chk)
```
