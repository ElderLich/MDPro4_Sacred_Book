# RushDuel.FusionOperation

Alias: `RD.FusionOperation`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.FusionOperation(any card, any matfilter, any spfilter, any exfilter, any s_range, any o_range, any mat_check, any mat_move, any including_self, any self_leave, any pos, any action, any limit) -> any
```

## Description

Rush Duel helper declared in `RDFusion.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
融合召唤 - 处理
```

## Parameters

- `card` `any`: Type and behavior are not yet reviewed; see the source.
- `matfilter` `any`: Type and behavior are not yet reviewed; see the source.
- `spfilter` `any`: Type and behavior are not yet reviewed; see the source.
- `exfilter` `any`: Type and behavior are not yet reviewed; see the source.
- `s_range` `any`: Type and behavior are not yet reviewed; see the source.
- `o_range` `any`: Type and behavior are not yet reviewed; see the source.
- `mat_check` `any`: Type and behavior are not yet reviewed; see the source.
- `mat_move` `any`: Type and behavior are not yet reviewed; see the source.
- `including_self` `any`: Type and behavior are not yet reviewed; see the source.
- `self_leave` `any`: Type and behavior are not yet reviewed; see the source.
- `pos` `any`: Type and behavior are not yet reviewed; see the source.
- `action` `any`: Type and behavior are not yet reviewed; see the source.
- `limit` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDFusion.lua:550`

```lua
function RushDuel.FusionOperation(card, matfilter, spfilter, exfilter, s_range, o_range, mat_check, mat_move, including_self, self_leave, pos, action, limit)
    return function(e, tp, eg, ep, ev, re, r, rp)
        RushDuel.FusionExtraMaterialFilter = card.fusion_mat_filter
        RushDuel.FusionExtraChecker = RushDuel.FusionCheckLocation(e, self_leave, mat_check)
        local fusionable, list, chkf, gc = RushDuel.GetFusionSummonData(e, tp, pos, matfilter, spfilter, exfilter, s_range, o_range, including_self, self_leave, nil, e)
        if fusionable then
            local fc, mat = RushDuel.ExecuteFusionSummon(e, tp, pos, list, chkf, gc, mat_move)
            if action ~= nil then
                action(e, tp, eg, ep, ev, re, r, rp, mat, fc)
            end
        end
        RushDuel.FusionExtraMaterialFilter = nil
        RushDuel.FusionExtraChecker = nil
        if limit ~= nil then
            limit(e, tp, eg, ep, ev, re, r, rp)
        end
    end
end
```
