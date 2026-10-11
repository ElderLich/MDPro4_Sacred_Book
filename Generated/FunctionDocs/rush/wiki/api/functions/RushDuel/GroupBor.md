# RushDuel.GroupBor

Alias: `RD.GroupBor`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.GroupBor(any g, any func, ... any) -> any
```

## Description

Rush Duel helper declared in `RDFunction.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
对卡片组里的全部卡片作位或运算
```

## Parameters

- `g` `any`: Type and behavior are not yet reviewed; see the source.
- `func` `any`: Type and behavior are not yet reviewed; see the source.
- `...` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDFunction.lua:79`

```lua
function RushDuel.GroupBor(g, func, ...)
    local result = 0
    local args = {...}
    g:ForEach(function(tc)
        result = result | func(tc, table.unpack(args))
    end)
    return result
end
```
