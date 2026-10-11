# RushDuel.SummonAttackChangeOperation

Alias: `RD.SummonAttackChangeOperation`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.SummonAttackChangeOperation(any attack) -> any
```

## Description

Rush Duel helper declared in `RDSummon.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
改变攻击力的召唤效果
```

## Parameters

- `attack` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDSummon.lua:155`

```lua
function RushDuel.SummonAttackChangeOperation(attack)
    return function(e, tp, eg, ep, ev, re, r, rp)
        local c = e:GetHandler()
        local e1 = Effect.CreateEffect(c)
        e1:SetType(EFFECT_TYPE_SINGLE)
        e1:SetCode(EFFECT_SET_BASE_ATTACK)
        e1:SetProperty(EFFECT_FLAG_SINGLE_RANGE)
        e1:SetRange(LOCATION_MZONE)
        e1:SetValue(attack)
        e1:SetReset(RESET_EVENT + 0xff0000)
        c:RegisterEffect(e1)
    end
end
```

## Used By

Generated from the local `Rush/Scripts/` folder and `rush_cards.cdb`.

No indexed local card script currently calls this function.

This can mean the function is unused in the current script set, is only called through an alias, or is available for future/manual scripts.
