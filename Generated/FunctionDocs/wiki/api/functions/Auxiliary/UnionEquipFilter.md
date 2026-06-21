# Auxiliary.UnionEquipFilter

## Signature

```lua
Auxiliary.UnionEquipFilter(function filter) -> function
```

## Description

Returns a filter for modern Union equip effects. The target must be face-up, controlled by tp, have no modern Union monster equipped, and satisfy filter.

## Parameters

- `filter` `function`

## Returns

- `function` - Filter function taking Card c and int tp.

## Source

- `Utilities/utility.lua:385`
