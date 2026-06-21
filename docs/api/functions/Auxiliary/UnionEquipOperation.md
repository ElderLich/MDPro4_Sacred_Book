# Auxiliary.UnionEquipOperation

## Signature

```lua
Auxiliary.UnionEquipOperation(function equip_filter) -> function
```

## Description

Returns the operation function for the shared modern Union equip effect. It equips the handler to the selected target, or sends the handler to the Graveyard by rule if the target is no longer valid.

## Parameters

- `equip_filter` `function`

## Returns

- `function` - Operation function for the shared Union equip effect.

## Source

- `Utilities/utility.lua:408`
