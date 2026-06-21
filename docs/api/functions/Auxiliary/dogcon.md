# Auxiliary.dogcon

## Signature

```lua
Auxiliary.dogcon(Effect e, int tp, Group eg, int ep, any ev, Effect re, any r, int rp) -> void
```

## Description

Check if e:GetHandler() was destroyed by the opponent and sent to the Graveyard from your field, used for SetCondition
function Auxiliary.dogcon(e, tp, eg, ep, ev, re, r, rp)
  local c=e:GetHandler()
  return c:GetPreviousControler()==tp and c:IsReason(REASON_DESTROY) and rp==1-tp
end

## Parameters

- `e` `Effect`
- `tp` `int`
- `eg` `Group`
- `ep` `int`
- `ev` `any`
- `re` `Effect`
- `r` `any`
- `rp` `int`

## Source

- `Utilities/utility.lua:791`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **3** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer) with `Auxiliary.dogcon`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Noble Knight Joan | `18426196` | [Scripts/c18426196.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c18426196.lua) | 34 |
| Ice Hand | `95929069` | [Scripts/c95929069.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c95929069.lua) | 31 |
| Fire Hand | `68535320` | [Scripts/c68535320.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c68535320.lua) | 31 |

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
