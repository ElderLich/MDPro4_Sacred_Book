# RushDuel.FusionMaterialFilter

Alias: `RD.FusionMaterialFilter`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.FusionMaterialFilter(any c, any filter, any e) -> any
```

## Description

Rush Duel helper declared in `RDFusion.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
融合召唤 - 素材过滤
```

## Parameters

- `c` `any`: Type and behavior are not yet reviewed; see the source.
- `filter` `any`: Type and behavior are not yet reviewed; see the source.
- `e` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDFusion.lua:396`

```lua
function RushDuel.FusionMaterialFilter(c, filter, e)
    return (not filter or filter(c)) and (not e or not c:IsImmuneToEffect(e))
end
```

## Used By

Generated from the local `Rush/Scripts/` folder and `rush_cards.cdb`.

No indexed local card script currently calls this function.

This can mean the function is unused in the current script set, is only called through an alias, or is available for future/manual scripts.
