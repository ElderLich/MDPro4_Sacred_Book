# RushDuel.IsSummonOrSpecialSummonMainPhase

Alias: `RD.IsSummonOrSpecialSummonMainPhase`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.IsSummonOrSpecialSummonMainPhase(any card) -> any
```

## Description

Rush Duel helper declared in `RDCondition.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
条件: 这张卡召唤·特殊召唤的自己主要阶段
```

## Parameters

- `card` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDCondition.lua:47`

```lua
function RushDuel.IsSummonOrSpecialSummonMainPhase(card)
    return card:IsReason(REASON_SUMMON + REASON_SPSUMMON) and card:IsStatus(STATUS_SUMMON_TURN + STATUS_SPSUMMON_TURN)
        and card:GetFlagEffect(FLAG_SUMMON_MAIN_PHASE) ~= 0
end
```
