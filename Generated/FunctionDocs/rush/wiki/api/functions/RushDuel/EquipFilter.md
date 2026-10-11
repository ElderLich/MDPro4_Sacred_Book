# RushDuel.EquipFilter

Alias: `RD.EquipFilter`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.EquipFilter(any target) -> any
```

## Description

Rush Duel helper declared in `RDEquip.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

## Parameters

- `target` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDEquip.lua:52`

```lua
function RushDuel.EquipFilter(target)
    return function(e, c)
        return e:GetHandler():GetEquipTarget() == c or target(c, e, e:GetHandlerPlayer(), false)
    end
end
```
