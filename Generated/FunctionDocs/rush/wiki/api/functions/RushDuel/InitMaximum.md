# RushDuel.InitMaximum

Alias: `RD.InitMaximum`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.InitMaximum() -> any
```

## Description

Rush Duel helper declared in `RDMaximum.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
初始化极大怪兽规则
```

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDMaximum.lua:8`

```lua
function RushDuel.InitMaximum()
    -- 不可改变表示形式
    local e1 = Effect.GlobalEffect()
    e1:SetType(EFFECT_TYPE_FIELD)
    e1:SetCode(EFFECT_SET_POSITION)
    e1:SetTargetRange(LOCATION_MZONE, LOCATION_MZONE)
    e1:SetTarget(RushDuel.MaximumMonster)
    e1:SetValue(POS_FACEUP_ATTACK)
    Duel.RegisterEffect(e1, 0)
    local e2 = e1:Clone()
    e2:SetCode(EFFECT_CANNOT_CHANGE_POSITION)
    e2:SetValue(0)
    Duel.RegisterEffect(e2, 0)
    local e3 = e2:Clone()
    e3:SetCode(EFFECT_CANNOT_CHANGE_POS_E)
    e3:SetTarget(RushDuel.MaximumMonsterAtk)
    Duel.RegisterEffect(e3, 0)
    local e4 = e2:Clone()
    e4:SetCode(EFFECT_CANNOT_TURN_SET)
    Duel.RegisterEffect(e4, 0)
end
```
