# RushDuel.FusionToGrave

Alias: `RD.FusionToGrave`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.FusionToGrave(any tp, any mat) -> any
```

## Description

Rush Duel helper declared in `RDFusion.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
素材去向: 墓地
```

## Parameters

- `tp` `any`: Type and behavior are not yet reviewed; see the source.
- `mat` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDFusion.lua:620`

```lua
function RushDuel.FusionToGrave(tp, mat)
    Duel.SendtoGrave(mat, REASON_EFFECT + REASON_MATERIAL + REASON_FUSION)
end
```
