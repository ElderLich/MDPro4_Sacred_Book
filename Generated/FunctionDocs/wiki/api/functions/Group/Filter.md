# Group.Filter

## Signature

```lua
Group.Filter(Group g, function f, [Card|Group|nil ex], ... any) -> Group
```

## Description

The filter function filters the card from g that satisfies the filter condition f and is not equal to ex
Starting from the 4th parameter as an additional parameter

## Parameters

- `g` `Group`
- `f` `function`
- `ex` `Card|Group|nil` optional
- `...` `any`

## Returns

- `Group`

## Source

- `D:\Programs\GitHub\ygopro-core\libgroup.cpp:912`
