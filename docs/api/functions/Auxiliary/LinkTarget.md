# Auxiliary.LinkTarget

## Signature

```lua
Auxiliary.LinkTarget(function|nil f, int minct, int maxct, function|nil gf) -> function
```

## Description

Returns the target function for Link Summon procedures; it selects a valid Link Material subgroup and stores it on the effect.

## Parameters

- `f` `function|nil`
- `minct` `int`
- `maxct` `int`
- `gf` `function|nil`

## Returns

- `function` - Target function for a Link Summon procedure.

## Source

- `Utilities/procedure.lua:2232`
