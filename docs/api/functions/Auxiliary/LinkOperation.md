# Auxiliary.LinkOperation

## Signature

```lua
Auxiliary.LinkOperation(function|nil f, int minct, int maxct, function|nil gf) -> function
```

## Description

Returns the operation function for Link Summon procedures; it sets the materials, consumes extra-material count limits, and sends the materials to the Graveyard.

## Parameters

- `f` `function|nil`
- `minct` `int`
- `maxct` `int`
- `gf` `function|nil`

## Returns

- `function` - Operation function for a Link Summon procedure.

## Source

- `Utilities/procedure.lua:2263`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

No indexed local card script currently calls this function.

This can mean the function is unused in the current script set, is only called through an alias, or is available for future/manual scripts.
