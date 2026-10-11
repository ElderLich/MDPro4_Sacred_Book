# RushDuel.CreateCannotActivateSameCodeEffect

Alias: `RD.CreateCannotActivateSameCodeEffect`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.CreateCannotActivateSameCodeEffect(any e, any desc, any flag, any player, any code) -> any
```

## Description

Rush Duel helper declared in `RDLimit.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
创建限制: 这个回合，自己不能把「卡名」的效果发动
```

## Parameters

- `e` `any`: Type and behavior are not yet reviewed; see the source.
- `desc` `any`: Type and behavior are not yet reviewed; see the source.
- `flag` `any`: Type and behavior are not yet reviewed; see the source.
- `player` `any`: Type and behavior are not yet reviewed; see the source.
- `code` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDLimit.lua:346`

```lua
function RushDuel.CreateCannotActivateSameCodeEffect(e, desc, flag, player, code)
	if Duel.GetFlagEffect(player, flag) ~= 0 then
        return nil
    end
    local e1 = RushDuel.CreateCannotActivateMix(e, desc, player, 1, 0, RESET_PHASE + PHASE_END,
        function(e, re, tp)
	        return re:GetHandler():IsCode(code)
        end)
	Duel.RegisterFlagEffect(player, flag, RESET_PHASE + PHASE_END, 0, 1)
    return e1
end
```
