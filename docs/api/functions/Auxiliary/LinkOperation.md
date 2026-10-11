# Auxiliary.LinkOperation

## Signature

```lua
Auxiliary.LinkOperation(function|nil f, int minct, int maxct, function|nil gf) -> function
```

## Description

Returns the operation function for Link Summon procedures.
The returned function reads the selected group from the effect label object, records it with Card.SetMaterial, consumes valid extra-material count limits, sends the materials to the GY with REASON_MATERIAL+REASON_LINK, and deletes the kept-alive group.

## Parameters

- `f` `function|nil`
- `minct` `int`
- `maxct` `int`
- `gf` `function|nil`

## Returns

- `function` - Operation function for a Link Summon procedure.

## Source

- `Utilities/procedure.lua:2263`

## Guided Examples

Learn how to use this function in context:

- [Link Procedure Guide](/learn/link-procedure)

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

No indexed local card script currently calls this function.

This can mean the function is unused in the current script set, is only called through an alias, or is available for future/manual scripts.
