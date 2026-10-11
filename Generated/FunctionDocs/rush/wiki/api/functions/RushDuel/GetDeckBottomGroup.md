# RushDuel.GetDeckBottomGroup

Alias: `RD.GetDeckBottomGroup`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.GetDeckBottomGroup(any player, any count) -> any
```

## Description

Rush Duel helper declared in `RDFunction.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
获取卡组底的N张卡
```

## Parameters

- `player` `any`: Type and behavior are not yet reviewed; see the source.
- `count` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDFunction.lua:152`

```lua
function RushDuel.GetDeckBottomGroup(player, count)
    local dg = Duel.GetFieldGroup(player, LOCATION_DECK, 0)
    local ct = #dg
    if (count < ct) then
        local top = Duel.GetDecktopGroup(player, ct - count)
        dg:Sub(top)
    end
    return dg
end
```
