# Auxiliary.FilterEqualFunction

## Signature

```lua
Auxiliary.FilterEqualFunction(function f, any value, [... any]) -> function
```

## Description

Returns a card filter that calls f on the card and extra arguments, then checks whether the result equals value.

## Parameters

- `f` `function`
- `value` `any`
- `...` `any` optional

## Returns

- `function`

## Source

- `Utilities/utility.lua:460`
