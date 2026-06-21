# Auxiliary.XyzTarget

## Signature

```lua
Auxiliary.XyzTarget(function|nil f, int lv, int minct, int maxct, function|nil alterf, int|string|nil alterdesc, function|nil alterop) -> function
```

## Description

Returns the target function for standard Xyz Summon procedures; it chooses between alternate material, double-material group selection, and regular Xyz Material selection.

## Parameters

- `f` `function|nil`
- `lv` `int`
- `minct` `int`
- `maxct` `int`
- `alterf` `function|nil`
- `alterdesc` `int|string|nil`
- `alterop` `function|nil`

## Returns

- `function` - Target function for a standard Xyz Summon procedure.

## Source

- `Utilities/procedure.lua:576`
