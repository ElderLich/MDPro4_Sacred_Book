# RushDuel.ValueDoubleTributeAll

Alias: `RD.ValueDoubleTributeAll`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.ValueDoubleTributeAll(any ignore) -> any
```

## Description

Rush Duel helper declared in `RDValue.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
效果值: 双重解放 全范围
```

## Parameters

- `ignore` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDValue.lua:52`

```lua
function RushDuel.ValueDoubleTributeAll(ignore)
    return function(e, c)
        if e == nil then
            return ignore, 1
        end
        return true
    end
end
```
