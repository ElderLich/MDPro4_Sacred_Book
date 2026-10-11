# RushDuel.SendToHandAndExists

Alias: `RD.SendToHandAndExists`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.SendToHandAndExists(any target, any effect, any player, any reason, any filter, any count, any expect) -> any
```

## Description

Rush Duel helper declared in `RDAction.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
操作: 加入/返回手卡, 并给对方确认加入自己手卡的卡
```

## Parameters

- `target` `any`: Type and behavior are not yet reviewed; see the source.
- `effect` `any`: Type and behavior are not yet reviewed; see the source.
- `player` `any`: Type and behavior are not yet reviewed; see the source.
- `reason` `any`: Type and behavior are not yet reviewed; see the source.
- `filter` `any`: Type and behavior are not yet reviewed; see the source.
- `count` `any`: Type and behavior are not yet reviewed; see the source.
- `expect` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDAction.lua:277`

```lua
function RushDuel.SendToHandAndExists(target, effect, player, reason, filter, count, expect)
    local hints = Group.CreateGroup()
    local group = RushDuel.ToGroup(target):Filter(RushDuel.FilterToHandTarget, nil, effect, player, reason, hints)
    local g = RushDuel.ToMaximunGroup(group)
    local tc = hints:GetFirst()
    if tc then
        Duel.Hint(HINT_CARD, 0, tc:GetOriginalCode())
    end
    if #g == 0 then
        return false
    end
    if Duel.SendtoHand(g, nil, REASON_EFFECT) == 0 then
        return false
    end
    local cg = g:Filter(RushDuel.FilterToHandConfirm, nil, player)
    if #cg > 0 then
        Duel.ConfirmCards(1 - player, cg)
    end
    return RushDuel.IsOperatedGroupExists(filter, count, expect)
end
```
