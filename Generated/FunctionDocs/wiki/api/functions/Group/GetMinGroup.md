# Group.GetMinGroup

## Signature

```lua
Group.GetMinGroup(Group g, function f, [... any]) -> Group|nil,int|nil
```

## Description

Calls f for each card in g, forwards any extra arguments, and returns a Group containing every card tied for the minimum value.
The second return is the minimum integer value. If g is empty, this binding returns no Lua values.
Keep all ties when the card text affects every lowest-scoring card; call Group.Select when a player must choose one tied card.

## How To Use It

Use this to find every card tied for the lowest score in an existing Group.

```lua
local lowg,atk=g:GetMinGroup(Card.GetAttack)
if #lowg>0 then
    local sg=lowg:Select(tp,1,1,nil)
end
```

The return values are the tied Group and the minimum score. If the source Group is empty, this binding returns no values.

## Related Functions

- [Group.GetMaxGroup](/api/functions/Group/GetMaxGroup)
- [Group.Select](/api/functions/Group/Select)
- [Duel.SelectMatchingCard](/api/functions/Duel/SelectMatchingCard)

## Parameters

- `g` `Group`
- `f` `function`
- `...` `any` optional

## Returns

- `Group|nil` - Cards tied for the minimum value.
- `int|nil` - Minimum value.

## Source

- `D:\Programs\GitHub\ygopro-core\libgroup.cpp:924`
