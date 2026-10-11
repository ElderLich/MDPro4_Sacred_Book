# RushDuel.GetEffectValues

Alias: `RD.GetEffectValues`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.GetEffectValues(any card, any code) -> any
```

## Description

Rush Duel helper declared in `RDBase.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
获取效果值列表
```

## Parameters

- `card` `any`: Type and behavior are not yet reviewed; see the source.
- `code` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDBase.lua:268`

```lua
function RushDuel.GetEffectValues(card, code)
    local effects = RushDuel.GetAttachEffects(card, code)
    local values = {}
    for i, effect in ipairs(effects) do
        values[i] = effect:GetValue()
    end
    return values
end
```

## Used By

Generated from the local `Rush/Scripts/` folder and `rush_cards.cdb`.

No indexed local card script currently calls this function.

This can mean the function is unused in the current script set, is only called through an alias, or is available for future/manual scripts.
