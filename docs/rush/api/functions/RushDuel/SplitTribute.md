# RushDuel.SplitTribute

Alias: `RD.SplitTribute`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.SplitTribute(any card, any group) -> any
```

## Description

Rush Duel helper declared in `RDSummon.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
分割上级召唤的解放怪兽
```

## Parameters

- `card` `any`: Type and behavior are not yet reviewed; see the source.
- `group` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDSummon.lua:233`

```lua
function RushDuel.SplitTribute(card, group)
    local g = group or card:GetMaterial()
    local normal, double = Group.CreateGroup(), Group.CreateGroup()
    g:ForEach(function(tc)
        if RushDuel.IsCanDoubleTribute(tc, card) then
            double:AddCard(tc)
        else
            normal:AddCard(tc)
        end
    end)
    return normal, double
end
```

## Used By

Generated from the local `Rush/Scripts/` folder and `rush_cards.cdb`.

No indexed local card script currently calls this function.

This can mean the function is unused in the current script set, is only called through an alias, or is available for future/manual scripts.
