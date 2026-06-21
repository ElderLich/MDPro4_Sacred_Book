# Group.CheckWithSumGreater

## Signature

```lua
Group.CheckWithSumGreater(Group g, function f, int sum, ... any) -> bool
```

## Description

The sum of the subsets is determined by a function f, which is a function that returns an interger value
Check that there is a subset in g that satisfies that the sum of the values ​​of each element of the subset f is just greater than or equal to sum, starting at the fourth argument as an extra parameter
For example: g: CheckWithSumGreater (Card.GetRitualLevel, 8)
Check if the sum of the ritual classes in g satisfies a subset of 8 or greater
Note: The decision must be "just" greater than or equal to
To grade, for example, to make the total level is greater than or equal to 8, you can choose LV1 + LV7 and can not choose LV1 + LV4 + LV4

## Parameters

- `g` `Group`
- `f` `function`
- `sum` `int`
- `...` `any`

## Returns

- `bool`

## Source

- `D:\Programs\GitHub\ygopro-core\libgroup.cpp:922`
