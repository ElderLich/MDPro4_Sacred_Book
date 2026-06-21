# Auxiliary.NecroValleyFilter

## Signature

```lua
Auxiliary.NecroValleyFilter(function f) -> void
```

## Description

Return a new filter condition based on filter condition f: cards that satisfy f and are not affected by Necrovalley
function Auxiliary.NecroValleyFilter(f)
  return function(target,...)
    return f(target,...) and not (target:IsHasEffect(EFFECT_NECRO_VALLEY) and Duel.IsChainDisablable(0))
  end
end

## Parameters

- `f` `function`

## Source

- `Utilities/utility.lua:920`
