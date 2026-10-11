# RushDuel.AddMaximumProcedure

Alias: `RD.AddMaximumProcedure`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.AddMaximumProcedure(Card card, int max_atk, int left_code, int right_code) -> void
```

## Description

Registers the center monster's Maximum Summon procedure, Maximum ATK and zone-limit effect. left_code and right_code identify the two components selected from hand. The pinned implementation stores components as overlays; use the matching Rush helpers when moving a Maximum monster.

## Parameters

- `card` `Card`: Center Maximum monster.
- `max_atk` `int`: ATK while in Maximum mode.
- `left_code` `int`: Left component passcode.
- `right_code` `int`: Right component passcode.

## Returns

No return values.

## Example

```lua
-- Inside the center card's initial_effect:
RD.AddMaximumProcedure(c, 4000, 120150001, 120150003)
```

## Source

`Rush/Utilities/RDMaximum.lua:37`

```lua
function RushDuel.AddMaximumProcedure(card, max_atk, left_code, right_code)
    if card:IsStatus(STATUS_COPYING_EFFECT) then
        return
    end
    -- 记录状态
    if card.maximum_attack == nil then
        local mt = getmetatable(card)
        mt.maximum_attack = max_atk
    end
    -- 极大召唤 手续
    RushDuel.AddHandSpecialSummonProcedure(card, HINTMSG_MAXSUMMON, RushDuel.MaximumSummonCondition(left_code, right_code), RushDuel.MaximumSummonTarget(left_code, right_code),
        RushDuel.MaximumSummonOperation(left_code, right_code), RushDuel.MaximumSummonValue, POS_FACEUP_ATTACK)
    -- 极大攻击力
    local e1 = Effect.CreateEffect(card)
    e1:SetType(EFFECT_TYPE_SINGLE)
    e1:SetCode(EFFECT_SET_BASE_ATTACK)
    e1:SetProperty(EFFECT_FLAG_SINGLE_RANGE + EFFECT_FLAG_CANNOT_DISABLE + EFFECT_FLAG_UNCOPYABLE)
    e1:SetRange(LOCATION_MZONE)
    e1:SetCondition(RushDuel.MaximumMode)
    e1:SetValue(max_atk)
    card:RegisterEffect(e1)
    -- 占用3个主要怪兽区域
    local e2 = Effect.CreateEffect(card)
    e2:SetType(EFFECT_TYPE_FIELD)
    e2:SetCode(EFFECT_MAX_MZONE)
    e2:SetProperty(EFFECT_FLAG_PLAYER_TARGET + EFFECT_FLAG_CANNOT_DISABLE + EFFECT_FLAG_UNCOPYABLE)
    e2:SetRange(LOCATION_MZONE)
    e2:SetTargetRange(1, 0)
    e2:SetCondition(RushDuel.MaximumMode)
    e2:SetValue(1)
    card:RegisterEffect(e2)
end
```
