# RushDuel.ChangePosition

Alias: `RD.ChangePosition`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.ChangePosition(any target, any effect, any player, any reason, any pos) -> any
```

## Description

Rush Duel helper declared in `RDAction.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
操作: 改变表示形式
```

## Parameters

- `target` `any`: Type and behavior are not yet reviewed; see the source.
- `effect` `any`: Type and behavior are not yet reviewed; see the source.
- `player` `any`: Type and behavior are not yet reviewed; see the source.
- `reason` `any`: Type and behavior are not yet reviewed; see the source.
- `pos` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDAction.lua:236`

```lua
function RushDuel.ChangePosition(target, effect, player, reason, pos)
    local hints = Group.CreateGroup()
    local group = RushDuel.ToGroup(target):Filter(RushDuel.FilterChangePositionTarget, nil, effect, player, reason, hints)
    local tc = hints:GetFirst()
    if tc then
        Duel.Hint(HINT_CARD, 0, tc:GetOriginalCode())
    end
    if group:GetCount() > 0 then
        if pos == nil then
            return Duel.ChangePosition(group, POS_FACEUP_DEFENSE, POS_FACEUP_DEFENSE, POS_FACEUP_ATTACK, POS_FACEUP_ATTACK)
        else
            return Duel.ChangePosition(group, pos)
        end
    else
        return 0
    end
end
```
