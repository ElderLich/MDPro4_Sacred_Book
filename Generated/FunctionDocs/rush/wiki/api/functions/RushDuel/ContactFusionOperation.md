# RushDuel.ContactFusionOperation

Alias: `RD.ContactFusionOperation`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.ContactFusionOperation(any e, any tp, any eg, any ep, any ev, any re, any r, any rp, any c) -> any
```

## Description

Rush Duel helper declared in `RDFusion.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
接触融合术: 处理
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
- `c` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDFusion.lua:301`

```lua
function RushDuel.ContactFusionOperation(e, tp, eg, ep, ev, re, r, rp, c)
    local g = e:GetLabelObject()
    c:SetMaterial(g)
    Duel.SendtoDeck(g, nil, SEQ_DECKSHUFFLE, REASON_MATERIAL + REASON_FUSION + REASON_COST)
    g:DeleteGroup()
end
```
