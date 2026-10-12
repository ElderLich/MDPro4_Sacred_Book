# Auxiliary.SpiritReturnTargetOptional

## Signature

```lua
Auxiliary.SpiritReturnTargetOptional(Effect e, int tp, Group eg, int ep, any ev, Effect re, any r, int rp, bool chk) -> bool|nil
```

## Description

Target function for the optional Spirit Monster End Phase return effect. During the check step it requires the handler to be able to return to the hand, then registers return-to-hand operation info.

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

- `bool|nil` - true during valid target checks; otherwise no meaningful return value.

## Source

- `Utilities/utility.lua:212`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **1** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=standard&mode=code&q=Auxiliary.SpiritReturnTargetOptional) with `Auxiliary.SpiritReturnTargetOptional`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Sacred Spirit of the Ice Barrier | `44877690` | [Scripts/c44877690.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c44877690.lua) | 1 |

## Script Examples

### Sacred Spirit of the Ice Barrier (`44877690`)

Source: [Scripts/c44877690.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c44877690.lua)

```lua
	local e2=e1:Clone()
	e2:SetType(EFFECT_TYPE_FIELD+EFFECT_TYPE_TRIGGER_O)
	e2:SetTarget(aux.SpiritReturnTargetOptional)
	c:RegisterEffect(e2)
	--to hand, target version
```
