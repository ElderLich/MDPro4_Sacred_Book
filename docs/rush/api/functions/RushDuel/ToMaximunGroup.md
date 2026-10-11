# RushDuel.ToMaximunGroup

Alias: `RD.ToMaximunGroup`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.ToMaximunGroup(Group|Card|Effect target) -> Group
```

## Description

Converts the input to a Group and includes overlay components of cards satisfying RD.IsMaximumMode. The upstream name is spelled ToMaximunGroup; preserve that spelling.

## Parameters

- `target` `Group|Card|Effect`: Object to convert and expand.

## Returns

- `Group`: Group including Maximum components.

## Source

`Rush/Utilities/RDFunction.lua:112`

```lua
function RushDuel.ToMaximunGroup(target)
    local g = RushDuel.ToGroup(target)
    local overlay = Group.CreateGroup()
    g:ForEach(function(tc)
        if RushDuel.IsMaximumMode(tc) then
            overlay:Merge(tc:GetOverlayGroup())
        end
    end)
    g:Merge(overlay)
    return g
end
```

## Used By

Generated from the local `Rush/Scripts/` folder and `rush_cards.cdb`.

No indexed local card script currently calls this function.

This can mean the function is unused in the current script set, is only called through an alias, or is available for future/manual scripts.
