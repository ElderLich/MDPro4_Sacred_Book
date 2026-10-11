# RushDuel.AddContinuousEffect

Alias: `RD.AddContinuousEffect`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.AddContinuousEffect(any c, ... any) -> any
```

## Description

Rush Duel helper declared in `RDContinuous.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
添加永续效果列表
```

## Parameters

- `c` `any`: Type and behavior are not yet reviewed; see the source.
- `...` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDContinuous.lua:5`

```lua
function RushDuel.AddContinuousEffect(c, ...)
    if c:IsStatus(STATUS_COPYING_EFFECT) then
        return
    end
    if c.continuous_effect == nil then
        local mt = getmetatable(c)
        mt.continuous_effect = {...}
    else
        for _, e in ipairs {...} do
            table.insert(c.continuous_effect, e)
        end
    end
end
```
