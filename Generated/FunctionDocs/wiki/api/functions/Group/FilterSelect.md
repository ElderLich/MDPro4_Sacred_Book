# Group.FilterSelect

## Signature

```lua
Group.FilterSelect(Group g, int player, function f, int min, int max, [Card|Group|nil ex], ... any) -> Group
```

## Description

Lets player choose min to max cards from g that satisfy filter f, excluding ex, and returns the selected Group.
Extra arguments after ex are passed to f after the Card argument.
This is a selection from an existing Group, not an official Chain target selection.

## How To Use It

Use this when you already have a Group, but only some cards in it should be selectable.

```lua
local sg=g:FilterSelect(tp,s.filter,1,1,nil,e,tp)
if #sg>0 then
    Duel.SendtoHand(sg,nil,REASON_EFFECT)
end
```

This is still an ordinary selection, not an official Chain target selection. Use `Duel.SelectTarget` during targeting effects.

## Related Functions

- [Group.Filter](/api/functions/Group/Filter)
- [Group.Select](/api/functions/Group/Select)
- [Duel.SelectMatchingCard](/api/functions/Duel/SelectMatchingCard)

## Parameters

- `g` `Group`
- `player` `int`
- `f` `function`
- `min` `int`
- `max` `int`
- `ex` `Card|Group|nil` optional
- `...` `any`

## Returns

- `Group`

## Source

- `D:\Programs\GitHub\ygopro-core\libgroup.cpp:914`
