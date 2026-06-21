# Auxiliary.ContactFusionOperation

## Signature

```lua
Auxiliary.ContactFusionOperation(function mat_operation, table operation_params) -> function
```

## Description

Returns the operation function for Contact Fusion procedures. It sets the selected materials on the Fusion Monster, runs mat_operation, and deletes the kept-alive group.

## Parameters

- `mat_operation` `function`
- `operation_params` `table`

## Returns

- `function` - Operation function for a Contact Fusion procedure.

## Source

- `Utilities/procedure.lua:1725`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

No indexed local card script currently calls this function.

This can mean the function is unused in the current script set, is only called through an alias, or is available for future/manual scripts.
