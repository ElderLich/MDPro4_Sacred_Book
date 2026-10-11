# RushDuel.FlatCheck

Alias: `RD.FlatCheck`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.FlatCheck(any check, ... any) -> any
```

## Description

Rush Duel helper declared in `RDBase.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
递归检查表
```

## Parameters

- `check` `any`: Type and behavior are not yet reviewed; see the source.
- `...` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDBase.lua:293`

```lua
function RushDuel.FlatCheck(check, ...)
    for _, item in ipairs({...}) do
        if type(item) == "table" then
            if RushDuel.FlatCheck(check, table.unpack(item)) then
                return true
            end
        elseif check(item) then
            return true
        end
    end
    return false
end

-- 重载 ForEach
if not Group.ForEach then
    Group.ForEach = function(g, func, ...)
        local tc = g:GetFirst()
        while tc do
            func(tc, ...)
            tc = g:GetNext()
        end
    end
end
```
