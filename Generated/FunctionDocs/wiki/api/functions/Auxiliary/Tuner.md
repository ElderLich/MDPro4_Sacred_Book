# Auxiliary.Tuner

## Signature

```lua
Auxiliary.Tuner(function|nil f, [... any]) -> function
```

## Description

Returns a material filter that accepts cards that are Tuners for syncard and also satisfy f(target, ...), when f is supplied.

## Parameters

- `f` `function|nil`
- `...` `any` optional

## Returns

- `function`

## Source

- `Utilities/procedure.lua:42`
