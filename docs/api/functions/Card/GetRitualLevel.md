# Card.GetRitualLevel

## Signature

```lua
Card.GetRitualLevel(Card c, Card rc) -> int
```

## Description

Returns the Ritual Level value c contributes for Ritual Monster rc.

## Parameters

- `c` `Card`
- `rc` `Card`

## Returns

- `int`

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3412`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **7** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer) with `Card.GetRitualLevel`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Nekroz Kaleidoscope](/examples/cards/51124303) | `51124303` | [Scripts/c51124303.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c51124303.lua) | 1 |
| Drytron Meteonis Draconids | `69815951` | [Scripts/c69815951.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c69815951.lua) | 2 |
| Drytron Meteonis Quadrantids | `95209656` | [Scripts/c95209656.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c95209656.lua) | 2 |
| Vendread Reunion | `2266498` | [Scripts/c2266498.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c2266498.lua) | 1 |
| Advanced Ritual Art | `46052429` | [Scripts/c46052429.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c46052429.lua) | 2 |
| Luminous Dragon Ritual | `34834619` | [Scripts/c34834619.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c34834619.lua) | 2 |
| Emperor Tanuki's Critter Count | `20560620` | [Scripts/c20560620.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c20560620.lua) | 2 |

## Script Examples

### Nekroz Kaleidoscope (`51124303`)

Source: [Scripts/c51124303.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c51124303.lua)

```lua
end
function c51124303.rfilter(c,mc)
	local mlv=mc:GetRitualLevel(c)
	if mlv==mc:GetLevel() then return false end
	local lv=c:GetLevel()
```

### Drytron Meteonis Draconids (`69815951`)

Source: [Scripts/c69815951.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c69815951.lua)

```lua
end
function c69815951.lvfilter(c,rc)
	return c:GetRitualLevel(rc)>0
end
function c69815951.valcheck(e,c)
```

### Drytron Meteonis Quadrantids (`95209656`)

Source: [Scripts/c95209656.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c95209656.lua)

```lua
end
function c95209656.lvfilter(c,rc)
	return c:GetRitualLevel(rc)>0
end
function c95209656.valcheck(e,c)
```
