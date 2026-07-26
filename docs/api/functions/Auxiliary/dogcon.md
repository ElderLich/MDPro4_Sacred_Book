# Auxiliary.dogcon

## Signature

```lua
Auxiliary.dogcon(Effect e, int tp, Group eg, int ep, int ev, Effect re, int r, int rp) -> bool
```

## Description

EVENT_TO_GRAVE condition helper that checks whether the handler was previously controlled by tp and destroyed by the opponent.

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

- `Utilities/utility.lua:791`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **3** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer) with `Auxiliary.dogcon`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Noble Knight Joan | `18426196` | [Scripts/c18426196.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c18426196.lua) | 1 |
| Ice Hand | `95929069` | [Scripts/c95929069.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c95929069.lua) | 1 |
| Fire Hand | `68535320` | [Scripts/c68535320.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c68535320.lua) | 1 |

## Script Examples

### Noble Knight Joan (`18426196`)

Source: [Scripts/c18426196.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c18426196.lua)

```lua
	e1:SetType(EFFECT_TYPE_SINGLE+EFFECT_TYPE_TRIGGER_O)
	e1:SetCode(EVENT_TO_GRAVE)
	e1:SetCondition(aux.dogcon)
	e1:SetCost(c18426196.thcost)
	e1:SetTarget(c18426196.thtg)
```

### Ice Hand (`95929069`)

Source: [Scripts/c95929069.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c95929069.lua)

```lua
	e1:SetProperty(EFFECT_FLAG_CARD_TARGET+EFFECT_FLAG_DAMAGE_STEP)
	e1:SetCode(EVENT_TO_GRAVE)
	e1:SetCondition(aux.dogcon)
	e1:SetTarget(c95929069.target)
	e1:SetOperation(c95929069.operation)
```

### Fire Hand (`68535320`)

Source: [Scripts/c68535320.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c68535320.lua)

```lua
	e1:SetProperty(EFFECT_FLAG_CARD_TARGET+EFFECT_FLAG_DAMAGE_STEP)
	e1:SetCode(EVENT_TO_GRAVE)
	e1:SetCondition(aux.dogcon)
	e1:SetTarget(c68535320.target)
	e1:SetOperation(c68535320.operation)
```
