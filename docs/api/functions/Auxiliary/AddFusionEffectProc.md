# Auxiliary.AddFusionEffectProc

## Signature

```lua
Auxiliary.AddFusionEffectProc(Card c, function filter, int mat_location, [function|nil mat_filter], [function|nil mat_operation], [table|nil params]) -> Effect
```

## Description

Convenience wrapper for Auxiliary.AddFusionEffectProcUltimate. It builds a params table from the common arguments and returns the created Fusion effect.

## Parameters

- `c` `Card`
- `filter` `function`
- `mat_location` `int`
- `mat_filter` `function|nil` optional
- `mat_operation` `function|nil` optional
- `params` `table|nil` optional

## Returns

- `Effect` - The created Fusion effect.

## Source

- `Utilities/procedure.lua:1677`
