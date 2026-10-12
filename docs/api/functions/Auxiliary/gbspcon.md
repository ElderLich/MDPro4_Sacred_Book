# Auxiliary.gbspcon

## Signature

```lua
Auxiliary.gbspcon(Effect e, int tp, Group eg, int ep, int ev, Effect re, int r, int rp) -> bool
```

## Description

Special Summon condition helper for Gladiator Beast-style returns and set 0x1019 monster Special Summons.

## Parameters

- `e` `Effect`
- `tp` `int`
- `eg` `Group`
- `ep` `int`
- `ev` `int`
- `re` `Effect`
- `r` `int`
- `rp` `int`

## Returns

- `bool`

## Source

- `Utilities/utility.lua:911`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **16** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=standard&mode=code&q=Auxiliary.gbspcon) with `Auxiliary.gbspcon`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Gladiator Beast Lanista | `2067935` | [Scripts/c2067935.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c2067935.lua) | 1 |
| Gladiator Beast Gistel | `26582143` | [Scripts/c26582143.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c26582143.lua) | 1 |
| Gladiator Beast Attorix | `52502677` | [Scripts/c52502677.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c52502677.lua) | 1 |
| Gladiator Beast Darius | `25924653` | [Scripts/c25924653.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c25924653.lua) | 1 |
| Gladiator Beast Noxious | `67385964` | [Scripts/c67385964.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c67385964.lua) | 1 |
| Gladiator Beast Retiari | `612115` | [Scripts/c612115.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c612115.lua) | 1 |
| Gladiator Beast Vespasius | `88996322` | [Scripts/c88996322.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c88996322.lua) | 1 |
| Gladiator Beast Augustus | `7573135` | [Scripts/c7573135.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c7573135.lua) | 1 |
| Gladiator Beast Equeste | `57731460` | [Scripts/c57731460.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c57731460.lua) | 1 |
| Gladiator Beast Sagittarii | `16003979` | [Scripts/c16003979.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c16003979.lua) | 1 |
| Gladiator Beast Bestiari | `41470137` | [Scripts/c41470137.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c41470137.lua) | 1 |
| Gladiator Beast Murmillo | `5975022` | [Scripts/c5975022.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c5975022.lua) | 1 |
| Gladiator Beast Octavius | `29590752` | [Scripts/c29590752.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c29590752.lua) | 1 |
| Gladiator Beast Secutor | `77642288` | [Scripts/c77642288.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c77642288.lua) | 1 |
| Gladiator Beast Tygerius | `50893987` | [Scripts/c50893987.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c50893987.lua) | 1 |
| Gladiator Beast Torax | `65984457` | [Scripts/c65984457.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c65984457.lua) | 1 |

## Script Examples

### Gladiator Beast Lanista (`2067935`)

Source: [Scripts/c2067935.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c2067935.lua)

```lua
	e1:SetProperty(EFFECT_FLAG_CARD_TARGET)
	e1:SetCode(EVENT_SPSUMMON_SUCCESS)
	e1:SetCondition(aux.gbspcon)
	e1:SetTarget(c2067935.rmtg)
	e1:SetOperation(c2067935.rmop)
```

### Gladiator Beast Gistel (`26582143`)

Source: [Scripts/c26582143.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c26582143.lua)

```lua
	e2:SetProperty(EFFECT_FLAG_DELAY)
	e2:SetCountLimit(1,id+o)
	e2:SetCondition(aux.gbspcon)
	e2:SetTarget(s.thtg)
	e2:SetOperation(s.thop)
```

### Gladiator Beast Attorix (`52502677`)

Source: [Scripts/c52502677.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c52502677.lua)

```lua
	e1:SetCode(EVENT_SPSUMMON_SUCCESS)
	e1:SetProperty(EFFECT_FLAG_DELAY)
	e1:SetCondition(aux.gbspcon)
	e1:SetCost(c52502677.cost)
	e1:SetOperation(c52502677.operation)
```
