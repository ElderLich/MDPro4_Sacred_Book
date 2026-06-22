# Card.GetColumnGroupCount

## Signature

```lua
Card.GetColumnGroupCount(Card c) -> int
```

## Description

Returns the number of cards in columns overlapping c.

## Parameters

- `c` `Card`

## Returns

- `int`

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3428`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **8** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer) with `Card.GetColumnGroupCount`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Mekk-Knight Purple Nightfall | `28692962` | [Scripts/c28692962.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c28692962.lua) | 53 |
| Mekk-Knight Red Moon | `56809158` | [Scripts/c56809158.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c56809158.lua) | 41 |
| Mekk-Knight Blue Sky | `20537097` | [Scripts/c20537097.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c20537097.lua) | 39 |
| Mekk-Knight Green Horizon | `66022706` | [Scripts/c66022706.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c66022706.lua) | 38 |
| Mekk-Knight Yellow Star | `29415459` | [Scripts/c29415459.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c29415459.lua) | 38 |
| Mekk-Knight Orange Sunset | `93020401` | [Scripts/c93020401.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c93020401.lua) | 35 |
| Mekk-Knight Indigo Eclipse | `92204263` | [Scripts/c92204263.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c92204263.lua) | 31 |
| Iron Dragon Tiamaton | `46247282` | [Scripts/c46247282.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c46247282.lua) | 29 |

## Script Examples

### Mekk-Knight Purple Nightfall (`28692962`)

Source: [Scripts/c28692962.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c28692962.lua)

```lua
end
function c28692962.cfilter(c)
	return c:GetColumnGroupCount()>0
end
function c28692962.hspcon(e,c)
```

### Mekk-Knight Red Moon (`56809158`)

Source: [Scripts/c56809158.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c56809158.lua)

```lua
end
function c56809158.cfilter(c)
	return c:GetColumnGroupCount()>0
end
function c56809158.hspcon(e,c)
```

### Mekk-Knight Blue Sky (`20537097`)

Source: [Scripts/c20537097.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c20537097.lua)

```lua
end
function c20537097.cfilter(c)
	return c:GetColumnGroupCount()>0
end
function c20537097.hspcon(e,c)
```
