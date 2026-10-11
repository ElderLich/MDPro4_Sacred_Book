# RushDuel.RitualTypeFilter

Alias: `RD.RitualTypeFilter`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.RitualTypeFilter(any c, any type) -> any
```

## Description

Rush Duel helper declared in `RDRitual.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
仪式召唤 - 类型素材过滤
```

## Parameters

- `c` `any`: Type and behavior are not yet reviewed; see the source.
- `type` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDRitual.lua:58`

```lua
function RushDuel.RitualTypeFilter(c, type)
    if type == RITUAL_ORIGINAL_LEVEL_EQUAL or type == RITUAL_ORIGINAL_LEVEL_GREATER then
        return c:IsLevelAbove(1)
    elseif type == RITUAL_CURRENT_LEVEL_EQUAL or type == RITUAL_CURRENT_LEVEL_GREATER then
        return c:IsLevelAbove(1)
    elseif type == RITUAL_ORIGINAL_ATTACK_EQUAL or type == RITUAL_ORIGINAL_ATTACK_GREATER then
        return c:IsAttackAbove(1)
    elseif type == RITUAL_CURRENT_ATTACK_EQUAL or type == RITUAL_CURRENT_ATTACK_GREATER then
        return c:IsAttackAbove(1)
    end
end
```
