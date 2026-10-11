# RushDuel.InitFlag

Alias: `RD.InitFlag`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.InitFlag() -> any
```

## Description

Rush Duel helper declared in `RDRule.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
初始化标记
```

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDRule.lua:99`

```lua
function RushDuel.InitFlag()
    local reg_summon = function(e, tp, eg, ep, ev, re, r, rp)
        eg:ForEach(function(tc)
            tc:RegisterFlagEffect(FLAG_SUMMON_TURN, RESET_EVENT + RESETS_STANDARD + RESET_PHASE + PHASE_END, EFFECT_FLAG_CLIENT_HINT, 1, 0, HINTMSG_SUMMON_TURN)
            if RushDuel.IsMainPhase() then
                tc:RegisterFlagEffect(FLAG_SUMMON_MAIN_PHASE, RESET_EVENT + RESETS_STANDARD + RESET_PHASE + PHASE_MAIN1 + PHASE_MAIN2, 0, 1)
            end
        end)
    end
    local reg_spsummon = function(e, tp, eg, ep, ev, re, r, rp)
        eg:ForEach(function(tc)
            tc:RegisterFlagEffect(FLAG_SUMMON_TURN, RESET_EVENT + RESETS_STANDARD + RESET_PHASE + PHASE_END, EFFECT_FLAG_CLIENT_HINT, 1, 0, HINTMSG_SPSUMMON_TURN)
            if RushDuel.IsMainPhase() then
                tc:RegisterFlagEffect(FLAG_SUMMON_MAIN_PHASE, RESET_EVENT + RESETS_STANDARD + RESET_PHASE + PHASE_MAIN1 + PHASE_MAIN2, 0, 1)
            end
        end)
    end
    local reg_flip = function(e, tp, eg, ep, ev, re, r, rp)
        eg:ForEach(function(tc)
            tc:RegisterFlagEffect(FLAG_FLIP_TURN, RESET_EVENT + RESETS_STANDARD + RESET_PHASE + PHASE_END, EFFECT_FLAG_CLIENT_HINT, 1, 0, HINTMSG_FILP_TURN)
            if RushDuel.IsMainPhase() then
                tc:RegisterFlagEffect(FLAG_FLIP_MAIN_PHASE, RESET_EVENT + RESETS_STANDARD + RESET_PHASE + PHASE_MAIN1 + PHASE_MAIN2, 0, 1)
            end
        end)
    end
    local reg_attack = function(e, tp, eg, ep, ev, re, r, rp)
        Duel.RegisterFlagEffect(rp, FLAG_ATTACK_ANNOUNCED, RESET_PHASE + PHASE_DAMAGE, 0, 1)
    end
    local reg_draw = function(e, tp, eg, ep, ev, re, r, rp)
        local ph = Duel.GetCurrentPhase()
        if ph == PHASE_MAIN1 or ph == PHASE_MAIN2 then
            Duel.RegisterFlagEffect(ep, FLAG_HAS_DRAW_IN_MAIN_PHASE, RESET_PHASE + PHASE_MAIN1 + PHASE_MAIN2, 0, 1)
        end
        Duel.RegisterFlagEffect(ep, FLAG_HAS_DRAW_IN_TURN, RESET_PHASE + PHASE_END, 0, 1)
    end
    RushDuel.CreateFieldGlobalEffect(true, EVENT_SUMMON_SUCCESS, reg_summon)
    RushDuel.CreateFieldGlobalEffect(true, EVENT_SPSUMMON_SUCCESS, reg_spsummon)
    RushDuel.CreateFieldGlobalEffect(true, EVENT_FLIP, reg_flip)
    RushDuel.CreateFieldGlobalEffect(true, EVENT_ATTACK_ANNOUNCE, reg_attack)
    RushDuel.CreateFieldGlobalEffect(true, EVENT_DRAW, reg_draw)
end
```
