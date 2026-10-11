# RushDuel.SelectRitualMaterial

Alias: `RD.SelectRitualMaterial`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.SelectRitualMaterial(any tp, any rc, any type, any mat, any gc) -> any
```

## Description

Rush Duel helper declared in `RDRitual.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
仪式召唤 - 选择仪式素材
```

## Parameters

- `tp` `any`: Type and behavior are not yet reviewed; see the source.
- `rc` `any`: Type and behavior are not yet reviewed; see the source.
- `type` `any`: Type and behavior are not yet reviewed; see the source.
- `mat` `any`: Type and behavior are not yet reviewed; see the source.
- `gc` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDRitual.lua:165`

```lua
function RushDuel.SelectRitualMaterial(tp, rc, type, mat, gc)
    local mg, max = RushDuel.GetRitualMaterial(tp, rc, type, mat)
    Auxiliary.GCheckAdditional = RushDuel.RitualCheckAdditional(rc, type)
    local minc = RushDuel.MinRitualMaterialCount or 1
    local maxc = RushDuel.MaxRitualMaterialCount or max
    local sg = RushDuel.Select(HINTMSG_RITUAL_MATERIAL, tp, mg, RushDuel.RitualChecker, true, minc, maxc, rc, tp, type, gc)
    Auxiliary.GCheckAdditional = nil
    return sg
end
```
