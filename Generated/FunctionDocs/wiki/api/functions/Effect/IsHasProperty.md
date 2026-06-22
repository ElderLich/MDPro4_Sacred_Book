# Effect.IsHasProperty

## Signature

```lua
Effect.IsHasProperty(Effect e, int prop1, [int prop2]) -> bool
```

## Description

Checks whether e contains the requested effect property flags.
prop1 is checked against the first property word and optional prop2 against the second property word. Passing 0 for a word makes that word pass.

## Parameters

- `e` `Effect` - Effect whose property words are checked.
- `prop1` `int` - Mask checked against the first property word. Use 0 to ignore this word.
- `prop2` `int` optional - Mask checked against the second property word. Omitted or 0 means this word passes.

## Returns

- `bool` - True when every nonzero requested property mask is present on e.

## Source

- `D:\Programs\GitHub\ygopro-core\libeffect.cpp:650`
