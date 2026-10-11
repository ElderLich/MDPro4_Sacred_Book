# RushDuel.CanSendOpponentHandToGrave

Alias: `RD.CanSendOpponentHandToGrave`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.CanSendOpponentHandToGrave(any desc, any tp, any hint, any min, any max, any break_effect) -> any
```

## Description

Rush Duel helper declared in `RDAction.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
可选操作: 随机选对方的手卡送去墓地
```

## Parameters

- `desc` `any`: Type and behavior are not yet reviewed; see the source.
- `tp` `any`: Type and behavior are not yet reviewed; see the source.
- `hint` `any`: Type and behavior are not yet reviewed; see the source.
- `min` `any`: Type and behavior are not yet reviewed; see the source.
- `max` `any`: Type and behavior are not yet reviewed; see the source.
- `break_effect` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDAction.lua:341`

```lua
function RushDuel.CanSendOpponentHandToGrave(desc, tp, hint, min, max, break_effect)
    local g = Duel.GetFieldGroup(tp, 0, LOCATION_HAND)
    local ct = #g
    if ct > 0 and Duel.SelectYesNo(tp, desc) then
        if break_effect then
            Duel.BreakEffect()
        end
        return RushDuel.SendOpponentHandToGrave(tp, hint, min, max)
    end
    return 0
end
```
