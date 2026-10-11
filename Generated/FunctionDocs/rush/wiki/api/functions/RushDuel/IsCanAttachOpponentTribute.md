# RushDuel.IsCanAttachOpponentTribute

Alias: `RD.IsCanAttachOpponentTribute`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.IsCanAttachOpponentTribute(any card, any player, any flag) -> any
```

## Description

Rush Duel helper declared in `RDCondition.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
条件: 可否赋予效果 - 使用对方的怪兽解放
```

## Parameters

- `card` `any`: Type and behavior are not yet reviewed; see the source.
- `player` `any`: Type and behavior are not yet reviewed; see the source.
- `flag` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDCondition.lua:299`

```lua
function RushDuel.IsCanAttachOpponentTribute(card, player, flag)
    if Duel.IsPlayerAffectedByEffect(player, EFFECT_CANNOT_SINGLE_TRIBUTE) and Duel.IsPlayerAffectedByEffect(player, EFFECT_CANNOT_DOUBLE_TRIBUTE) then
        return false
    end
    return not card:IsHasEffect(EFFECT_UNRELEASABLE_SUM) and card:GetFlagEffect(flag) == 0
end
```
