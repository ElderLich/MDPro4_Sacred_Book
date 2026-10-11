# RushDuel.IsCanAttachExtraAttack

Alias: `RD.IsCanAttachExtraAttack`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.IsCanAttachExtraAttack(any card, any value) -> any
```

## Description

Rush Duel helper declared in `RDCondition.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
条件: 可否赋予效果 - 多次攻击
```

## Parameters

- `card` `any`: Type and behavior are not yet reviewed; see the source.
- `value` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDCondition.lua:247`

```lua
function RushDuel.IsCanAttachExtraAttack(card, value)
    if not RushDuel.IsCanAttack(card) then
        return false
    end
    local values = RushDuel.GetEffectValues(card, EFFECT_EXTRA_ATTACK)
    for _, val in ipairs(values) do
        if val >= value then
            return false
        end
    end
    return true
end
```
