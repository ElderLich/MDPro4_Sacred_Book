# Auxiliary.TargetBoolFunction

## Signature

```lua
Auxiliary.TargetBoolFunction(function f, ... any) -> function
```

## Description

Returns an effect target callback that calls f(target, ...) with the extra arguments captured now.
Use this when SetTarget or similar APIs expect a function with parameters (effect, target).

## Parameters

- `f` `function`
- `...` `any`

## Returns

- `function` - A target callback with parameters (effect, target).

## Source

- `Utilities/utility.lua:454`
