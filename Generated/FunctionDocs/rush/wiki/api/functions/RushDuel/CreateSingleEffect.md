# RushDuel.CreateSingleEffect

Alias: `RD.CreateSingleEffect`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.CreateSingleEffect(any e, any desc, any card, any code, any value, any reset, any forced) -> any
```

## Description

Rush Duel helper declared in `RDBase.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
创建效果: Buff类效果
```

## Parameters

- `e` `any`: Type and behavior are not yet reviewed; see the source.
- `desc` `any`: Type and behavior are not yet reviewed; see the source.
- `card` `any`: Type and behavior are not yet reviewed; see the source.
- `code` `any`: Type and behavior are not yet reviewed; see the source.
- `value` `any`: Type and behavior are not yet reviewed; see the source.
- `reset` `any`: Type and behavior are not yet reviewed; see the source.
- `forced` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDBase.lua:163`

```lua
function RushDuel.CreateSingleEffect(e, desc, card, code, value, reset, forced)
    local e1 = Effect.CreateEffect(e:GetHandler())
    e1:SetType(EFFECT_TYPE_SINGLE)
    e1:SetCode(code)
    if desc ~= nil then
        e1:SetDescription(desc)
        e1:SetProperty(EFFECT_FLAG_CLIENT_HINT)
    end
    e1:SetLabel(FLAG_ATTACH_EFFECT)
    if value ~= nil then
        e1:SetValue(value)
    end
    if reset ~= nil then
        e1:SetReset(reset)
    end
    card:RegisterEffect(e1, forced)
    return e1
end
```
