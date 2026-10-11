# RushDuel.IsOperatedGroupExists

Alias: `RD.IsOperatedGroupExists`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.IsOperatedGroupExists(any filter, any count, any expect) -> any
```

## Description

Rush Duel helper declared in `RDCondition.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
额外条件: 最后的操作是否包含某种卡
```

## Parameters

- `filter` `any`: Type and behavior are not yet reviewed; see the source.
- `count` `any`: Type and behavior are not yet reviewed; see the source.
- `expect` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDCondition.lua:422`

```lua
function RushDuel.IsOperatedGroupExists(filter, count, expect)
    return filter == nil or Duel.GetOperatedGroup():IsExists(filter, count, expect)
end
```
