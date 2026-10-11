# RushDuel.SkipCurrentPhase

Alias: `RD.SkipCurrentPhase`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.SkipCurrentPhase() -> any
```

## Description

Rush Duel helper declared in `RDAction.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
操作: 结束当前阶段
```

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDAction.lua:560`

```lua
function RushDuel.SkipCurrentPhase()
    local player = Duel.GetTurnPlayer()
    local phase = Duel.GetCurrentPhase()
    Duel.SkipPhase(player, phase, RESET_PHASE + PHASE_END, 1)
    if phase == PHASE_MAIN1 or phase == PHASE_MAIN2 then
        Duel.RegisterFlagEffect(player, FLAG_SKIP_MAIN_PHASE, RESET_PHASE + PHASE_END, 0, 1)
    end
end
```
