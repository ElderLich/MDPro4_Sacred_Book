# Auxiliary.FilterBoolFunction

## Signature

```lua
Auxiliary.FilterBoolFunction(function f, ... any) -> void
```

## Description

Returns a filter function that calls f(target, ...) with the extra arguments captured now.
Use this when another API expects a one-argument Card filter but the real filter needs fixed extra values.

## Parameters

- `f` `function`
- `...` `any`

## Source

- `Utilities/utility.lua:466`
