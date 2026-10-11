# RushDuel.GetFusionSummonData

Alias: `RD.GetFusionSummonData`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.GetFusionSummonData(any e, any tp, any pos, any matfilter, any spfilter, any exfilter, any s_range, any o_range, any including_self, any self_leave, any except, any effect) -> any
```

## Description

Rush Duel helper declared in `RDFusion.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
融合召唤 - 获取融合素材与融合怪兽
```

## Parameters

- `e` `any`: Type and behavior are not yet reviewed; see the source.
- `tp` `any`: Type and behavior are not yet reviewed; see the source.
- `pos` `any`: Type and behavior are not yet reviewed; see the source.
- `matfilter` `any`: Type and behavior are not yet reviewed; see the source.
- `spfilter` `any`: Type and behavior are not yet reviewed; see the source.
- `exfilter` `any`: Type and behavior are not yet reviewed; see the source.
- `s_range` `any`: Type and behavior are not yet reviewed; see the source.
- `o_range` `any`: Type and behavior are not yet reviewed; see the source.
- `including_self` `any`: Type and behavior are not yet reviewed; see the source.
- `self_leave` `any`: Type and behavior are not yet reviewed; see the source.
- `except` `any`: Type and behavior are not yet reviewed; see the source.
- `effect` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDFusion.lua:412`

```lua
function RushDuel.GetFusionSummonData(e, tp, pos, matfilter, spfilter, exfilter, s_range, o_range, including_self, self_leave, except, effect)
    local chkf = tp
    if except and self_leave then
        except:AddCard(e:GetHandler())
    elseif self_leave then
        except = e:GetHandler()
    end
    local mg = Duel.GetFusionMaterial(tp):Filter(RushDuel.FusionMaterialFilter, except, matfilter, effect)
    if s_range ~= 0 or o_range ~= 0 then
        local ext = Duel.GetMatchingGroup(Auxiliary.NecroValleyFilter(exfilter), tp, s_range, o_range, except, effect)
        mg:Merge(ext)
    end
    local gc = nil
    if including_self then
        gc = e:GetHandler()
    end
    if RushDuel.FusionExtraMaterialFilter then
        mg = mg:Filter(RushDuel.FusionExtraMaterialFilter, nil, e, tp, mg)
    end
    local sg = Duel.GetMatchingGroup(RushDuel.FusionSpecialSummonFilter, tp, LOCATION_EXTRA, 0, nil, e, tp, pos, mg, nil, gc, chkf, spfilter)
    local list = {}
    local fusionable = false
    if #sg > 0 then
        table.insert(list, {nil, mg, sg})
        fusionable = true
    end
    local effects = {Duel.IsPlayerAffectedByEffect(tp, EFFECT_CHAIN_MATERIAL)}
    for _, effect in ipairs(effects) do
        local target = effect:GetTarget()
        local mg2 = target(effect, e, tp, mg)
        if RushDuel.FusionExtraMaterialFilter then
            mg2 = mg2:Filter(RushDuel.FusionExtraMaterialFilter, nil, e, tp, mg2)
        end
        if #mg2 > 0 then
            local mf = effect:GetValue()
            local sg2 = Duel.GetMatchingGroup(RushDuel.FusionSpecialSummonFilter, tp, LOCATION_EXTRA, 0, nil, e, tp, pos, mg2, mf, gc, chkf, spfilter)
            if #sg2 > 0 then
                table.insert(list, {effect, mg2, sg2})
                fusionable = true
            end
        end
    end
    return fusionable, list, chkf, gc
end
```
