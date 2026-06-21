# Auxiliary.MustMaterialCheck

## Signature

```lua
Auxiliary.MustMaterialCheck(any v, int tp, Effect code) -> void
```

## Description

Check if value contains cards or a group affected by player's effect type code
Currently involved codes are:
EFFECT_MUST_BE_SMATERIAL
EFFECT_MUST_BE_XMATERIAL
EFFECT_MUST_BE_FMATERIAL
EFFECT_MUST_BE_LMATERIAL
All are checks for required materials

## Parameters

- `v` `any`
- `tp` `int`
- `code` `Effect`

## Source

- `Utilities/procedure.lua:2274`
