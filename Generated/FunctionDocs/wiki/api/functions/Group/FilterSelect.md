# Group.FilterSelect

## Signature

```lua
Group.FilterSelect(Group g, int player, function f, int min, int max, [Card|Group|nil ex], ... any) -> Group
```

## Description

Lets player choose min to max cards from g that satisfy filter f, excluding ex, and returns the selected Group.
Extra arguments after ex are passed to f after the Card argument.

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
