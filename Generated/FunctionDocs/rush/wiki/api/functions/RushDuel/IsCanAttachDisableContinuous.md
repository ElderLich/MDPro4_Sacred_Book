# RushDuel.IsCanAttachDisableContinuous

Alias: `RD.IsCanAttachDisableContinuous`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.IsCanAttachDisableContinuous(any card) -> any
```

## Description

Rush Duel helper declared in `RDCondition.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
条件: 可否赋予效果 - 永续效果无效化
```

## Parameters

- `card` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDCondition.lua:346`

```lua
function RushDuel.IsCanAttachDisableContinuous(card)
    return RushDuel.IsHasContinuousEffect(card) and not card:IsHasEffect(EFFECT_DISABLE)
end
```
