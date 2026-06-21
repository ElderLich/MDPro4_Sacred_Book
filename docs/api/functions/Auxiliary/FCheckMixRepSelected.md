# Auxiliary.FCheckMixRepSelected

## Signature

```lua
Auxiliary.FCheckMixRepSelected(Card c, ... any) -> bool
```

## Description

Selection-recursion helper for mixed-repeat Fusion Materials; it delegates to Auxiliary.FCheckMixRepTemplate using the selected-material condition.

## Parameters

- `c` `Card`
- `...` `any`

## Returns

- `bool` - true if the selected-material recursion can succeed.

## Source

- `Utilities/procedure.lua:1153`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

No indexed local card script currently calls this function.

This can mean the function is unused in the current script set, is only called through an alias, or is available for future/manual scripts.
