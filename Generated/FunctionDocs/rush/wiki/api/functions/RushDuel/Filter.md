# RushDuel.Filter

Alias: `RD.Filter`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.Filter(function filter, ... any) -> function
```

## Description

Returns a one-card predicate that invokes filter(c, ...) with the captured extra arguments.

## Parameters

- `filter` `function`: Predicate called with a Card followed by the captured arguments.
- `...` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `function`: Single-card predicate.

## Example

```lua
local machine = RD.Filter(Card.IsRace, RACE_MACHINE)
local g = Duel.GetMatchingGroup(machine, tp, LOCATION_MZONE, 0, nil)
```

## Source

`Rush/Utilities/RDFunction.lua:17`

```lua
function RushDuel.Filter(filter, ...)
    local args = {...}
    return function(c)
        return filter(c, table.unpack(args))
    end
end
```
