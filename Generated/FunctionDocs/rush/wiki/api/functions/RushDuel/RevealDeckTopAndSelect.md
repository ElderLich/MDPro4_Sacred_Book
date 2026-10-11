# RushDuel.RevealDeckTopAndSelect

Alias: `RD.RevealDeckTopAndSelect`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.RevealDeckTopAndSelect(any player, any count, any hint, any filter, any min, any max, ... any) -> any
```

## Description

Rush Duel helper declared in `RDAction.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
操作: 翻开卡组并选择卡
```

## Parameters

- `player` `any`: Type and behavior are not yet reviewed; see the source.
- `count` `any`: Type and behavior are not yet reviewed; see the source.
- `hint` `any`: Type and behavior are not yet reviewed; see the source.
- `filter` `any`: Type and behavior are not yet reviewed; see the source.
- `min` `any`: Type and behavior are not yet reviewed; see the source.
- `max` `any`: Type and behavior are not yet reviewed; see the source.
- `...` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDAction.lua:427`

```lua
function RushDuel.RevealDeckTopAndSelect(player, count, hint, filter, min, max, ...)
    Duel.ConfirmDecktop(player, count)
    local g = Duel.GetDecktopGroup(player, count)
    local mg = g:Filter(filter, nil, ...)
    if #mg >= min then
        local sg = RushDuel.Select(hint, player, mg, nil, false, min, max)
        if sg and #sg > 0 then
            g:Sub(sg)
            return sg, g
        end
    else
        return Group.CreateGroup(), g
    end
end
```
