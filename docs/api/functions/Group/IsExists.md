# Group.IsExists

## Signature

```lua
Group.IsExists(Group g, function f, int count, [Card|Group|nil ex], ... any) -> bool
```

## Description

Filter function to check if there is at least count of cards in g that satisfy the filter condition f and not equal to ex
Starting from the 5th parameter as an additional parameter

## Parameters

- `g` `Group`
- `f` `function`
- `count` `int`
- `ex` `Card|Group|nil` optional
- `...` `any`

## Returns

- `bool`

## Source

- `D:\Programs\GitHub\ygopro-core\libgroup.cpp:919`
