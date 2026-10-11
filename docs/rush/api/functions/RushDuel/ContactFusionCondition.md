# RushDuel.ContactFusionCondition

Alias: `RD.ContactFusionCondition`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.ContactFusionCondition(any e, any c) -> any
```

## Description

Rush Duel helper declared in `RDFusion.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
接触融合术: 条件
```

## Parameters

- `e` `any`: Type and behavior are not yet reviewed; see the source.
- `c` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDFusion.lua:272`

```lua
function RushDuel.ContactFusionCondition(e, c)
    if c == nil then
        return true
    end
    if c:IsType(TYPE_PENDULUM) and c:IsFaceup() then
        return false
    end
    local tp = c:GetControler()
    RushDuel.FusionExtraChecker = RushDuel.FusionCheckLocation(e)
    local mg = Duel.GetMatchingGroup(RushDuel.ContactFusionMaterialFilter, tp, LOCATION_MZONE, 0, c, c)
    local res = c:CheckFusionMaterial(mg, nil, tp)
    RushDuel.FusionExtraChecker = nil
    return res
end
```

## Used By

Generated from the local `Rush/Scripts/` folder and `rush_cards.cdb`.

No indexed local card script currently calls this function.

This can mean the function is unused in the current script set, is only called through an alias, or is available for future/manual scripts.
