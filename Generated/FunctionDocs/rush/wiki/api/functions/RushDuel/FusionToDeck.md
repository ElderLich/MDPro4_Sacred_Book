# RushDuel.FusionToDeck

Alias: `RD.FusionToDeck`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.FusionToDeck(any tp, any mat) -> any
```

## Description

Rush Duel helper declared in `RDFusion.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
素材去向: 卡组
```

## Parameters

- `tp` `any`: Type and behavior are not yet reviewed; see the source.
- `mat` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDFusion.lua:624`

```lua
function RushDuel.FusionToDeck(tp, mat)
    local g = mat:Filter(Card.IsFacedown, nil)
    if #g > 0 then
        Duel.ConfirmCards(1 - tp, g)
    end
    Duel.SendtoDeck(mat, nil, SEQ_DECKSHUFFLE, REASON_EFFECT + REASON_MATERIAL + REASON_FUSION)
end
```
