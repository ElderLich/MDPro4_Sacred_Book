# RushDuel.OverrideFunction

Alias: `RD.OverrideFunction`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.OverrideFunction() -> any
```

## Description

Rush Duel helper declared in `RDRule.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
重载函数
```

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDRule.lua:141`

```lua
function RushDuel.OverrideFunction()
    -- "那之后" 不打断时点
    Duel.BreakEffect = function()
    end
end
```

## Used By

Generated from the local `Rush/Scripts/` folder and `rush_cards.cdb`.

No indexed local card script currently calls this function.

This can mean the function is unused in the current script set, is only called through an alias, or is available for future/manual scripts.
