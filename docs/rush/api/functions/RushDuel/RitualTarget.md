# RushDuel.RitualTarget

Alias: `RD.RitualTarget`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.RitualTarget(any card, any type, any matfilter, any spfilter, any exfilter, any s_range, any o_range, any mat_check, any including_self, any self_leave, any action) -> any
```

## Description

Rush Duel helper declared in `RDRitual.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
仪式召唤 - 目标
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
- `including_self` `any`: Type and behavior are not yet reviewed; see the source.
- `self_leave` `any`: Type and behavior are not yet reviewed; see the source.
- `action` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDRitual.lua:346`

```lua
function RushDuel.RitualTarget(card, type, matfilter, spfilter, exfilter, s_range, o_range, mat_check, including_self, self_leave, action)
    return function(e, tp, eg, ep, ev, re, r, rp, chk)
        if chk == 0 then
            if e:IsHasProperty(EFFECT_FLAG_SPSUM_PARAM) then
                local min, max = e:GetLabel()
                RushDuel.MinRitualMaterialCount = min
                RushDuel.MaxRitualMaterialCount = max
            end
            RushDuel.RitualExtraMaterialFilter = card.ritual_mat_filter
            local res = RushDuel.IsCanRitualSummon(e, tp, type, matfilter, spfilter, exfilter, s_range, o_range, mat_check, including_self, self_leave, nil)
            RushDuel.RitualExtraMaterialFilter = nil
            RushDuel.MinRitualMaterialCount = nil
            RushDuel.MaxRitualMaterialCount = nil
            return res
        end
        if action ~= nil then
            action(e, tp, eg, ep, ev, re, r, rp)
        end
        Duel.SetOperationInfo(0, CATEGORY_SPECIAL_SUMMON, nil, 1, tp, LOCATION_EXTRA)
    end
end
```

## Used By

Generated from the local `Rush/Scripts/` folder and `rush_cards.cdb`.

No indexed local card script currently calls this function.

This can mean the function is unused in the current script set, is only called through an alias, or is available for future/manual scripts.
