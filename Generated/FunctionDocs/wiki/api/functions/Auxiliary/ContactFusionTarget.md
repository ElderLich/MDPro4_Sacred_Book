# Auxiliary.ContactFusionTarget

## Signature

```lua
Auxiliary.ContactFusionTarget([function|nil filter], int self_location, int opponent_location) -> function
```

## Description

Returns the target function for Contact Fusion procedures. It selects Fusion Materials, keeps the selected group alive, stores it on the effect, and returns whether selection succeeded.

## Parameters

- `filter` `function|nil` optional
- `self_location` `int`
- `opponent_location` `int`

## Returns

- `function` - Target function for a Contact Fusion procedure.

## Source

- `Utilities/procedure.lua:1714`
