# RushDuel.AddHandConfirmSpecialSummonProcedure

Alias: `RD.AddHandConfirmSpecialSummonProcedure`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.AddHandConfirmSpecialSummonProcedure(any card, any desc, any filter, any value, any position) -> any
```

## Description

Rush Duel helper declared in `RDSummon.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
添加手卡特殊召唤手续: 把手卡1张卡给对方观看
```

## Parameters

- `card` `any`: Type and behavior are not yet reviewed; see the source.
- `desc` `any`: Type and behavior are not yet reviewed; see the source.
- `filter` `any`: Type and behavior are not yet reviewed; see the source.
- `value` `any`: Type and behavior are not yet reviewed; see the source.
- `position` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDSummon.lua:411`

```lua
function RushDuel.AddHandConfirmSpecialSummonProcedure(card, desc, filter, value, position)
    local con = RushDuel.HandConfirmSpecialSummonCondition(filter)
    local tg = RushDuel.HandConfirmSpecialSummonTarget(filter)
    local op = RushDuel.HandConfirmSpecialSummonOperation
    local e1 = RD.AddHandSpecialSummonProcedure(card, desc, con, tg, op, value, position)
    return e1
end
```
