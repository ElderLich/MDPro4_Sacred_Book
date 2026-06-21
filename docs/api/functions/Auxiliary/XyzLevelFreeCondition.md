# Auxiliary.XyzLevelFreeCondition

## Signature

```lua
Auxiliary.XyzLevelFreeCondition(function|nil f, function|nil gf, int minct, int maxct, function|nil alterf, int|string|nil alterdesc, function|nil alterop) -> function
```

## Description

Returns the condition function for Level-free Xyz Summon procedures with optional group filter and alternate one-card Xyz Summon support.

## Parameters

- `f` `function|nil`
- `gf` `function|nil`
- `minct` `int`
- `maxct` `int`
- `alterf` `function|nil`
- `alterdesc` `int|string|nil`
- `alterop` `function|nil`

## Returns

- `function` - Condition function for a Level-free Xyz Summon procedure.

## Source

- `Utilities/procedure.lua:728`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

No indexed local card script currently calls this function.

This can mean the function is unused in the current script set, is only called through an alias, or is available for future/manual scripts.
