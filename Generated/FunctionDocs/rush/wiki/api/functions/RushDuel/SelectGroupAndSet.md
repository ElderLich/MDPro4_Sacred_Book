# RushDuel.SelectGroupAndSet

Alias: `RD.SelectGroupAndSet`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.SelectGroupAndSet(any filter, any check, any tp, any s_range, any o_range, any min, any max, any expect, any e, any break_effect) -> any
```

## Description

Rush Duel helper declared in `RDAction.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
操作: 选择魔法, 陷阱卡盖放 (子卡片组)
```

## Parameters

- `filter` `any`: Type and behavior are not yet reviewed; see the source.
- `check` `any`: Type and behavior are not yet reviewed; see the source.
- `tp` `any`: Type and behavior are not yet reviewed; see the source.
- `s_range` `any`: Type and behavior are not yet reviewed; see the source.
- `o_range` `any`: Type and behavior are not yet reviewed; see the source.
- `min` `any`: Type and behavior are not yet reviewed; see the source.
- `max` `any`: Type and behavior are not yet reviewed; see the source.
- `expect` `any`: Type and behavior are not yet reviewed; see the source.
- `e` `any`: Type and behavior are not yet reviewed; see the source.
- `break_effect` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDAction.lua:204`

```lua
function RushDuel.SelectGroupAndSet(filter, check, tp, s_range, o_range, min, max, expect, e, break_effect)
    local ct = RushDuel.GetSZoneCount(tp, max)
    if ct >= min then
        return RushDuel._private_action_select_group(HINTMSG_SET, filter, check, tp, s_range, o_range, min, ct, expect, false, false, RushDuel._set_spell_trap, e, tp, break_effect)
    end
    return 0
end
```
