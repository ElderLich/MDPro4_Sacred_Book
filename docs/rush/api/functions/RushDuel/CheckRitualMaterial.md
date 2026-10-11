# RushDuel.CheckRitualMaterial

Alias: `RD.CheckRitualMaterial`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.CheckRitualMaterial(any tp, any rc, any type, any mat, any gc) -> any
```

## Description

Rush Duel helper declared in `RDRitual.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
仪式召唤 - 检测仪式素材
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

`Rush/Utilities/RDRitual.lua:155`

```lua
function RushDuel.CheckRitualMaterial(tp, rc, type, mat, gc)
    local mg, max = RushDuel.GetRitualMaterial(tp, rc, type, mat)
    Auxiliary.GCheckAdditional = RushDuel.RitualCheckAdditional(rc, type)
    local minc = RushDuel.MinRitualMaterialCount or 1
    local maxc = RushDuel.MaxRitualMaterialCount or max
    local res = mg:CheckSubGroup(RushDuel.RitualChecker, minc, maxc, rc, tp, type, gc)
    Auxiliary.GCheckAdditional = nil
    return res
end
```

## Used By

Generated from the local `Rush/Scripts/` folder and `rush_cards.cdb`.

No indexed local card script currently calls this function.

This can mean the function is unused in the current script set, is only called through an alias, or is available for future/manual scripts.
