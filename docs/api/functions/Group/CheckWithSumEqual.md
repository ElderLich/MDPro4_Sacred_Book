# Group.CheckWithSumEqual

## Signature

```lua
Group.CheckWithSumEqual(Group g, function f, int sum, int min, int max, ... any) -> bool
```

## Description

The subset summation decision function, f, is a function that returns an interger value
Check whether there is a subset of min-max in g that satisfies that the sum of the values ​​of each element of the subset f is equal to sum, starting at the 6th argument as an extra parameter
For example: g: CheckWithSumEqual (Card.GetSynchroLevel, 7,2,99)
Check if the sum of the same call levels in a subset of g satisfies a subset equal to 7

## Parameters

- `g` `Group`
- `f` `function`
- `sum` `int`
- `min` `int` - default: 0
- `max` `int`
- `...` `any`

## Returns

- `bool`

## Source

- `D:\Programs\GitHub\ygopro-core\libgroup.cpp:920`
