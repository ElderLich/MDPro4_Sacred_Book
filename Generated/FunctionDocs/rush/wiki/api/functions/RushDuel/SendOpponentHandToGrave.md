# RushDuel.SendOpponentHandToGrave

Alias: `RD.SendOpponentHandToGrave`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.SendOpponentHandToGrave(any tp, any hint, any min, any max) -> any
```

## Description

Rush Duel helper declared in `RDAction.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
操作: 随机选对方的手卡送去墓地
```

## Parameters

- `tp` `any`: Type and behavior are not yet reviewed; see the source.
- `hint` `any`: Type and behavior are not yet reviewed; see the source.
- `min` `any`: Type and behavior are not yet reviewed; see the source.
- `max` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDAction.lua:317`

```lua
function RushDuel.SendOpponentHandToGrave(tp, hint, min, max)
    local g = Duel.GetFieldGroup(tp, 0, LOCATION_HAND)
    local ct = #g
    if ct < min then
        return 0
    end
    local ops = {}
    for i = min, math.min(max, ct) do
        table.insert(ops, i)
    end
    local ac = 0
    if #ops == 1 then
        ac = table.remove(ops)
    elseif #ops > 1 then
        Duel.Hint(HINT_SELECTMSG, tp, HINTMSG_OPERATE_COUNT)
        ac = Duel.AnnounceNumber(tp, table.unpack(ops))
    end
    if ac > 0 then
        local sg = g:RandomSelect(tp, ac)
        return Duel.SendtoGrave(sg, REASON_EFFECT)
    end
    return 0
end
```
