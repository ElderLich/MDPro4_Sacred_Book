# RushDuel.TripleTributeTarget

Alias: `RD.TripleTributeTarget`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.TripleTributeTarget(any value) -> any
```

## Description

Rush Duel helper declared in `RDSummon.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

## Parameters

- `value` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDSummon.lua:350`

```lua
function RushDuel.TripleTributeTarget(value)
    return function(e, c)
        return value(e, c) and c.is_can_triple_tribute
    end
end
```

## Used By

Generated from the local `Rush/Scripts/` folder and `rush_cards.cdb`.

No indexed local card script currently calls this function.

This can mean the function is unused in the current script set, is only called through an alias, or is available for future/manual scripts.
