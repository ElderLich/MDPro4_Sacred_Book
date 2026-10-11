# RushDuel.CreatePlayerTargetGlobalEffect

Alias: `RD.CreatePlayerTargetGlobalEffect`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.CreatePlayerTargetGlobalEffect(any code, any value) -> any
```

## Description

Rush Duel helper declared in `RDBase.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
创建效果: 玩家对象的全局效果
```

## Parameters

- `code` `any`: Type and behavior are not yet reviewed; see the source.
- `value` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDBase.lua:123`

```lua
function RushDuel.CreatePlayerTargetGlobalEffect(code, value)
    local e1 = Effect.GlobalEffect()
    e1:SetType(EFFECT_TYPE_FIELD)
    e1:SetCode(code)
    e1:SetProperty(EFFECT_FLAG_PLAYER_TARGET)
    e1:SetTargetRange(1, 1)
    if value ~= nil then
        e1:SetValue(value)
    end
    Duel.RegisterEffect(e1, 0)
    return e1
end
```

## Used By

Generated from the local `Rush/Scripts/` folder and `rush_cards.cdb`.

No indexed local card script currently calls this function.

This can mean the function is unused in the current script set, is only called through an alias, or is available for future/manual scripts.
