# Card.IsAllCardTypes

## Signature

```lua
Card.IsAllCardTypes(Card c, int type) -> bool
```

## Description

Returns true if every bit in type is present in c:GetCardType(). A zero mask matches.

## Parameters

- `c` `Card`
- `type` `int` - TYPE_* bitmask.

## Returns

- `bool`

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3534`

## Guided Examples

Learn how to use this function in context:

- [Applying The Latest Engine And Script Changes](/learn/engine-updates)

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **11** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=standard&mode=code&q=Card.IsAllCardTypes) with `Card.IsAllCardTypes`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Pere-Zenet Em Heru](/examples/cards/46273941) | `46273941` | [Scripts/c46273941.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c46273941.lua) | 1 |
| [Am Duazenet](/examples/cards/45151304) | `45151304` | [Scripts/c45151304.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c45151304.lua) | 2 |
| Zenet Revelator Nefertari | `84512726` | [Scripts/c84512726.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c84512726.lua) | 1 |
| Tauzenet Wadjet | `73490148` | [Scripts/c73490148.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c73490148.lua) | 1 |
| Zenet-Nakhte Sphinx | `47095439` | [Scripts/c47095439.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c47095439.lua) | 1 |
| Zenet Prophet - Amenhotep | `10007434` | [Scripts/c10007434.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c10007434.lua) | 1 |
| A Journey Back to the Light - "Zenet" | `9762295` | [Scripts/c9762295.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c9762295.lua) | 1 |
| Zenetmes Nekhbet | `10884847` | [Scripts/c10884847.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c10884847.lua) | 1 |
| Zenet Cataract | `12555008` | [Scripts/c12555008.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c12555008.lua) | 1 |
| Zenet Thunderfall | `48940617` | [Scripts/c48940617.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c48940617.lua) | 1 |
| Ancient Secrets | `30752324` | [Scripts/c30752324.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c30752324.lua) | 1 |

## Script Examples

### Pere-Zenet Em Heru (`46273941`)

Source: [Scripts/c46273941.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c46273941.lua)

```lua
end
function s.matfilter(c)
	return c:IsAllCardTypes(TYPE_NORMAL+TYPE_MONSTER)
		and c:IsFaceupEx() and c:IsAbleToGrave()
end
```

### Am Duazenet (`45151304`)

Source: [Scripts/c45151304.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c45151304.lua)

```lua
end
function s.matfilter(c)
	return c:IsAllCardTypes(TYPE_NORMAL+TYPE_MONSTER)
		and c:IsFaceupEx() and c:IsAbleToGrave()
end
```

### Zenet Revelator Nefertari (`84512726`)

Source: [Scripts/c84512726.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c84512726.lua)

```lua
end
function s.chkfilter(c)
	return c:IsFaceupEx() and c:IsAllCardTypes(TYPE_NORMAL+TYPE_MONSTER)
end
function s.setfilter(c)
```
