# Group.SelectWithSumGreater

## Signature

```lua
Group.SelectWithSumGreater(Group g, int player, function f, int sum, ... any) -> Group
```

## Description

Lets player select a subset of g whose f-value sum reaches or exceeds sum according to the core's exact greater-sum selection rule; returns an empty Group if no valid subset exists.

## Parameters

- `g` `Group`
- `player` `int`
- `f` `function`
- `sum` `int`
- `...` `any`

## Returns

- `Group`

## Source

- `D:\Programs\GitHub\ygopro-core\libgroup.cpp:923`
