# RushDuel.ContinuousBattleDestroyToGrave

Alias: `RD.ContinuousBattleDestroyToGrave`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.ContinuousBattleDestroyToGrave(any card, any condition, any operation, any register) -> any
```

## Description

Rush Duel helper declared in `RDContinuous.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
永续效果: 战斗破坏怪兽送去墓地时的处理
```

## Parameters

- `card` `any`: Type and behavior are not yet reviewed; see the source.
- `condition` `any`: Type and behavior are not yet reviewed; see the source.
- `operation` `any`: Type and behavior are not yet reviewed; see the source.
- `register` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDContinuous.lua:85`

```lua
function RushDuel.ContinuousBattleDestroyToGrave(card, condition, operation, register)
    local e1 = Effect.CreateEffect(card)
    e1:SetType(EFFECT_TYPE_SINGLE + EFFECT_TYPE_CONTINUOUS)
    e1:SetCode(EVENT_BATTLE_DESTROYING)
    e1:SetCondition(RushDuel.BattleDestroyToGraveCondition(condition))
    e1:SetOperation(RushDuel.BattleDestroyToGraveOperation(operation))
    if register ~= false then
        card:RegisterEffect(e1)
    end
    return e1
end
```
