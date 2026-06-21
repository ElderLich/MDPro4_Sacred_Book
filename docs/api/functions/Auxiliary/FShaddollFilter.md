# Auxiliary.FShaddollFilter

## Signature

```lua
Auxiliary.FShaddollFilter(Card c, Card fc, int attr) -> bool
```

## Description

Standard Shaddoll Fusion Material filter. The card must be either a Shaddoll monster or match the required Attribute, be usable as Fusion Material, and not be blocked by effect 6205579.

## Parameters

- `c` `Card`
- `fc` `Card`
- `attr` `int`

## Returns

- `bool` - true if c is valid Shaddoll Fusion Material.

## Source

- `Utilities/procedure.lua:1351`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

No indexed local card script currently calls this function.

This can mean the function is unused in the current script set, is only called through an alias, or is available for future/manual scripts.
