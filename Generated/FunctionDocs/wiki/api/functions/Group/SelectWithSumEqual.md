# Group.SelectWithSumEqual

## Signature

```lua
Group.SelectWithSumEqual(Group g, int player, function f, int sum, int min, int max, ... any) -> Group
```

## Description

Let the player player select a subset of min-max from g so that the sum of the specific functions of the subset is equal to sum, starting at the 7th argument as an extra parameter

## Parameters

- `g` `Group`
- `player` `int`
- `f` `function`
- `sum` `int`
- `min` `int`
- `max` `int`
- `...` `any`

## Returns

- `Group`

## Source

- `D:\Programs\GitHub\ygopro-core\libgroup.cpp:921`
