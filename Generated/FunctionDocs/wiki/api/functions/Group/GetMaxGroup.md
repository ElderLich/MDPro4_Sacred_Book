# Group.GetMaxGroup

## Signature

```lua
Group.GetMaxGroup(Group g, function f, [... any]) -> Group|nil,int|nil
```

## Description

Calls f for each card in g, forwards any extra arguments, and returns a Group containing every card tied for the maximum value.
The second return is the maximum integer value. If g is empty, this binding returns no Lua values.

## Parameters

- `g` `Group`
- `f` `function`
- `...` `any` optional

## Returns

- `Group|nil` - Cards tied for maximum value.
- `int|nil` - Maximum value.

## Source

- `D:\Programs\GitHub\ygopro-core\libgroup.cpp:925`
