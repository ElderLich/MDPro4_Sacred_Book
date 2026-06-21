# Auxiliary.FilterEqualFunction

## Signature

```lua
Auxiliary.FilterEqualFunction(function f, Effect value, ... any) -> void
```

## Description

Filter cards satisfying a single filter condition f with value value, returning a function with a bool return type; additional parameters start from the third parameter
function Auxiliary.FilterEqualFunction(f, value, ...)
  local ext_params={...}
  return function(target)
    return f(target, table.unpack(ext_params))==value
  end
end

## Parameters

- `f` `function`
- `value` `Effect`
- `...` `any`

## Source

- `Utilities/utility.lua:460`
