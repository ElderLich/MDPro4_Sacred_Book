# RushDuel.IsCanAttachDirectAttack

Alias: `RD.IsCanAttachDirectAttack`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.IsCanAttachDirectAttack(any card) -> any
```

## Description

Rush Duel helper declared in `RDCondition.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
条件: 可否赋予效果 - 直接攻击
```

## Parameters

- `card` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDCondition.lua:239`

```lua
function RushDuel.IsCanAttachDirectAttack(card)
    return RushDuel.IsCanAttack(card) and not card:IsHasEffect(EFFECT_CANNOT_DIRECT_ATTACK) and not RushDuel.IsHasAttachEffect(card, EFFECT_DIRECT_ATTACK)
end
```
