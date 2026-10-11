# RushDuel.CanSelectAndToHandOrSpecialSummon

Alias: `RD.CanSelectAndToHandOrSpecialSummon`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.CanSelectAndToHandOrSpecialSummon(any desc, any hint, any filter, any tp, any s_range, any o_range, any expect, any e, any pos, any break_effect, any target_player) -> any
```

## Description

Rush Duel helper declared in `RDAction.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
可选操作: 选择怪兽加入手卡或者特殊召唤 (限定 1 只怪兽)
```

## Parameters

- `desc` `any`: Type and behavior are not yet reviewed; see the source.
- `hint` `any`: Type and behavior are not yet reviewed; see the source.
- `filter` `any`: Type and behavior are not yet reviewed; see the source.
- `tp` `any`: Type and behavior are not yet reviewed; see the source.
- `s_range` `any`: Type and behavior are not yet reviewed; see the source.
- `o_range` `any`: Type and behavior are not yet reviewed; see the source.
- `expect` `any`: Type and behavior are not yet reviewed; see the source.
- `e` `any`: Type and behavior are not yet reviewed; see the source.
- `pos` `any`: Type and behavior are not yet reviewed; see the source.
- `break_effect` `any`: Type and behavior are not yet reviewed; see the source.
- `target_player` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDAction.lua:173`

```lua
function RushDuel.CanSelectAndToHandOrSpecialSummon(desc, hint, filter, tp, s_range, o_range, expect, e, pos, break_effect, target_player)
    return RushDuel._private_action_can_select_match(desc, hint, filter, tp, s_range, o_range, 1, 1, expect, false, false, function(g)
        local tc = g:GetFirst()
        local ft = RushDuel.GetMZoneCount(target_player or tp, 1)
        if tc:IsAbleToHand() and (not RD.IsCanBeSpecialSummoned(tc, e, tp, pos) or ft <= 0 or Duel.SelectOption(tp, 1190, 1152) == 0) then
            if break_effect then
                Duel.BreakEffect()
            end
            return RushDuel.SendToHandAndExists(tc, e, tp, REASON_EFFECT)
        else
            return RushDuel._special_summon(tc, e, tp, pos, break_effect, target_player)~=0
        end
    end, e, tp)
end
```
