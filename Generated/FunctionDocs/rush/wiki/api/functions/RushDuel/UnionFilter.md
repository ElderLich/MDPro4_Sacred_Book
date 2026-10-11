# RushDuel.UnionFilter

Alias: `RD.UnionFilter`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.UnionFilter(any target) -> any
```

## Description

Rush Duel helper declared in `RDUnion.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

## Parameters

- `target` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDUnion.lua:65`

```lua
function RushDuel.UnionFilter(target)
    return function(e, c)
        return e:GetHandler():GetEquipTarget() == c
    end
end
```
