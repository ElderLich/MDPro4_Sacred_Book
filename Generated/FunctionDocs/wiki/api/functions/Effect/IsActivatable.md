# Effect.IsActivatable

## Signature

```lua
Effect.IsActivatable(Effect e, int player, [bool neglect_loc], [bool neglect_target]) -> bool
```

## Description

Checks whether e can currently be activated by player, with optional booleans to ignore location and target checks.

## Parameters

- `e` `Effect`
- `player` `int`
- `neglect_loc` `bool` optional
- `neglect_target` `bool` optional

## Returns

- `bool`

## Source

- `D:\Programs\GitHub\ygopro-core\libeffect.cpp:654`
