# RushDuel.IsCanRitualSummon

Alias: `RD.IsCanRitualSummon`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.IsCanRitualSummon(any e, any tp, any type, any matfilter, any spfilter, any exfilter, any s_range, any o_range, any mat_check, any including_self, any self_leave, any except) -> any
```

## Description

Rush Duel helper declared in `RDRitual.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
判断条件: 是否可以进行仪式召唤
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
- `mat_check` `any`: Type and behavior are not yet reviewed; see the source.
- `including_self` `any`: Type and behavior are not yet reviewed; see the source.
- `self_leave` `any`: Type and behavior are not yet reviewed; see the source.
- `except` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDRitual.lua:339`

```lua
function RushDuel.IsCanRitualSummon(e, tp, type, matfilter, spfilter, exfilter, s_range, o_range, mat_check, including_self, self_leave, except)
    RushDuel.RitualExtraChecker = RushDuel.RitualCheckLocation(e, self_leave, mat_check)
    local ritualable = RushDuel.GetRitualSummonData(e, tp, type, matfilter, spfilter, exfilter, s_range, o_range, including_self, self_leave, except)
    RushDuel.RitualExtraChecker = nil
    return ritualable
end
```
