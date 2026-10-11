# RushDuel.IsMainPhase

Alias: `RD.IsMainPhase`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.IsMainPhase() -> any
```

## Description

Rush Duel helper declared in `RDCondition.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
条件: 玩家的主要阶段
```

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDCondition.lua:21`

```lua
function RushDuel.IsMainPhase()
    local player = Duel.GetTurnPlayer()
    if Duel.GetFlagEffect(player, FLAG_SKIP_MAIN_PHASE) ~= 0 then
        return false
    end
    local ph = Duel.GetCurrentPhase()
    return ph == PHASE_MAIN1 or ph == PHASE_MAIN2
end
```
