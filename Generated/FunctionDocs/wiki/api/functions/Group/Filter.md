# Group.Filter

## Signature

```lua
Group.Filter(Group g, function f, [Card|Group|nil ex], ... any) -> Group
```

## Description

Returns a new Group containing cards from g that satisfy filter f and are not excluded by ex.
Extra arguments after ex are passed to f after the card argument.

## How To Use It

Use this when you already have a Group and want a smaller Group from it.

```lua
local g=Duel.GetFieldGroup(tp,LOCATION_MZONE,0)
local fg=g:Filter(Card.IsFaceup,nil)
```

Extra arguments after `ex` are passed to the filter after the card. The original Group is not destroyed; the function returns a new Group.

## Parameters

- `g` `Group`
- `f` `function`
- `ex` `Card|Group|nil` optional
- `...` `any`

## Returns

- `Group`

## Source

- `D:\Programs\GitHub\ygopro-core\libgroup.cpp:912`
