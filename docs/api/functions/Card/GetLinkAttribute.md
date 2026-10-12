# Card.GetLinkAttribute

## Signature

```lua
Card.GetLinkAttribute(Card c, [int player]) -> int
```

## Description

Returns the Attribute c uses as Link Material for player, defaulting to the current reason player.

## Parameters

- `c` `Card`
- `player` `int` optional - default: current reason player

## Returns

- `int`

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3485`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **10** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=standard&mode=code&q=Card.GetLinkAttribute) with `Card.GetLinkAttribute`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Union Carrier | `83152482` | [Scripts/c83152482.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c83152482.lua) | 2 |
| Decode Talker Heatsoul | `61245672` | [Scripts/c61245672.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c61245672.lua) | 1 |
| ASHLAN U1000 | `44376395` | [Scripts/c44376395.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c44376395.lua) | 1 |
| Five-Headed Link Dragon | `10669138` | [Scripts/c10669138.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c10669138.lua) | 1 |
| Curious, the Lightsworn Dominion | `98095162` | [Scripts/c98095162.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c98095162.lua) | 1 |
| Herald of Mirage Lights | `46935289` | [Scripts/c46935289.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c46935289.lua) | 1 |
| Darkness Metal, the Dragon of Dark Steel | `79266769` | [Scripts/c79266769.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c79266769.lua) | 1 |
| The Arrival Cyberse @Ignister | `11738489` | [Scripts/c11738489.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c11738489.lua) | 1 |
| Ib the World Chalice Priestess | `77610772` | [Scripts/c77610772.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c77610772.lua) | 1 |
| Aleister the Invoker of Madness | `97973962` | [Scripts/c97973962.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c97973962.lua) | 1 |

## Script Examples

### Union Carrier (`83152482`)

Source: [Scripts/c83152482.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c83152482.lua)

```lua
	local c1=g:GetFirst()
	local c2=g:GetNext()
	return c1:GetLinkAttribute()&c2:GetLinkAttribute()>0 or c1:GetLinkRace()&c2:GetLinkRace()>0
end
function c83152482.lmlimit(e)
```

### Decode Talker Heatsoul (`61245672`)

Source: [Scripts/c61245672.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c61245672.lua)

```lua
end
function c61245672.lcheck(g)
	return g:GetClassCount(Card.GetLinkAttribute)==g:GetCount()
end
function c61245672.atkval(e,c)
```

### ASHLAN U1000 (`44376395`)

Source: [Scripts/c44376395.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c44376395.lua)

```lua
end
function s.lcheck(g)
	return not aux.SameValueCheck(g,Card.GetLinkRace) and not aux.SameValueCheck(g,Card.GetLinkAttribute)
end
function s.piercetg(e,c)
```
