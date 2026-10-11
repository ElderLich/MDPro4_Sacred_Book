# RushDuel.AttachTripleTribute

Alias: `RD.AttachTripleTribute`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.AttachTripleTribute(any e, any card, any value, any desc1, any desc2, any reset, any forced) -> any
```

## Description

Rush Duel helper declared in `RDAttach.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
赋予: 三重解放
```

## Parameters

- `e` `any`: Type and behavior are not yet reviewed; see the source.
- `card` `any`: Type and behavior are not yet reviewed; see the source.
- `value` `any`: Type and behavior are not yet reviewed; see the source.
- `desc1` `any`: Type and behavior are not yet reviewed; see the source.
- `desc2` `any`: Type and behavior are not yet reviewed; see the source.
- `reset` `any`: Type and behavior are not yet reviewed; see the source.
- `forced` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDAttach.lua:46`

```lua
function RushDuel.AttachTripleTribute(e, card, value, desc1, desc2, reset, forced)
    local e1 = RushDuel.CreateSingleEffect(e, desc1, card, EFFECT_TRIPLE_TRIBUTE, value, reset, forced)
    local e2 = RushDuel.CreateTripleTribute(e:GetHandler(), card, desc2, value, forced)
    e2:SetReset(reset)
    return e1, e2
end
```
