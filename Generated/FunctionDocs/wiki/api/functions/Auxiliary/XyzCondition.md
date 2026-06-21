# Auxiliary.XyzCondition

## Signature

```lua
Auxiliary.XyzCondition(function|nil f, int lv, int minct, int maxct, function|nil alterf, int|string|nil alterdesc, function|nil alterop) -> function
```

## Description

Returns the condition function for standard Xyz Summon procedures, including optional alternate one-card Xyz Summon and EFFECT_DOUBLE_XMATERIAL handling.

## Parameters

- `f` `function|nil`
- `lv` `int`
- `minct` `int`
- `maxct` `int`
- `alterf` `function|nil`
- `alterdesc` `int|string|nil`
- `alterop` `function|nil`

## Returns

- `function` - Condition function for a standard Xyz Summon procedure.

## Source

- `Utilities/procedure.lua:499`
