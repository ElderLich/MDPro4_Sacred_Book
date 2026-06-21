# Auxiliary.FCheckSelectMixRepM

## Signature

```lua
Auxiliary.FCheckSelectMixRepM(Card c, int tp, ... any) -> bool
```

## Description

Recursive helper for mixed-repeat Fusion selection that requires the next candidate to be controlled by tp in the Monster Zone.

## Parameters

- `c` `Card`
- `tp` `int`
- `...` `any`

## Returns

- `bool` - true if c is a valid Monster Zone candidate and the selection can be completed.

## Source

- `Utilities/procedure.lua:1184`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

No indexed local card script currently calls this function.

This can mean the function is unused in the current script set, is only called through an alias, or is available for future/manual scripts.
