# Card.IsXyzLevel

## Signature

```lua
Card.IsXyzLevel(Card c, Card xyzc, int lv) -> bool
```

## Description

Checks whether c can provide Xyz Level lv for Xyz Monster xyzc.

## Parameters

- `c` `Card`
- `xyzc` `Card`
- `lv` `int`

## Returns

- `bool`

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3412`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **4** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer) with `Card.IsXyzLevel`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Rilliona, the Wondrous Magistus Witch Wardrobe | `74689476` | [Scripts/c74689476.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c74689476.lua) | 44 |
| Eclipse Twins | `45852939` | [Scripts/c45852939.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c45852939.lua) | 44 |
| Gigantic Spright | `54498517` | [Scripts/c54498517.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c54498517.lua) | 35 |
| Virtual World Dragon - Longlong | `61641818` | [Scripts/c61641818.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c61641818.lua) | 35 |

## Script Examples

### Rilliona, the Wondrous Magistus Witch Wardrobe (`74689476`)

Source: [Scripts/c74689476.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c74689476.lua)

```lua
end
function c74689476.mfilter(c,xyzc)
	return c:IsXyzType(TYPE_MONSTER) and c:IsXyzLevel(xyzc,4) and c:IsRace(RACE_SPELLCASTER)
end
function c74689476.xyzcheck(g)
```

### Eclipse Twins (`45852939`)

Source: [Scripts/c45852939.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c45852939.lua)

```lua
end
function s.mfilter(c,xyzc)
	return c:IsXyzLevel(xyzc,4) or c:IsRank(4)
end
function s.xatkcon(e,tp,eg,ep,ev,re,r,rp)
```

### Gigantic Spright (`54498517`)

Source: [Scripts/c54498517.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c54498517.lua)

```lua
end
function c54498517.mfilter(c,xyzc)
	return c:IsXyzLevel(xyzc,2) or c:IsLink(2)
end
function c54498517.adcon(e)
```
