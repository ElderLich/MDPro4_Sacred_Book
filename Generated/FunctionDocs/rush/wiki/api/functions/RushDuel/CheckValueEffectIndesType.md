# RushDuel.CheckValueEffectIndesType

Alias: `RD.CheckValueEffectIndesType`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.CheckValueEffectIndesType(any player, any effects, any value) -> any
```

## Description

Rush Duel helper declared in `RDValue.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
判断： 是否可以赋予效果破坏抗性
```

## Parameters

- `player` `any`: Type and behavior are not yet reviewed; see the source.
- `effects` `any`: Type and behavior are not yet reviewed; see the source.
- `value` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDValue.lua:125`

```lua
function RushDuel.CheckValueEffectIndesType(player, effects, value)
    local attachs_s, attachs_o = 0, 0
    for _, effect in ipairs(effects) do
        local val = effect:GetValue()
        if val == 1 then
            -- 全破坏抗性, 无法再赋予其他抗性
            return false
        else
            -- 已有抗性全部叠加
            local ignore, s_type, o_type = val(nil)
            if not ignore then
                if effect:GetHandlerPlayer() ~= effect:GetOwnerPlayer() then
                    s_type, o_type = o_type, s_type
                end
                attachs_s = attachs_s | s_type
                attachs_o = attachs_o | o_type
            end
        end
    end
    -- 判断抗性是否有变化
    local _, s_type, o_type = value(nil)
    return (attachs_s | s_type) ~= attachs_s or (attachs_o | o_type) ~= attachs_o
end
```
