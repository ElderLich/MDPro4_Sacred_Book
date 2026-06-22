# Group.CheckWithSumEqual

## Signature

```lua
Group.CheckWithSumEqual(Group g, function f, int acc, int min, int max, [... any]) -> bool
```

## Description

Checks whether a subset of g, including any must-select cards, can make the f-sum exactly acc using between min and max cards.

## Parameters

- `g` `Group`
- `f` `function`
- `acc` `int`
- `min` `int`
- `max` `int`
- `...` `any` optional

## Returns

- `bool`

## Source

- `D:\Programs\GitHub\ygopro-core\libgroup.cpp:920`
