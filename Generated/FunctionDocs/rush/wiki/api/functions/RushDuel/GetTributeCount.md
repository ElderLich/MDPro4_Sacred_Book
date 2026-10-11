# RushDuel.GetTributeCount

Alias: `RD.GetTributeCount`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.GetTributeCount(any card) -> any
```

## Description

Rush Duel helper declared in `RDSummon.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
获取召唤的解放数量
```

## Parameters

- `card` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDSummon.lua:214`

```lua
function RushDuel.GetTributeCount(card)
    if card:IsSummonType(SUMMON_VALUE_ZERO) then
        return 0
    elseif card:IsSummonType(SUMMON_VALUE_ONE) then
        return 1
    elseif card:IsSummonType(SUMMON_VALUE_TWO) then
        return 2
    elseif card:IsSummonType(SUMMON_VALUE_THREE) then
        return 3
    elseif card:IsLevelBelow(4) then
        return 0
    elseif card:IsLevelBelow(6) then
        return 1
    else
        return 2
    end
end
```
