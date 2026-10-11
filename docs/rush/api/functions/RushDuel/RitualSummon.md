# RushDuel.RitualSummon

Alias: `RD.RitualSummon`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.RitualSummon(any type, any matfilter, any spfilter, any exfilter, any s_range, any o_range, any mat_check, any mat_move, any e, any tp, any break_effect, any including_self, any self_leave) -> any
```

## Description

Known limitation in the pinned RDRitual.lua: this direct action wrapper reads card.ritual_mat_filter, but card is neither a parameter nor a local variable. Without an unrelated global card value it errors before selecting or summoning.
No imported card script directly calls this wrapper. Use CreateRitualEffect and its generated operation for ordinary Ritual effects; do not create a global card variable to work around the missing reference. The vendored source is preserved for provenance.

## Parameters

- `type` `any`: Type and behavior are not yet reviewed; see the source.
- `matfilter` `any`: Type and behavior are not yet reviewed; see the source.
- `spfilter` `any`: Type and behavior are not yet reviewed; see the source.
- `exfilter` `any`: Type and behavior are not yet reviewed; see the source.
- `s_range` `any`: Type and behavior are not yet reviewed; see the source.
- `o_range` `any`: Type and behavior are not yet reviewed; see the source.
- `mat_check` `any`: Type and behavior are not yet reviewed; see the source.
- `mat_move` `any`: Type and behavior are not yet reviewed; see the source.
- `e` `any`: Type and behavior are not yet reviewed; see the source.
- `tp` `any`: Type and behavior are not yet reviewed; see the source.
- `break_effect` `any`: Type and behavior are not yet reviewed; see the source.
- `including_self` `any`: Type and behavior are not yet reviewed; see the source.
- `self_leave` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: No reliable completion contract in the stock environment because of the unresolved card reference.

## Source

`Rush/Utilities/RDRitual.lua:395`

```lua
function RushDuel.RitualSummon(type, matfilter, spfilter, exfilter, s_range, o_range, mat_check, mat_move, e, tp, break_effect, including_self, self_leave)
    local include = including_self or false
    local leave = self_leave or false
    RushDuel.RitualExtraMaterialFilter = card.ritual_mat_filter
    RushDuel.RitualExtraChecker = RushDuel.RitualCheckLocation(e, self_leave, mat_check)
    local ritualable, list, chkf, gc = RushDuel.GetRitualSummonData(e, tp, type, matfilter, spfilter, exfilter, s_range, o_range, include, leave, nil, e)
    local rc = nil
    if ritualable then
        if break_effect then
            Duel.BreakEffect()
        end
        rc = RushDuel.ExecuteRitualSummon(e, tp, type, list, chkf, gc, mat_move)
    end
    RushDuel.RitualExtraMaterialFilter = nil
    RushDuel.RitualExtraChecker = nil
    RushDuel.MinRitualMaterialCount = nil
    RushDuel.MaxRitualMaterialCount = nil
    return rc
end
```

## Used By

Generated from the local `Rush/Scripts/` folder and `rush_cards.cdb`.

No indexed local card script currently calls this function.

This can mean the function is unused in the current script set, is only called through an alias, or is available for future/manual scripts.
