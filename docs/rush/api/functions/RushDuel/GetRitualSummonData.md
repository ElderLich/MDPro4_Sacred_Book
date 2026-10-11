# RushDuel.GetRitualSummonData

Alias: `RD.GetRitualSummonData`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.GetRitualSummonData(any e, any tp, any type, any matfilter, any spfilter, any exfilter, any s_range, any o_range, any including_self, any self_leave, any except, any effect) -> any
```

## Description

Rush Duel helper declared in `RDRitual.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
仪式召唤 - 获取仪式素材与仪式怪兽
```

## Parameters

- `e` `any`: Type and behavior are not yet reviewed; see the source.
- `tp` `any`: Type and behavior are not yet reviewed; see the source.
- `type` `any`: Type and behavior are not yet reviewed; see the source.
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

`Rush/Utilities/RDRitual.lua:223`

```lua
function RushDuel.GetRitualSummonData(e, tp, type, matfilter, spfilter, exfilter, s_range, o_range, including_self, self_leave, except, effect)
    local chkf = tp
    if except and self_leave then
        except:AddCard(e:GetHandler())
    elseif self_leave then
        except = e:GetHandler()
    end
    local mg = Duel.GetRitualMaterial(tp):Filter(RushDuel.RitualMaterialFilter, except, type, matfilter, effect)
    if s_range ~= 0 or o_range ~= 0 then
        local ext = Duel.GetMatchingGroup(Auxiliary.NecroValleyFilter(exfilter), tp, s_range, o_range, except, effect)
        mg:Merge(ext:Filter(RushDuel.RitualMaterialFilter, nil, type, nil, effect))
    end
    local gc = nil
    if including_self then
        gc = e:GetHandler()
    end
    local sg = Duel.GetMatchingGroup(RushDuel.RitualSpecialSummonFilter, tp, LOCATION_EXTRA, 0, nil, e, tp, type, mg, nil, gc, chkf, spfilter)
    local list = {}
    local ritualable = false
    if #sg > 0 then
        table.insert(list, {nil, mg, sg})
        ritualable = true
    end
    local effects = {Duel.IsPlayerAffectedByEffect(tp, EFFECT_RITUAL_MATERIAL)}
    for _, effect in ipairs(effects) do
        local target = effect:GetTarget()
        local mg2 = target(effect, e, tp, mg)
        if #mg2 > 0 then
            local mf = effect:GetValue()
            local sg2 = Duel.GetMatchingGroup(RushDuel.RitualSpecialSummonFilter, tp, LOCATION_EXTRA, 0, nil, e, tp, type, mg2, mf, gc, chkf, spfilter)
            if #sg2 > 0 then
                table.insert(list, {effect, mg2, sg2})
                ritualable = true
            end
        end
    end
    return ritualable, list, chkf, gc
end
```

## Used By

Generated from the local `Rush/Scripts/` folder and `rush_cards.cdb`.

No indexed local card script currently calls this function.

This can mean the function is unused in the current script set, is only called through an alias, or is available for future/manual scripts.
