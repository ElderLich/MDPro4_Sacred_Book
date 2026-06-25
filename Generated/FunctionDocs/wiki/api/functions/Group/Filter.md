# Group.Filter

## Signature

```lua
Group.Filter(Group g, function f, [Card|Group|nil ex], ... any) -> Group
```

## Description

Returns a new Group containing cards from g that satisfy filter f and are not excluded by ex.
Extra arguments after ex are passed to f after the card argument.
The source Group is not modified.

## How To Use It

Use this when you already have a Group and want a smaller Group from it.

```lua
local g=Duel.GetFieldGroup(tp,LOCATION_MZONE,0)
local fg=g:Filter(Card.IsFaceup,nil)
```

Extra arguments after `ex` are passed to the filter after the card. The original Group is not destroyed; the function returns a new Group.

## Related Functions

- [Group.FilterCount](/api/functions/Group/FilterCount)
- [Group.Select](/api/functions/Group/Select)
- [Group.FilterSelect](/api/functions/Group/FilterSelect)

## Parameters

- `g` `Group` - Group to filter; it is not modified.
- `f` `function` - Filter callback called for each candidate card.
- `ex` `Card|Group|nil` optional - Card or Group excluded before filtering; nil excludes nothing.
- `...` `any` - Extra values forwarded to f after the candidate Card.

## Returns

- `Group` - New Group containing cards that passed f.

## Source

- `D:\Programs\GitHub\ygopro-core\libgroup.cpp:912`
