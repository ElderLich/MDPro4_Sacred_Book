# RushDuel.IsPreviousAttack

Alias: `RD.IsPreviousAttack`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.IsPreviousAttack(any card, any atk) -> any
```

## Description

Rush Duel helper declared in `RDCondition.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
条件: 位置变化前的攻击力
```

## Parameters

- `card` `any`: Type and behavior are not yet reviewed; see the source.
- `atk` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDCondition.lua:222`

```lua
function RushDuel.IsPreviousAttack(card, atk)
    return card:GetPreviousAttackOnField() == atk
end
```
