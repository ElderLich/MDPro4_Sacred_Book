# RushDuel.SendToGraveAndExists

Alias: `RD.SendToGraveAndExists`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.SendToGraveAndExists(any target, any filter, any count, any expect) -> any
```

## Description

Rush Duel helper declared in `RDAction.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
操作: 送去墓地
```

## Parameters

- `target` `any`: Type and behavior are not yet reviewed; see the source.
- `filter` `any`: Type and behavior are not yet reviewed; see the source.
- `count` `any`: Type and behavior are not yet reviewed; see the source.
- `expect` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDAction.lua:299`

```lua
function RushDuel.SendToGraveAndExists(target, filter, count, expect)
    local g = RushDuel.ToMaximunGroup(target)
    return Duel.SendtoGrave(g, REASON_EFFECT) ~= 0 and RushDuel.IsOperatedGroupExists(filter, count, expect)
end
```
