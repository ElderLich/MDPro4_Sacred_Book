# Auxiliary.FilterBoolFunction

## Signature

```lua
Auxiliary.FilterBoolFunction(function f, ... any) -> void
```

## Description

Filter cards satisfying a single filter condition f, returning a function with a bool return type; additional parameters start from the second parameter
function Auxiliary.FilterBoolFunction(f,...)
  local ext_params={...}
  return function(target)
    return f(target,table.unpack(ext_params))
  end
end

## Parameters

- `f` `function`
- `...` `any`

## Source

- `Utilities/utility.lua:466`
