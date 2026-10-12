# Auxiliary.MimighoulFlipCondition

## Signature

```lua
Auxiliary.MimighoulFlipCondition(Effect e, int tp, Group eg, int ep, any ev, Effect re, any r, int rp) -> bool
```

## Description

Returns true during either Main Phase.

## Parameters

- `e` `Effect`
- `tp` `int`
- `eg` `Group`
- `ep` `int`
- `ev` `any`
- `re` `Effect`
- `r` `any`
- `rp` `int`

## Returns

- `bool` - true during either Main Phase.

## Source

- `Utilities/utility.lua:2002`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **7** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=standard&mode=code&q=Auxiliary.MimighoulFlipCondition) with `Auxiliary.MimighoulFlipCondition`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Mimighoul Archfiend | `50415441` | [Scripts/c50415441.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c50415441.lua) | 1 |
| Mimighoul Fairy | `43066927` | [Scripts/c43066927.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c43066927.lua) | 1 |
| Mimighoul Cerberus | `23920796` | [Scripts/c23920796.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c23920796.lua) | 1 |
| Mimighoul Dragon | `81522098` | [Scripts/c81522098.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c81522098.lua) | 1 |
| Mimighoul Flower | `82933935` | [Scripts/c82933935.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c82933935.lua) | 1 |
| Mimighoul Armor | `11677278` | [Scripts/c11677278.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c11677278.lua) | 1 |
| Mimighoul Slime | `80551022` | [Scripts/c80551022.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c80551022.lua) | 1 |

## Script Examples

### Mimighoul Archfiend (`50415441`)

Source: [Scripts/c50415441.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c50415441.lua)

```lua
	e1:SetProperty(EFFECT_FLAG_DELAY)
	e1:SetCountLimit(1,id)
	e1:SetCondition(aux.MimighoulFlipCondition)
	e1:SetTarget(s.target)
	e1:SetOperation(s.operation)
```

### Mimighoul Fairy (`43066927`)

Source: [Scripts/c43066927.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c43066927.lua)

```lua
	e1:SetProperty(EFFECT_FLAG_DELAY)
	e1:SetCountLimit(1,id)
	e1:SetCondition(aux.MimighoulFlipCondition)
	e1:SetTarget(s.target)
	e1:SetOperation(s.operation)
```

### Mimighoul Cerberus (`23920796`)

Source: [Scripts/c23920796.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c23920796.lua)

```lua
	e1:SetProperty(EFFECT_FLAG_DELAY)
	e1:SetCountLimit(1,id)
	e1:SetCondition(aux.MimighoulFlipCondition)
	e1:SetTarget(s.target)
	e1:SetOperation(s.operation)
```
