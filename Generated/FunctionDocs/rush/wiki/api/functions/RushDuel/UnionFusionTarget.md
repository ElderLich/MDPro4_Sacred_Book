# RushDuel.UnionFusionTarget

Alias: `RD.UnionFusionTarget`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.UnionFusionTarget(any e, any tp, any eg, any ep, any ev, any re, any r, any rp, any chk, any c) -> any
```

## Description

Rush Duel helper declared in `RDFusion.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
同盟融合术: 对象
```

## Parameters

- `e` `any`: Type and behavior are not yet reviewed; see the source.
- `tp` `any`: Type and behavior are not yet reviewed; see the source.
- `eg` `any`: Type and behavior are not yet reviewed; see the source.
- `ep` `any`: Type and behavior are not yet reviewed; see the source.
- `ev` `any`: Type and behavior are not yet reviewed; see the source.
- `re` `any`: Type and behavior are not yet reviewed; see the source.
- `r` `any`: Type and behavior are not yet reviewed; see the source.
- `rp` `any`: Type and behavior are not yet reviewed; see the source.
- `chk` `any`: Type and behavior are not yet reviewed; see the source.
- `c` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDFusion.lua:343`

```lua
function RushDuel.UnionFusionTarget(e, tp, eg, ep, ev, re, r, rp, chk, c)
    RushDuel.FusionExtraChecker = RushDuel.FusionCheckLocation(e)
    local mg = Duel.GetMatchingGroup(RushDuel.UnionFusionMaterialFilter, tp, LOCATION_ONFIELD, 0, c, c)
    local g = Duel.SelectFusionMaterial(tp, c, mg, nil, tp)
    RushDuel.FusionExtraChecker = nil
    if #g > 0 then
        g:KeepAlive()
        e:SetLabelObject(g)
        return true
    else
        return false
    end
end
```
