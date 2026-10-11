# Auxiliary.ArcanaCoinTarget

## Signature

```lua
Auxiliary.ArcanaCoinTarget(Effect e, int tp, Group eg, int ep, any ev, Effect re, any r, int rp, bool chk) -> void
```

## Description

Declares that the shared Arcana Force effect will perform one coin toss for tp.

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

- `Utilities/utility.lua:281`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **1** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=standard&mode=code&q=Auxiliary.ArcanaCoinTarget) with `Auxiliary.ArcanaCoinTarget`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Arcana Force VII - The Chariot | `34568403` | [Scripts/c34568403.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c34568403.lua) | 1 |

## Script Examples

### Arcana Force VII - The Chariot (`34568403`)

Source: [Scripts/c34568403.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c34568403.lua)

```lua
	e1:SetType(EFFECT_TYPE_SINGLE+EFFECT_TYPE_TRIGGER_F)
	e1:SetCode(EVENT_SUMMON_SUCCESS)
	e1:SetTarget(aux.ArcanaCoinTarget)
	e1:SetOperation(c34568403.coinop)
	c:RegisterEffect(e1)
```
