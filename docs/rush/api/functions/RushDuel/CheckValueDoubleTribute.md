# RushDuel.CheckValueDoubleTribute

Alias: `RD.CheckValueDoubleTribute`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.CheckValueDoubleTribute(any values, any value) -> any
```

## Description

Rush Duel helper declared in `RDValue.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
判断： 是否可以赋予双重解放
```

## Parameters

- `values` `any`: Type and behavior are not yet reviewed; see the source.
- `value` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDValue.lua:82`

```lua
function RushDuel.CheckValueDoubleTribute(values, value)
    local _, info = value(nil)
    for _, val in ipairs(values) do
        if val == 1 then
            -- 全范围双重解放, 无法再赋予双重解放
            return false
        else
            -- 已有抗性全部叠加
            local ignore, attach_info = val(nil)
            if not ignore then
                if attach_info == 1 then
                    -- 全范围双重解放, 无法再赋予双重解放
                    return false
                elseif info == 1 then
                    -- 全范围双重解放, 无需判断
                elseif not RushDuel._private_is_double_tribute_info_different(info, attach_info) then
                    -- 已存在相同的双重解放效果
                    return false
                end
            end
        end
    end
    return true
end
```

## Used By

Generated from the local `Rush/Scripts/` folder and `rush_cards.cdb`.

No indexed local card script currently calls this function.

This can mean the function is unused in the current script set, is only called through an alias, or is available for future/manual scripts.
