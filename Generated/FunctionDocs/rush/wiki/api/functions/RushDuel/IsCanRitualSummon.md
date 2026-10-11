# RushDuel.IsCanRitualSummon

Alias: `RD.IsCanRitualSummon`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.IsCanRitualSummon(any e, any tp, any type, any matfilter, any spfilter, any exfilter, any s_range, any o_range, any mat_check, any including_self, any self_leave, any except) -> bool
```

## Description

Checks whether a Ritual candidate and legal material selection exist, including the material-group and zone restriction. This predicate does not open the monster/material selection prompts.
Advanced helper used by CreateRitualEffect: pass explicit location masks and the remaining builder arguments. The factory normalizes optional inputs for ordinary card scripts; calling this lower-level function with omitted location arguments is not equivalent.

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

- `bool`: Whether at least one supported summon route exists.

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
