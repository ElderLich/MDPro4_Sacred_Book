# RushDuel.FusionSummonFlagCondition

Alias: `RD.FusionSummonFlagCondition`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.FusionSummonFlagCondition(any e, any tp, any eg, any ep, any ev, any re, any r, any rp) -> any
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

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDSummon.lua:319`

```lua
function RushDuel.FusionSummonFlagCondition(e, tp, eg, ep, ev, re, r, rp)
    return e:GetHandler():IsSummonType(SUMMON_TYPE_FUSION)
end
```

## Used By

Generated from the local `Rush/Scripts/` folder and `rush_cards.cdb`.

No indexed local card script currently calls this function.

This can mean the function is unused in the current script set, is only called through an alias, or is available for future/manual scripts.
