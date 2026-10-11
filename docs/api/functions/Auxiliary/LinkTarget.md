# Auxiliary.LinkTarget

## Signature

```lua
Auxiliary.LinkTarget(function|nil f, int minct, int maxct, function|nil gf) -> function
```

## Description

Returns the target function for Link Summon procedures.
The returned function selects a Link Material subgroup with Group.SelectSubGroup and Auxiliary.LCheckGoal, keeps that group alive, and stores it on the effect for LinkOperation.

## Parameters

- `f` `function|nil`
- `minct` `int`
- `maxct` `int`
- `gf` `function|nil`

## Returns

- `function` - Target function for a Link Summon procedure.

## Source

- `Utilities/procedure.lua:2232`

## Guided Examples

Learn how to use this function in context:

- [Link Procedure Guide](/learn/link-procedure)

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

No indexed local card script currently calls this function.

This can mean the function is unused in the current script set, is only called through an alias, or is available for future/manual scripts.
