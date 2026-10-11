# RushDuel.ToGroup

Alias: `RD.ToGroup`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.ToGroup(Group|Card|Effect target) -> Group
```

## Description

Creates a new Group from a Group, Card or Effect (using the Effect handler). Unsupported input produces an empty Group.

## Parameters

- `target` `Group|Card|Effect`: Object to convert.

## Returns

- `Group`: New Group containing the supplied cards or handler.

## Source

`Rush/Utilities/RDFunction.lua:98`

```lua
function RushDuel.ToGroup(target)
    local type = Auxiliary.GetValueType(target)
    local g = Group.CreateGroup()
    if type == "Group" then
        g:Merge(target)
    elseif type == "Card" then
        g:AddCard(target)
    elseif type == "Effect" then
        g:AddCard(target:GetHandler())
    end
    return g
end
```

## Used By

Generated from the local `Rush/Scripts/` folder and `rush_cards.cdb`.

No indexed local card script currently calls this function.

This can mean the function is unused in the current script set, is only called through an alias, or is available for future/manual scripts.
