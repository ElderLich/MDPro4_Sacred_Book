# RushDuel.TripleTributeOperation

Alias: `RD.TripleTributeOperation`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.TripleTributeOperation(any e, any tp, any eg, any ep, any ev, any re, any r, any rp, any c) -> any
```

## Description

Rush Duel helper declared in `RDSummon.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

## Parameters

- `e` `any`: Type and behavior are not yet reviewed; see the source.
- `tp` `any`: Type and behavior are not yet reviewed; see the source.
- `eg` `any`: Type and behavior are not yet reviewed; see the source.
- `ep` `any`: Type and behavior are not yet reviewed; see the source.
- `ev` `any`: Type and behavior are not yet reviewed; see the source.
- `re` `any`: Type and behavior are not yet reviewed; see the source.
- `r` `any`: Type and behavior are not yet reviewed; see the source.
- `rp` `any`: Type and behavior are not yet reviewed; see the source.
- `c` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDSummon.lua:355`

```lua
function RushDuel.TripleTributeOperation(e, tp, eg, ep, ev, re, r, rp, c)
    local mg = Group.FromCards(e:GetHandler())
    c:SetMaterial(mg)
    Duel.Release(mg, REASON_SUMMON + REASON_MATERIAL)
end
```

## Used By

Generated from the local `Rush/Scripts/` folder and `rush_cards.cdb`.

No indexed local card script currently calls this function.

This can mean the function is unused in the current script set, is only called through an alias, or is available for future/manual scripts.
