# RushDuel.AddCodeList

Alias: `RD.AddCodeList`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.AddCodeList(Card card, ... int|table) -> void
```

## Description

Accepts passcodes or flat tables of passcodes, registering each through Auxiliary.AddCodeList. This is mention metadata for other scripts; it does not create a Summon procedure or change the card's name.

## Parameters

- `card` `Card`: Card whose script mentions these passcodes.
- `...` `int|table`: Passcodes or flat tables of passcodes.

## Returns

No return values.

## Source

`Rush/Utilities/RDBase.lua:244`

```lua
function RushDuel.AddCodeList(card, ...)
    for _, list in ipairs {...} do
        local type = Auxiliary.GetValueType(list)
        if type == "number" then
            Auxiliary.AddCodeList(card, list)
        elseif type == "table" then
            Auxiliary.AddCodeList(card, table.unpack(list))
        end
    end
end
```
