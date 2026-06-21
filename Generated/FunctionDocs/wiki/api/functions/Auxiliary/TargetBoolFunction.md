# Auxiliary.TargetBoolFunction

## Signature

```lua
Auxiliary.TargetBoolFunction(function f, ... any) -> void
```

## Description

Used in effect registration, returns a function with a bool return type; additional parameters start from the second parameter
function Auxiliary.TargetBoolFunction(f,...)
  local ext_params={...}
  return function(effect,target)
    return f(target,table.unpack(ext_params))
  end
end

## Parameters

- `f` `function`
- `...` `any`

## Source

- `Utilities/utility.lua:454`
