# RushDuel.GetRitualTypeValue

Alias: `RD.GetRitualTypeValue`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.GetRitualTypeValue(any c, any type) -> any
```

## Description

Rush Duel helper declared in `RDRitual.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
仪式召唤 - 数值合计参考
```

## Parameters

- `c` `any`: Type and behavior are not yet reviewed; see the source.
- `type` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDRitual.lua:70`

```lua
function RushDuel.GetRitualTypeValue(c, type)
    if type == RITUAL_ORIGINAL_LEVEL_EQUAL or type == RITUAL_ORIGINAL_LEVEL_GREATER then
        return c:GetOriginalLevel()
    elseif type == RITUAL_CURRENT_LEVEL_EQUAL or type == RITUAL_CURRENT_LEVEL_GREATER then
        return c:GetLevel()
    elseif type == RITUAL_ORIGINAL_ATTACK_EQUAL or type == RITUAL_ORIGINAL_ATTACK_GREATER then
        return c:GetBaseAttack()
    elseif type == RITUAL_CURRENT_ATTACK_EQUAL or type == RITUAL_CURRENT_ATTACK_GREATER then
        return c:GetAttack()
    end
end
```
