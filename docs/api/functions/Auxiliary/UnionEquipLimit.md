# Auxiliary.UnionEquipLimit

## Signature

```lua
Auxiliary.UnionEquipLimit(function filter) -> function
```

## Description

Returns an Equip Limit value function for modern Union monsters. It allows cards controlled by the handler's player that satisfy filter, and also keeps the current equip target legal.

## Parameters

- `filter` `function`

## Returns

- `function` - Equip Limit value function.

## Source

- `Utilities/utility.lua:391`
