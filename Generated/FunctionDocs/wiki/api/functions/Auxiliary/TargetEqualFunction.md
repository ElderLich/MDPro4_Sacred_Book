# Auxiliary.TargetEqualFunction

## Signature

```lua
Auxiliary.TargetEqualFunction(function f, any value, [... any]) -> function
```

## Description

Returns an effect target-value function that calls f on the target card and extra arguments, then checks whether the result equals value.

## Parameters

- `f` `function`
- `value` `any`
- `...` `any` optional

## Returns

- `function`

## Source

- `Utilities/utility.lua:448`
