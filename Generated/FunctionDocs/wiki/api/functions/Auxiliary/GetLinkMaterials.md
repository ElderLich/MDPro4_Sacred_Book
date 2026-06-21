# Auxiliary.GetLinkMaterials

## Signature

```lua
Auxiliary.GetLinkMaterials(int tp, function|nil f, Card lc, Effect e) -> Group
```

## Description

Returns the available Link Materials for tp, including regular Monster Zone materials and cards allowed by extra Link Material effects.

## Parameters

- `tp` `int`
- `f` `function|nil`
- `lc` `Card`
- `e` `Effect`

## Returns

- `Group` - Available Link Materials.

## Source

- `Utilities/procedure.lua:2163`
