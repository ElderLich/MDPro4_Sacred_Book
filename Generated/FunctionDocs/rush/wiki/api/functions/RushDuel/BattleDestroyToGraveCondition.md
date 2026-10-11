# RushDuel.BattleDestroyToGraveCondition

Alias: `RD.BattleDestroyToGraveCondition`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.BattleDestroyToGraveCondition(any condition) -> any
```

## Description

Rush Duel helper declared in `RDContinuous.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

## Parameters

- `condition` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDContinuous.lua:96`

```lua
function RushDuel.BattleDestroyToGraveCondition(condition)
    return function(e, tp, eg, ep, ev, re, r, rp)
        local c = e:GetHandler()
        local tc = c:GetBattleTarget()
        return c:IsRelateToBattle() and tc:IsLocation(LOCATION_GRAVE) and tc:IsType(TYPE_MONSTER) and (not condition or condition(e, tp, eg, ep, ev, re, r, rp))
    end
end
```
