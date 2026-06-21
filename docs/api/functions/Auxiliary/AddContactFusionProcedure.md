# Auxiliary.AddContactFusionProcedure

## Signature

```lua
Auxiliary.AddContactFusionProcedure(Card c, function filter, [int self_location], [int opponent_location], function mat_operation, ... any) -> Effect
```

## Description

Registers a Contact Fusion Special Summon procedure on c, using material filter locations and the provided material operation, and returns the created procedure effect.

## Parameters

- `c` `Card`
- `filter` `function`
- `self_location` `int` optional
- `opponent_location` `int` optional
- `mat_operation` `function`
- `...` `any`

## Returns

- `Effect` - The created Contact Fusion procedure effect.

## Source

- `Utilities/procedure.lua:1687`
