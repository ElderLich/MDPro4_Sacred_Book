# Auxiliary.nbtg

## Signature

```lua
Auxiliary.nbtg(Effect e, int tp, Group eg, int ep, any ev, Effect re, any r, int rp, bool chk) -> void
```

## Description

Target helper for effects that negate an activation and banish the activating card. It sets negate operation info, adds banish info when the activating card is still related, and marks CATEGORY_GRAVE_ACTION for effects activated in the Graveyard.

## Parameters

- `e` `Effect`
- `tp` `int`
- `eg` `Group`
- `ep` `int`
- `ev` `any`
- `re` `Effect`
- `r` `any`
- `rp` `int`
- `chk` `bool`

## Source

- `Utilities/utility.lua:1472`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **18** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=standard&mode=code&q=Auxiliary.nbtg) with `Auxiliary.nbtg`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Eclipse, Dragon Ruler of Catastrophes | `30350202` | [Scripts/c30350202.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c30350202.lua) | 1 |
| Allied Code Talker @Ignister | `39138610` | [Scripts/c39138610.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c39138610.lua) | 1 |
| Infernoid Onuncu | `14799437` | [Scripts/c14799437.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c14799437.lua) | 1 |
| Infernoid Devyaty | `23440231` | [Scripts/c23440231.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c23440231.lua) | 1 |
| Dragunity Knight - Areadbhair | `88234821` | [Scripts/c88234821.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c88234821.lua) | 1 |
| Myutant Ultimus | `6182103` | [Scripts/c6182103.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c6182103.lua) | 1 |
| Orcust Crescendo | `703897` | [Scripts/c703897.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c703897.lua) | 1 |
| Nekroz of Areadbhair | `39468724` | [Scripts/c39468724.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c39468724.lua) | 1 |
| Myutant Beast | `34695290` | [Scripts/c34695290.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c34695290.lua) | 1 |
| Tri-Gate Wizard | `32617464` | [Scripts/c32617464.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c32617464.lua) | 1 |
| Gameciel, the Sea Turtle Kaiju | `55063751` | [Scripts/c55063751.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c55063751.lua) | 1 |
| Bending Destiny | `94662235` | [Scripts/c94662235.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c94662235.lua) | 1 |
| Cynet Conflict | `7403341` | [Scripts/c7403341.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c7403341.lua) | 1 |
| Invoked Mechaba | `75286621` | [Scripts/c75286621.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c75286621.lua) | 1 |
| Dragunity Oubliette | `51849216` | [Scripts/c51849216.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c51849216.lua) | 1 |
| The Huge Revolution is Over | `99188141` | [Scripts/c99188141.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c99188141.lua) | 1 |
| Unwavering Bond | `72648810` | [Scripts/c72648810.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c72648810.lua) | 1 |
| Debunk | `65703851` | [Scripts/c65703851.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c65703851.lua) | 1 |

## Script Examples

### Eclipse, Dragon Ruler of Catastrophes (`30350202`)

Source: [Scripts/c30350202.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c30350202.lua)

```lua
	e2:SetCondition(s.negcon)
	e2:SetCost(s.negcost)
	e2:SetTarget(aux.nbtg)
	e2:SetOperation(s.negop)
	c:RegisterEffect(e2)
```

### Allied Code Talker @Ignister (`39138610`)

Source: [Scripts/c39138610.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c39138610.lua)

```lua
	e2:SetCondition(s.discon)
	e2:SetCost(s.discost)
	e2:SetTarget(aux.nbtg)
	e2:SetOperation(s.disop)
	c:RegisterEffect(e2)
```

### Infernoid Onuncu (`14799437`)

Source: [Scripts/c14799437.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c14799437.lua)

```lua
	e4:SetCondition(c14799437.negcon)
	e4:SetCost(c14799437.negcost)
	e4:SetTarget(aux.nbtg)
	e4:SetOperation(c14799437.negop)
	c:RegisterEffect(e4)
```
