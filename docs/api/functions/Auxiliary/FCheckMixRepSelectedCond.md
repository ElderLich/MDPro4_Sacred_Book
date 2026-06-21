# Auxiliary.FCheckMixRepSelectedCond

## Signature

```lua
Auxiliary.FCheckMixRepSelectedCond(int tp, Group mg, Group sg, Group g, ... any) -> bool
```

## Description

Checks whether the recursive mixed-repeat selection can continue from the currently selected group, or can finish through Auxiliary.FCheckSelectMixRep.

## Parameters

- `tp` `int`
- `mg` `Group`
- `sg` `Group`
- `g` `Group`
- `...` `any`

## Returns

- `bool` - true if the current mixed-repeat selection can continue or finish.

## Source

- `Utilities/procedure.lua:1146`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

No indexed local card script currently calls this function.

This can mean the function is unused in the current script set, is only called through an alias, or is available for future/manual scripts.
