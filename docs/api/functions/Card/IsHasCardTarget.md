# Card.IsHasCardTarget

## Signature

```lua
Card.IsHasCardTarget(Card c1, Card c2) -> bool
```

## Description

Checks whether c1 currently has c2 as a persistent card target.

## Parameters

- `c1` `Card`
- `c2` `Card`

## Returns

- `bool`

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3543`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **22** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer) with `Card.IsHasCardTarget`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Sea Lancer | `22842214` | [Scripts/c22842214.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c22842214.lua) | 1 |
| Zero Extra Link | `60162470` | [Scripts/c60162470.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c60162470.lua) | 2 |
| Underground Arachnid | `63465535` | [Scripts/c63465535.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c63465535.lua) | 2 |
| Prevention Star | `94303232` | [Scripts/c94303232.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c94303232.lua) | 1 |
| Mermaid Archer | `4252828` | [Scripts/c4252828.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c4252828.lua) | 2 |
| Alien Hypno | `38468214` | [Scripts/c38468214.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c38468214.lua) | 1 |
| Heavenly Zephyr - Miradora | `17063599` | [Scripts/c17063599.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c17063599.lua) | 1 |
| Elemental HERO Tempest | `83121692` | [Scripts/c83121692.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c83121692.lua) | 2 |
| Number 66: Master Key Beetle | `76067258` | [Scripts/c76067258.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c76067258.lua) | 1 |
| Spiders' Lair | `26640671` | [Scripts/c26640671.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c26640671.lua) | 3 |
| Hysteric Party | `77778835` | [Scripts/c77778835.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c77778835.lua) | 1 |
| Aussa the Earth Charmer | `37970940` | [Scripts/c37970940.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c37970940.lua) | 1 |
| Eria the Water Charmer | `74364659` | [Scripts/c74364659.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c74364659.lua) | 1 |
| Hiita the Fire Charmer | `759393` | [Scripts/c759393.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c759393.lua) | 1 |
| Wynn the Wind Charmer | `37744402` | [Scripts/c37744402.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c37744402.lua) | 1 |
| Lyna the Light Charmer | `73318863` | [Scripts/c73318863.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c73318863.lua) | 1 |
| Dharc the Dark Charmer | `19327348` | [Scripts/c19327348.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c19327348.lua) | 1 |
| Heart of Clear Water | `64801562` | [Scripts/c64801562.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c64801562.lua) | 1 |
| Power Supplier | `55063681` | [Scripts/c55063681.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c55063681.lua) | 2 |
| Confronting the "C" | `15721123` | [Scripts/c15721123.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c15721123.lua) | 1 |
| Sergeant Electro | `43359262` | [Scripts/c43359262.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c43359262.lua) | 2 |
| Gora Turtle of Illusion | `42868711` | [Scripts/c42868711.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c42868711.lua) | 1 |

## Script Examples

### Sea Lancer (`22842214`)

Source: [Scripts/c22842214.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c22842214.lua)

```lua
end
function c22842214.eqfilter(c,ec)
	return c:GetFlagEffect(22842214)~=0 and c:IsHasCardTarget(ec)
end
function c22842214.repfilter(c,e,ec)
```

### Zero Extra Link (`60162470`)

Source: [Scripts/c60162470.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c60162470.lua)

```lua
end
function c60162470.matfilter(c,mc)
	return mc:IsHasCardTarget(c)
end
function c60162470.valcheck(e,c)
```

### Underground Arachnid (`63465535`)

Source: [Scripts/c63465535.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c63465535.lua)

```lua
	local c=e:GetHandler()
	local ec=e:GetLabelObject()
	return ec==nil or not ec:IsHasCardTarget(c) or ec:GetFlagEffect(63465535)==0
end
function c63465535.filter(c)
```
