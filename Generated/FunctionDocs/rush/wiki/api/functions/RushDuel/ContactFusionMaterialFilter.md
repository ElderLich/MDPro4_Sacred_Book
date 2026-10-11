# RushDuel.ContactFusionMaterialFilter

Alias: `RD.ContactFusionMaterialFilter`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.ContactFusionMaterialFilter(any c, any fc) -> any
```

## Description

Rush Duel helper declared in `RDFusion.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
接触融合术: 素材过滤
```

## Parameters

- `c` `any`: Type and behavior are not yet reviewed; see the source.
- `fc` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDFusion.lua:268`

```lua
function RushDuel.ContactFusionMaterialFilter(c, fc)
    return c:IsFaceup() and c:IsCanBeFusionMaterial(fc) and c:IsAbleToDeckOrExtraAsCost()
end
```
