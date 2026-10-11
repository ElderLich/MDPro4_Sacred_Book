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

## Used By

Generated from the local `Rush/Scripts/` folder and `rush_cards.cdb`.

- Detected in **1** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=rush&mode=code&q=RushDuel.SkipCurrentPhase) with `RushDuel.SkipCurrentPhase`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Neo-Spacian Grand Mole | `120306067` | [Rush/Scripts/c120306067.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120306067.lua) | 1 |

## Script Examples

### Neo-Spacian Grand Mole (`120306067`)

Source: [Rush/Scripts/c120306067.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120306067.lua)

```lua
				Duel.BreakEffect()
				RD.SendToHandAndExists(Group.FromCards(c,tc),e,tp,REASON_EFFECT)
				RD.SkipCurrentPhase()
			end
		end)
```
