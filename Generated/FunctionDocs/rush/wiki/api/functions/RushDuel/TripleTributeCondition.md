# RushDuel.TripleTributeCondition

Alias: `RD.TripleTributeCondition`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.TripleTributeCondition(any e, any c, any minc) -> any
```

## Description

Rush Duel helper declared in `RDSummon.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

## Parameters

- `e` `any`: Type and behavior are not yet reviewed; see the source.
- `c` `any`: Type and behavior are not yet reviewed; see the source.
- `minc` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDSummon.lua:341`

```lua
function RushDuel.TripleTributeCondition(e, c, minc)
    if c == nil then
        return true
    end
    local tc = e:GetHandler()
    local tp = c:GetControler()
    local mg = Duel.GetTributeGroup(c)
    return minc <= 3 and mg:IsContains(tc) and Duel.GetMZoneCount(tp, tc) > 0
end
```
