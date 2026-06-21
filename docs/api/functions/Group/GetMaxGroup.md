# Group.GetMaxGroup

## Signature

```lua
Group.GetMaxGroup(Group g, function f, ... any) -> Group,int
```

## Description

F is the function that returns an interger value, and the card with the largest value of f is selected from g
The second return value is the maximum value, starting with the third parameter as an additional parameter
To use the second return value Note Check g is not empty

## Parameters

- `g` `Group`
- `f` `function`
- `...` `any`

## Returns

- `Group`
- `int`

## Source

- `D:\Programs\GitHub\ygopro-core\libgroup.cpp:925`
