# RushDuel.HintOrConfirm

Alias: `RD.HintOrConfirm`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.HintOrConfirm(any group, any hint_selection, any confirm, any target_player) -> any
```

## Description

Rush Duel helper declared in `RDFunction.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
显示选择动画, 或者展示卡片组
```

## Parameters

- `group` `any`: Type and behavior are not yet reviewed; see the source.
- `hint_selection` `any`: Type and behavior are not yet reviewed; see the source.
- `confirm` `any`: Type and behavior are not yet reviewed; see the source.
- `target_player` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDFunction.lua:89`

```lua
function RushDuel.HintOrConfirm(group, hint_selection, confirm, target_player)
    if hint_selection then
        Duel.HintSelection(group)
    elseif confirm then
        Duel.ConfirmCards(target_player, group)
    end
end
```
