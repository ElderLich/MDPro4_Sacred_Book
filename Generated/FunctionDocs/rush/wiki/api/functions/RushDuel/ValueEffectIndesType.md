# RushDuel.ValueEffectIndesType

Alias: `RD.ValueEffectIndesType`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.ValueEffectIndesType(any self_type, any opponent_type, any ignore) -> any
```

## Description

Rush Duel helper declared in `RDValue.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
效果值: 效果破坏抗性 抵抗类型
```

## Parameters

- `self_type` `any`: Type and behavior are not yet reviewed; see the source.
- `opponent_type` `any`: Type and behavior are not yet reviewed; see the source.
- `ignore` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDValue.lua:108`

```lua
function RushDuel.ValueEffectIndesType(self_type, opponent_type, ignore)
    local s_type = self_type or 0
    local o_type = opponent_type or 0
    return function(e, re, rp)
        if e == nil then
            return ignore or false, s_type, o_type
        end
        local op = e:GetOwnerPlayer()
        if rp == op then
            return s_type ~= 0 and re:IsActiveType(s_type)
        else
            return o_type ~= 0 and re:IsActiveType(o_type)
        end
    end
end
```
