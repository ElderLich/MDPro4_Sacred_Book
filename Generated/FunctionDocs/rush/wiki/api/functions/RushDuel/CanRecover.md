# RushDuel.CanRecover

Alias: `RD.CanRecover`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.CanRecover(any desc, any player, any recover, any break_effect) -> any
```

## Description

Rush Duel helper declared in `RDAction.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
可选操作: 回复
```

## Parameters

- `desc` `any`: Type and behavior are not yet reviewed; see the source.
- `player` `any`: Type and behavior are not yet reviewed; see the source.
- `recover` `any`: Type and behavior are not yet reviewed; see the source.
- `break_effect` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDAction.lua:606`

```lua
function RushDuel.CanRecover(desc, player, recover, break_effect)
    if recover > 0 and Duel.SelectYesNo(player, desc) then
        if break_effect then
            Duel.BreakEffect()
        end
        return Duel.Recover(player, recover, REASON_EFFECT)
    end
    return 0
end
```
