# RushDuel.AddPrimeSummonProcedure

Alias: `RD.AddPrimeSummonProcedure`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.AddPrimeSummonProcedure(any card, any desc, any attack, any filter) -> any
```

## Description

Rush Duel helper declared in `RDSummon.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
添加解放1只的妥协召唤手续 (改变原本攻击力)
```

## Parameters

- `card` `any`: Type and behavior are not yet reviewed; see the source.
- `desc` `any`: Type and behavior are not yet reviewed; see the source.
- `attack` `any`: Type and behavior are not yet reviewed; see the source.
- `filter` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDSummon.lua:175`

```lua
function RushDuel.AddPrimeSummonProcedure(card, desc, attack, filter)
    return RushDuel.AddSummonProcedureOne(card, desc, nil, filter, RushDuel.SummonAttackChangeOperation(attack))
end
```
