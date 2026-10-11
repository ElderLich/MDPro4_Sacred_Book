# RushDuel.DecreaseSummonTribute

Alias: `RD.DecreaseSummonTribute`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.DecreaseSummonTribute(any card, any condition, any value) -> any
```

## Description

Rush Duel helper declared in `RDSummon.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
上级召唤所需的解放数量可以减少
```

## Parameters

- `card` `any`: Type and behavior are not yet reviewed; see the source.
- `condition` `any`: Type and behavior are not yet reviewed; see the source.
- `value` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDSummon.lua:362`

```lua
function RushDuel.DecreaseSummonTribute(card, condition, value)
    local e1 = Effect.CreateEffect(card)
    e1:SetType(EFFECT_TYPE_SINGLE)
    e1:SetCode(EFFECT_DECREASE_TRIBUTE)
    e1:SetProperty(EFFECT_FLAG_CANNOT_DISABLE + EFFECT_FLAG_UNCOPYABLE + EFFECT_FLAG_SINGLE_RANGE)
    if condition then
        e1:SetCondition(condition)
    end
    e1:SetRange(LOCATION_HAND)
    e1:SetValue(RushDuel.DecreaseSummonValue(value or 0x1))
    card:RegisterEffect(e1)
    return e1
end
```
