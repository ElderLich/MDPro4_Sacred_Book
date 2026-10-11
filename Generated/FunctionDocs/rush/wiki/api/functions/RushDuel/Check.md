# RushDuel.Check

Alias: `RD.Check`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.Check(function check, ... any) -> function
```

## Description

Returns a group predicate that invokes check(g, ...) with captured extra arguments. Use for subgroup constraints.

## Parameters

- `check` `function`: Predicate receiving the selected Group and captured arguments.
- `...` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `function`: Group predicate.

## Source

`Rush/Utilities/RDFunction.lua:24`

```lua
function RushDuel.Check(check, ...)
    local args = {...}
    return function(g)
        return check(g, table.unpack(args))
    end
end
```
