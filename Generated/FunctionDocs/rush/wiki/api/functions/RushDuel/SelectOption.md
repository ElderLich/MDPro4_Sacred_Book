# RushDuel.SelectOption

Alias: `RD.SelectOption`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.SelectOption(int player, ... table) -> any|nil
```

## Description

Accepts option tables {available, description, value}. Unavailable options are omitted; a sole option is announced automatically. Returns the chosen value (or its original one-based option index), not Duel.SelectOption's zero-based menu index.

## Parameters

- `player` `int`: Selecting player, 0 or 1.
- `...` `table`: Each option is {available, description, value}; value may be omitted.

## Returns

- `any|nil`: Chosen option value; nil when no options are available.

## Source

`Rush/Utilities/RDFunction.lua:59`

```lua
function RushDuel.SelectOption(player, ...)
    local options = {...}
    local ops = {}
    local opvals = {}
    for i = 1, #options do
        if options[i][1] then
            table.insert(ops, options[i][2])
            table.insert(opvals, options[i][3] or i)
        end
    end
    if #ops == 0 then return nil end
    if #ops == 1 then
        Duel.Hint(HINT_OPSELECTED, 1 - player, ops[1])
        return opvals[1]
    end
    local select = Duel.SelectOption(player, table.unpack(ops))
    return opvals[select + 1]
end
```
