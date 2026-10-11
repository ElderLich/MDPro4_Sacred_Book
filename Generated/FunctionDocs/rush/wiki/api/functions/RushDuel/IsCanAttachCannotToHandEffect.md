# RushDuel.IsCanAttachCannotToHandEffect

Alias: `RD.IsCanAttachCannotToHandEffect`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.IsCanAttachCannotToHandEffect(any card, any value) -> any
```

## Description

Rush Duel helper declared in `RDCondition.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
条件: 可否赋予效果 - 不会因效果回到手卡
```

## Parameters

- `card` `any`: Type and behavior are not yet reviewed; see the source.
- `value` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDCondition.lua:321`

```lua
function RushDuel.IsCanAttachCannotToHandEffect(card, value)
    local values = RushDuel.GetEffectValues(card, EFFECT_CANNOT_TO_HAND_EFFECT)
    for _, val in ipairs(values) do
        if val == 1 then
            return false
        end
    end
    return true
end
```
