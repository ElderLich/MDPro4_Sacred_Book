# Auxiliary.XyzOperation

## Signature

```lua
Auxiliary.XyzOperation(function|nil f, int lv, int minct, int maxct, function|nil alterf, int|string|nil alterdesc, function|nil alterop) -> function
```

## Description

Returns the operation function for standard Xyz Summon procedures; it handles alternate summons, double-material count limits, sends old overlay cards to the Graveyard by rule, sets materials, and overlays them.

## Parameters

- `f` `function|nil`
- `lv` `int`
- `minct` `int`
- `maxct` `int`
- `alterf` `function|nil`
- `alterdesc` `int|string|nil`
- `alterop` `function|nil`

## Returns

- `function` - Operation function for a standard Xyz Summon procedure.

## Source

- `Utilities/procedure.lua:637`
