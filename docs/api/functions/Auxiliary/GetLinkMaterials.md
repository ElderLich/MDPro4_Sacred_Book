# Auxiliary.GetLinkMaterials

## Signature

```lua
Auxiliary.GetLinkMaterials(int tp, function|nil f, Card lc, Effect e) -> Group
```

## Description

Returns the available Link Materials for tp, including regular Monster Zone materials and cards allowed by extra Link Material effects.

## Parameters

- `tp` `int`
- `f` `function|nil`
- `lc` `Card`
- `e` `Effect`

## Returns

- `Group` - Available Link Materials.

## Source

- `Utilities/procedure.lua:2163`

## Guided Examples

Learn how to use this function in context:

- [Link Procedure Guide](/learn/link-procedure)

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

No indexed local card script currently calls this function.

This can mean the function is unused in the current script set, is only called through an alias, or is available for future/manual scripts.
