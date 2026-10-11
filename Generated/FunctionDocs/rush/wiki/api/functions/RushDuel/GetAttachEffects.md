# RushDuel.GetAttachEffects

Alias: `RD.GetAttachEffects`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.GetAttachEffects(any card, any code) -> any
```

## Description

Rush Duel helper declared in `RDBase.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
获取附加的效果
```

## Parameters

- `card` `any`: Type and behavior are not yet reviewed; see the source.
- `code` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDBase.lua:256`

```lua
function RushDuel.GetAttachEffects(card, code)
    local effects = {card:IsHasEffect(code)}
    local attachs = {}
    for i, effect in ipairs(effects) do
        if effect:GetLabel() == FLAG_ATTACH_EFFECT then
            table.insert(attachs, effect)
        end
    end
    return attachs
end
```
