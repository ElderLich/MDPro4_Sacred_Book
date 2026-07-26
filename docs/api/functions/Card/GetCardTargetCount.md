# Card.GetCardTargetCount

## Signature

```lua
Card.GetCardTargetCount(Card c) -> int
```

## Description

Returns the number of persistent card targets currently recorded on c.

## Parameters

- `c` `Card`

## Returns

- `int`

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3542`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **17** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer) with `Card.GetCardTargetCount`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Dark General Freed | `70676581` | [Scripts/c70676581.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c70676581.lua) | 1 |
| Miracle Fertilizer | `44887817` | [Scripts/c44887817.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c44887817.lua) | 1 |
| Ancient Gear Engineer | `1953925` | [Scripts/c1953925.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c1953925.lua) | 1 |
| Freed the Matchless General | `49681811` | [Scripts/c49681811.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c49681811.lua) | 1 |
| Brainwashing Beam | `59258334` | [Scripts/c59258334.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c59258334.lua) | 1 |
| Cyber Phoenix | `3370104` | [Scripts/c3370104.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c3370104.lua) | 1 |
| Doom Shaman | `94944637` | [Scripts/c94944637.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c94944637.lua) | 1 |
| Il Blud | `70595331` | [Scripts/c70595331.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c70595331.lua) | 1 |
| Ryu Senshi | `49868263` | [Scripts/c49868263.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c49868263.lua) | 1 |
| Rod of Silence - Kay'est | `95515060` | [Scripts/c95515060.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c95515060.lua) | 1 |
| Tyrant Dragon | `94568601` | [Scripts/c94568601.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c94568601.lua) | 1 |
| Widespread Dud | `42167046` | [Scripts/c42167046.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c42167046.lua) | 1 |
| Arcana Force 0 - The Fool | `62892347` | [Scripts/c62892347.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c62892347.lua) | 1 |
| Obsidian Dragon | `90464188` | [Scripts/c90464188.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c90464188.lua) | 1 |
| Frontier Wiseman | `38742075` | [Scripts/c38742075.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c38742075.lua) | 1 |
| Fiend Skull Dragon | `66235877` | [Scripts/c66235877.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c66235877.lua) | 1 |
| Chaos Command Magician | `72630549` | [Scripts/c72630549.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c72630549.lua) | 1 |

## Script Examples

### Dark General Freed (`70676581`)

Source: [Scripts/c70676581.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c70676581.lua)

```lua
end
function c70676581.distg(e,c)
	if c:GetCardTargetCount()==0 or not c:IsType(TYPE_SPELL) then return false end
	return c:GetCardTarget():IsExists(c70676581.disfilter,1,nil,e:GetHandlerPlayer())
end
```

### Miracle Fertilizer (`44887817`)

Source: [Scripts/c44887817.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c44887817.lua)

```lua
function c44887817.descon(e,tp,eg,ep,ev,re,r,rp)
	local c=e:GetHandler()
	if c:GetCardTargetCount()==0 then return false end
	return c:GetCardTarget():IsExists(c44887817.dfilter,1,nil,eg)
end
```

### Ancient Gear Engineer (`1953925`)

Source: [Scripts/c1953925.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c1953925.lua)

```lua
end
function c1953925.distg(e,c)
	if not c:IsType(TYPE_TRAP) or c:GetCardTargetCount()==0 then return false end
	return c:GetCardTarget():IsContains(e:GetHandler())
end
```
