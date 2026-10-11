# RushDuel.FusionTarget

Alias: `RD.FusionTarget`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.FusionTarget(any card, any matfilter, any spfilter, any exfilter, any s_range, any o_range, any mat_check, any including_self, any self_leave, any pos, any action) -> any
```

## Description

Rush Duel helper declared in `RDFusion.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
融合召唤 - 目标
```

## Parameters

- `card` `any`: Type and behavior are not yet reviewed; see the source.
- `matfilter` `any`: Type and behavior are not yet reviewed; see the source.
- `spfilter` `any`: Type and behavior are not yet reviewed; see the source.
- `exfilter` `any`: Type and behavior are not yet reviewed; see the source.
- `s_range` `any`: Type and behavior are not yet reviewed; see the source.
- `o_range` `any`: Type and behavior are not yet reviewed; see the source.
- `mat_check` `any`: Type and behavior are not yet reviewed; see the source.
- `including_self` `any`: Type and behavior are not yet reviewed; see the source.
- `self_leave` `any`: Type and behavior are not yet reviewed; see the source.
- `pos` `any`: Type and behavior are not yet reviewed; see the source.
- `action` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDFusion.lua:535`

```lua
function RushDuel.FusionTarget(card, matfilter, spfilter, exfilter, s_range, o_range, mat_check, including_self, self_leave, pos, action)
    return function(e, tp, eg, ep, ev, re, r, rp, chk)
        if chk == 0 then
            RushDuel.FusionExtraMaterialFilter = card.fusion_mat_filter
            local res = RushDuel.IsCanFusionSummon(e, tp, pos, matfilter, spfilter, exfilter, s_range, o_range, mat_check, including_self, self_leave, nil)
            RushDuel.FusionExtraMaterialFilter = nil
            return res
        end
        if action ~= nil then
            action(e, tp, eg, ep, ev, re, r, rp)
        end
        Duel.SetOperationInfo(0, CATEGORY_SPECIAL_SUMMON, nil, 1, tp, LOCATION_EXTRA)
    end
end
```
