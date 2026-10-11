# RushDuel.RevealDeckTopAndCanSelectGroup

Alias: `RD.RevealDeckTopAndCanSelectGroup`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.RevealDeckTopAndCanSelectGroup(any player, any count, any desc, any hint, any filter, any check, any min, any max, ... any) -> any
```

## Description

Rush Duel helper declared in `RDAction.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
操作: 翻开卡组并可以选择卡 (子卡片组)
```

## Parameters

- `player` `any`: Type and behavior are not yet reviewed; see the source.
- `count` `any`: Type and behavior are not yet reviewed; see the source.
- `desc` `any`: Type and behavior are not yet reviewed; see the source.
- `hint` `any`: Type and behavior are not yet reviewed; see the source.
- `filter` `any`: Type and behavior are not yet reviewed; see the source.
- `check` `any`: Type and behavior are not yet reviewed; see the source.
- `min` `any`: Type and behavior are not yet reviewed; see the source.
- `max` `any`: Type and behavior are not yet reviewed; see the source.
- `...` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDAction.lua:456`

```lua
function RushDuel.RevealDeckTopAndCanSelectGroup(player, count, desc, hint, filter, check, min, max, ...)
    Duel.ConfirmDecktop(player, count)
    local g = Duel.GetDecktopGroup(player, count)
    local mg = g:Filter(filter, nil, ...)
    if mg:CheckSubGroup(check, min, max, ...) then
        local sg = RushDuel.CanSelect(desc, hint, player, mg, check, min, max, ...)
        if sg and #sg > 0 then
            g:Sub(sg)
            return sg, g
        end
    end
    return Group.CreateGroup(), g
end
```
