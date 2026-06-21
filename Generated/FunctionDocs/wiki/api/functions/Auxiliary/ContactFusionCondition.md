# Auxiliary.ContactFusionCondition

## Signature

```lua
Auxiliary.ContactFusionCondition([function|nil filter], int self_location, int opponent_location) -> function
```

## Description

Returns the condition function for Contact Fusion procedures. It collects valid materials from the configured locations and checks c's Fusion Material requirement.

## Parameters

- `filter` `function|nil` optional
- `self_location` `int`
- `opponent_location` `int`

## Returns

- `function` - Condition function for a Contact Fusion procedure.

## Source

- `Utilities/procedure.lua:1705`
