# RushDuel.IsCanAttachTripleTribute

Alias: `RD.IsCanAttachTripleTribute`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.IsCanAttachTripleTribute(any card, any value) -> any
```

## Description

Rush Duel helper declared in `RDCondition.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
条件: 可否赋予效果 - 三重解放
```

## Parameters

- `card` `any`: Type and behavior are not yet reviewed; see the source.
- `value` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDCondition.lua:288`

```lua
function RushDuel.IsCanAttachTripleTribute(card, value)
    if Duel.IsPlayerAffectedByEffect(card:GetControler(), EFFECT_CANNOT_DOUBLE_TRIBUTE) then
        return false
    end
    if card:IsHasEffect(EFFECT_UNRELEASABLE_SUM) then
        return false
    end
    local values = RushDuel.GetEffectValues(card, EFFECT_TRIPLE_TRIBUTE)
    return RushDuel.CheckValueDoubleTribute(values, value)
end
```
