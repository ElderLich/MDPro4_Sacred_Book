# RushDuel.DecreaseSummonValue

Alias: `RD.DecreaseSummonValue`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.DecreaseSummonValue(any value) -> any
```

## Description

Rush Duel helper declared in `RDSummon.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

## Parameters

- `value` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDSummon.lua:375`

```lua
function RushDuel.DecreaseSummonValue(value)
    return function(e, c)
        return value, 1
    end
end
```
