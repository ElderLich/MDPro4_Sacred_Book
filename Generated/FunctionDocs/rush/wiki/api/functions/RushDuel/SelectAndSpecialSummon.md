# RushDuel.SelectAndSpecialSummon

Alias: `RD.SelectAndSpecialSummon`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.SelectAndSpecialSummon(function filter, int tp, int s_range, int o_range, int min, int max, Card|Group|nil expect, Effect e, int pos, [bool break_effect], [int target_player]) -> int
```

## Description

Checks destination Monster Zone capacity, selects a nonempty Group and performs an ordinary Special Summon with summon type 0, nocheck=false and nolimit=false. The filter must supply per-card summon legality; zone capacity alone does not make every monster summonable.
Unlike the general SelectAndDoAction wrapper, this helper passes e,tp,pos,break_effect,target_player as extra filter arguments. The return value is the actual Duel.SpecialSummon count, or 0 when no selection/summon occurs. Face-down summon confirmation is handled by the Rush private wrapper.

## Parameters

- `filter` `function`: Candidate predicate; receives card,e,tp,pos,break_effect,target_player. Include per-card summon legality.
- `tp` `int`: Selecting and summoning player.
- `s_range` `int`: Source locations on tp side.
- `o_range` `int`: Source locations on the opponent side.
- `min` `int`: Minimum selected count.
- `max` `int`: Maximum count, capped by the destination zone count.
- `expect` `Card|Group|nil`: Excluded Card(s), or nil.
- `e` `Effect`: Source effect passed to the filter.
- `pos` `int`: Required summon position mask.
- `break_effect` `bool` (optional): Call Duel.BreakEffect immediately before summoning; default false.
- `target_player` `int` (optional): Destination player; defaults to tp. Does not change which player makes the choice.

## Returns

- `int`: Actual summon count, or 0 if capacity/candidates/selection do not permit the operation.

## Source

`Rush/Utilities/RDAction.lua:123`

```lua
function RushDuel.SelectAndSpecialSummon(filter, tp, s_range, o_range, min, max, expect, e, pos, break_effect, target_player)
    local ct = RushDuel.GetMZoneCount(target_player or tp, max)
    if ct >= min then
        return RushDuel._private_action_select_match(HINTMSG_SPSUMMON, filter, tp, s_range, o_range, min, ct, expect, false, false, RushDuel._special_summon, e, tp, pos, break_effect, target_player)
    end
    return 0
end
```
