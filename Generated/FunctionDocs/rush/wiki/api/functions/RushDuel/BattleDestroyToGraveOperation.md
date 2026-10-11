# RushDuel.BattleDestroyToGraveOperation

Alias: `RD.BattleDestroyToGraveOperation`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.BattleDestroyToGraveOperation(any operation) -> any
```

## Description

Rush Duel helper declared in `RDContinuous.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

## Parameters

- `operation` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDContinuous.lua:103`

```lua
function RushDuel.BattleDestroyToGraveOperation(operation)
    return function(e, tp, eg, ep, ev, re, r, rp)
        local tc = e:GetHandler():GetBattleTarget()
        operation(e, tp, eg, ep, ev, re, r, rp, tc)
    end
end
```
