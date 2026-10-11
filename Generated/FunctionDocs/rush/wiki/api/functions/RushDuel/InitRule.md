# RushDuel.InitRule

Alias: `RD.InitRule`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.InitRule() -> any
```

## Description

Rush Duel helper declared in `RDRule.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
初始化规则
```

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDRule.lua:26`

```lua
function RushDuel.InitRule()
    -- 禁用最左与最右列
    RushDuel.CreateFieldGlobalEffect(false, EFFECT_DISABLE_FIELD, function()
        return 0x11711171
    end)
    -- 抽卡阶段, 抽卡至5张, 超过5张时改为抽1张
    RushDuel.CreatePlayerTargetGlobalEffect(EFFECT_DRAW_COUNT, function()
        return math.max(1, 5 - Duel.GetFieldGroupCount(Duel.GetTurnPlayer(), LOCATION_HAND, 0))
    end)
    -- 抽卡阶段抽卡后, 洗切手卡
    local e1 = Effect.GlobalEffect()
    e1:SetType(EFFECT_TYPE_FIELD + EFFECT_TYPE_CONTINUOUS)
    e1:SetCode(EVENT_DRAW)
    e1:SetCondition(function()
        return Duel.GetCurrentPhase() == PHASE_DRAW
    end)
    e1:SetOperation(function()
        local tp = Duel.GetTurnPlayer()
        if RushDuel.NeedShuffleHand[tp + 1] then
            Duel.ShuffleHand(tp)
        end
        RushDuel.NeedShuffleHand[1] = false
        RushDuel.NeedShuffleHand[2] = false
    end)
    Duel.RegisterEffect(e1, 0)
    -- 跳过准备阶段
    RushDuel.CreatePlayerTargetGlobalEffect(EFFECT_SKIP_SP)
    -- 召唤次数无限制
    RushDuel.CreatePlayerTargetGlobalEffect(EFFECT_SET_SUMMON_COUNT_LIMIT, 100)
    -- 场上的怪兽的效果强制1回合1次
    local function get_effect_owner_code(e)
        if e:GetType() & EFFECT_TYPE_XMATERIAL == EFFECT_TYPE_XMATERIAL then
            -- 极大怪兽的L/R部分的效果分开计算
            return e:GetLabel()
        else
            return e:GetOwner():GetOriginalCode()
        end
    end
    RushDuel.CreatePlayerTargetGlobalEffect(EFFECT_CANNOT_ACTIVATE, function(e, re, tp)
        return re:GetHandler():GetFlagEffect(get_effect_owner_code(re)) ~= 0
    end)
    RushDuel.CreateFieldGlobalEffect(true, EVENT_CHAIN_SOLVING, function(e, tp, eg, ep, ev, re, r, rp)
        local te = Duel.GetChainInfo(ev, CHAININFO_TRIGGERING_EFFECT)
        local tc=te:GetHandler()
        local code = get_effect_owner_code(te)
        tc:RegisterFlagEffect(code, RESET_EVENT + RESETS_STANDARD + RESET_PHASE + PHASE_END, EFFECT_FLAG_CLIENT_HINT, 1, 0, HINTMSG_EFFECT_USED)
        RushDuel.ActivateCodes[ep + 1][tc:GetCode()] = true
    end)
    -- 同一时点只能发动一张陷阱卡
    local function is_trap(e)
        return e:IsHasType(EFFECT_TYPE_ACTIVATE) and e:IsActiveType(TYPE_TRAP)
    end
    local function tarp_limit(e, rp, tp)
        return not is_trap(e)
    end
    RushDuel.CreateFieldGlobalEffect(true, EVENT_CHAINING, function(e, tp, eg, ep, ev, re, r, rp)
        if is_trap(re) then
            Duel.SetChainLimit(tarp_limit)
        end
    end)
    -- 没有主要阶段2
    RushDuel.CreatePlayerTargetGlobalEffect(EFFECT_SKIP_M2)
    --RushDuel.CreatePlayerTargetGlobalEffect(EFFECT_CANNOT_M2)
    -- 手卡无限制
    RushDuel.CreatePlayerTargetGlobalEffect(EFFECT_HAND_LIMIT, 100)
    -- 结束阶段重置计数
    RushDuel.CreateFieldGlobalEffect(true, EVENT_PHASE_START + PHASE_DRAW, function(e, tp, eg, ep, ev, re, r, rp)
        RushDuel.ActivateCodes = {{}, {}}
    end, 1)
    -- 极大怪兽
    RushDuel.InitMaximum()
end
```
