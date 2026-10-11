# RushDuel.IsCanAttachCannotTrigger

Alias: `RD.IsCanAttachCannotTrigger`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.IsCanAttachCannotTrigger(any card) -> any
```

## Description

Rush Duel helper declared in `RDCondition.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
条件: 可否赋予效果 - 不能发动效果
```

## Parameters

- `card` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDCondition.lua:350`

```lua
function RushDuel.IsCanAttachCannotTrigger(card)
    return not card:IsHasEffect(EFFECT_CANNOT_TRIGGER)
end
```
