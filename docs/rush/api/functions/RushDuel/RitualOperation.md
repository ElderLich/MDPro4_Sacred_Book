# RushDuel.RitualOperation

Alias: `RD.RitualOperation`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.RitualOperation(any card, any type, any matfilter, any spfilter, any exfilter, any s_range, any o_range, any mat_check, any mat_move, any including_self, any self_leave, any action, any limit) -> any
```

## Description

Rush Duel helper declared in `RDRitual.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
仪式召唤 - 处理
```

## Parameters

- `card` `any`: Type and behavior are not yet reviewed; see the source.
- `type` `any`: Type and behavior are not yet reviewed; see the source.
- `matfilter` `any`: Type and behavior are not yet reviewed; see the source.
- `spfilter` `any`: Type and behavior are not yet reviewed; see the source.
- `exfilter` `any`: Type and behavior are not yet reviewed; see the source.
- `s_range` `any`: Type and behavior are not yet reviewed; see the source.
- `o_range` `any`: Type and behavior are not yet reviewed; see the source.
- `mat_check` `any`: Type and behavior are not yet reviewed; see the source.
- `mat_move` `any`: Type and behavior are not yet reviewed; see the source.
- `including_self` `any`: Type and behavior are not yet reviewed; see the source.
- `self_leave` `any`: Type and behavior are not yet reviewed; see the source.
- `action` `any`: Type and behavior are not yet reviewed; see the source.
- `limit` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDRitual.lua:368`

```lua
function RushDuel.RitualOperation(card, type, matfilter, spfilter, exfilter, s_range, o_range, mat_check, mat_move, including_self, self_leave, action, limit)
    return function(e, tp, eg, ep, ev, re, r, rp)
        if e:IsHasProperty(EFFECT_FLAG_SPSUM_PARAM) then
            local min, max = e:GetLabel()
            RushDuel.MinRitualMaterialCount = min
            RushDuel.MaxRitualMaterialCount = max
        end
        RushDuel.RitualExtraMaterialFilter = card.ritual_mat_filter
        RushDuel.RitualExtraChecker = RushDuel.RitualCheckLocation(e, self_leave, mat_check)
        local ritualable, list, chkf, gc = RushDuel.GetRitualSummonData(e, tp, type, matfilter, spfilter, exfilter, s_range, o_range, including_self, self_leave, nil, e)
        if ritualable then
            local fc, mat = RushDuel.ExecuteRitualSummon(e, tp, type, list, chkf, gc, mat_move)
            if action ~= nil then
                action(e, tp, eg, ep, ev, re, r, rp, mat, fc)
            end
        end
        RushDuel.RitualExtraMaterialFilter = nil
        RushDuel.RitualExtraChecker = nil
        RushDuel.MinRitualMaterialCount = nil
        RushDuel.MaxRitualMaterialCount = nil
        if limit ~= nil then
            limit(e, tp, eg, ep, ev, re, r, rp)
        end
    end
end
```

## Used By

Generated from the local `Rush/Scripts/` folder and `rush_cards.cdb`.

No indexed local card script currently calls this function.

This can mean the function is unused in the current script set, is only called through an alias, or is available for future/manual scripts.
