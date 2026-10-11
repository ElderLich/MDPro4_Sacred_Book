# RushDuel.IsCanAttachPierce

Alias: `RD.IsCanAttachPierce`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.IsCanAttachPierce(any card) -> any
```

## Description

Rush Duel helper declared in `RDCondition.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
条件: 可否赋予效果 - 贯通
```

## Parameters

- `card` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDCondition.lua:243`

```lua
function RushDuel.IsCanAttachPierce(card)
    return RushDuel.IsCanAttack(card) and not RushDuel.IsHasAttachEffect(card, EFFECT_PIERCE)
end
```
