# RushDuel.AttachSummonNotChainTrapLimit

Alias: `RD.AttachSummonNotChainTrapLimit`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.AttachSummonNotChainTrapLimit(any e, any rp, any tp) -> any
```

## Description

Rush Duel helper declared in `RDContinuous.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

## Parameters

- `e` `any`: Type and behavior are not yet reviewed; see the source.
- `rp` `any`: Type and behavior are not yet reviewed; see the source.
- `tp` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDContinuous.lua:62`

```lua
function RushDuel.AttachSummonNotChainTrapLimit(e, rp, tp)
    return not (rp ~= tp and e:IsHasType(EFFECT_TYPE_ACTIVATE) and e:IsActiveType(TYPE_TRAP))
end
```
