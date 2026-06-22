# Auxiliary.IsUnionState

## Signature

```lua
Auxiliary.IsUnionState(Effect effect) -> Card|false|nil
```

## Description

Returns the equipped Union target for effect's handler when it has EFFECT_UNION_STATUS and is equipped.
The Lua expression returns a truthy Card on success, false when the status effect is missing, or nil when no equip target exists.

## Parameters

- `effect` `Effect`

## Returns

- `Card|false|nil` - Equipped target when truthy.

## Source

- `Utilities/utility.lua:307`
