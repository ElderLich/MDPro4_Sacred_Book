# Auxiliary.ThisCardInGraveAlreadyCheckReg

## Signature

```lua
Auxiliary.ThisCardInGraveAlreadyCheckReg(Effect e, int tp, Group eg, int ep, any ev, Effect re, any r, int rp) -> bool
```

## Description

Condition callback used by Auxiliary.AddThisCardInGraveAlreadyCheck. When this card is sent to the Graveyard by an effect, material use, or non-activated cost, it stores the responsible effect and installs reset effects; it then returns false so no separate effect operation runs.

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

- `bool` - Always false after any tracking setup is done.

## Source

- `Utilities/utility.lua:1556`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

No indexed local card script currently calls this function.

This can mean the function is unused in the current script set, is only called through an alias, or is available for future/manual scripts.
