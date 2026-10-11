# Auxiliary.SpiritReturnTargetForced

## Signature

```lua
Auxiliary.SpiritReturnTargetForced(Effect e, int tp, Group eg, int ep, any ev, Effect re, any r, int rp, bool chk) -> bool|nil
```

## Description

Target function for the mandatory Spirit Monster End Phase return effect. During the check step it always returns true, then registers return-to-hand operation info.

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

## Returns

- `bool|nil` - true during target checks; otherwise no meaningful return value.

## Source

- `Utilities/utility.lua:204`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **1** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=standard&mode=code&q=Auxiliary.SpiritReturnTargetForced) with `Auxiliary.SpiritReturnTargetForced`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Sacred Spirit of the Ice Barrier | `44877690` | [Scripts/c44877690.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c44877690.lua) | 1 |

## Script Examples

### Sacred Spirit of the Ice Barrier (`44877690`)

Source: [Scripts/c44877690.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c44877690.lua)

```lua
	e1:SetReset(RESET_EVENT+0x1ee0000+RESET_PHASE+PHASE_END)
	e1:SetCondition(c44877690.retcon)
	e1:SetTarget(aux.SpiritReturnTargetForced)
	e1:SetOperation(aux.SpiritReturnOperation)
	c:RegisterEffect(e1)
```
