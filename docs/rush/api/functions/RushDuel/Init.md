# RushDuel.Init

Alias: `RD.Init`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.Init() -> void
```

## Description

Initializes Rush rules, tracking flags and function overrides, and schedules the opening-turn setup. The pinned special.lua calls this through Auxiliary.PreloadUds; an MDPro4 integration may install its own bootstrap. This function is not guarded against repeated calls: do not call it from every card script.

## Returns

No return values.

## Source

`Rush/Utilities/RDRule.lua:10`

```lua
function RushDuel.Init()
    RushDuel.InitRule()
    RushDuel.InitFlag()
    RushDuel.OverrideFunction()
    -- 决斗开始
    RushDuel.CreateFieldGlobalEffect(true, EVENT_PHASE_START + PHASE_DRAW, function(e)
        -- 传说卡
        RushDuel.InitLegend()
        -- 先攻抽卡
        if not Auxiliary.Load2PickRule then
            Duel.Draw(0, 1, REASON_RULE)
        end
        e:Reset()
    end)
end
```

## Used By

Generated from the local `Rush/Scripts/` folder and `rush_cards.cdb`.

No indexed local card script currently calls this function.

This can mean the function is unused in the current script set, is only called through an alias, or is available for future/manual scripts.
