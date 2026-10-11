# RushDuel.AddHealthySummonProcedure

Alias: `RD.AddHealthySummonProcedure`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.AddHealthySummonProcedure(any card, any desc, any attack) -> any
```

## Description

Rush Duel helper declared in `RDSummon.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
添加不用解放的妥协召唤手续 (改变原本攻击力)
```

## Parameters

- `card` `any`: Type and behavior are not yet reviewed; see the source.
- `desc` `any`: Type and behavior are not yet reviewed; see the source.
- `attack` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDSummon.lua:170`

```lua
function RushDuel.AddHealthySummonProcedure(card, desc, attack)
    return RushDuel.AddSummonProcedureZero(card, desc, nil, RushDuel.SummonAttackChangeOperation(attack))
end
```
