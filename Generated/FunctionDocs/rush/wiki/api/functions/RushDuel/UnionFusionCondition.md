# RushDuel.UnionFusionCondition

Alias: `RD.UnionFusionCondition`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.UnionFusionCondition(any e, any c) -> any
```

## Description

Rush Duel helper declared in `RDFusion.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
同盟融合术: 条件
```

## Parameters

- `e` `any`: Type and behavior are not yet reviewed; see the source.
- `c` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDFusion.lua:328`

```lua
function RushDuel.UnionFusionCondition(e, c)
    if c == nil then
        return true
    end
    if c:IsType(TYPE_PENDULUM) and c:IsFaceup() then
        return false
    end
    local tp = c:GetControler()
    RushDuel.FusionExtraChecker = RushDuel.FusionCheckLocation(e)
    local mg = Duel.GetMatchingGroup(RushDuel.UnionFusionMaterialFilter, tp, LOCATION_ONFIELD, 0, c, c)
    local res = c:CheckFusionMaterial(mg, nil, tp)
    RushDuel.FusionExtraChecker = nil
    return res
end
```
