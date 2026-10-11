# RushDuel.IsSpecialSummonMainPhase

Alias: `RD.IsSpecialSummonMainPhase`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.IsSpecialSummonMainPhase(any card, any type) -> any
```

## Description

Rush Duel helper declared in `RDCondition.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
条件: 这张卡特殊召唤的自己主要阶段
```

## Parameters

- `card` `any`: Type and behavior are not yet reviewed; see the source.
- `type` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDCondition.lua:42`

```lua
function RushDuel.IsSpecialSummonMainPhase(card, type)
    return card:IsReason(REASON_SPSUMMON) and card:IsStatus(STATUS_SPSUMMON_TURN) and card:GetFlagEffect(FLAG_SUMMON_MAIN_PHASE) ~= 0
        and (not type or card:IsSummonType(type))
end
```
