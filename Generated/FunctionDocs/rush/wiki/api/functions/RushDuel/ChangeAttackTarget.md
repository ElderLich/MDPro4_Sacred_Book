# RushDuel.ChangeAttackTarget

Alias: `RD.ChangeAttackTarget`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.ChangeAttackTarget(any card, any player, any target) -> any
```

## Description

Rush Duel helper declared in `RDAction.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
操作: 改变攻击对象
```

## Parameters

- `card` `any`: Type and behavior are not yet reviewed; see the source.
- `player` `any`: Type and behavior are not yet reviewed; see the source.
- `target` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDAction.lua:552`

```lua
function RushDuel.ChangeAttackTarget(card, player, target)
    local g = card:GetAttackableTarget()
    Duel.Hint(HINT_SELECTMSG, player, HINTMSG_ATTACKTARGET)
    local sg = g:Select(player, 1, 1, nil)
    local tc = sg:GetFirst()
    return tc and (tc == target or Duel.ChangeAttackTarget(tc))
end
```
