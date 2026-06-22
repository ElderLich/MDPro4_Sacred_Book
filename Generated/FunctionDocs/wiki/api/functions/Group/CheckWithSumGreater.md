# Group.CheckWithSumGreater

## Signature

```lua
Group.CheckWithSumGreater(Group g, function f, int acc, [... any]) -> bool
```

## Description

Checks whether g can satisfy an f-sum of at least acc.
Cards previously set with Duel.SetSelectedCard are forced into the sum and the must-select list is cleared before returning.

## Parameters

- `g` `Group`
- `f` `function`
- `acc` `int`
- `...` `any` optional

## Returns

- `bool`

## Source

- `D:\Programs\GitHub\ygopro-core\libgroup.cpp:922`
