# Effect.IsHasProperty

## Signature

```lua
Effect.IsHasProperty(Effect e, int prop1, [int prop2]) -> bool
```

## Description

Checks whether e contains the requested effect property flags.
prop1 is checked against the first property word and optional prop2 against the second property word. Passing 0 for a word makes that word pass.

## Parameters

- `e` `Effect`
- `prop1` `int`
- `prop2` `int` optional

## Returns

- `bool`

## Source

- `D:\Programs\GitHub\ygopro-core\libeffect.cpp:650`
