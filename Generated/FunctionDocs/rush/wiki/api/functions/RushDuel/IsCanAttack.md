# RushDuel.IsCanAttack

Alias: `RD.IsCanAttack`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.IsCanAttack(any card) -> any
```

## Description

Rush Duel helper declared in `RDCondition.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
条件: 可以攻击
```

## Parameters

- `card` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDCondition.lua:231`

```lua
function RushDuel.IsCanAttack(card)
    return not card:IsHasEffect(EFFECT_CANNOT_ATTACK)
end
```
