# RushDuel.GroupAllCount

Alias: `RD.GroupAllCount`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.GroupAllCount(any group, any filter, any count, ... any) -> any
```

## Description

Rush Duel helper declared in `RDCondition.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
条件: 卡片组全部满足条件与数量
```

## Parameters

- `group` `any`: Type and behavior are not yet reviewed; see the source.
- `filter` `any`: Type and behavior are not yet reviewed; see the source.
- `count` `any`: Type and behavior are not yet reviewed; see the source.
- `...` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDCondition.lua:427`

```lua
function RushDuel.GroupAllCount(group, filter, count, ...)
    return group:GetCount() == count and group:FilterCount(filter, nil, ...) == count
end
```

## Used By

Generated from the local `Rush/Scripts/` folder and `rush_cards.cdb`.

No indexed local card script currently calls this function.

This can mean the function is unused in the current script set, is only called through an alias, or is available for future/manual scripts.
