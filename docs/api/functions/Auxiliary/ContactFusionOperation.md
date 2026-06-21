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
