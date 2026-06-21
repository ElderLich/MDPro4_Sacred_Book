# Auxiliary.TargetEqualFunction

## Signature

```lua
Auxiliary.TargetEqualFunction(function f, Effect value, ... any) -> void
```

## Description

Used in effect registration, returns a function with a bool return type; additional parameters start from the third parameter
function Auxiliary.TargetEqualFunction(f, value, ...)
  local ext_params={...}
  return function(effect,target)
    return f(target,table.unpack(ext_params))==value
  end
end

## Parameters

- `f` `function`
- `value` `Effect`
- `...` `any`

## Source

- `Utilities/utility.lua:448`
