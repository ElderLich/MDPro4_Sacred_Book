# RushDuel.CreateTripleTribute

Alias: `RD.CreateTripleTribute`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.CreateTripleTribute(any source, any card, any desc, any value, any forced) -> any
```

## Description

Rush Duel helper declared in `RDSummon.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
三重解放 (临时处理方法)
```

## Parameters

- `source` `any`: Type and behavior are not yet reviewed; see the source.
- `card` `any`: Type and behavior are not yet reviewed; see the source.
- `desc` `any`: Type and behavior are not yet reviewed; see the source.
- `value` `any`: Type and behavior are not yet reviewed; see the source.
- `forced` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDSummon.lua:327`

```lua
function RushDuel.CreateTripleTribute(source, card, desc, value, forced)
    local e1 = Effect.CreateEffect(source)
    e1:SetDescription(desc)
    e1:SetType(EFFECT_TYPE_FIELD)
    e1:SetCode(EFFECT_SUMMON_PROC)
    e1:SetRange(LOCATION_MZONE)
    e1:SetTargetRange(LOCATION_HAND, 0)
    e1:SetCondition(RushDuel.TripleTributeCondition)
    e1:SetTarget(RushDuel.TripleTributeTarget(value))
    e1:SetOperation(RushDuel.TripleTributeOperation)
    e1:SetValue(SUMMON_TYPE_ADVANCE + SUMMON_VALUE_THREE + SUMMON_VALUE_SELF)
    card:RegisterEffect(e1, forced)
    return e1
end
```

## Used By

Generated from the local `Rush/Scripts/` folder and `rush_cards.cdb`.

No indexed local card script currently calls this function.

This can mean the function is unused in the current script set, is only called through an alias, or is available for future/manual scripts.
