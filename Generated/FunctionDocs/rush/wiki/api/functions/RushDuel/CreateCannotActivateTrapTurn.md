# RushDuel.CreateCannotActivateTrapTurn

Alias: `RD.CreateCannotActivateTrapTurn`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.CreateCannotActivateTrapTurn(any e, any desc, any player, any s_range, any o_range) -> any
```

## Description

Rush Duel helper declared in `RDLimit.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
创建限制: 整个回合, 不能发动陷阱卡
```

## Parameters

- `e` `any`: Type and behavior are not yet reviewed; see the source.
- `desc` `any`: Type and behavior are not yet reviewed; see the source.
- `player` `any`: Type and behavior are not yet reviewed; see the source.
- `s_range` `any`: Type and behavior are not yet reviewed; see the source.
- `o_range` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDLimit.lua:314`

```lua
function RushDuel.CreateCannotActivateTrapTurn(e, desc, player, s_range, o_range)
    local e1 = RushDuel.CreateCannotActivateMix(e, desc, player, s_range, o_range, RESET_PHASE + PHASE_END,
        function(e, re, tp)
            return re:IsHasType(EFFECT_TYPE_ACTIVATE) and re:IsActiveType(TYPE_TRAP)
        end)
    local e2 = Effect.CreateEffect(e:GetHandler())
    e2:SetType(EFFECT_TYPE_FIELD)
    e2:SetCode(EFFECT_PLAYER_CANNOT_ACTIVATE_TRAP)
    e2:SetProperty(EFFECT_FLAG_PLAYER_TARGET)
    e2:SetTargetRange(s_range, o_range)
    e2:SetReset(RESET_PHASE + PHASE_END)
    Duel.RegisterEffect(e2, player)
    return e1, e2
end
```
