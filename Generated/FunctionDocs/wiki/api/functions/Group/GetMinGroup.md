# Group.GetMinGroup

## Signature

```lua
Group.GetMinGroup(Group g, function f, [... any]) -> Group|nil,int|nil
```

## Description

Calls f for each card in g, forwards any extra arguments, and returns a Group containing every card tied for the minimum value.
The second return is the minimum integer value. If g is empty, this binding returns no Lua values.

## Parameters

- `g` `Group`
- `f` `function`
- `...` `any` optional

## Returns

- `Group|nil` - Cards tied for the minimum value.
- `int|nil` - Minimum value.

## Source

- `D:\Programs\GitHub\ygopro-core\libgroup.cpp:924`
