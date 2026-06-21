# Auxiliary.XyzLevelFreeTarget

## Signature

```lua
Auxiliary.XyzLevelFreeTarget(function|nil f, function|nil gf, int minct, int maxct, function|nil alterf, int|string|nil alterdesc, function|nil alterop) -> function
```

## Description

Returns the target function for Level-free Xyz Summon procedures; it chooses between alternate material and regular group selection and stores the selected group.

## Parameters

- `f` `function|nil`
- `gf` `function|nil`
- `minct` `int`
- `maxct` `int`
- `alterf` `function|nil`
- `alterdesc` `int|string|nil`
- `alterop` `function|nil`

## Returns

- `function` - Target function for a Level-free Xyz Summon procedure.

## Source

- `Utilities/procedure.lua:761`
