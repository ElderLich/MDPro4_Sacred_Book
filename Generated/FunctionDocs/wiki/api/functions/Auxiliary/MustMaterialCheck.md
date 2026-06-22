# Auxiliary.MustMaterialCheck

## Signature

```lua
Auxiliary.MustMaterialCheck(Card|Group|nil v, int tp, int code) -> bool
```

## Description

Checks whether tp's required-material effects of type code are satisfied.
When v is nil, the helper succeeds only if Duel.GetMustMaterial(tp, code) is empty, except for the hard-coded Xyz and Synchro material exceptions present in the utility script. When v is supplied, it returns Duel.CheckMustMaterial(tp, v, code).

## Parameters

- `v` `Card|Group|nil`
- `tp` `int`
- `code` `int`

## Returns

- `bool`

## Source

- `Utilities/procedure.lua:2274`
