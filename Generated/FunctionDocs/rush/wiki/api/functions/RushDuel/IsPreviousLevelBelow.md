# RushDuel.IsPreviousLevelBelow

Alias: `RD.IsPreviousLevelBelow`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.IsPreviousLevelBelow(any card, any level) -> any
```

## Description

Rush Duel helper declared in `RDCondition.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
条件: 位置变化前的等级小于
```

## Parameters

- `card` `any`: Type and behavior are not yet reviewed; see the source.
- `level` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDCondition.lua:218`

```lua
function RushDuel.IsPreviousLevelBelow(card, level)
    return card:GetPreviousLevelOnField() > 0 and card:GetPreviousLevelOnField() <= level
end
```
