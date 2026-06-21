# Group.GetMinGroup

## Signature

```lua
Group.GetMinGroup(Group g, function f, ... any) -> Group,int
```

## Description

F is a function that returns an interger value, and the card with the smallest value of f is selected from g
The second return value is the minimum value, starting at the third parameter as an additional parameter
To use the second return value Note Check g is not empty

## Parameters

- `g` `Group`
- `f` `function`
- `...` `any`

## Returns

- `Group`
- `int`

## Source

- `D:\Programs\GitHub\ygopro-core\libgroup.cpp:924`
