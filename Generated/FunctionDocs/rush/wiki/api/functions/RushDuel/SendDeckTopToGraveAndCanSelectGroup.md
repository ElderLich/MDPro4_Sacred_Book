# RushDuel.SendDeckTopToGraveAndCanSelectGroup

Alias: `RD.SendDeckTopToGraveAndCanSelectGroup`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.SendDeckTopToGraveAndCanSelectGroup(any player, any count, any desc, any hint, any filter, any check, any min, any max, ... any) -> any
```

## Description

Rush Duel helper declared in `RDAction.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
操作: 从卡组上面把卡送去墓地, 并可以选择被送去墓地的卡片 (子卡片组)
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

`Rush/Utilities/RDAction.lua:517`

```lua
function RushDuel.SendDeckTopToGraveAndCanSelectGroup(player, count, desc, hint, filter, check, min, max, ...)
    if Duel.DiscardDeck(player, count, REASON_EFFECT) ~= 0 then
        local g = Duel.GetOperatedGroup()
        local mg = g:Filter(filter, nil, ...)
        if #mg >= min then
            local sg = RushDuel.CanSelect(desc, hint, player, mg, check, min, max, ...)
            if sg and #sg > 0 then
                g:Sub(sg)
                return sg, g
            end
        end
        return Group.CreateGroup(), g
    end
    return Group.CreateGroup(), Group.CreateGroup()
end
```
