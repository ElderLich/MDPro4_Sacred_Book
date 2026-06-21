# Auxiliary.ContactFusionMaterialFilter

## Signature

```lua
Auxiliary.ContactFusionMaterialFilter(Card c, Card fc, [function|nil filter]) -> bool
```

## Description

Material filter for Contact Fusion procedures. The card must be usable as Fusion Material for fc and must satisfy filter when one is provided.

## Parameters

- `c` `Card`
- `fc` `Card`
- `filter` `function|nil` optional

## Returns

- `bool` - true if c is valid Contact Fusion material for fc.

## Source

- `Utilities/procedure.lua:1702`
