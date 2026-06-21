# Auxiliary.FConditionFilterMix

## Signature

```lua
Auxiliary.FConditionFilterMix(Card c, Card fc, bool sub, bool notfusion, ... function) -> bool
```

## Description

Material filter used by mixed Fusion procedures. It checks whether c can be used as Fusion Material for fc and satisfies at least one required material function.

## Parameters

- `c` `Card`
- `fc` `Card`
- `sub` `bool`
- `notfusion` `bool`
- `...` `function`

## Returns

- `bool` - true if c is valid material and satisfies any required material function.

## Source

- `Utilities/procedure.lua:948`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

No indexed local card script currently calls this function.

This can mean the function is unused in the current script set, is only called through an alias, or is available for future/manual scripts.
