# Auxiliary.SpiritReturnOperation

## Signature

```lua
Auxiliary.SpiritReturnOperation(Effect e, int tp, Group eg, int ep, any ev, Effect re, any r, int rp) -> void
```

## Description

Operation for the shared Spirit Monster End Phase return effect. If the handler is still related to the effect, it returns that card to the hand.

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

- `Utilities/utility.lua:216`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **1** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer) with `Auxiliary.SpiritReturnOperation`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Sacred Spirit of the Ice Barrier | `44877690` | [Scripts/c44877690.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c44877690.lua) | 1 |

## Script Examples

### Sacred Spirit of the Ice Barrier (`44877690`)

Source: [Scripts/c44877690.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c44877690.lua)

```lua
	e1:SetCondition(c44877690.retcon)
	e1:SetTarget(aux.SpiritReturnTargetForced)
	e1:SetOperation(aux.SpiritReturnOperation)
	c:RegisterEffect(e1)
	local e2=e1:Clone()
```
