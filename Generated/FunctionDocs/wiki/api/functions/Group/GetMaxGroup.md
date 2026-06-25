# Group.GetMaxGroup

## Signature

```lua
Group.GetMaxGroup(Group g, function f, [... any]) -> Group|nil,int|nil
```

## Description

Calls f for each card in g, forwards any extra arguments, and returns a Group containing every card tied for the maximum value.
The second return is the maximum integer value. If g is empty, this binding returns no Lua values.
Keep all ties when the card text affects every highest-scoring card; call Group.Select when a player must choose one tied card.

## How To Use It

Use this to find every card tied for the highest score in an existing Group.

```lua
local highg,atk=g:GetMaxGroup(Card.GetAttack)
if #highg>0 then
    Duel.HintSelection(highg)
end
```

The score function receives each candidate card first, then any extra arguments. Ties stay in the returned Group so the script can let a player choose or affect all tied cards.

## Related Functions

- [Group.GetMinGroup](/api/functions/Group/GetMinGroup)
- [Group.Select](/api/functions/Group/Select)
- [Duel.SelectMatchingCard](/api/functions/Duel/SelectMatchingCard)

## Parameters

- `g` `Group`
- `f` `function`
- `...` `any` optional

## Returns

- `Group|nil` - Cards tied for maximum value.
- `int|nil` - Maximum value.

## Source

- `D:\Programs\GitHub\ygopro-core\libgroup.cpp:925`
