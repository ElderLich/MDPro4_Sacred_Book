# RushDuel.CreateFieldGlobalEffect

Alias: `RD.CreateFieldGlobalEffect`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.CreateFieldGlobalEffect(any is_continuous, any code, any operation, any limit) -> any
```

## Description

Rush Duel helper declared in `RDBase.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
创建效果: 影响全场的全局效果
```

## Parameters

- `is_continuous` `any`: Type and behavior are not yet reviewed; see the source.
- `code` `any`: Type and behavior are not yet reviewed; see the source.
- `operation` `any`: Type and behavior are not yet reviewed; see the source.
- `limit` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDBase.lua:136`

```lua
function RushDuel.CreateFieldGlobalEffect(is_continuous, code, operation, limit)
    local e1 = Effect.GlobalEffect()
    if is_continuous then
        e1:SetType(EFFECT_TYPE_FIELD + EFFECT_TYPE_CONTINUOUS)
    else
        e1:SetType(EFFECT_TYPE_FIELD)
    end
    if limit then
        e1:SetCountLimit(limit)
    end
    e1:SetCode(code)
    e1:SetOperation(operation)
    Duel.RegisterEffect(e1, 0)
    return e1
end
```
