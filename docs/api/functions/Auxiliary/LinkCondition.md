# Auxiliary.LinkCondition

## Signature

```lua
Auxiliary.LinkCondition(function|nil f, int minct, int maxct, function|nil gf) -> function
```

## Description

Returns the condition function for Link Summon procedures.
The returned function rejects face-up Pendulum Link Monsters in the Extra Deck, builds or filters the material pool, applies runtime min/max limits, includes required lmat material when supplied, checks EFFECT_MUST_BE_LMATERIAL, and asks whether a valid subgroup exists.

## Parameters

- `f` `function|nil`
- `minct` `int`
- `maxct` `int`
- `gf` `function|nil`

## Returns

- `function` - Condition function for a Link Summon procedure.

## Source

- `Utilities/procedure.lua:2204`

## Guided Examples

Learn how to use this function in context:

- [Link Procedure Guide](/learn/link-procedure)

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

No indexed local card script currently calls this function.

This can mean the function is unused in the current script set, is only called through an alias, or is available for future/manual scripts.
