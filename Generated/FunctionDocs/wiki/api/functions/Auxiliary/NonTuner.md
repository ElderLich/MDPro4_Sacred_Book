# Auxiliary.NonTuner

## Signature

```lua
Auxiliary.NonTuner(function f, ... any) -> void
```

## Description

Filter non-Tuner monsters satisfying a single filter condition f, returning a function with a bool return type; if only non-Tuner monsters are required, use aux.NonTuner(nil)
Additional parameters start from the second parameter

## Parameters

- `f` `function`
- `...` `any`

## Source

- `Utilities/procedure.lua:48`
