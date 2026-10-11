# RushDuel.CanSelectAndSpecialSummon

Alias: `RD.CanSelectAndSpecialSummon`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.CanSelectAndSpecialSummon(int desc, function filter, int tp, int s_range, int o_range, int min, int max, Card|Group|nil expect, Effect e, int pos, [bool break_effect], [int target_player]) -> int
```

## Description

Optional action version of SelectAndSpecialSummon. If capacity and candidates exist, asks yes/no before selecting and summoning. Declining returns 0; canceling card selection returns to the yes/no question.
This performs work and belongs in resolution, not chk==0. It uses the same filter arguments, destination rules and actual numeric summon count as SelectAndSpecialSummon.

## Parameters

- `desc` `int`: Yes/no prompt description identifier.
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

- `int`: Actual summon count, or 0 when declined/unavailable.

## Source

`Rush/Utilities/RDAction.lua:131`

```lua
function RushDuel.CanSelectAndSpecialSummon(desc, filter, tp, s_range, o_range, min, max, expect, e, pos, break_effect, target_player)
    local ct = RushDuel.GetMZoneCount(target_player or tp, max)
    if ct >= min then
        return RushDuel._private_action_can_select_match(desc, HINTMSG_SPSUMMON, filter, tp, s_range, o_range, min, ct, expect, false, false, RushDuel._special_summon, e, tp, pos, break_effect,
            target_player)
    end
    return 0
end
```
